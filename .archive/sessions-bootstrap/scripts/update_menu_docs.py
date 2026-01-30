
import re
import datetime
import os

MENU_CONFIG_PATH = r"c:\00mindra\retail-erp-platform\frontend\src\app\menuConfig.ts"
OUTPUT_PATH = r"c:\00mindra\retail-erp-platform\.steering\03_DESIGN_SYSTEM\MENU_TREE_STRUCTURE.md"

ICON_MAP = {
    'Activity': '🟥',
    'Store': '🏪',
    'LayoutDashboard': '📊',
    'CreditCard': '💳',
    'Clock': '⏰',
    'TrendingUp': '📈',
    'Database': '🗄️',
    'Package': '📦',
    'ShoppingBag': '🛍️',
    'Users': '👥',
    'DollarSign': '💰',
    'BookOpen': '📖',
    'Receipt': '🧾',
    'Landmark': '🏛️',
    'Banknote': '💵',
    'Percent': '🔢',
    'BarChart3': '📈',
    'Lock': '🔒',
    'Zap': '⚡',
    'Shield': '🛡️',
    'Settings': '⚙️',
    'UserCog': '👥',
    'FolderTree': '📂',
    'FileText': '📄',
    'Truck': '🚚',
    'Layout': '📐',
    'HardDrive': '💾',
    'PieChart': '🥧',
    'Award': '🏆',
    'MessageSquare': '💬',
    'Handshake': '🤝',
    'Briefcase': '💼',
    'Link': '🔗',
    'UserPlus': '➕',
    'User': '👤',
    'Building': '🏢',
    'Target': '🎯',
    'Megaphone': '📣',
    'Mail': '📧',
    'Headphones': '🎧',
    'MapPin': '📍',
    'Calendar': '📅',
    'CheckCircle': '✅',
    'LogOut': '🚪',
    'Code': '💻',
    'Coins': '🪙',
    'Calculator': '🧮',
    'Heart': '❤️',
    'LineChart': '📉',
    'Bell': '🔔',
    'Upload': '📤',
    'Star': '⭐',
    'GitBranch': '🌿',
    'Route': '🔀',
    'Sprout': '🌱',
    'ArrowRight': '➡️',
    'Copy': '📋',
    'UserCircle': '👤',
    'Filter': '🌪️',
    'Sitemap': '🕸️',
    'GitMerge': '🔀',
    'Sparkles': '✨',
    'Share2': '🔗',
    'FilePlus': '➕',
    'Book': '📘',
    'PenTool': '✒️',
    'PlayCircle': '▶️',
    'Eye': '👁️',
    'List': '📝',
    'Droplet': '💧',
    'UserX': '🚫',
    'GitPullRequest': '⤴️',
    'Ticket': '🎫',
    'MessageCircle': '🗨️',
    'Bot': '🤖',
    'ThumbsUp': '👍',
    'CheckSquare': '☑️',
    'Video': '📹',
    'Phone': '📞',
    'History': '📜',
    'Gift': '🎁',
    'Layers': '📚',
    'Globe': '🌐',
    'AlertTriangle': '⚠️',
    'RefreshCw': '🔄',
    'FolderOpen': '📂',
    'GraduationCap': '🎓',
    'Wrench': '🔧',
    'Smartphone': '📱',
    'WifiOff': '📶',
    'TrendingDown': '📉',
    'Trophy': '🏆',
    'LayoutGrid': '▦',
    'Download': '📥',
    'Reply': '↩️',
    'Edit3': '✏️',
    'RefreshCw': '🔄',
    'Webhook': '🪝',
    'UserCheck': '✅',
    'PieChart': '🥧',
    'ClipboardList': '📋',
    'FileCheck': '✅',
    'ZoomIn': '🔍',
    'ZoomOut': '🔍',
    'Move': '↔️',
    'SlidersHorizontal': '🎚️',
    'FileType': '📄',
    'Plus': '➕',
    'Search': '🔍',
    'Menu': '☰',
    'X': '❌',
    'ChevronRight': '>',
    'ChevronDown': 'v',
    'ChevronLeft': '<',
    'ChevronUp': '^',
    'MoreHorizontal': '...',
    'MoreVertical': ':',
    'Trash2': '🗑️',
    'Edit': '✏️',
    'Save': '💾',
    'Printer': '🖨️',
    'Share': '🔗',
    'ExternalLink': '↗️',
    'HelpCircle': '❓',
    'Info': 'ℹ️',
    'AlertCircle': '⚠️',
    'Check': '✅',
    'XCircle': '❌',
    'Minus': '➖',
    'ArrowUp': '⬆️',
    'ArrowDown': '⬇️',
    'ArrowLeft': '⬅️',
    'ArrowRight': '➡️',
    'ChevronsLeft': '<<',
    'ChevronsRight': '>>',
    'ChevronsUp': '^^',
    'ChevronsDown': 'vv',
    'Pause': '⏸️',
    'Play': '▶️',
    'StopCircle': '⏹️',
    'FastForward': '⏩',
    'Rewind': '⏪',
    'SkipBack': '⏮️',
    'SkipForward': '⏭️',
    'Volume': '🔊',
    'Volume1': '🔉',
    'Volume2': '🔊',
    'VolumeX': '🔇',
    'Mic': '🎤',
    'MicOff': '🔇',
    'Camera': '📷',
    'CameraOff': '📷',
    'VideoOff': '📹',
    'Maximize': '🔲',
    'Minimize': '_ ',
    'Maximize2': '🔲',
    'Minimize2': '_ ',
}

