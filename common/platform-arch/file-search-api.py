#!/usr/bin/env python3
"""
File Search API Server for Olivine Platform
Provides REST API endpoints for searching and viewing file contents
"""

import os
import re
import json
import mimetypes
import subprocess
import sys
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import time

class FileSearchAPI(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.base_path = Path(r'd:\olvine-erp')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        try:
            # Serve the HTML file for root path
            if path == '/' or path == '':
                self.serve_html_file()
                return
            # Serve the HTML file for specific path
            elif path == '/file-search-explorer.html':
                self.serve_html_file()
                return
            # Handle favicon.ico request
            elif path == '/favicon.ico':
                self.serve_favicon()
                return
            # API endpoints
            elif path.startswith('/api/'):
                # Enable CORS for API endpoints
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                
                if path == '/api/search':
                    response = self.handle_search(query_params)
                elif path == '/api/file':
                    response = self.handle_file_content(query_params)
                elif path == '/api/open':
                    response = self.handle_open_file(query_params)
                elif path == '/api/health':
                    response = {'status': 'ok', 'base_path': str(self.base_path)}
                else:
                    response = {'error': 'Endpoint not found'}
                    
                self.wfile.write(json.dumps(response).encode('utf-8'))
            else:
                self.send_error(404, "File not found")
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            error_response = {'error': str(e)}
            self.wfile.write(json.dumps(error_response).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle OPTIONS requests for CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_search(self, query_params):
        """Handle file search requests"""
        query = query_params.get('q', [''])[0].strip()
        case_sensitive = query_params.get('case', ['false'])[0].lower() == 'true'
        extensions = query_params.get('ext', [])
        
        if not query:
            return {'error': 'Search query is required'}
        
        if not extensions:
            return {'error': 'At least one file extension is required'}
        
        # Search for files
        results = []
        total_matches = 0
        max_results = 50  # Limit results to prevent timeout
        files_searched = 0
        max_files_to_search = 100  # Limit files to search
        
        try:
            # Prioritize certain directories for faster results
            priority_dirs = ['HRM', 'BBPs', 'README.md', 'QUICK_START.md']
            
            for ext in extensions:
                pattern = f"*{ext}"
                files_searched = 0
                
                # Search in priority directories first
                for priority_dir in priority_dirs:
                    priority_path = self.base_path / priority_dir
                    if priority_path.exists():
                        for file_path in priority_path.rglob(pattern):
                            if not file_path.is_file():
                                continue
                            
                            files_searched += 1
                            if files_searched > max_files_to_search:
                                break
                                
                            try:
                                matches = self.search_in_file(file_path, query, case_sensitive)
                                if matches > 0:
                                    # Get relative path from base_path
                                    rel_path = file_path.relative_to(self.base_path)
                                    # Convert to forward slashes for web display
                                    web_path = str(rel_path).replace('\\', '/')
                                    
                                    # Get file size
                                    size = self.format_file_size(file_path.stat().st_size)
                                    
                                    results.append({
                                        'path': web_path,
                                        'matches': matches,
                                        'size': size
                                    })
                                    total_matches += 1
                                    
                                    if len(results) >= max_results:
                                        break
                            except (UnicodeDecodeError, PermissionError):
                                # Skip binary files or files we can't read
                                continue
                        
                        if len(results) >= max_results:
                            break
                
                if len(results) >= max_results:
                    break
                            
        except Exception as e:
            return {'error': f'Search failed: {str(e)}'}
        
        # Sort results by number of matches (descending)
        results.sort(key=lambda x: x['matches'], reverse=True)
        
        return {
            'results': results,
            'total_matches': total_matches,
            'query': query,
            'case_sensitive': case_sensitive,
            'extensions': extensions,
            'files_searched': files_searched,
            'max_results_reached': len(results) >= max_results
        }

    def handle_file_content(self, query_params):
        """Handle file content requests"""
        file_path = query_params.get('path', [''])[0]
        query = query_params.get('q', [''])[0].strip()
        case_sensitive = query_params.get('case', ['false'])[0].lower() == 'true'
        
        if not file_path:
            return {'error': 'File path is required'}
        
        # Convert web path to local path
        local_path = self.base_path / file_path.replace('/', '\\')
        
        if not local_path.exists() or not local_path.is_file():
            return {'error': 'File not found'}
        
        try:
            with open(local_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            # Process lines and find matches
            processed_lines = []
            total_matches = 0
            
            for i, line in enumerate(lines, 1):
                line_content = line.rstrip('\n\r')
                is_match = False
                
                if query:
                    search_pattern = re.escape(query)
                    flags = 0 if case_sensitive else re.IGNORECASE
                    if re.search(search_pattern, line_content, flags):
                        is_match = True
                        total_matches += 1
                
                processed_lines.append({
                    'number': i,
                    'content': line_content,
                    'isMatch': is_match
                })
            
            return {
                'path': file_path,
                'lines': processed_lines,
                'total_lines': len(processed_lines),
                'matches': total_matches
            }
            
        except Exception as e:
            return {'error': f'Failed to read file: {str(e)}'}

    def handle_open_file(self, query_params):
        """Handle file open requests"""
        file_path = query_params.get('path', [''])[0]
        show_dialog = query_params.get('dialog', ['false'])[0].lower() == 'true'
        
        if not file_path:
            return {'error': 'File path is required'}
        
        # Convert web path to local path
        local_path = self.base_path / file_path.replace('/', '\\')
        
        if not local_path.exists() or not local_path.is_file():
            return {'error': 'File not found'}
        
        try:
            if show_dialog:
                # Use Windows "Open With" dialog
                os.startfile(str(local_path))
            else:
                # Try to open with default application
                if sys.platform == 'win32':
                    os.startfile(str(local_path))
                elif sys.platform == 'darwin':
                    subprocess.run(['open', str(local_path)])
                else:
                    subprocess.run(['xdg-open', str(local_path)])
            
            return {'success': True, 'path': file_path}
            
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def search_in_file(self, file_path, query, case_sensitive):
        """Search for query in a single file and return match count"""
        try:
            # Quick file size check - skip very large files
            if file_path.stat().st_size > 10 * 1024 * 1024:  # 10MB limit
                return 0
                
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            flags = 0 if case_sensitive else re.IGNORECASE
            pattern = re.escape(query)
            matches = len(re.findall(pattern, content, flags))
            return matches
            
        except (UnicodeDecodeError, PermissionError, OSError):
            return 0

    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        if size_bytes < 1024:
            return f"{size_bytes} B"
        elif size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.1f} KB"
        else:
            return f"{size_bytes / (1024 * 1024):.1f} MB"

    def serve_html_file(self):
        """Serve the HTML file"""
        try:
            html_file = Path(__file__).parent / 'file-search-explorer.html'
            if not html_file.exists():
                self.send_error(404, "HTML file not found")
                return
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Error serving HTML file: {str(e)}".encode('utf-8'))

    def serve_favicon(self):
        """Serve a simple favicon or return 204 No Content"""
        # Return 204 No Content to indicate no favicon
        self.send_response(204)
        self.end_headers()

    def log_message(self, format, *args):
        """Override to reduce log spam"""
        pass  # Suppress default logging

def run_server():
    """Start the API server"""
    server_address = ('', 8888)
    httpd = HTTPServer(server_address, FileSearchAPI)
    
    print("=" * 60)
    print("File Search API Server Started")
    print("=" * 60)
    print(f"Server running on: http://localhost:8888")
    print(f"Base directory: {Path(r'd:\olvine-erp')}")
    print("=" * 60)
    print("Available endpoints:")
    print("  GET /api/search?q=QUERY&ext=.md&ext=.py&case=false")
    print("  GET /api/file?path=FILE_PATH&q=QUERY&case=false")
    print("  GET /api/open?path=FILE_PATH&dialog=true")
    print("  GET /api/health")
    print("=" * 60)
    print("Press Ctrl+C to stop the server")
    print()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        httpd.server_close()

if __name__ == '__main__':
    # Check if base directory exists
    base_dir = Path(r'd:\olvine-erp')
    if not base_dir.exists():
        print(f"Error: Base directory not found: {base_dir}")
        print("Please make sure the olvine-erp directory exists at the specified path.")
        sys.exit(1)
    
    run_server()
