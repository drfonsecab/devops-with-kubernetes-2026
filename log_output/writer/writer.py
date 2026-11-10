import os
import time
import uuid
from datetime import datetime, timezone

def main():
    folder = "/usr/src/app/files"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "log.txt")
    
    instance_id = str(uuid.uuid4())
    print(f"Log writer started with ID: {instance_id}", flush=True)

    while True:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        content = f"{ts}: {instance_id}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Wrote to log.txt: {content.strip()}", flush=True)
        time.sleep(5)

if __name__ == "__main__":
    main()