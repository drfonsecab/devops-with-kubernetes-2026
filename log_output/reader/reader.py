import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

LOG_PATH = "/usr/src/app/files/log.txt"
PINGPONG_PATH = "/usr/src/app/files/pingpong.txt"

class LogReaderHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        log_text = "Waiting for log..."
        if os.path.exists(LOG_PATH):
            try:
                with open(LOG_PATH, "r", encoding="utf-8") as f:
                    log_text = f.read().strip()
            except Exception as e:
                log_text = f"Error reading log: {e}"

        if not log_text.endswith("."):
            log_text += "."

        pongs = 0
        if os.path.exists(PINGPONG_PATH):
            try:
                with open(PINGPONG_PATH, "r", encoding="utf-8") as f:
                    val = f.read().strip()
                    if val.isdigit():
                        pongs = int(val)
            except Exception as e:
                print(f"Error reading pingpong file: {e}", flush=True)

        body = f"{log_text}\nPing / Pongs: {pongs}\n".encode("utf-8")
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