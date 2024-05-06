import http.server
import socketserver

# Convert wasm module.
#  py2wasm sample.py -o sample.wasm
# Running the server.
#  python server.py
#

PORT = 8000

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

Handler = HTTPRequestHandler
Handler.extensions_map['.wasm'] = 'application/wasm'

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()