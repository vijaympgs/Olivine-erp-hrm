# File Search Explorer - Olivine Platform

A powerful file search and preview tool for the Olivine ERP platform. Search through source code, documentation, and configuration files with an intuitive web interface.

## 🚀 Quick Start

### Option 1: Use the Startup Script (Recommended)
```bash
# Navigate to the platform-arch directory
cd common\platform-arch

# Run the startup script
start-file-search.bat
```

### Option 2: Manual Start
```bash
# Step 1: Start the backend API server
python file-search-api.py

# Step 2: Open the web interface in your browser
# Open: http://localhost:8888/file-search-explorer.html
```

## 📁 Files Overview

- **`file-search-explorer.html`** - Main web interface
- **`file-search-api.py`** - Backend API server (Python)
- **`start-file-search.bat`** - Windows startup script
- **`README.md`** - This documentation file

## 🔍 Features

### Search Capabilities
- **Full-text search** across all file types
- **Case-sensitive/insensitive** search options
- **Multiple file type filters**:
  - 📝 Markdown files (`.md`)
  - 🐍 Python files (`.py`)
  - 📜 JavaScript/TypeScript (`.js`, `.ts`)
  - ⚛️ React components (`.tsx`, `.jsx`)
  - 📦 Configuration files (`.json`)
  - 🔧 Batch/Shell scripts (`.bat`, `.sh`)

### File Preview
- **Syntax highlighting** for code files
- **Markdown rendering** for documentation
- **Line numbers** and match highlighting
- **Search term highlighting** in context

### Productivity Features
- **One-click file opening** in default editor
- **Copy file paths** to clipboard
- **Real-time search results** with match counts
- **File size information**
- **Responsive design** for different screen sizes

## 🛠️ Usage Guide

### Basic Search
1. **Enter search term** in the search box (e.g., "Employee", "toolbar", "merge")
2. **Select file types** to search using the checkboxes
3. **Choose case sensitivity** (default: case-insensitive)
4. **Click "Search"** or press Enter

### Working with Results
- **Click on any file** in the results list to preview its content
- **Use "Copy Path"** to copy the full file path to clipboard
- **Use "Open in Editor"** to open the file in your default editor
- **View match statistics** in the status bar

### Search Tips
- **Use specific terms** for better results (e.g., "EmployeeRecords" instead of "employee")
- **Search for function names**, class names, or specific keywords
- **Try different file types** if you don't find what you're looking for
- **Use case-sensitive search** for exact matches

## 🔧 Technical Details

### API Endpoints

The backend server provides these REST API endpoints:

- **`GET /api/search?q=QUERY&ext=.md&ext=.py&case=false`**
  - Search for files containing the query
  - Parameters:
    - `q`: Search term (required)
    - `ext`: File extensions to search (can be multiple)
    - `case`: Case sensitivity (true/false)

- **`GET /api/file?path=FILE_PATH&q=QUERY&case=false`**
  - Get file content with search highlighting
  - Parameters:
    - `path`: File path (required)
    - `q`: Search term for highlighting (optional)
    - `case`: Case sensitivity (true/false)

- **`GET /api/open?path=FILE_PATH&dialog=true`**
  - Open file in default editor
  - Parameters:
    - `path`: File path (required)
    - `dialog`: Show "Open With" dialog (true/false)

- **`GET /api/health`**
  - Check server status and configuration

### Configuration

- **Base Directory**: `d:\olvine-erp` (automatically detected)
- **Server Port**: `8888`
- **Supported File Types**: `.md`, `.py`, `.js`, `.ts`, `.tsx`, `.jsx`, `.json`, `.bat`, `.sh`
- **Encoding**: UTF-8 with error handling for binary files

## 🐛 Troubleshooting

### Common Issues

**Server won't start**
```bash
# Check if Python is installed
python --version

# If not installed, install Python from https://python.org
```

**"Backend server not running" error**
- Make sure the API server is running (check for the console window)
- Verify the server is running on port 8888
- Try restarting the backend server

**No search results found**
- Check if you've selected the right file types
- Try broader search terms
- Verify the files exist in the `d:\olvine-erp` directory

**File won't open in editor**
- Check if you have a default editor configured
- Try copying the path and opening manually
- On Windows, ensure file associations are set correctly

### Performance Tips

- **Large searches** may take a few seconds on first run
- **Binary files** are automatically skipped
- **Search is optimized** for text files only
- **Server caches** results for better performance

## 🔄 Updates and Maintenance

### Adding New File Types
To add support for additional file types:

1. **Update the HTML interface** (`file-search-explorer.html`):
   ```html
   <label class="checkbox-label">
       <input type="checkbox" id="filterNewType">
       <span>.newext files</span>
   </label>
   ```

2. **Update the JavaScript**:
   ```javascript
   if (filterNewType.checked) extensions.push('.newext');
   ```

### Changing Base Directory
To search a different directory:

1. **Update the API server** (`file-search-api.py`):
   ```python
   self.base_path = Path(r'your\new\directory')
   ```

2. **Update the HTML interface** (`file-search-explorer.html`):
   ```javascript
   const BASE_PATH = 'your\\new\\directory';
   ```

## 📝 Development Notes

### Architecture
- **Frontend**: Pure HTML/CSS/JavaScript with no external dependencies (except marked.js for Markdown)
- **Backend**: Python HTTP server with CORS support
- **Communication**: REST API with JSON responses
- **File Handling**: UTF-8 encoding with graceful error handling

### Security Considerations
- **Local only**: Server runs on localhost (127.0.0.1)
- **No authentication**: Designed for local development use
- **File access**: Limited to the specified base directory
- **Input validation**: Search terms are sanitized and escaped

## 📞 Support

For issues or questions:
1. Check this README for troubleshooting tips
2. Verify the base directory path is correct
3. Ensure Python is properly installed
4. Check that port 8888 is not in use

---

**Version**: 1.0.0  
**Last Updated**: 2026-01-21  
**Compatible with**: Olivine ERP Platform  
**Requirements**: Python 3.6+, Modern web browser
