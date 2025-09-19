#!/bin/bash
set -e  # berhenti kalau ada error

# Masuk ke folder repo
cd ~/DarkNote

# Simpan perubahan sementara kalau ada (stash)
git stash push -m "auto-stash before pull" || true

# Tarik update terbaru dari GitHub
git pull --rebase origin main

# Apply kembali perubahan lokal jika ada
git stash pop || true

# Jalankan script Python
python generate_files.py

# Lihat file json
cat files.json
ls -l files.json

# Set Git user
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Stage files.json
git add files.json

# Commit & push jika ada perubahan
if ! git diff --cached --quiet; then
  COMMIT_MSG="⚡ Update otomatis $(date '+%Y-%m-%d %H:%M:%S')"
  git commit -m "$COMMIT_MSG"
  echo "✅ Commit dibuat: $COMMIT_MSG"
  git push origin main
  echo "🚀 Perubahan berhasil dipush ke GitHub!"
else
  echo "✅ Tidak ada perubahan untuk di-commit."
fi
