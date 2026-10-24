#!/usr/bin/python3
"""Module that implements a simple API using the http.server module."""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """Handler that answers GET requests for a small set of endpoints."""

    def do_GET(self):
        """Handle GET requests and route them according to the path."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))


def run(port=8000):
    """Start the HTTP server and serve requests until it is stopped."""
    server = http.server.HTTPServer(("", port), SimpleAPIHandler)
    print("Serving on port {}".format(port))
    server.serve_forever()


if __name__ == "__main__":
    run()
