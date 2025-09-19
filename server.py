import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

# Folder yang berisi file
FOLDERS = {
    "CONFIGS_FILES": "files/configs",
    "APLIKASI_FILES": "files/aplikasi",
    "SCRIPTS_FILES": "files/scripts"
}

class MyHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        """
        Override agar folder files bisa diakses langsung
        URL /files/... -> folder project/files/...
        """
        if path.startswith("/files/"):
            return os.path.join(os.getcwd(), path[1:])
        return super().translate_path(path)

    def do_GET(self):
        path_map = {
            "/": "index.html",
            "/index.html": "index.html",
            "/configs.html": "configs.html",
            "/aplikasi.html": "aplikasi.html",
            "/scripts.html": "scripts.html",
        }

        if self.path in path_map:
            file_name = path_map[self.path]
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    html = f.read()

                # Pilih folder yang akan ditampilkan berdasarkan halaman
                if file_name == "index.html":
                    placeholders = FOLDERS
                elif file_name == "configs.html":
                    placeholders = {"CONFIGS_FILES": FOLDERS["CONFIGS_FILES"]}
                elif file_name == "aplikasi.html":
                    placeholders = {"APLIKASI_FILES": FOLDERS["APLIKASI_FILES"]}
                elif file_name == "scripts.html":
                    placeholders = {"SCRIPTS_FILES": FOLDERS["SCRIPTS_FILES"]}
                else:
                    placeholders = {}

                # Loop tiap placeholder untuk generate list file
                for placeholder, folder in placeholders.items():
                    folder_path = os.path.join(os.getcwd(), folder)
                    files_list = ""

                    if os.path.exists(folder_path):
                        # Hanya file, urutkan berdasarkan modified time terbaru
                        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                        files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)

                        if files:
                            for file in files:
                                url_path = f"/{folder}/{file}"
                                files_list += f'''
<div class="download-item">
    <span>{file}</span>
    <a href="{url_path}" download="{file}">Download</a>
</div>
'''
                        else:
                            files_list = "<p>Files not found!</p>"
                    else:
                        files_list = "<p>Folder not found!</p>"

                    # Ganti placeholder di HTML
                    html = html.replace(f"{{{{{placeholder}}}}}", files_list)

                # Kirim response
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(html.encode())

            except FileNotFoundError:
                self.send_error(404, f"{file_name} Not Found!")
        else:
            # Biarkan SimpleHTTPRequestHandler menangani request lainnya
            super().do_GET()


if __name__ == "__main__":
    os.chdir(".")
    server = HTTPServer(("", PORT), MyHandler)
    try:
        print(f"Server running on port {PORT}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped!")
        server.server_close()