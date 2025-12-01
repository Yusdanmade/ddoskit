# Network Security Toolkit 2025

🛡️ **Advanced Network Security Analysis Toolkit**

## 📋 Features

### 🔍 Network Analysis Tools
- **Port Scanner** - Comprehensive port scanning with customizable ranges
- **Network Discovery** - Automatic device detection on local networks
- **Packet Sniffer** - Real-time packet capture and analysis
- **Traffic Analyzer** - Network traffic monitoring and statistics

### 🚨 Security Tools
- **Intrusion Detection System** - Real-time threat monitoring
- **Firewall Manager** - IP and port rule management
- **Password Auditor** - Password strength analysis and cracking simulation
- **Encryption Tools** - AES, RSA encryption and hash generation

## 🚀 Quick Start

### Windows
```batch
# Double-click or run:
NetworkSecurityToolkit.bat
```

### Termux (Android)
```bash
# Install dependencies
pkg update && pkg install -y git curl wget clang cmake make openssl libcurl dotnet

# Clone and run
git clone <repository-url>
cd NetworkSecurityToolkit
chmod +x start.sh
./start.sh
```

### Manual Installation
```bash
# Install .NET (if not installed)
dotnet --version

# Build and run
dotnet build
dotnet run
```

## 📱 Termux Support

### Automatic Installation
```bash
# Download and run installer
wget https://raw.githubusercontent.com/user/repo/main/install_termux.sh
chmod +x install_termux.sh
./install_termux.sh
```

### Manual Termux Setup
```bash
# 1. Update packages
pkg update -y && pkg upgrade -y

# 2. Install dependencies
pkg install -y clang cmake make openssl libcurl dotnet

# 3. Run the toolkit
cd NetworkSecurityToolkit
./start.sh
```

## 🔧 Requirements

- **.NET 7.0** or higher
- **Windows 10+** or **Termux (Android)**
- **Administrator privileges** (for some features)

## 🛡️ Security Features

### Real-time Monitoring
- Live packet capture
- Intrusion detection alerts
- Traffic pattern analysis
- Automated threat response

### Encryption & Security
- AES-256 encryption/decryption
- RSA key generation
- SHA-256 hash calculation
- Secure password generation

### Network Analysis
- Multi-threaded port scanning
- Network device discovery
- Protocol analysis
- Bandwidth monitoring

## 📊 Usage Examples

### Port Scanning
```
Target: 192.168.1.1
Port Range: 1-1000
Results: 5 open ports found
```

### Network Discovery
```
Network: 192.168.1.0/24
Devices Found: 12
Scan Time: 2.3 seconds
```

### Password Analysis
```
Password: MySecurePass123!
Strength: Strong (5/5)
Crack Time: ~3 years
```

## ⚠️ Legal Notice

This toolkit is designed for:
- Educational purposes
- Network security testing
- Authorized penetration testing
- Security research

**Only use on networks and systems you own or have explicit permission to test.**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

- **Issues**: Report bugs via GitHub Issues
- **Features**: Request new features via Discussions
- **Security**: Report security vulnerabilities privately

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**🛡️ Network Security Toolkit 2025 - Your Complete Security Analysis Solution**