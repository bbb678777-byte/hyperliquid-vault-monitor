# collector/main.py
import time
import signal
import sys
from datetime import datetime

RUNNING = True


def handle_exit(signum, frame):
    global RUNNING
    print(f"\n[collector] received signal {signum}, shutting down...")
    RUNNING = False


def collector_loop():
    print("[collector] Vault Monitor V3 collector started")

    tick = 0
    while RUNNING:
        tick += 1

        snapshot = {
            "vault": "example-vault",
            "tvl": 1_000_000 + tick * 1000,
            "timestamp": datetime.utcnow().isoformat()
        }

        print(f"[collector] tick={tick} snapshot={snapshot}")

        time.sleep(5)

    print("[collector] collector stopped gracefully")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)

    try:
        collector_loop()
    except Exception as e:
        print(f"[collector] fatal error: {e}")
        sys.exit(1)
