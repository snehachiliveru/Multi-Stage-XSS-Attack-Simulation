# safe_logger.py
# Minimal HTTP server to accept benign JSON POSTs for POC demonstration only.
# Usage: python3 safe_logger.py --port 8000

import http.server
import socketserver
import json
import argparse

class Handler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(content_length).decode('utf-8', errors='replace')
        try:
            data = json.loads(raw)
        except Exception:
            data = {"raw": raw}
        print("POC received:", data)
        self._set_headers(200)
        self.wfile.write(json.dumps({"status":"ok","received":data}).encode('utf-8'))

    def log_message(self, format, *args):
        # quieter logging (still prints requests line)
        print("%s - - [%s] %s" % (self.client_address[0], self.log_date_time_string(), format%args))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    print(f"Listening on port {args.port} (safe logger) - Accepts JSON POSTs with synthetic tokens only.")
    with socketserver.TCPServer(('', args.port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down.")
            httpd.server_close()