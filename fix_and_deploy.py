import subprocess
import os

os.chdir(r'c:\Users\Lenovo\Desktop\quantum2')

# Reset the file to last commit
print("Resetting file...")
result = subprocess.run(['git', 'checkout', 'HEAD~1', '--', 'quantum_workbench.py'], 
                       capture_output=True, text=True)
print(f"Reset: {result.returncode}")

# Check status
result = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True)
print(f"Status:\n{result.stdout}")

# Add file
result = subprocess.run(['git', 'add', 'quantum_workbench.py'], capture_output=True, text=True)
print(f"Add: {result.returncode}")

# Commit
result = subprocess.run(['git', 'commit', '-m', 'Fix: Restore to working version before IndentationError'], 
                       capture_output=True, text=True)
print(f"Commit: {result.returncode}\n{result.stdout}")

# Push
result = subprocess.run(['git', 'push', 'origin', 'main'], capture_output=True, text=True)
print(f"Push: {result.returncode}\n{result.stdout}\n{result.stderr}")

print("\nDone! Check https://quantum-research-platform.streamlit.app/")
