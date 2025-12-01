#!/bin/bash
# DDoS Toolkit - Termux Launcher
# Made for Termux on Android

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                🚀 NUCLEAR DDoS ULTIMATE 2025              ║"
echo "║                  ⚡ ADVANCED CYBER FRAMEWORK                ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if .NET is installed
if ! command -v dotnet &> /dev/null; then
    echo "❌ .NET is not installed!"
    echo "📦 Installing .NET..."
    pkg install -y dotnet
fi

# Check if required packages are installed
echo "🔧 Checking dependencies..."
pkg install -y clang cmake make openssl libcurl

# Navigate to script directory
cd "$(dirname "$0")"

# Build and run
echo "🚀 Building DDoS Toolkit..."
dotnet build --configuration Release

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "🚀 Starting DDoS Toolkit..."
    echo ""
    dotnet run --configuration Release --no-build
else
    echo "❌ Build failed!"
    echo "🔧 Trying to fix dependencies..."
    pkg install -y dotnet-runtime-7.0
    dotnet build --configuration Release
    dotnet run --configuration Release --no-build
fi

echo ""
echo "Program closed. Press any key to exit..."
read -n 1