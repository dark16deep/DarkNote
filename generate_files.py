import os, json, datetime

FOLDERS = {
    "aplikasi": "files/aplikasi",
    "configs": "files/configs",
    "scripts": "files/scripts",
    "video": "files/video",
    "arsip": "files/arsip"
}

data = {}

for key, folder in FOLDERS.items():
    items = []
    if os.path.exists(folder):
        for f in os.listdir(folder):
            file_path = os.path.join(folder, f)
            if os.path.isfile(file_path):
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                items.append({
                    "name": f,
                    "path": file_path.replace("\\", "/"),
                    "date": mtime.strftime("%Y-%m-%d %H:%M")
                })
    items.sort(key=lambda x: x["date"], reverse=True)
    data[key] = items

with open("files.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ files.json berhasil digenerate")
