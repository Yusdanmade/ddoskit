# DDoS Toolkit - Termux Compatible

## 🚀 Termux'ta Çalıştırma (Git ile)

### 1. GitHub'dan Klonla
```bash
# Termux'ta çalıştır:
pkg update && pkg upgrade
pkg install git dotnet-sdk nodejs

# Repoyu klonla
git clone https://github.com/KULLANICIADI/DDoS-Toolkit.git
cd DDoS-Toolkit
```

### 2. Programı Çalıştır
```bash
# DDoS programı
dotnet run

# Ayrı terminalde sunucu için
node server.js
```

## 📱 Android Notları
- ✅ Termux'ta .NET desteği var
- ✅ Node.js sunucusu çalışır
- ✅ Tüm özellikler aktif
- ⚠️ Android performansı daha düşük

## 🔧 Kurulum Detayları
```bash
# Gerekli paketler
pkg install git dotnet-sdk nodejs curl wget

# .NET kontrol
dotnet --version

# Node.js kontrol  
node --version
```

## 🌐 GitHub Yükleme
1. Bu dosyaları GitHub'a yükle
2. Termux'ta `git clone` ile indir
3. `dotnet run` ile çalıştır