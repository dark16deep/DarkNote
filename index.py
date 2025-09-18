import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080
FOLDERS = {
    "CONFIGS_FILES": "files/configs",
    "APLIKASI_FILES": "files/aplikasi"
}

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        path_map = {
            "/": "index.html",
            "/index.html": "index.html",
            "/configs.html": "configs.html",
            "/aplikasi.html": "aplikasi.html"
        }

        if self.path in path_map:
            file_name = path_map[self.path]
            try:
                with open(file_name, "r") as f:
                    html = f.read()

                # Tentukan placeholder sesuai file
                if file_name == "index.html":
                    placeholders = FOLDERS
                elif file_name == "configs.html":
                    placeholders = {"CONFIGS_FILES": FOLDERS["CONFIGS_FILES"]}
                elif file_name == "aplikasi.html":
                    placeholders = {"APLIKASI_FILES": FOLDERS["APLIKASI_FILES"]}
                else:
                    placeholders = {}

                # Replace placeholder dengan daftar file
                for placeholder, folder in placeholders.items():
                    files_list = ""
                    if os.path.exists(folder):
                        files = os.listdir(folder)
                        if files:
                            for file in files:
                                files_list += f'''
<div class="download-item">
    <span>{file}</span>
    <a href="{folder}/{file}" download>Download</a>
</div>
'''
                        else:
                            files_list = "<p>Folder kosong</p>"
                    else:
                        files_list = "<p>Folder tidak ditemukan</p>"

                    html = html.replace(f"{{{{{placeholder}}}}}", files_list)

                # Kirim response
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())

            except FileNotFoundError:
                self.send_error(404, f"{file_name} tidak ditemukan")
        else:
            super().do_GET()

# Jalankan server dengan clean exit saat Ctrl+C
os.chdir(".")
server = HTTPServer(("", PORT), MyHandler)
try:
    print(f"Server jalan di port {PORT}")
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer dihentikan.")
    server.server_close()