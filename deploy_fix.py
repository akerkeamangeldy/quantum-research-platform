#!/usr/bin/env python3
import subprocess
import sys
import os

os.chdir(r'c:\Users\Lenovo\Desktop\quantum2')

# First verify the file compiles
print("Checking syntax...")
try:
    import py_compile
    py_compile.compile('quantum_workbench.py', doraise=True)
    print("✓ Syntax OK")
except SyntaxError as e:
    print(f"✗ Syntax error at line {e.lineno}: {e.msg}")
    sys.exit(1)

# Git operations
commands = [
    (['git', 'add', 'quantum_workbench.py'], "Adding file"),
    (['git', 'commit', '-m', 'Fix: Restore proper TRANSLATIONS dict structure'], "Committing"),
    (['git', 'push', 'origin', 'main'], "Pushing to GitHub")
]

for cmd, desc in commands:
    print(f"\n{desc}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ {desc} successful")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"✗ {desc} failed")
        if result.stderr:
            print(result.stderr)
        if "nothing to commit" in result.stdout:
            print("(No changes to commit)")

print("\n✓ Done! Check https://quantum-research-platform.streamlit.app/")
