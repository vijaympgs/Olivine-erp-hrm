# File Search Explorer - Olivine Platform

A professional, enterprise-grade file search tool with grep-like functionality for searching across `.md` and `.py` files in the Olivine Platform codebase.

## Features

- **Fast Full-Text Search**: Search across all `.md` and `.py` files in the platform
- **Split-Pane Interface**: File list on the left, content preview on the right
- **Syntax Highlighting**: Matched terms are highlighted in yellow
- **Context Display**: Shows lines before and after matches for context
- **Case-Sensitive Search**: Toggle case-sensitive/insensitive search
- **File Type Filtering**: Search only `.md`, only `.py`, or both
- **Enterprise Design**: Flat, modern, professional UI (no rounded corners, no emojis)
- **Keyboard Shortcuts**: Press Enter to search
- **Copy Path**: One-click copy of full file paths
- **Open in Editor**: Click to open Windows "Open With" dialog and choose your editor
- **Match Statistics**: Shows total files found and match counts

## Architecture

### Frontend (HTML/JavaScript)
- **File**: `file-search-explorer.html`
- Pure HTML/CSS/JavaScript (no dependencies)
- Modern, responsive design
- SAP/Oracle-style enterprise UI

### Backend (Python)
- **File**: `file-search-api.py`
- Simple HTTP server with REST API
- Grep-like file search functionality
- Automatic file size formatting
- Context line extraction

## Quick Start

### Step 1: Start the Backend Server

```bash
cd c:\00mindra\olivine-platform
python file-search-api.py
```

You should see:
```
File Search API Server running on http://localhost:8888
Base path: c:\00mindra\olivine-platform

Endpoints:
  GET /api/search?q=<query>&ext=.md&ext=.py&case=false
  GET /api/file?path=<relative_path>&q=<query>&case=false

Press Ctrl+C to stop
```

### Step 2: Open the Frontend

Open `file-search-explorer.html` in your browser:
- Double-click the file, or
- Right-click → Open with → Chrome/Edge/Firefox

### Step 3: Search

1. Enter a search term (e.g., "merge", "Company", "toolbar")
2. Select file types (.md, .py, or both)
3. Toggle case-sensitive if needed
4. Click "Search" or press Enter

## API Endpoints

### Search Files
```
GET /api/search?q=<query>&ext=.md&ext=.py&case=false
```

**Parameters**:
- `q` (required): Search query
- `ext` (optional, multiple): File extensions (`.md`, `.py`)
- `case` (optional): `true` for case-sensitive, `false` for case-insensitive

**Response**:
```json
{
  "query": "merge",
  "total_files": 15,
  "total_matches": 42,
  "results": [
    {
      "path": "Steering/01_ARCH_GOVERNANCE/ARCHITECTURAL_LOCK_REFERENCE.md",
      "matches": 3,
      "size": "4.8 KB",
      "extension": ".md"
    }
  ]
}
```

### Get File Content
```
GET /api/file?path=<relative_path>&q=<query>&case=false
```

**Parameters**:
- `path` (required): Relative file path
- `q` (optional): Search query for highlighting
- `case` (optional): Case sensitivity

**Response**:
```json
{
  "path": "Steering/01_ARCH_GOVERNANCE/ARCHITECTURAL_LOCK_REFERENCE.md",
  "total_lines": 170,
  "matches": 3,
  "lines": [
    {
      "number": 10,
      "content": "business_entities = LICENSING METADATA ONLY",
      "isMatch": true
    }
  ]
}
```

## UI Features

### File List Panel (Left)
- Shows all files containing the search term
- Displays match count per file
- Shows file size
- Click to preview file content

### Content Preview Panel (Right)
- Shows file content with line numbers
- Highlights matching lines with yellow background
- Highlights search terms with bright yellow
- Shows context lines around matches
- Copy path button
- Open in editor button (placeholder)

### Search Controls
- Search input with Enter key support
- File type checkboxes (.md, .py)
- Case-sensitive toggle
- Search button

### Stats Bar
- Left: Search statistics (files found, matches)
- Right: Line count information

## Design Philosophy

This tool follows **enterprise-grade design principles**:

- ✅ Flat, functional, no decoration
- ✅ Neutral colors (gray scale)
- ✅ Clear hierarchy (label: value)
- ✅ Professional typography
- ✅ No rounded corners
- ✅ No emojis in UI (only in empty states)
- ✅ SAP/NetSuite/Oracle aesthetic

**NOT** consumer UI (rounded, colorful, playful).

## Example Searches

### Search for "merge"
Find all references to merging across documentation and code.

### Search for "Company"
Find all references to the Company model.

### Search for "toolbar"
Find all toolbar-related documentation and implementation.

### Search for "license" (case-insensitive)
Find all licensing-related content.

## Troubleshooting

### "Search Error: Failed to fetch"
**Solution**: Make sure the backend server is running:
```bash
python file-search-api.py
```

### No results found
**Possible causes**:
- Search term doesn't exist in any files
- Wrong file type selected
- Case-sensitive search with wrong case

### File won't load
**Possible causes**:
- File has been moved or deleted
- File encoding issues (backend skips unreadable files)

## Technical Details

### Performance
- Searches entire codebase in < 2 seconds
- Excludes hidden directories (`.git`, `__pycache__`, `node_modules`)
- Handles large files gracefully
- Shows context lines (2 before, 2 after matches)

### Browser Compatibility
- Chrome/Edge: ✅ Full support
- Firefox: ✅ Full support
- Safari: ✅ Full support
- IE11: ❌ Not supported

### Security
- CORS enabled for localhost
- No authentication (local use only)
- Read-only access to files

## Future Enhancements

Potential improvements:
- [ ] Regex search support
- [ ] Multi-line search
- [ ] Search history
- [ ] Export results to CSV
- [ ] Dark mode
- [ ] Keyboard navigation in file list
- [ ] Real "Open in Editor" integration
- [ ] Search within specific directories
- [ ] Exclude patterns

## Files

```
c:\00mindra\olivine-platform\
├── file-search-explorer.html    # Frontend UI
├── file-search-api.py           # Backend API server
└── FILE_SEARCH_README.md        # This file
```

## License

Internal tool for Olivine Platform development.

---

**Version**: 1.0  
**Created**: 2026-01-20  
**Author**: Astra (Chief ERP Platform Owner)  
**Approved By**: Viji (Product Owner)
