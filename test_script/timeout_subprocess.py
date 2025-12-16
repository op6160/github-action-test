import subprocess
import time
import sys

timeout = 30 # 30秒

try:
    result = subprocess.run(
        ["python", "./timeout.py"],
        timeout=timeout
    )

finally:
    time.sleep(1)
    sys.exit(1)