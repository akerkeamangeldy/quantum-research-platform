"""
Automatic string extraction tool for i18n
Finds all user-visible strings in quantum_workbench.py
"""

import re
import json

def extract_strings_from_file(filepath):
    """Extract all user-visible strings from Python file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Patterns to extract
    patterns = [
        # st.markdown with headings
        (r'st\.markdown\s*\(\s*["\']#+\s*([^"\']+)["\']', 'markdown_heading'),
        # st.markdown with plain text (excluding HTML/LaTeX)
        (r'st\.markdown\s*\(\s*["\']([^<\$\{][^"\']{10,100})["\']', 'markdown_text'),
        # st.title, st.header, st.subheader
        (r'st\.(title|header|subheader)\s*\(\s*["\']([^"\']+)["\']', 'heading'),
        # st.selectbox, st.radio first param
        (r'st\.(selectbox|radio)\s*\(\s*["\']([^"\']+)["\']', 'control_label'),
        # st.slider first param
        (r'st\.slider\s*\(\s*["\']([^"\']+)["\']', 'slider_label'),
        # st.button first param
        (r'st\.button\s*\(\s*["\']([^"\']+)["\']', 'button_text'),
        # st.success, st.info, st.warning, st.error
        (r'st\.(success|info|warning|error)\s*\(\s*[f]?["\']([^"\']+)["\']', 'message'),
        # List items in arrays
        (r'\[\s*"([^"]{5,50})"[\s,]+', 'list_item'),
    ]
    
    extracted = {}
    
    for pattern, category in patterns:
        matches = re.findall(pattern, content, re.MULTILINE)
        for match in matches:
            text = match if isinstance(match, str) else match[-1]
            # Clean up
            text = text.strip()
            # Skip if contains code markers, HTML, LaTeX
            if any(marker in text for marker in ['<', '>', '{', '}', '\\', 'class=', 'div', 'span']):
                continue
            # Skip if too short
            if len(text) < 3:
                continue
            # Skip if looks like a key
            if text.replace('_', '').replace('.', '').isalnum() and '_' in text:
                continue
                
            if category not in extracted:
                extracted[category] = []
            if text not in extracted[category]:
                extracted[category].append(text)
    
    return extracted

if __name__ == "__main__":
    strings = extract_strings_from_file('quantum_workbench.py')
    
    print("=== EXTRACTED STRINGS ===\n")
    for category, items in strings.items():
        print(f"\n{category.upper()} ({len(items)} items):")
        for item in items[:10]:  # Show first 10
            print(f"  - {item[:80]}")
        if len(items) > 10:
            print(f"  ... and {len(items) - 10} more")
    
    # Save to JSON
    with open('extracted_strings.json', 'w', encoding='utf-8') as f:
        json.dump(strings, f, ensure_ascii=False, indent=2)
    
    print("\n\n✓ Saved to extracted_strings.json")
