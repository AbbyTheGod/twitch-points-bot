# 🎮 Twitch Channel Points Bot

Automatically collect Twitch channel points for Yugi2x channel on your VPS.

## ✨ Features

- ✅ Auto-watch streams and collect points (+10/min)
- ✅ Auto-claim bonus chests (+50 points each)
- ✅ Catch watch streak bonuses (+450 points when stream starts)
- ✅ Auto-join raids (+250 points)
- ✅ Claim game drops
- ✅ Auto-restart on VPS boot
- ✅ Comprehensive logging
- ✅ Minimal resource usage (~100MB RAM)

## 📋 Prerequisites

- VPS with Docker installed
- Twitch account
- Twitch OAuth token

## 🚀 Quick Setup (5 minutes)

### Step 1: Get Your OAuth Token

1. Visit: https://twitchtokengenerator.com/
2. Click "Generate Token"
3. Grant all requested permissions
4. Copy your token (starts with `oauth:` or is a long random string)

### Step 2: Upload Files to VPS

```bash
# SSH into your VPS
ssh your-user@your-vps-ip

# Create project directory
mkdir -p ~/twitch-points-bot
cd ~/twitch-points-bot

# Upload these files (using scp or sftp):
# - run.py
# - docker-compose.yml
# - .env.example
```

### Step 3: Configure Your Credentials

```bash
# Copy example env file
cp .env.example .env

# Edit with your credentials
nano .env
```

Update these values in `.env`:
```bash
TWITCH_USERNAME=your_actual_twitch_username
TWITCH_PASSWORD=oauth:your_actual_oauth_token
TARGET_CHANNEL=Yugi2x
```

### Step 4: Start Bot

```bash
# Start bot using Docker Compose
docker compose up -d

# View logs
docker compose logs -f

# Check if it's running
docker compose ps
```

### Step 5: Enable Auto-Start on Boot (Optional but Recommended)

```bash
# Copy service file to systemd
sudo cp twitch-bot.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable service
sudo systemctl enable twitch-bot.service

# Start service
sudo systemctl start twitch-bot.service

# Check status
sudo systemctl status twitch-bot.service
```

## 🔍 Monitoring

### View Real-Time Logs

```bash
# Docker logs (most recent)
docker compose logs -f twitch-points-bot

# View last 100 lines
docker compose logs --tail=100

# View log files directly
ls -la logs/
tail -f logs/*.log
```

### Check Bot Status

```bash
# Check if container is running
docker compose ps

# Check container resource usage
docker stats twitch-points-bot
```

## 🛠️ Management Commands

### Start/Stop/Restart

```bash
# Start bot
docker compose up -d

# Stop bot
docker compose down

# Restart bot
docker compose restart

# View running status
docker compose ps
```

### Update Configuration

```bash
# Stop bot
docker compose down

# Edit configuration
nano .env

# or

nano run.py

# Restart with new config
docker compose up -d
```

### View Logs History

```bash
# Log files are stored in ./logs/ directory
ls -lh logs/

# View specific log
cat logs/your-username.timestamp.log

# Watch in real-time
tail -f logs/your-username.timestamp.log
```

## 📊 What Bot Does

The bot will automatically:

1. **Watch Stream**: Continuously watch Yugi2x when online
2. **Collect Points**: Earn ~10 points per minute
3. **Claim Bonuses**: Auto-click bonus chests (+50 points)
4. **Watch Streak**: Catch stream start bonus (+450 points)
5. **Join Raids**: Auto-follow raids (+250 points)
6. **Claim Drops**: Collect game drop rewards
7. **Join IRC Chat**: Increase watch time detection

## 🎯 Point Collection Breakdown

| Action | Points |
|--------|---------|
| Watching stream | ~10/min |
| Bonus chest claim | +50 |
| Watch streak | +450 |
| Raid participation | +250 |
| Drop rewards | Varies |

## ⚠️ Important Notes

### Security

- Never share your OAuth token
- If compromised, revoke and generate a new one
- OAuth token ≠ Twitch password
- You can revoke OAuth tokens anytime in Twitch settings

### Twitch Terms of Service

- Automated viewers may violate Twitch ToS
- Account suspension is possible
- Use at your own risk

