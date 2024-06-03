#!/usr/bin/python3
""" Nameless module for Task 3 """


import json
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

class WebRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            d = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(bytes(d, 'UTF-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "plain/text")
            self.end_headers()

            self.wfile.write("OK".encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write("404 Not Found".encode())


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    print("Web server started at localhost:8000")
    server.serve_forever()
