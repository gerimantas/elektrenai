#!/usr/bin/env python
"""Local dev server for the map: like `python -m http.server 8123`, but tells the
browser not to cache, so a plain reload always shows the latest edit.

Usage:  python gen_config.py && python serve.py   ->  http://localhost:8123/sklypas-google.html
"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

PORT = 8123


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


if __name__ == "__main__":
    handler = partial(NoCacheHandler, directory=str(Path(__file__).parent))
    print(f"http://localhost:{PORT}/sklypas-google.html")
    ThreadingHTTPServer(("127.0.0.1", PORT), handler).serve_forever()
