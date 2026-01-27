"""
Batch Translation Extraction for All Modules
Automatically extracts ALL user-facing strings from quantum_workbench.py
"""

import re
import json
from collections import defaultdict

def extract_module_strings(filepath):
    """Extract all strings organized by module"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all module sections
    module_pattern = r'elif module_id == "(.*?)":(.*?)(?=elif module_id ==|# MAIN APPLICATION LOGIC|$)'
    modules = re.findall(module_pattern, content, re.DOTALL)
    
    print(f"Found {len(modules)} modules\n")
    
    all_translations = defaultdict(lambda: {
        'en': {},
        'ru': {}
    })
    
    for module_id, module_content in modules:
        print(f"=== Processing {module_id.upper()} ===")
        
        strings = {
            'headings': [],
            'paragraphs': [],
            'labels': [],
            'buttons': [],
            'messages': [],
            'chart_titles': []
        }
        
        # Extract headings (# or ### in markdown)
        headings = re.findall(r'st\.markdown\s*\(["\']#{1,4}\s*([^"\'<]+)["\']', module_content)
        strings['headings'].extend(headings)
        
        # Extract plain paragraphs in research cards
        cards = re.findall(r'<div class=["\']research-card["\']>(.*?)</div>', module_content, re.DOTALL)
        for card in cards:
            # Extract <h3> content
            h3 = re.findall(r'<h3>([^<]+)</h3>', card)
            strings['headings'].extend(h3)
            # Extract <p> content
            paragraphs = re.findall(r'<p>([^<]+)</p>', card)
            strings['paragraphs'].extend(paragraphs)
        
        # Extract selectbox/radio labels
        labels = re.findall(r'st\.(selectbox|radio)\s*\(\s*["\']([^"\']+)["\']', module_content)
        strings['labels'].extend([label[1] for label in labels])
        
        # Extract slider labels
        sliders = re.findall(r'st\.slider\s*\(\s*["\']([^"\']+)["\']', module_content)
        strings['labels'].extend(sliders)
        
        # Extract button text
        buttons = re.findall(r'st\.button\s*\(\s*["\']([^"\']+)["\']', module_content)
        strings['buttons'].extend(buttons)
        
        # Extract status messages
        messages = re.findall(r'st\.(success|info|warning|error)\s*\(\s*[f]?["\']([^"\'{}]+)["\']', module_content)
        strings['messages'].extend([msg[1] for msg in messages])
        
        # Extract status.markdown messages
        status_msgs = re.findall(r'status\.markdown\s*\(["\'](?:\*\*)?([^"\'*<]+)(?:\*\*)?["\']', module_content)
        strings['messages'].extend(status_msgs)
        
        # Extract chart/figure titles from plotly
        chart_titles = re.findall(r'(title|xaxis_title|yaxis_title)\s*=\s*["\']([^"\'<]+)["\']', module_content)
        strings['chart_titles'].extend([title[1] for title in chart_titles])
        
        # Clean and deduplicate
        for category in strings:
            strings[category] = [s.strip() for s in strings[category] if s.strip() and len(s.strip()) > 2]
            strings[category] = list(dict.fromkeys(strings[category]))  # Remove duplicates
        
        # Print summary
        total = sum(len(strings[cat]) for cat in strings)
        print(f"  Headings: {len(strings['headings'])}")
        print(f"  Paragraphs: {len(strings['paragraphs'])}")
        print(f"  Labels: {len(strings['labels'])}")
        print(f"  Buttons: {len(strings['buttons'])}")
        print(f"  Messages: {len(strings['messages'])}")
        print(f"  Chart titles: {len(strings['chart_titles'])}")
        print(f"  TOTAL: {total} strings\n")
        
        # Store for JSON generation
        all_translations[module_id] = strings
    
    return all_translations

def generate_translation_keys(module_strings):
    """Generate translation key structure"""
    
    translations_en = {}
    translations_ru = {}
    
    for module_id, strings in module_strings.items():
        module_key = f"{module_id}_content"
        translations_en[module_key] = {}
        translations_ru[module_key] = {}
        
        # Generate keys for each category
        for category, items in strings.items():
            for idx, text in enumerate(items):
                key = f"{category[:-1]}_{idx+1}" if len(items) > 1 else category[:-1]
                translations_en[module_key][key] = text
                # Placeholder for Russian (to be filled manually or via API)
                translations_ru[module_key][key] = f"[RU] {text}"
    
    return translations_en, translations_ru

if __name__ == "__main__":
    print("BATCH TRANSLATION EXTRACTION\n")
    print("="*50 + "\n")
    
    module_strings = extract_module_strings('quantum_workbench.py')
    
    # Save detailed extraction
    with open('module_strings_extracted.json', 'w', encoding='utf-8') as f:
        json.dump(module_strings, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*50)
    print(f"✓ Extracted strings from {len(module_strings)} modules")
    print(f"✓ Saved to module_strings_extracted.json")
    
    # Calculate total
    total_strings = sum(
        sum(len(strings[cat]) for cat in strings)
        for strings in module_strings.values()
    )
    print(f"✓ Total strings to translate: {total_strings}")
