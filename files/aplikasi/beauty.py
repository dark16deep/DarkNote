import os
import sys
import time
import json
import re

def clear_screen():
    os.system("clear")

def progress(message, time_limit, delay):
    for i in range(time_limit + 1):
        percent = round((i / time_limit) * 100)
        progress_bar = "▬" * i + " " * (time_limit - i)
        sys.stdout.write(f"\r{message} [{progress_bar}] {percent}%\r")
        sys.stdout.flush()
        time.sleep(delay / 1_000_000)  # delay in microseconds
    sys.stdout.write(" " * 50 + "\r")
    sys.stdout.flush()

def pretty_json_match(match):
    json_str = match.group(0)
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        return json_str  # return as-is if not valid JSON

    pretty = json.dumps(data, indent=4, ensure_ascii=False)
    prefixed = "\n".join("║  " + line for line in pretty.splitlines())
    return prefixed

def main():
    clear_screen()
    time.sleep(1)

    print("PASTE KODE LALU TEKAN CTRL+D:\n")
    log = sys.stdin.read()

    progress("Processing", 30, 60000)
    time.sleep(1)
    clear_screen()

    formatted_log = re.sub(r"\{.*?\}", pretty_json_match, log, flags=re.S)

    print("\n=== HASIL KODE YANG DI RAPIKAN ===\n")
    print(formatted_log)

    output_file = "/sdcard/beauty.log"
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(formatted_log)
        print(f"\n\n✔ Hasil disimpan ke: {output_file}")
    except Exception:
        print(f"\n\n✘ Gagal menyimpan ke: {output_file}")
        print("Coba kasih izin Termux:  termux-setup-storage")

if __name__ == "__main__":
    main()