import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

counter = 0
lock = threading.Lock()

class PingPongHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        with lock:
            current = counter
            counter += 1
        
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
    print(f"PingPong server started on port {port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    main()