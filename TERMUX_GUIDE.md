# Python DDoS Toolkit - Termux Installation Guide

## 🐍 Termux'ta Çalıştırma

### Method 1: Direct Python Execution
```bash
# 1. Repository'i klonla
git clone https://github.com/Yusdanmade/ddoskit.git
cd ddoskit

# 2. Python kur (yoksa)
pkg update && pkg install python

# 3. Doğrudan çalıştır
python3 test_ddos.py
```

### Method 2: Manual Script Setup
```bash
# 1. Script'i oluştur
cat > run_ddos.sh << 'EOF'
#!/bin/bash
echo "🚀 Starting DDoS Toolkit..."
cd ~/ddoskit
python3 test_ddos.py
EOF

# 2. Çalıştırma izni ver
chmod +x run_ddos.sh

# 3. Çalıştır
./run_ddos.sh
```

### Method 3: One-Liner
```bash
git clone https://github.com/Yusdanmade/ddoskit.git && cd ddoskit && python3 test_ddos.py
```

## 🔧 Windows'ta Çalıştırma

### Method 1: Batch File
```batch
# Double-click or run:
run_python_ddos.bat
```

### Method 2: Command Line
```cmd
git clone https://github.com/Yusdanmade/ddoskit.git
cd ddoskit
python test_ddos.py
```

## ⚠️ Sorun Giderme

### "cannot access" hatası alırsan:
```bash
# Dosya izinlerini kontrol et
ls -la start_python.sh

# İzin ver
chmod +x start_python.sh

# Veya doğrudan python ile çalıştır
python3 test_ddos.py
```

### Python bulunamazsa:
```bash
# Python kur
pkg install python

# Kontrol et
python3 --version
```

### Repository bulunamazsa:
```bash
# Internet bağlantısını kontrol et
ping google.com

# Manuel indir
wget https://github.com/Yusdanmade/ddoskit/archive/main.zip
unzip main.zip
cd ddoskit-main
python3 test_ddos.py
```

## 📱 Termux Optimizasyonu

### Performans için:
```bash
# CPU optimizasyonu
export OMP_NUM_THREADS=4

# Memory limit
export MALLOC_ARENA_MAX=2

# Çalıştır
python3 test_ddos.py
```

### Battery optimizasyonunu kapat:
```bash
# Termux ayarlarından battery optimization'ı kapat
# veya:
termux-wake-lock
```

## 🚀 Hızlı Başlatma

### Alias oluştur:
```bash
# .bashrc'ye ekle
echo 'alias ddos="cd ~/ddoskit && python3 test_ddos.py"' >> ~/.bashrc
source ~/.bashrc

# Artık sadece yaz:
ddos
```

## 📊 Test

### Local test:
```bash
# Localhost test
python3 -c "
import test_ddos
test_ddos.single_target_attack()
"
```

### Network test:
```bash
# Ağ testi
ping -c 3 google.com
python3 test_ddos.py
```

---

**🚀 Python DDoS Toolkit - Termux Compatible**