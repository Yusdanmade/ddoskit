#!/bin/bash
# Termux Installation Script for Network Security Toolkit

echo "🛡️ Network Security Toolkit - Termux Installer"
echo "=============================================="

# Update packages
echo "📦 Updating Termux packages..."
pkg update -y && pkg upgrade -y

# Install required packages
echo "🔧 Installing dependencies..."
pkg install -y git curl wget unzip nano
pkg install -y clang cmake make
pkg install -y openssl libcurl
pkg install -y dotnet

# Create directory
echo "📁 Creating application directory..."
mkdir -p ~/NetworkSecurityToolkit
cd ~/NetworkSecurityToolkit

# Download .NET if not available
if ! command -v dotnet &> /dev/null; then
    echo "📦 Installing .NET SDK..."
    wget https://download.visualstudio.microsoft.com/download/pr/8c4b4b7c-3b2c-4b2c-9c2c-3b2c4b2c9c2c/dotnet-sdk-7.0.404-linux-x64.tar.gz
    mkdir -p ~/.dotnet
    tar xzf dotnet-sdk-7.0.404-linux-x64.tar.gz -C ~/.dotnet
    echo 'export DOTNET_ROOT=$HOME/.dotnet' >> ~/.bashrc
    echo 'export PATH=$PATH:$HOME/.dotnet' >> ~/.bashrc
    export DOTNET_ROOT=$HOME/.dotnet
    export PATH=$PATH:$HOME/.dotnet
fi

# Create launcher script
echo "🚀 Creating launcher script..."
cat > ~/NetworkSecurityToolkit/nst.sh << 'EOF'
#!/bin/bash
cd ~/NetworkSecurityToolkit
echo "🛡️ Starting Network Security Toolkit..."
dotnet run
EOF

chmod +x ~/NetworkSecurityToolkit/nst.sh

# Create desktop shortcut
echo "📱 Creating desktop shortcut..."
mkdir -p ~/Desktop
cat > ~/Desktop/NetworkSecurityToolkit << 'EOF'
#!/bin/bash
cd ~/NetworkSecurityToolkit
./nst.sh
EOF

chmod +x ~/Desktop/NetworkSecurityToolkit

echo "✅ Installation complete!"
echo ""
echo "🚀 To run the toolkit:"
echo "   Method 1: ~/NetworkSecurityToolkit/nst.sh"
echo "   Method 2: ~/Desktop/NetworkSecurityToolkit"
echo "   Method 3: cd ~/NetworkSecurityToolkit && dotnet run"
echo ""
echo "🛡️ Network Security Toolkit is ready to use!"