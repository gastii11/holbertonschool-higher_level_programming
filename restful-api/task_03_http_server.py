from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Base(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            # Endpoint raíz: texto plano
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            # Endpoint /data: JSON exacto que suele esperar el test
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"data": "Hello World"}  # Contenido exacto
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            # Endpoint /status: texto exacto
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")  # Contenido exacto

        else:
            # Cualquier otra ruta: 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


server_address = ('', 8000)
httpd = HTTPServer(server_address, Base)

print("Servidor escuchando en http://localhost:8000")
httpd.serve_forever()
