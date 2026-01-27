print("Commit and push fix...")
import subprocess
import os
import sys

try:
    os.chdir(r'c:\Users\Lenovo\Desktop\quantum2')
    
    # Add all changes
    result1 = subprocess.run(['git', 'add', '.'], capture_output=True, text=True)
    print(f"Git add: {result1.returncode}")
    
    # Commit
    result2 = subprocess.run(['git', 'commit', '-m', 'Critical fix: Restore TRANSLATIONS_LEGACY structure to resolve IndentationError'], capture_output=True, text=True)
    print(f"Git commit: {result2.returncode}")
    if result2.stderr:
        print(f"Commit stderr: {result2.stderr}")
    
    # Push
    result3 = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
    print(f"Git push: {result3.returncode}")
    if result3.stderr:
        print(f"Push stderr: {result3.stderr}")
    
    print("✓ DEPLOYED")
    
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)