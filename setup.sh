#!/bin/bash

# Twitch Points Bot - Quick Setup Script
# Run this on your VPS to get started quickly

set -e

echo "🎮 Twitch Points Bot - Quick Setup"
echo "======================================"
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Don't run this script as root. Run as regular user."
    exit 1
fi

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo ""
    echo "Install Docker first:"
    echo "  curl -fsSL https://get.docker.com -o get-docker.sh"
    echo "  sudo sh get-docker.sh"
    echo "  sudo usermod -aG docker \$USER"
    echo "  (logout and login again for group change to take effect)"
    exit 1
fi

# Check if Docker Compose is available
if ! docker compose version &> /dev/null && ! docker-compose version &> /dev/null; then
    echo "❌ Docker Compose is not installed!"
    exit 1
fi

echo "✅ Docker found: $(docker --version)"
echo "✅ Docker Compose found"
echo ""

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "✅ .env file created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env with your credentials!"
    echo "   nano .env"
    echo ""
    read -p "Press Enter after you've configured .env, or Ctrl+C to exit..."
else
    echo "✅ .env file already exists"
fi

# Create logs directory
mkdir -p logs
echo "✅ Logs directory created"

echo ""
echo "======================================"
echo "🚀 Starting bot..."
echo "======================================"

# Start of bot using Docker Compose
docker compose up -d

# Check if started
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Bot started successfully!"
    echo ""
    echo "📊 View logs: docker compose logs -f"
    echo "🛑 Stop bot:   docker compose down"
    echo "🔄 Restart:    docker compose restart"
    echo ""
    echo "💡 To enable auto-start on boot:"
    echo "   sudo cp twitch-bot.service /etc/systemd/system/"
    echo "   sudo systemctl daemon-reload"
    echo "   sudo systemctl enable twitch-bot.service"
    echo "   sudo systemctl start twitch-bot.service"
    echo ""
else
    echo ""
    echo "❌ Failed to start bot. Check logs:"
    echo "   docker compose logs"
    exit 1
fi
