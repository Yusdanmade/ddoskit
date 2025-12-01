#!/bin/bash
# Termux Installation Script for DDoS Toolkit

echo "🚀 DDoS Toolkit - Termux Installer"
echo "=================================="

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
mkdir -p ~/DDoSToolkit
cd ~/DDoSToolkit

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
cat > ~/DDoSToolkit/ddos.sh << 'EOF'
#!/bin/bash
cd ~/DDoSToolkit
echo "🚀 Starting DDoS Toolkit..."
dotnet run
EOF

chmod +x ~/DDoSToolkit/ddos.sh

# Create desktop shortcut
echo "📱 Creating desktop shortcut..."
mkdir -p ~/Desktop
cat > ~/Desktop/DDoSToolkit << 'EOF'
#!/bin/bash
cd ~/DDoSToolkit
./ddos.sh
EOF

chmod +x ~/Desktop/DDoSToolkit

echo "✅ Installation complete!"
echo ""
echo "🚀 To run the toolkit:"
echo "   Method 1: ~/DDoSToolkit/ddos.sh"
echo "   Method 2: ~/Desktop/DDoSToolkit"
echo "   Method 3: cd ~/DDoSToolkit && dotnet run"
echo ""
echo "⚡ DDoS Toolkit is ready to use!"