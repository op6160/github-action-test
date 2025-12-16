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

    print(result.stdout, flush=True)

except subprocess.TimeoutExpired:
    print(f"[timeout_subprocess.py] [log]: Time Limit Exceeded({timeout}s) {time.strftime('%H:%M:%S')}", flush=True)


finally:
    sys.exit(1)