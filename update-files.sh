#!/bin/bash

# Simpan credential biar gak diminta ulang
git config --global credential.helper store

# Tambah semua perubahan
git add .

# Commit kalau ada perubahan
if ! git diff --cached --quiet; then
  git commit -m "Update otomatis $(date '+%Y-%m-%d %H:%M:%S')"
  git push
else
  echo "✅ Tidak ada perubahan untuk di-commit."
fi
