#!/usr/bin/python3
import http.server
import socketserver
import json

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data).encode("utf-8")
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(response)

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested resource was not found on this server.")

PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running on http://localhost:{PORT}")
    httpd.serve_forever()
