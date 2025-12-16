import time

def printer(msg):
    print(f"[timeout.py] [log]: {msg} {time.strftime('%H:%M:%S')}")

def main():
    cnt = 0
    while(cnt != 1000):
        cnt += 1
        time.sleep(1)
        printer(cnt)
    printer(f"Time Limit Exceeded {cnt}(s)")

if __name__ == "__main__":
    main()