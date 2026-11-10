import os
import sys
import time
import uuid
import threading
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler

current_status = ""
status_lock = threading.Lock()

def timestamp_loop(instance_id):
    global current_status
    while True:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        line = f"{ts}: {instance_id}"
        with status_lock:
            current_status = line
        print(line, flush=True)
        time.sleep(5)

class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        with status_lock:
            body = (current_status + "\n").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

def main():
    instance_id = str(uuid.uuid4())
    t = threading.Thread(target=timestamp_loop, args=(instance_id,), daemon=True)
    t.start()
    time.sleep(0.1)

    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), StatusHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()