### Resource Usage

- **RAM**: ~100MB minimum
- **CPU**: <5% when idle
- **Network**: Low (~1MB/min)

## 🐛 Troubleshooting

### Bot Not Starting

```bash
# Check logs
docker compose logs

# Common issues:
# 1. Invalid OAuth token - regenerate from twitchtokengenerator.com
# 2. Wrong username - check case sensitivity
# 3. Network issues - check VPS can reach Twitch
```

### Points Not Collecting

```bash
# Verify bot is connected
docker compose logs | grep "Online"

# Check if channel is actually streaming
# Visit https://www.twitch.tv/Yugi2x manually

# Ensure bot is in IRC chat
docker compose logs | grep "JOIN"
```

### Container Keeps Restarting

```bash
# Check detailed logs
docker compose logs --tail=100

# Common fixes:
# 1. Rebuild container: docker compose up -d --build
# 2. Check disk space: df -h
# 3. Verify Docker is running: sudo systemctl status docker
```

### Can't Stop Bot

```bash
# Force stop
docker compose down --remove-orphans

# Kill container
docker kill twitch-points-bot

# Use systemd (if enabled)
sudo systemctl stop twitch-bot.service
```

## 🔧 Advanced Configuration

### Change Target Channel

Edit `.env` file:
```bash
TARGET_CHANNEL=some_other_channel
```

Then restart:
```bash
docker compose restart
```

### Enable Betting/Predictions

Edit `run.py`, change:
```python
make_predictions=False,  # Change to True
```

### Adjust Watch Priorities

Edit `priority` in `run.py`:
```python
priority=[
    Priority.STREAK,    # Catch streak bonuses first
    Priority.DROPS,     # Then collect drops
    Priority.ORDER       # Finally watch in order
]
```

### Set Timezone

Edit `.env` file:
```bash
TZ=America/New_York  # Or Europe/London, Asia/Kolkata, etc.
```

## 📦 Systemd Service Details

The `twitch-bot.service` file ensures:
- Bot starts automatically on VPS boot
- Bot restarts if it crashes
- Clean shutdown on system shutdown

### Service Management

```bash
# Enable auto-start on boot
sudo systemctl enable twitch-bot.service

# Disable auto-start
sudo systemctl disable twitch-bot.service

# Check service status
sudo systemctl status twitch-bot.service

# View service logs
sudo journalctl -u twitch-bot.service -f
```

## 📁 File Structure

```
twitch-points-bot/
├── run.py                  # Bot configuration (watching Yugi2x)
├── docker-compose.yml       # Docker deployment config
├── .env.example            # Credentials template
├── .env                   # Your actual credentials (DON'T share!)
├── twitch-bot.service       # Systemd service file
├── logs/                   # Bot logs directory
│   └── *.log             # Log files
└── README.md              # This file
```

## 🆘 Support

If you encounter issues:

1. Check logs: `docker compose logs -f`
2. Verify Twitch OAuth token is valid
3. Ensure VPS can reach Twitch servers
4. Check Docker is running: `sudo systemctl status docker`

## 📝 Logs Analysis

The bot creates detailed logs showing:
- When streamer goes online/offline
- Points collected (watch, claim, raid, streak)
- Prediction results (if enabled)
- Errors and warnings

Example log output:
```
21/01/26 20:15:30 - 🥳  Yugi2x (5000 points) is Online!
21/01/26 20:15:35 - 🚀  +12 → Yugi2x (5012 points) - Reason: WATCH.
21/01/26 20:16:35 - 🎁  Claiming the bonus for Yugi2x!
21/01/26 20:16:36 - 🚀  +60 → Yugi2x (5072 points) - Reason: CLAIM.
```

## 🔄 Updating the Bot

To update to the latest version:

```bash
# Stop bot
docker compose down

# Pull latest image
docker compose pull

# Restart with updated image
docker compose up -d

# Check logs
docker compose logs -f
```

## 📚 References

- Original Project: https://github.com/rdavydov/Twitch-Channel-Points-Miner-v2
- Twitch Points Guide: https://help.twitch.tv/s/article/channel-points-guide
- Twitch OAuth: https://twitchtokengenerator.com/

---

**🎮 Enjoy your automated point collection!**
