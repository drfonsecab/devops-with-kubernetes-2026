import os
import sys
import time
import urllib.request
from http.server import HTTPServer, BaseHTTPRequestHandler

IMAGE_DIR = "/usr/src/app/files"
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")
IMAGE_URL = "https://picsum.photos/1200"
CACHE_SECONDS = 600

def get_or_update_image():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    need_download = False
    
    if not os.path.exists(IMAGE_PATH):
        need_download = True
    else:
        file_age = time.time() - os.path.getmtime(IMAGE_PATH)
        if file_age > CACHE_SECONDS:
            need_download = True

    if need_download:
        print("Downloading new image from picsum...", flush=True)
        try:
            req = urllib.request.Request(
                IMAGE_URL,
                headers={"User-Agent": "Mozilla/5.0"}
            )
            with urllib.request.urlopen(req, timeout=15) as response:
                img_data = response.read()
                tmp_path = IMAGE_PATH + ".tmp"
                with open(tmp_path, "wb") as f:
                    f.write(img_data)
                os.replace(tmp_path, IMAGE_PATH)
            print("Image downloaded successfully.", flush=True)
        except Exception as e:
            print(f"Error fetching image: {e}", flush=True)

class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/image.jpg":
            get_or_update_image()
            if os.path.exists(IMAGE_PATH):
                with open(IMAGE_PATH, "rb") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "image/jpeg")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"Image not found")
            return

        if self.path in ("/", "/index.html"):
            get_or_update_image()
            html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <p>DevOps with Kubernetes 2026 - Project</p>
    <img src="/image.jpg" width="400" alt="Daily picture" />
</body>
</html>
"""
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

def main():
    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), TodoHandler)
    print(f"Server started in port {port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    main()