# -*- coding: utf-8 -*-

import logging
import os
from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Settings import Priority, Events, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Bet import (
    Strategy,
    BetSettings,
    Condition,
    OutcomeKeys,
    FilterCondition,
)
from TwitchChannelPointsMiner.classes.entities.Streamer import (
    Streamer,
    StreamerSettings,
)

# Load credentials from environment variables
TWITCH_USERNAME = os.getenv("TWITCH_USERNAME", "").strip()
TWITCH_PASSWORD = os.getenv("TWITCH_PASSWORD", "").strip()  # This is your OAuth token
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL", "Yugi2x").strip()

# Validate configuration
if not TWITCH_USERNAME:
    raise ValueError(
        "❌ ERROR: TWITCH_USERNAME is not set in environment variables. "
        "Please set it in your .env file."
    )

if not TWITCH_PASSWORD:
    raise ValueError(
        "❌ ERROR: TWITCH_PASSWORD (OAuth token) is not set in environment variables. "
        "Please set it in your .env file."
    )

# Validate OAuth token format
if not TWITCH_PASSWORD.startswith("oauth:"):
    logging.warning(
        "⚠️  WARNING: Your OAuth token should start with 'oauth:' "
        "Current token may not work correctly."
    )

if not TWITCH_USERNAME.isalnum() and "_" not in TWITCH_USERNAME:
    raise ValueError(
        f"❌ ERROR: Invalid Twitch username format: '{TWITCH_USERNAME}'. "
        "Username should only contain letters, numbers, and underscores."
    )

twitch_miner = TwitchChannelPointsMiner(
    username=TWITCH_USERNAME,
    password=TWITCH_PASSWORD,
    claim_drops_startup=False,  # Claim drops from inventory on startup
    priority=[  # Priority order for watching
        Priority.STREAK,  # Catch watch streak bonus (+450 points)
        Priority.DROPS,  # Collect drops
        Priority.ORDER,  # Watch based on order below
    ],
    logger_settings=LoggerSettings(
        save=True,  # Save logs to file
        console_level=logging.INFO,  # Console log level
        file_level=logging.DEBUG,  # File log level (more detailed)
        emoji=True,  # Show emojis in logs
        less=False,  # Show verbose logs
        colored=True,  # Colored output
        color_palette=ColorPalette(
            streamer_online="GREEN",  # Green when streamer is online
            streamer_offline="RED",  # Red when streamer is offline
            bet_win=Fore.MAGENTA,  # Magenta for betting wins
        ),
    ),
    streamer_settings=StreamerSettings(
        make_predictions=False,  # Disabled betting for now (can be enabled)
        follow_raid=True,  # Auto-join raids (+250 points)
        claim_drops=True,  # Claim game drops
        watch_streak=True,  # Watch for streak bonuses (+450)
        chat=ChatPresence.ONLINE,  # Join IRC chat when streamer is online
    ),
    streamers=[  # Channels to watch
        Streamer(
            username=TARGET_CHANNEL,
            settings=StreamerSettings(
                make_predictions=False,  # No automatic predictions
                follow_raid=True,
                claim_drops=True,
                watch_streak=True,
                chat=ChatPresence.ONLINE,
            ),
        ),
    ],
)

if __name__ == "__main__":
    print(f"\n{'=' * 50}")
    print(f"🎮 Twitch Channel Points Bot")
    print(f"{'=' * 50}")
    print(f"👤 Username: {TWITCH_USERNAME}")
    print(f"📺 Watching: {TARGET_CHANNEL}")
    print(f"🔍 Auto-detecting stream status...")
    print(f"{'=' * 50}\n")

    try:
        logging.info("🚀 Starting bot...")
        logging.info(f"📺 Configured to watch: {TARGET_CHANNEL}")
        logging.info(f"✅ Features enabled: watch_streak, claim_drops, follow_raid, chat_presence")
        logging.info("⏳ Waiting for streamer to go online...")

        twitch_miner.run()

    except KeyboardInterrupt:
        logging.info("\n\n🛑 Bot stopped by user (Ctrl+C)")
    except Exception as e:
        logging.error(f"\n❌ Fatal error: {e}")
        logging.error("💡 Check logs for more details: docker compose logs -f")
        raise
