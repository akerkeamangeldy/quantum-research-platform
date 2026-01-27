#!/usr/bin/env python3
import ast
import traceback

try:
    print("Checking quantum_workbench.py syntax...")
    with open('quantum_workbench.py', 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Parse the AST
    ast.parse(code)
    print("✅ SUCCESS: File compiles without errors!")
    
except SyntaxError as e:
    print(f"❌ SYNTAX ERROR:")
    print(f"   File: {e.filename}")
    print(f"   Line: {e.lineno}")
    print(f"   Column: {e.offset}")
    print(f"   Error: {e.msg}")
    print(f"   Text: {repr(e.text)}")
    
except Exception as e:
    print(f"❌ OTHER ERROR: {e}")
    traceback.print_exc()
