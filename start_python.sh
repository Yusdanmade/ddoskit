#!/bin/bash
# Python DDoS Toolkit - Termux Compatible
# Made for Termux on Android

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                🚀 PYTHON DDoS TOOLKIT 2025                ║"
echo "║                  ⚡ ADVANCED CYBER FRAMEWORK                ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed!"
    echo "📦 Installing Python..."
    pkg install -y python
fi

# Install required packages
echo "📦 Installing dependencies..."
pkg install -y python-pip
pip install requests aiohttp asyncio colorama

# Navigate to script directory
cd "$(dirname "$0")"

# Run Python DDoS toolkit
echo "🚀 Starting Python DDoS Toolkit..."
echo ""
python3 ddos_toolkit.py

echo ""
echo "Program closed. Press any key to exit..."
read -n 1