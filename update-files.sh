#!/bin/bash

# Simpan credential biar gak diminta ulang
git config --global credential.helper store

# Sync dulu biar gak ada konflik
echo "🔄 Menarik update terbaru dari GitHub..."
git pull --rebase origin main

# Tambah semua perubahan
git add .

# Commit kalau ada perubahan
if ! git diff --cached --quiet; then
  COMMIT_MSG="⚡ Update otomatis $(date '+%Y-%m-%d %H:%M:%S')"
  git commit -m "$COMMIT_MSG"
  echo "✅ Commit dibuat: $COMMIT_MSG"
  
  # Push ke GitHub
  git push
  echo "🚀 Perubahan berhasil dipush ke GitHub!"
else
  echo "✅ Tidak ada perubahan untuk di-commit."
fi
