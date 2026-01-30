#!/usr/bin/env python3
"""
BBP Section Extractor
Extracts specific sections from a large BBP markdown file
Usage: python bbp_extractor.py 2.1  (extracts section 2.1)
"""

import re
import sys

def extract_section(file_path, section_number):
    """
    Extract a specific section from BBP markdown file
    
    Args:
        file_path: Path to BBP file
        section_number: Section number like "2.1" or "3.2.1"
    
    Returns:
        Extracted section content as string
    """
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Normalize section number (e.g., "2.1" or "2.1.1")
    section_pattern = section_number.replace('.', r'\.')
    
    # Pattern to match section header
    # Matches: ## 2.1 SectionName or ### 2.1.1 Subsection
    header_pattern = rf'^(#{1,6})\s+{section_pattern}\s+(.+?)$'
    
    # Find the section header
    header_match = re.search(header_pattern, content, re.MULTILINE)
    
    if not header_match:
        return None
    
    # Get the heading level (number of #)
    section_level = len(header_match.group(1))
    section_start = header_match.start()
    section_title = header_match.group(0)
    
    # Find the next section at the same or higher level
    # This marks the end of our section
    next_section_pattern = rf'^#{{{1},{section_level}}}}\s+\d+\.'
    
    # Search for next section after current one
    remaining_content = content[section_start + len(section_title):]
    next_section_match = re.search(next_section_pattern, remaining_content, re.MULTILINE)
    
    if next_section_match:
        section_end = section_start + len(section_title) + next_section_match.start()
        section_content = content[section_start:section_end]
    else:
        # No next section found, take till end of file
        section_content = content[section_start:]
    
    return section_content.strip()


def save_section(section_content, output_file):
    """Save extracted section to file"""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(section_content)
    print(f"✅ Section saved to: {output_file}")


def print_section(section_content, max_lines=None):
    """Print section to console"""
    lines = section_content.split('\n')
    
    if max_lines and len(lines) > max_lines:
        print('\n'.join(lines[:max_lines]))
        print(f"\n... ({len(lines) - max_lines} more lines)")
    else:
        print(section_content)


def count_tokens_estimate(text):
    """Rough estimate of tokens (1 token ≈ 4 characters)"""
    return len(text) // 4


def main():
    if len(sys.argv) < 2:
        print("Usage: python bbp_extractor.py <section_number> [bbp_file] [output_file]")
        print("Example: python bbp_extractor.py 2.1")
        print("Example: python bbp_extractor.py 3.2 custom_bbp.md output.md")
        sys.exit(1)
    
    section_number = sys.argv[1]
    bbp_file = sys.argv[2] if len(sys.argv) > 2 else '01retail_bbp_v_0_3_till_3.md'
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    print(f"📄 Reading BBP file: {bbp_file}")
    print(f"🔍 Extracting section: {section_number}")
    
    try:
        section_content = extract_section(bbp_file, section_number)
        
        if not section_content:
            print(f"❌ Section {section_number} not found!")
            sys.exit(1)
        
        # Calculate token estimate
        token_count = count_tokens_estimate(section_content)
        lines_count = len(section_content.split('\n'))
        
        print(f"\n📊 Section Stats:")
        print(f"   Lines: {lines_count}")
        print(f"   Characters: {len(section_content):,}")
        print(f"   Estimated tokens: ~{token_count:,}")
        print(f"   Estimated cost (Sonnet 4): ~${(token_count * 3 / 1_000_000):.4f} (input only)")
        
        if output_file:
            save_section(section_content, output_file)
        else:
            print("\n" + "="*60)
            print_section(section_content, max_lines=50)
            print("="*60)
            
            # Ask if user wants to save
            save_choice = input("\n💾 Save to file? (y/n): ").strip().lower()
            if save_choice == 'y':
                default_output = f"section_{section_number.replace('.', '_')}.md"
                filename = input(f"Filename [{default_output}]: ").strip() or default_output
                save_section(section_content, filename)
    
    except FileNotFoundError:
        print(f"❌ BBP file not found: {bbp_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()



