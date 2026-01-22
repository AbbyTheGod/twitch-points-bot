# ⚡ Quick Reference Card

## 🚀 3 Commands to Get Started

```bash
# 1. Validate your setup
./validate.sh

# 2. Start the bot
docker compose up -d

# 3. Watch logs
docker compose logs -f
```

That's it! Everything is automatic.

---

## 📊 Monitoring Commands

```bash
# Real-time logs
docker compose logs -f

# Last 100 lines
docker compose logs --tail=100

# Check if running
docker compose ps

# Stop the bot
docker compose down

# Restart the bot
docker compose restart
```

---

## 🔧 Configuration

**Edit these files:**
- `.env` - Your Twitch username and OAuth token
- `run.py` - Bot behavior and settings

---

## ✅ Auto-Detection Features

The bot **automatically**:
- ✅ Detects when Yugi2x goes online
- ✅ Starts watching immediately
- ✅ Collects points (~10/min)
- ✅ Claims bonus chests (+50)
- ✅ Gets watch streak bonus (+450)
- ✅ Joins raids (+250)
- ✅ Detects when Yugi2x goes offline
- ✅ Waits for Yugi2x to return
- ✅ Restarts if it crashes
- ✅ Joins IRC chat for watch time

**No manual intervention needed!**

---

## 📁 File List

```
twitch-points-bot/
├── README.md              # Full documentation
├── QUICK_START.md         # This file
├── AUTO_DETECTION.md      # Auto-detection details
├── SETUP_COMPLETE.md         # Complete setup summary
├── run.py                # Bot configuration
├── docker-compose.yml      # Docker setup
├── .env.example          # Credential template
├── .env                 # Your credentials (DON'T share!)
├── validate.sh           # Configuration validator
├── setup.sh             # Quick setup script
├── twitch-bot.service     # Systemd service
└── logs/                # Log files (created automatically)
```

---

## 🆘 Troubleshooting

### Bot not starting?
```bash
# Check configuration
./validate.sh

# View errors
docker compose logs
```

### Points not collecting?
```bash
# Check if bot is connected
docker compose logs | grep "Online"

# Verify streamer is live
# Visit https://www.twitch.tv/Yugi2x
```

### Need to change channel?
```bash
# Edit .env
nano .env
# Change: TARGET_CHANNEL=NewChannel

# Restart
docker compose restart
```

---

## 📚 Full Documentation

- **Setup Guide**: See `README.md`
- **Auto-Detection**: See `AUTO_DETECTION.md`

---

**🎮 Happy point collecting!**
