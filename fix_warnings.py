#!/usr/bin/env python3
"""Fix Streamlit deprecation warnings in AlphaNova Quantum"""

with open('alphanova_quantum.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix use_container_width deprecation
content = content.replace('use_container_width=True', "width='stretch'")

with open('alphanova_quantum.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed all use_container_width deprecation warnings")
print("🚀 AlphaNova Quantum platform is now updated for Streamlit compatibility")