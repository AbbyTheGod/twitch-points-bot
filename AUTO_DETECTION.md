# 🤖 Auto-Detection FAQ

## How Does The Bot Detect When Streamer Goes Online?

### Yes! The bot **automatically detects** when Yugi2x goes online and starts watching.

### How It Works:

```
┌─────────────────────────────────────────┐
│  BOT RUNNING 24/7                        │
│  Polling Twitch API every ~10 seconds        │
└─────────────────────────────────────────┘
                    ↓
        ┌──────────────────┐
        │  Yugi2x OFFLINE │
        │  (Waiting...)    │
        └──────────────────┘
                    ↓
        ┌──────────────────┐
        │  Yugi2x ONLINE!  │  ← Bot detects this
        │  ⏳ JOINING...  │     automatically
        └──────────────────┘
                    ↓
        ┌──────────────────┐
        │  🎮 WATCHING     │
        │  ✅ Collecting    │
        │  🎁 Bonus        │
        │  💰 Points        │
        └──────────────────┘
                    ↓
        ┌──────────────────┐
        │  Yugi2x OFFLINE │  ← Bot detects this
        │  (Saving logs)   │     automatically
        └──────────────────┘
```

---

## What Happens Automatically:

### 1️⃣ Streamer Goes Online:
```
21/01/26 21:00:00 - 🥳  Yugi2x (5000 points) is Online!
21/01/26 21:00:01 - ⏳  JOINING IRC CHAT...
21/01/26 21:00:05 - ✅  JOINED CHAT
21/01/26 21:00:30 - 🚀  +450 → Yugi2x (5450 points) - Reason: WATCH_STREAK.
```

**Bot automatically:**
- ✅ Joins stream
- ✅ Connects to IRC chat
- ✅ Starts collecting points (~10/min)
- ✅ Claims watch streak bonus (+450)

---

### 2️⃣ While Streaming:
```
21/01/26 21:01:30 - 🚀  +12 → Yugi2x (5462 points) - Reason: WATCH.
21/01/26 21:02:35 - 🎁  Bonus chest available!
21/01/26 21:02:36 - 🚀  +60 → Yugi2x (5522 points) - Reason: CLAIM.
21/01/26 21:03:30 - 🚀  +12 → Yugi2x (5534 points) - Reason: WATCH.
```

**Bot automatically:**
- ✅ Continuously watches
- ✅ Auto-claims bonus chests (+50)
- ✅ Collects points every minute
- ✅ Updates real-time logs

---

### 3️⃣ Streamer Goes Offline:
```
21/01/26 22:30:00 - 😴  Yugi2x (15000 points) is Offline!
21/01/26 22:30:01 - 💾  Session summary saved
21/01/26 22:30:02 - ⏳  Waiting for streamer to go live again...
```

**Bot automatically:**
- ✅ Saves session summary
- ✅ Continues monitoring
- ✅ Waits for streamer to come back online

---

### 4️⃣ Raid Events:
```
21/01/26 21:30:00 - 🎭  Raid detected! Yugi2x is raiding AnotherStreamer
21/01/26 21:30:05 - 🚀  +250 → Yugi2x (15250 points) - Reason: RAID.
```

**Bot automatically:**
- ✅ Detects raid
- ✅ Joins raid
- ✅ Collects raid bonus (+250)

---

## 🎯 Full Auto-Detection Features

| Feature | Status | Points |
|---------|--------|---------|
| **Detect Online** | ✅ Auto | - |
| **Start Watching** | ✅ Auto | - |
| **Collect Watch Points** | ✅ Auto | ~10/min |
| **Claim Bonus Chests** | ✅ Auto | +50 each |
| **Watch Streak Bonus** | ✅ Auto | +450 |
| **Join Raids** | ✅ Auto | +250 |
| **Claim Drops** | ✅ Auto | Varies |
| **IRC Chat Presence** | ✅ Auto | - |
| **Detect Offline** | ✅ Auto | - |
| **Save Logs** | ✅ Auto | - |
| **Wait for Return** | ✅ Auto | - |

---

## ⚙️ How It Works Technically

### Polling Interval:
- Every **10 seconds**, bot checks stream status via Twitch API
- When status changes (OFFLINE → ONLINE), it immediately connects
- When status changes (ONLINE → OFFLINE), it disconnects and saves logs

### Point Collection:
- **Watch points**: Collected automatically every ~60 seconds
- **Bonus chests**: Detected and claimed automatically
- **Watch streak**: Automatically claimed when streamer starts
- **Raids**: Automatically detected and joined

### Connection:
- **IRC Chat**: Joins when streamer is online
- **API Calls**: Used for status detection and point tracking
- **Retry Logic**: Automatically reconnects if connection drops

---

## 🚀 No Manual Intervention Needed!

### What YOU need to do:
1. Configure `.env` file with your credentials
2. Run bot once: `docker compose up -d`
3. That's it!

### What THE BOT does automatically:
- ✅ Detects when Yugi2x goes online
- ✅ Starts watching
- ✅ Collects all points
- ✅ Claims all bonuses
- ✅ Handles offline events
- ✅ Reconnects when Yugi2x comes back
- ✅ Logs everything

---

## 🔍 Monitoring Auto-Detection

### See Bot Detecting Changes:
```bash
# Watch real-time logs
docker compose logs -f
```

You'll see:
```
⏳ Waiting for streamer...
⏳ Waiting for streamer...
🥳  Yugi2x is Online!      ← Bot detected online!
🚀  +12 → Yugi2x...         ← Now collecting points
🚀  +12 → Yugi2x...
😴  Yugi2x is Offline!      ← Bot detected offline!
⏳  Waiting for streamer...     ← Waiting for return
```

---

## ❓ Common Questions

### Q: How long does it take to detect online status?
**A:** Usually within 10-20 seconds of streamer going live.

### Q: Does it work if I start bot while streamer is already online?
**A:** Yes! Bot detects current status on startup and immediately joins.

### Q: What if streamer goes online/offline multiple times?
**A:** Bot handles this automatically - it will reconnect each time.

### Q: Do I need to do anything manually?
**A:** No! Just start the bot once. Everything is automatic.

### Q: What happens if bot crashes?
**A:** With `restart: unless-stopped` in docker-compose.yml, bot restarts automatically.

### Q: Will it miss any points if I start late?
**A:** You won't get the "watch streak" bonus for the start if you're late, but it will collect all future points automatically.

---

## 🎮 Summary

**The bot is fully automatic:**
1. ✅ Detects Yugi2x going online
2. ✅ Starts watching immediately
3. ✅ Collects all points automatically
4. ✅ Claims all bonuses automatically
5. ✅ Detects when Yugi2x goes offline
6. ✅ Waits for Yugi2x to come back
7. ✅ Repeats forever

**No manual intervention needed!**
