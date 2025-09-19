#!/bin/bash
set -e

# Masuk ke repo
cd ~/DarkNote

echo "🔹 Memeriksa perubahan lokal..."
# Stash perubahan sementara supaya pull/rebase aman
git stash push -m "auto-stash before pull" || true

echo "🔹 Menarik update terbaru dari GitHub..."
git pull --rebase origin main || true

# Apply kembali stash jika ada
git stash pop || true

echo "🔹 Menjalankan generate_files.py..."
python generate_files.py

echo "🔹 Memeriksa files.json..."
ls -l files.json
cat files.json

# Set Git user
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Stage files.json
git add files.json

# Commit & push kalau ada perubahan
if ! git diff --cached --quiet; then
  COMMIT_MSG="⚡ Update otomatis $(date '+%Y-%m-%d %H:%M:%S')"
  git commit -m "$COMMIT_MSG"
  git push origin main
  echo "✅ Perubahan berhasil dipush ke GitHub!"
else
  echo "✅ Tidak ada perubahan untuk di-commit."
fi

echo "🔹 Selesai. Repo sekarang sinkron dengan GitHub."
