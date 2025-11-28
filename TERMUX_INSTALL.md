# Termux için .NET Kurulumu

## 1. Termux Kurulumu
- F-Droid'den Termux'u indir
- Termux'u aç ve güncelle:
```bash
pkg update && pkg upgrade
```

## 2. .NET SDK Kurulumu
```bash
# .NET SDK'yı kur
pkg install dotnet-sdk

# Kurulumu kontrol et
dotnet --version
```

## 3. Proje Kopyalama
Bilgisayardaki DDoS klasörünü telefondaki konuma kopyala:
- `/sdcard/Download/DDoS/`
- veya `/storage/emulated/0/Download/DDoS/`

## 4. Çalıştırma
```bash
# Proje klasörüne git
cd /sdcard/Download/DDoS

# Programı çalıştır
dotnet run
```

## 5. Sunucu için (Node.js)
```bash
# Node.js kur
pkg install nodejs

# Sunucuyu başlat
node server.js
```

## NOTLAR:
- ✅ Aynı kod, hiçbir değişiklik yok
- ✅ Tüm özellikler çalışır
- ✅ Güvenlik ayarları aktif
- ⚠️ Android performansı daha düşük olabilir