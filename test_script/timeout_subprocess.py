import subprocess
import time
import sys

timeout = 30 # 30秒

try:
    result = subprocess.run(
        ["python", "./timeout.py"],
        timeout=timeout, 
        capture_output=True, 
        text=True
    )

    print(result.stdout)

except subprocess.TimeoutExpired:
    print(f"[timeout_subprocess.py] [log]: Time Limit Exceeded({timeout}s) {time.strftime('%H:%M:%S')}")
    sys.exit(1)