import ast
try:
    with open('quantum_workbench.py', 'r', encoding='utf-8') as f:
        code = f.read()
    ast.parse(code)
    print("SUCCESS")
except SyntaxError as e:
    print(f"ERROR at line {e.lineno}: {e.msg}")
