import os
import sys
import json
import threading
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

todos = [
    {"id": 1, "content": "TODO 1"},
    {"id": 2, "content": "TODO 2"}
]
next_id = 3
lock = threading.Lock()

class BackendHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = self.path.split("?")[0].rstrip("/")
        if not path:
            path = "/"

        if path in ("/todos", "/"):
            with lock:
                data = list(todos)
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        global next_id
        path = self.path.split("?")[0].rstrip("/")
        if not path:
            path = "/"

        if path in ("/todos", "/"):
            content_length = int(self.headers.get("Content-Length", 0))
            raw_body = self.rfile.read(content_length).decode("utf-8")
            content_type = self.headers.get("Content-Type", "")

            todo_text = ""
            if "application/json" in content_type:
                try:
                    payload = json.loads(raw_body)
                    todo_text = payload.get("content") or payload.get("todo") or ""
                except Exception:
                    pass
            elif "application/x-www-form-urlencoded" in content_type:
                parsed = urllib.parse.parse_qs(raw_body)
                todo_text = (parsed.get("todo", [""])[0] or parsed.get("content", [""])[0])
            else:
                try:
                    payload = json.loads(raw_body)
                    todo_text = payload.get("content") or payload.get("todo") or ""
                except Exception:
                    todo_text = raw_body.strip()

            todo_text = todo_text.strip()
            if not todo_text:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"TODO content is required\n")
                return

            if len(todo_text) > 140:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"TODO content exceeds 140 characters\n")
                return

            with lock:
                new_todo = {"id": next_id, "content": todo_text}
                next_id += 1
                todos.append(new_todo)

            print(f"Added new todo: {new_todo}", flush=True)

            accept = self.headers.get("Accept", "")
            if "text/html" in accept and "application/json" not in accept:
                self.send_response(303)
                self.send_header("Location", "/")
                self.end_headers()
                return

            body = json.dumps(new_todo).encode("utf-8")
            self.send_response(201)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" % (self.address_string(), self.log_date_time_string(), format % args))

def main():
    port = int(os.environ.get("PORT", "3000"))
    server = HTTPServer(("", port), BackendHandler)
    print(f"Todo backend started on port {port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    main()