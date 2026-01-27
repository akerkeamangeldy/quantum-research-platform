import subprocess
import sys

try:
    result = subprocess.run(['git', 'checkout', 'HEAD', '--', 'quantum_workbench.py'], 
                          capture_output=True, text=True, cwd=r'c:\Users\Lenovo\Desktop\quantum2')
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
    sys.exit(result.returncode)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
