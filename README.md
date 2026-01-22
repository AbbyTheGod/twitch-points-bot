# 🎮 Twitch Channel Points Bot

Automatically collect Twitch channel points for Yugi2x channel.

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

- Python 3.8+ OR Docker
- Twitch account
- Twitch access token

## 🚀 Quick Setup

### Option 1: Run with Python (No Docker)

#### Step 1: Install Dependencies

```bash
pip install TwitchChannelPointsMiner-v2 python-dotenv colorama
```

#### Step 2: Clone Repository

```bash
git clone https://github.com/AbbyTheGod/twitch-points-bot.git
cd twitch-points-bot
```

#### Step 3: Create `.env` File

```bash
cp .env.example .env
nano .env
```

Add your credentials:
```
TWITCH_USERNAME=your_twitch_username
TWITCH_PASSWORD=your_access_token
TARGET_CHANNEL=Yugi2x
```

#### Step 4: Run

```bash
python run.py
```

---

### Option 2: Run with Docker

#### Step 1: Clone Repository

```bash
git clone https://github.com/AbbyTheGod/twitch-points-bot.git
cd twitch-points-bot
```

#### Step 2: Create `.env` File

```bash
cp .env.example .env
nano .env
```

Add your credentials:
```
TWITCH_USERNAME=your_twitch_username
TWITCH_PASSWORD=your_access_token
TARGET_CHANNEL=Yugi2x
```

#### Step 3: Run with Docker

```bash
docker compose up -d
docker compose logs -f
```

---

## 🔑 Getting Your Access Token

1. Visit: https://twitchtokengenerator.com/
2. Click "Generate Token"
3. Grant all requested permissions
4. Copy your token (can be `oauth:xxx` or just the token string like `p3d500ltgq7...`)

**Both formats work:**
- `oauth:abc123xyz` ✅
- `abc123xyz` ✅

---

## 🔍 Monitoring

### View Real-Time Logs

```bash
# Docker
docker compose logs -f

# Python (runs in foreground, logs visible directly)
```

### Check Bot Status

```bash
# Docker
docker compose ps
docker stats twitch-points-bot
```

---

## 🛠️ Management Commands (Docker)

```bash
# Start bot
docker compose up -d

# Stop bot
docker compose down

# Restart bot
docker compose restart

# View logs
docker compose logs -f
```

---

## 📊 Point Collection Breakdown

| Action | Points |
|--------|--------|
| Watching stream | ~10/min |
| Bonus chest claim | +50 |
| Watch streak | +450 |
| Raid participation | +250 |
| Drop rewards | Varies |

---

## ⚠️ Important Notes

### Security

- Never share your access token
- If compromised, revoke and generate a new one
- You can revoke tokens anytime in Twitch settings

### Twitch Terms of Service

- Automated viewers may violate Twitch ToS
- Account suspension is possible
- Use at your own risk

---

## 🐛 Troubleshooting

### Bot Not Starting

```bash
# Check logs
docker compose logs

# Common issues:
# 1. Invalid access token - regenerate from twitchtokengenerator.com
# 2. Wrong username - check case sensitivity
# 3. Missing .env file - create it with your credentials
```

### Python Import Error

```bash
# Install missing dependencies
pip install TwitchChannelPointsMiner-v2 python-dotenv colorama
```

### Container: "can't open file '/usr/src/app/run.py'"

```bash
# Pull latest changes (this bug is fixed)
git pull
docker compose down
docker compose up -d
```

---

## 📁 File Structure

```
twitch-points-bot/
├── run.py                  # Bot configuration
├── docker-compose.yml      # Docker deployment config
├── .env.example            # Credentials template
├── .env                    # Your credentials (DON'T share!)
├── logs/                   # Bot logs directory
└── README.md               # This file
```

---

## 🔧 Advanced Configuration

### Change Target Channel

Edit `.env` file:
```bash
TARGET_CHANNEL=some_other_channel
```

### Enable Betting/Predictions

Edit `run.py`, change:
```python
make_predictions=False,  # Change to True
```

---

## 📚 References

- Original Project: https://github.com/rdavydov/Twitch-Channel-Points-Miner-v2
- Twitch Points Guide: https://help.twitch.tv/s/article/channel-points-guide
- Twitch OAuth: https://twitchtokengenerator.com/

---

**🎮 Enjoy your automated point collection!**
