from http.server import HTTPServer, BaseHTTPRequestHandler

class Base(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(b"Hello, this is a simple API!")

server_address = ('', 8000)
httpd = HTTPServer(server_address, Base)

print("Servidor escuchando en http://localhost:8000")
httpd.serve_forever()
