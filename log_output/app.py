import time
import uuid
from datetime import datetime, timezone

def main():
    instance_id = str(uuid.uuid4())
    while True:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        print(f"{timestamp}: {instance_id}", flush=True)
        time.sleep(5)

if __name__ == "__main__":
    main()