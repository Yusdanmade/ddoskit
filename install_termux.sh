#!/bin/bash
# DDoS Toolkit - Termux Kurulum Scripti

echo "🚀 DDoS Toolkit - Termux Kurulumu"
echo "=================================="

# Sistem güncelleme
echo "📦 Sistem güncelleniyor..."
pkg update && pkg upgrade -y

# Gerekli paketler
echo "📦 Gerekli paketler kuruluyor..."
pkg install -y git dotnet-sdk nodejs curl wget

# .NET kontrol
echo "🔍 .NET kontrol ediliyor..."
dotnet --version

# Node.js kontrol
echo "🔍 Node.js kontrol ediliyor..."
node --version

echo "✅ Kurulum tamamlandı!"
echo ""
echo "🚀 Çalıştırmak için:"
echo "cd DDoS-Toolkit"
echo "dotnet run"
echo ""
echo "🌐 Sunucu için:"
echo "node server.js"