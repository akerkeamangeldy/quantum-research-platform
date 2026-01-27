#!/usr/bin/env python
import sys
import py_compile

try:
    py_compile.compile('quantum_workbench.py', doraise=True)
    print("✓ File compiles successfully!")
    sys.exit(0)
except SyntaxError as e:
    print(f"✗ Syntax Error: {e}")
    print(f"  File: {e.filename}")
    print(f"  Line: {e.lineno}")
    print(f"  Message: {e.msg}")
    sys.exit(1)
