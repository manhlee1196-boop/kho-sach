# -*- coding: utf-8 -*-
"""Server xem lá số — tắt cache để luôn thấy bản mới nhất."""
import functools, http.server, os, socketserver

ROOT = os.path.dirname(os.path.abspath(__file__))

class NoCache(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()
    def log_message(self, fmt, *a):
        print("%s - %s" % (self.address_string(), fmt % a), flush=True)

class Srv(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == "__main__":
    with Srv(("0.0.0.0", 8848), functools.partial(NoCache, directory=ROOT)) as httpd:
        print("phục vụ", ROOT, "tại http://0.0.0.0:8848  (Cache-Control: no-store)", flush=True)
        httpd.serve_forever()
