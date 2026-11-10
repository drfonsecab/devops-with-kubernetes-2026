import os
import sys
import time
import json
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

IMAGE_DIR = "/usr/src/app/files"
IMAGE_PATH = os.path.join(IMAGE_DIR, "image.jpg")
IMAGE_URL = "https://picsum.photos/1200"
BACKEND_URL = os.environ.get("BACKEND_URL", "http://todo-backend-svc:2345/todos")
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

def fetch_todos():
    try:
        req = urllib.request.Request(BACKEND_URL, headers={"User-Agent": "todo-frontend"})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"Error fetching todos from {BACKEND_URL}: {e}", flush=True)
        return [{"id": 0, "content": "Unable to load todos"}]

class TodoHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        if self.path == "/image.jpg":
            get_or_update_image()
            if os.path.exists(IMAGE_PATH):
                self.send_response(200)
                self.send_header("Content-Type", "image/jpeg")
                self.send_header("Content-Length", str(os.path.getsize(IMAGE_PATH)))
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
            return
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            return
        self.send_response(404)
        self.end_headers()

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
            todos_list = fetch_todos()
            
            todos_html = ""
            for item in todos_list:
                content = item.get("content", str(item)) if isinstance(item, dict) else str(item)
                todos_html += f"        <li>{content}</li>\n"

            html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Todo App</title>
</head>
<body>
    <h1>Todo App</h1>
    <p>DevOps with Kubernetes 2026 - Project</p>
    <img src="/image.jpg" width="400" alt="Daily picture" />
    <form action="/todos" method="POST" style="margin-top: 15px;">
        <input type="text" name="todo" maxlength="140" placeholder="New todo" required />
        <button type="submit">Create TODO</button>
    </form>
    <ul>
{todos_html}    </ul>
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

    def do_POST(self):
        # Handle form submission if routed to frontend
        content_length = int(self.headers.get("Content-Length", 0))
        raw_body = self.rfile.read(content_length).decode("utf-8")
        parsed = urllib.parse.parse_qs(raw_body)
        todo_text = parsed.get("todo", [""])[0]

        if todo_text:
            try:
                payload = json.dumps({"content": todo_text}).encode("utf-8")
                req = urllib.request.Request(
                    BACKEND_URL,
                    data=payload,
                    headers={"Content-Type": "application/json", "User-Agent": "todo-frontend"}
                )
                with urllib.request.urlopen(req, timeout=5) as resp:
                    pass
            except Exception as e:
                print(f"Error forwarding POST to backend: {e}", flush=True)

        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

def main():
    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), TodoHandler)
    print(f"Server started in port {port} (Backend at {BACKEND_URL})", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    main()