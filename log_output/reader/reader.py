import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

class LogReaderHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        filepath = "/usr/src/app/files/log.txt"
        content = "Waiting for log...\n"
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"Error reading log: {e}\n"

        body = content.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass

def main():
    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), LogReaderHandler)
    print(f"Log reader HTTP server started on port {port}", flush=True)
    server.serve_forever()

if __name__ == "__main__":
    main()