#!/usr/bin/env python3
"""
scripts/serve.py - GitHub Pages Local Dev Server with Live Reload & Clean URLs

Features:
1. Zero dependencies: Pure Python 3 standard library (http.server, socketserver).
2. GitHub Pages Simulation:
   - Clean URLs (/gym -> /gym/index.html or /gym.html).
   - Serves directory index.html automatically.
   - Proper MIME types (.woff2, .svg, .js, .json).
3. Zero Cache:
   - Sends 'Cache-Control: no-store, no-cache' so browser always sees latest files.
4. Auto Live-Reload:
   - Watches workspace files (.html, .css, .js, .svg, etc.).
   - Injects a lightweight reload snippet into HTML pages.
   - Automatically refreshes the browser when any file is saved.
"""

import os
import sys
import time
import mimetypes
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Ensure correct MIME types
mimetypes.init()
mimetypes.add_type("font/woff2", ".woff2")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/html; charset=utf-8", ".html")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Directories / extensions to ignore when watching for changes
IGNORE_DIRS = {".git", ".github", "__pycache__", ".vscode", ".idea", "tex"}
WATCH_EXTS = {".html", ".css", ".js", ".json", ".svg", ".png", ".jpg", ".jpeg", ".woff2"}


def get_latest_mtime(directory: str) -> float:
    """Recursively find the most recent file modification timestamp."""
    max_mtime = 0.0
    for root, dirs, files in os.walk(directory):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in WATCH_EXTS:
                try:
                    fp = os.path.join(root, file)
                    mt = os.path.getmtime(fp)
                    if mt > max_mtime:
                        max_mtime = mt
                except OSError:
                    continue
    return max_mtime


LIVE_RELOAD_SNIPPET = b"""
<!-- Live Reload Script (Local Dev Only) -->
<script>
(() => {
    let currentMtime = null;
    function checkUpdate() {
        fetch('/__livereload_ping__?t=' + Date.now())
            .then(res => res.text())
            .then(mtime => {
                if (currentMtime !== null && currentMtime !== mtime) {
                    console.log('[LiveReload] Change detected, reloading page...');
                    location.reload();
                }
                currentMtime = mtime;
            })
            .catch(() => {})
            .finally(() => {
                setTimeout(checkUpdate, 800);
            });
    }
    setTimeout(checkUpdate, 500);
})();
</script>
</body>
"""


class GitHubPagesHandler(SimpleHTTPRequestHandler):
    """HTTP Request Handler simulating GitHub Pages routing and zero-cache."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT_DIR, **kwargs)

    def end_headers(self):
        # Strictly disable browser caching so code edits reflect immediately
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        # 1. Handle live-reload timestamp query
        if self.path.startswith("/__livereload_ping__"):
            mtime = str(get_latest_mtime(ROOT_DIR))
            content = mtime.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        # 2. Simulate GitHub Pages URL mapping
        clean_path = self.path.split("?")[0].split("#")[0]
        local_rel = clean_path.lstrip("/")
        full_target = os.path.join(ROOT_DIR, local_rel)

        # Case A: /gym or /market -> directory with index.html (redirect to /gym/ for relative asset paths)
        if os.path.isdir(full_target) and not clean_path.endswith("/"):
            self.send_response(HTTPStatus.MOVED_PERMANENTLY)
            query = self.path[len(clean_path):]
            self.send_header("Location", clean_path + "/" + query)
            self.end_headers()
            return

        # Case B: clean URL without .html extension (e.g. /resume -> /resume.html)
        if not os.path.exists(full_target) and not clean_path.endswith("/"):
            if os.path.isfile(full_target + ".html"):
                self.path = clean_path + ".html"
            elif os.path.isfile(os.path.join(full_target, "index.html")):
                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
                self.send_header("Location", clean_path + "/")
                self.end_headers()
                return

        # Delegate normal static resolution to SimpleHTTPRequestHandler
        super().do_GET()

    def do_HEAD(self):
        if self.path.startswith("/__livereload_ping__"):
            mtime = str(get_latest_mtime(ROOT_DIR))
            content = mtime.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            return
        super().do_HEAD()

    def send_head(self):
        """Inject live-reload client script into HTML responses on the fly."""
        path = self.translate_path(self.path)
        f = None

        if os.path.isdir(path):
            parts = self.path.split("?")
            if not parts[0].endswith("/"):
                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
                new_url = parts[0] + "/" + ("?" + parts[1] if len(parts) > 1 else "")
                self.send_header("Location", new_url)
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index_path = os.path.join(path, index)
                if os.path.exists(index_path):
                    path = index_path
                    break
            else:
                return super().send_head()

        ctype = self.guess_type(path)

        # Inject reload snippet for HTML files
        if ctype.startswith("text/html") and os.path.isfile(path):
            try:
                with open(path, "rb") as source_file:
                    data = source_file.read()

                # Replace </body> with live reload snippet + </body>
                if b"</body>" in data:
                    data = data.replace(b"</body>", LIVE_RELOAD_SNIPPET)
                else:
                    data += LIVE_RELOAD_SNIPPET

                self.send_response(HTTPStatus.OK)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()

                import io
                return io.BytesIO(data)
            except OSError:
                self.send_error(HTTPStatus.NOT_FOUND, "File not found")
                return None

        return super().send_head()

    def log_message(self, format, *args):
        # Keep logs clean by ignoring repetitive reload ping requests
        if args and any("__livereload_ping__" in str(a) for a in args):
            return
        super().log_message(format, *args)


if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def run_server(port: int = 8000):
    TCPServer.allow_reuse_address = True
    server_address = ("", port)

    try:
        httpd = TCPServer(server_address, GitHubPagesHandler)
    except OSError as e:
        if "Address already in use" in str(e) or getattr(e, "winerror", 0) == 10048:
            print(f"[!] Port {port} is busy, trying port {port + 1}...")
            return run_server(port + 1)
        raise

    print("=" * 60)
    print(">> GitHub Pages Local Dev Server with Live Reload")
    print("=" * 60)
    print(f"   Root:       {ROOT_DIR}")
    print(f"   Homepage:   http://localhost:{port}/")
    print(f"   Gym Art:    http://localhost:{port}/gym")
    print(f"   Market:     http://localhost:{port}/market")
    print("   LiveReload: ENABLED (Auto-refreshes when files change)")
    print("   Cache:      DISABLED (Always reads latest files from disk)")
    print("=" * 60)
    print("Press Ctrl+C to stop the server.\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Server stopped.")
        httpd.server_close()


if __name__ == "__main__":
    port_arg = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8000
    run_server(port_arg)
