import http.server
import socketserver
import webbrowser
import os

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print("=" * 60)
        print(f"🚀 Portal @menosdametade.oficial rodando em:")
        print(f"👉 {url}")
        print("=" * 60)
        print("Pressione Ctrl+C para encerrar o servidor.")
        webbrowser.open(url)
        httpd.serve_forever()

if __name__ == "__main__":
    start_server()
