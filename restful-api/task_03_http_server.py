from http.server import HTTPServer, BaseHTTPRequestHandler

class Base(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            import json
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"message": "This is some JSON data"}  # ejemplo de JSON
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Status is OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

server_address = ('', 8000)
httpd = HTTPServer(server_address, Base)

print("Servidor escuchando en http://localhost:8000")
httpd.serve_forever()