def parse_menu_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Very naive parser assuming standard formatting as seen in the file
    # We will look for objects defined by { ... }
    # This is tricky with strictly regex. 
    # Let's try to parse the array of objects.
    
    # We will iterate lines and track structure by indentation or brackets.
    # But python execution of typescript file content isn't possible.
    # regex to find properties: id, label, icon, path, children
    
    # Let's clean the content to make it effectively JSON-like
    # Remove comments
    content = re.sub(r'//.*', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # We will assume a specific structure as read in the file:
    # keys are not quoted. Strings are single quoted.
    # We want to extract a list of Dicts.
    
    items = []
    
    # Instead of full parsing, let's process line by line and build a tree.
    # Assuming standard indentation in the file (2 spaces or 4 spaces)
    
    stack = []
    current_item = None
    root_items = []
    
    # Regexes for properties
    id_re = re.compile(r"id:\s*'([^']+)'")
    label_re = re.compile(r"label:\s*'([^']+)'")
    path_re = re.compile(r"path:\s*'([^']+)'")
    icon_re = re.compile(r"icon:\s*'([^']+)'")
    subtitle_re = re.compile(r"subtitle:\s*'([^']+)'")
    divider_re = re.compile(r"divider:\s*true")
    
    lines = content.split('\n')
    
    # We need to construct a hierarchy.
    # A simple approach: 
    # Find `{` that opens an item. 
    # Find `children: [` that opens a list.
    # Find `]` that closes children.
    # Find `},` that closes an item.
    
    # This might be too complex for a quick script without a proper parser. 
    # However, the file is very regular.
    
    # Let's try to just extract lines that define items and reconstruct hierarchy based on indentation?
    # No, indentation might vary or be unreliable if modified.
    
    # Better approach: Use `node` to output the JSON!
    # I can write a temporary JS script that imports the config and console.logs it as JSON.
    # But it is a TS file. I can't run TS directly without tx-node or compilation.
    # And it has imports `export interface ...`.
    
    # Fallback: Python text processing with stack.
    pass
    
    # Simplest reliable way for this specific file format:
    # It's a list of objects.
    # We can perform a "tokenizing" pass.
    
    active_stack = [] # List of lists (children)
    root_list = []
    active_stack.append(root_list) # Start with root
    
    current_obj = None
    
    # Simplified parser logic:
    # 1. Detect start of object `{`
    # 2. Detect end of object `}`
    # 3. Detect start of array `[` -> push new list to stack
    # 4. Detect end of array `]` -> pop list, assign to `children` of current_obj
    
    # But `children: [` is inside an object.
    
    code = content
    # Remove whitespace to make tokenizing easier? No, needed for strings.
    
    # Let's normalize strings to double quotes for easier parsing if we were doing json.
    
    # Start iterating char by char?
    token_accum = ""
    in_string = False
    string_char = "'"
    
    obj_stack = [] # Stack of objects being built
    list_stack = [] # Stack of lists being built. 
    # Actually we just need to know if we are in a list or object.
    
    # Root is a list `export const menuConfig: MenuItem[] = [`
    
    # Find the start of the array
    start_idx = code.find("export const menuConfig: MenuItem[] = [")
    if start_idx == -1:
        print("Could not find start of config")
        return []
    
    code = code[start_idx + len("export const menuConfig: MenuItem[] = "):] 
    # Now code starts with `[`
    
    # Let's use `ast.literal_eval`? No, JS syntax differs (true vs True, etc).
    
    # Let's write a recursive descent parser for this "JS Object" format.
    
    idx = 0
    length = len(code)
    
    def skip_whitespace(index):
        while index < length and code[index].isspace():
            index += 1
        return index
        
    def parse_value(index):
        index = skip_whitespace(index)
        if index >= length: return None, index
        
        char = code[index]
        
        if char == "'":
            # String
            end = code.find("'", index + 1)
            val = code[index+1:end]
            return val, end + 1
        elif char == '"':
            end = code.find('"', index + 1)
            val = code[index+1:end]
            return val, end + 1
        elif char == '{':
            return parse_object(index)
        elif char == '[':
            return parse_array(index)
        elif char.isalnum():
            # Boolean or number or unquoted key (but we are in value position)
            # Read until comma or closing brace/bracket
            end = index
            while end < length and (code[end].isalnum() or code[end] == '_'):
                end += 1
            val = code[index:end]
            if val == 'true': val = True
            if val == 'false': val = False
            return val, end
        else:
            return None, index + 1
            
    def parse_array(index):
        # index is at '['
        arr = []
        index += 1 # skip [
        while index < length:
            index = skip_whitespace(index)
            if code[index] == ']':
                return arr, index + 1
            
            val, index = parse_value(index)
            arr.append(val)
            
            index = skip_whitespace(index)
            if code[index] == ',':
                index += 1
    
    def parse_object(index):
        # index is at '{'
        obj = {}
        index += 1 # skip {
        while index < length:
            index = skip_whitespace(index)
            if code[index] == '}':
                return obj, index + 1
            
            # Parse Key
            # Keys are unquoted in this file usually
            key_start = index
            while index < length and (code[index].isalnum() or code[index] == '-' or code[index] == '_'):
                index += 1
            key = code[key_start:index]
            
            index = skip_whitespace(index)
            if code[index] != ':':
                # Maybe something else?
                pass
            index += 1 # skip :
            
            val, index = parse_value(index)
            obj[key] = val
            
            index = skip_whitespace(index)
            if code[index] == ',':
                index += 1
    
    result, _ = parse_array(0)
    return result

def generate_markdown(items):
    lines = []
    lines.append("# Application Menu Structure")
    lines.append(f"# Updated on {datetime.datetime.now().strftime('%d-%m-%Y, %H:%M')} by Agent")
    lines.append("This document reflects the current menu structure defined in `frontend/src/app/menuConfig.ts`.")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    def process_item(item, level=1):
        if item.get('divider'):
            lines.append("---")
            lines.append("")
            return
            
        label = item.get('label', 'Unnamed')
        path = item.get('path', '')
        subtitle = item.get('subtitle', '')
        icon_name = item.get('icon', '')
        emoji = ICON_MAP.get(icon_name, '')
        
        # Determine markdown level
        # Root items are often Modules (Level 2 Header)
        # Children are Level 3 or Bullets
        
        display_str = f"{emoji} {label}".strip()
        if path:
            display_str += f" (`{path}`)"
        if subtitle:
            display_str += f" - {subtitle}"
            
        if level == 1:
            lines.append(f"## {display_str}")
        elif level == 2:
            lines.append(f"### {display_str}")
        else:
            indent = "    " * (level - 3)
            lines.append(f"{indent}*   **{label}**{f' (`{path}`)' if path else ''} - {subtitle}")
            
        if level <= 2:
            lines.append("")
            
        if 'children' in item and isinstance(item['children'], list):
            for child in item['children']:
                process_item(child, level + 1)
                
    for item in items:
        # Check if item is just a module container or a real link
        # In current config, Top Level items are like "Retail", "Finance", "CRM"
        # We treat them as Sections (Level 2 ##)
        process_item(item, level=1)
        
    return "\n".join(lines)

if __name__ == "__main__":
    try:
        items = parse_menu_config(MENU_CONFIG_PATH)
        md_content = generate_markdown(items)
        
        with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        print("Successfully updated MENU_TREE_STRUCTURE.md")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()




