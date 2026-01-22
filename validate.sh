#!/bin/bash

# Twitch Points Bot - Configuration Validator
# Run this to verify your setup before starting to bot

set -e

echo "🔍 Twitch Points Bot - Configuration Validator"
echo "=============================================="
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ ERROR: .env file not found!"
    echo ""
    echo "Please create it from example:"
    echo "  cp .env.example .env"
    echo "  nano .env"
    echo ""
    echo "Then run this validator again."
    exit 1
fi

echo "✅ .env file found"
echo ""

# Source the .env file
export $(grep -v '^#' .env | xargs)

# Validate TWITCH_USERNAME
if [ -z "$TWITCH_USERNAME" ] || [ "$TWITCH_USERNAME" == "your_twitch_username_here" ]; then
    echo "❌ ERROR: TWITCH_USERNAME is not set or still has default value!"
    echo "   Please edit .env and set your actual Twitch username."
    exit 1
fi

echo "✅ TWITCH_USERNAME: $TWITCH_USERNAME"
echo ""

# Validate TWITCH_PASSWORD (OAuth token)
if [ -z "$TWITCH_PASSWORD" ] || [ "$TWITCH_PASSWORD" == "oauth:your_oauth_token_here" ]; then
    echo "❌ ERROR: TWITCH_PASSWORD (OAuth token) is not set or still has default value!"
    echo ""
    echo "Please get your OAuth token from: https://twitchtokengenerator.com/"
    echo "Then edit .env and set TWITCH_PASSWORD=oauth:your_actual_token"
    exit 1
fi

# Check OAuth token format
if [[ ! "$TWITCH_PASSWORD" =~ ^oauth:[a-zA-Z0-9]+$ ]]; then
    echo "⚠️  WARNING: TWITCH_PASSWORD doesn't look like a valid OAuth token!"
    echo "   Expected format: oauth:abcdef123456..."
    echo "   Your token: ${TWITCH_PASSWORD:0:20}..."
    echo ""
    echo "Get a proper token from: https://twitchtokengenerator.com/"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ Aborted. Please fix the token and try again."
        exit 1
    fi
fi

echo "✅ TWITCH_PASSWORD: ${TWITCH_PASSWORD:0:10}... (hidden)"
echo ""

# Validate TARGET_CHANNEL
if [ -z "$TARGET_CHANNEL" ]; then
    echo "⚠️  WARNING: TARGET_CHANNEL not set, using default: Yugi2x"
    export TARGET_CHANNEL="Yugi2x"
fi

echo "✅ TARGET_CHANNEL: $TARGET_CHANNEL"
echo ""

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ ERROR: Docker is not installed!"
    echo ""
    echo "Install Docker:"
    echo "  curl -fsSL https://get.docker.com -o get-docker.sh"
    echo "  sudo sh get-docker.sh"
    echo "  sudo usermod -aG docker \$USER"
    exit 1
fi

echo "✅ Docker: $(docker --version)"
echo ""

# Check Docker Compose
if docker compose version &> /dev/null; then
    COMPOSE_CMD="docker compose"
    echo "✅ Docker Compose: $(docker compose version --short)"
elif command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
    echo "✅ Docker Compose: $(docker-compose --version)"
else
    echo "❌ ERROR: Docker Compose not found!"
    exit 1
fi
echo ""

# Check if we can pull the Docker image
echo "📥 Checking if we can pull the Docker image..."
if docker pull rdavidoff/twitch-channel-points-miner-v2:latest &> /dev/null; then
    echo "✅ Docker image pull successful"
else
    echo "❌ ERROR: Failed to pull Docker image!"
    echo "   Check your internet connection and try again."
    exit 1
fi
echo ""

# Check network connectivity to Twitch
echo "🌐 Checking connectivity to Twitch..."
if curl -s --head https://www.twitch.tv | grep -q "200\|301\|302"; then
    echo "✅ Twitch is reachable"
else
    echo "⚠️  WARNING: Cannot reach Twitch!"
    echo "   Check your internet connection or firewall settings."
fi
echo ""

# All checks passed
echo "=============================================="
echo "✅ All validations passed!"
echo "=============================================="
echo ""
echo "📝 Configuration Summary:"
echo "   Username: $TWITCH_USERNAME"
echo "   Channel:  $TARGET_CHANNEL"
echo "   OAuth:    ${TWITCH_PASSWORD:0:10}... (valid format)"
echo ""
echo "🚀 You can now start the bot:"
echo "   $COMPOSE_CMD up -d"
echo ""
echo "📊 View logs:"
echo "   $COMPOSE_CMD logs -f"
echo ""
