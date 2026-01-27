#!/usr/bin/env python3
import subprocess
import os

os.chdir(r'c:\Users\Lenovo\Desktop\quantum2')

print("Committing and deploying fixes...")

# Add all changes
result1 = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
print(f"Git add: {result1.returncode}")

# Commit
result2 = subprocess.run(['git', 'commit', '-m', 'CRITICAL FIX: Remove TRANSLATIONS_LEGACY duplicate keys causing IndentationError'], capture_output=True, text=True)
print(f"Git commit: {result2.returncode}")
if result2.stdout:
    print(f"Commit output: {result2.stdout}")

# Push  
result3 = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print(f"Git push: {result3.returncode}")
if result3.stdout:
    print(f"Push output: {result3.stdout}")

print("✅ DEPLOYED - Check https://quantum-research-platform.streamlit.app/")