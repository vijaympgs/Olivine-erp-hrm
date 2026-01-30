"""
File Search API - Integrated into Django Backend
Provides file search and content retrieval for the File Search Explorer
Supports multiple base paths / folders for searching
"""
import os
import re
import subprocess
 
from pathlib import Path
from django.http import JsonResponse
from django.views import View


# Configurable search roots - add more folders here as needed
SEARCH_ROOTS = {
    'olivine-platform': Path(r"d:\olvine-erp"),
    'mindra-root': Path(r"d:\olvine-erp"),
    'user-documents': Path.home() / "Documents",
}

# Default search root
DEFAULT_ROOT = 'olivine-platform'


class BaseFileSearchView(View):
    """Base class for file search views"""
    
    def get_base_path(self, request) -> Path:
        """Get base path from root key or custom 'base' path parameter"""
        root_key = request.GET.get('root', DEFAULT_ROOT)
        custom_base = request.GET.get('base') or request.GET.get('path_root')
        
        # If a full path is provided as 'base' (contains backslash), use it directly
        if custom_base and ('\\' in custom_base or '/' in custom_base):
            p = Path(custom_base)
            if p.exists():
                return p
        
        # Otherwise use the lookup key
        if root_key in SEARCH_ROOTS:
            return SEARCH_ROOTS[root_key]
        return SEARCH_ROOTS[DEFAULT_ROOT]
    
    def format_size(self, size: int) -> str:
        """Format file size in human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"


class SearchRootsView(View):
    """List available search roots/folders"""
    
    def get(self, request):
        roots = []
        for key, path in SEARCH_ROOTS.items():
            roots.append({
                'key': key,
                'path': str(path),
                'exists': path.exists(),
                'is_default': key == DEFAULT_ROOT
            })
        return JsonResponse({
            'roots': roots,
            'default': DEFAULT_ROOT
        })




class FileSearchView(BaseFileSearchView):
    """Search files for content"""
    
    def get(self, request):
        try:
            query = request.GET.get('q', '')
            extensions = request.GET.getlist('ext') or ['.md', '.py', '.ts', '.tsx']
            case_sensitive = request.GET.get('case', 'false').lower() == 'true'
            
            if not query:
                return JsonResponse({'error': 'Query parameter required'}, status=400)
            
            base_path = self.get_base_path(request)
            results = self.search_files(query, extensions, case_sensitive, base_path)
            
            return JsonResponse({
                'query': query,
                'base_path': str(base_path),
                'total_files': len(results),
                'total_matches': sum(r['matches'] for r in results),
                'results': results
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def search_files(self, query: str, extensions: list, case_sensitive: bool, base_path: Path) -> list:
        """Search for files containing the query string"""
        results = []
        
        if not base_path.exists():
            return results
        
        # Compile regex pattern
        flags = 0 if case_sensitive else re.IGNORECASE
        pattern = re.compile(re.escape(query), flags)
        
        # Walk through directory
        for root, dirs, files in os.walk(base_path):
            # Skip hidden directories and common excludes
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules', 'venv', '.git']]
            
            for file in files:
                # Check extension
                if not any(file.endswith(ext) for ext in extensions):
                    continue
                
                file_path = Path(root) / file
                try:
                    relative_path = file_path.relative_to(base_path)
                except ValueError:
                    relative_path = file_path
                
                try:
                    # Read file and search
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = pattern.findall(content)
                        
                        if matches:
                            # Get file size
                            size = file_path.stat().st_size
                            size_str = self.format_size(size)
                            
                            results.append({
                                'path': str(relative_path).replace('\\', '/'),
                                'matches': len(matches),
                                'size': size_str,
                                'extension': file_path.suffix
                            })
                
                except Exception:
                    continue
        
        # Sort by number of matches (descending)
        results.sort(key=lambda x: x['matches'], reverse=True)
        
        return results


class FileContentView(BaseFileSearchView):
    """Get file content with match highlights"""
    
    def get(self, request):
        try:
            file_path = request.GET.get('path', '')
            query = request.GET.get('q', '')
            case_sensitive = request.GET.get('case', 'false').lower() == 'true'
            
            if not file_path:
                return JsonResponse({'error': 'File path required'}, status=400)
            
            base_path = self.get_base_path(request)
            content = self.get_file_content(file_path, query, case_sensitive, base_path)
            return JsonResponse(content)
            
        except FileNotFoundError as e:
            return JsonResponse({'error': str(e)}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def get_file_content(self, relative_path: str, query: str, case_sensitive: bool, base_path: Path) -> dict:
        """Get file content with highlighted matches"""
        file_path = base_path / relative_path.replace('/', '\\')
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {relative_path}")
        
        # Read file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        # Compile regex pattern
        flags = 0 if case_sensitive else re.IGNORECASE
        pattern = re.compile(re.escape(query), flags) if query else None
        
        # Process ALL lines
        result_lines = []
        match_line_numbers = set()
        
        # Find all matching lines
        for i, line in enumerate(lines, 1):
            if pattern and pattern.search(line):
                match_line_numbers.add(i)
        
        # Build result with ALL lines
        for i, line in enumerate(lines, 1):
            result_lines.append({
                'number': i,
                'content': line.rstrip('\n\r'),
                'isMatch': i in match_line_numbers
            })
        
        return {
            'path': relative_path,
            'total_lines': len(lines),
            'lines': result_lines,
            'matches': len(match_line_numbers)
        }


class FileOpenView(BaseFileSearchView):
    """Open file in editor or reveal in explorer"""
    
    def get(self, request):
        try:
            file_path = request.GET.get('path', '')
            show_dialog = request.GET.get('dialog', 'false').lower() == 'true'
            reveal = request.GET.get('reveal', 'false').lower() == 'true'
            
            if not file_path:
                return JsonResponse({'error': 'File path required'}, status=400)
            
            base_path = self.get_base_path(request)
            full_path = base_path / file_path.replace('/', '\\')
            
            if not full_path.exists():
                return JsonResponse({'error': f'File not found: {file_path}'}, status=404)
            
            if reveal:
                success = self.reveal_in_explorer(str(full_path))
                message = 'Folder opened and file selected' if success else 'Failed to reveal file'
            else:
                success = self.open_file_in_windows(str(full_path), show_dialog)
                message = 'File opened successfully' if success else 'Failed to open file'
            
            return JsonResponse({
                'success': success,
                'message': message,
                'path': str(full_path)
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
            
    def reveal_in_explorer(self, file_path: str) -> bool:
        """Open folder and select the file"""
        try:
            # Native Windows Explorer reveal
            # We use subprocess.run with list to ensure quoting is handled
            subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)
            return True
        except Exception as e:
            print(f"Error revealing file: {e}")
            return False
    
    def open_file_in_windows(self, file_path: str, show_dialog: bool = False) -> bool:
        """Open file using Windows shell"""
        try:
            if show_dialog:
                subprocess.Popen(['rundll32.exe', 'shell32.dll,OpenAs_RunDLL', file_path])
            else:
                os.startfile(file_path)
            return True
        except Exception as e:
            print(f"Error opening file: {e}")
            return False
