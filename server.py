import http.server;
import socketserver;

PORT = 8080;
Handler = http.server.SimpleHTTPRequestHandler;

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Starting server");
    httpd.serve_forever();


