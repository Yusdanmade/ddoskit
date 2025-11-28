@echo off
echo 🚀 GitHub'a Yükleme Scripti
echo ================================

echo 1. Git başlatılıyor...
git init

echo 2. Dosyalar ekleniyor...
git add .
git commit -m "DDoS Toolkit - Termux Compatible"

echo 3. GitHub repo bağlantısı...
echo Lütfen GitHub repo URL'ini gir:
set /p repo_url="GitHub URL: "

git remote add origin %repo_url%
git branch -M main

echo 4. GitHub'a yükleniyor...
git push -u origin main

echo ✅ Yükleme tamamlandı!
pause