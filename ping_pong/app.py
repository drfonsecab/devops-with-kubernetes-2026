import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

FILE_PATH = "/usr/src/app/files/pingpong.txt"
lock = threading.Lock()

def read_counter():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as f:
                val = f.read().strip()
                if val.isdigit():
                    return int(val)
        except Exception as e:
            print(f"Error reading {FILE_PATH}: {e}", flush=True)
    return 0

def write_counter(val):
    folder = os.path.dirname(FILE_PATH)
    os.makedirs(folder, exist_ok=True)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(str(val))

counter = read_counter()

class PingPongHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        with lock:
            current = counter
            counter += 1
            write_counter(counter)
        
        body = f"pong {current}\n".encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

def main():
    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), PingPongHandler)
    print(f"PingPong server started on port {port} (initial count: {counter})", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    main()