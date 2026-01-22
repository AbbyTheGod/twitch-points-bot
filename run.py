# -*- coding: utf-8 -*-

import logging
import os

# Auto-load .env file if it exists (for running without Docker)
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded .env file")
except ImportError:
    pass  # dotenv not installed, use environment variables directly

from colorama import Fore
from TwitchChannelPointsMiner import TwitchChannelPointsMiner
from TwitchChannelPointsMiner.logger import LoggerSettings, ColorPalette
from TwitchChannelPointsMiner.classes.Chat import ChatPresence
from TwitchChannelPointsMiner.classes.Settings import Priority, FollowersOrder
from TwitchChannelPointsMiner.classes.entities.Streamer import (
    Streamer,
    StreamerSettings,
)

# Load credentials from environment variables
TWITCH_USERNAME = os.getenv("TWITCH_USERNAME", "").strip()
TWITCH_PASSWORD = os.getenv("TWITCH_PASSWORD", "").strip()
TARGET_CHANNEL = os.getenv("TARGET_CHANNEL", "Yugi2x").strip()

# Validate configuration
if not TWITCH_USERNAME:
    raise ValueError(
        "❌ ERROR: TWITCH_USERNAME is not set.\n"
        "Create a .env file with:\n"
        "  TWITCH_USERNAME=your_username\n"
        "  TWITCH_PASSWORD=your_token\n"
        "  TARGET_CHANNEL=Yugi2x"
    )

if not TWITCH_PASSWORD:
    raise ValueError(
        "❌ ERROR: TWITCH_PASSWORD is not set.\n"
        "Create a .env file with:\n"
        "  TWITCH_USERNAME=your_username\n"
        "  TWITCH_PASSWORD=your_token\n"
        "  TARGET_CHANNEL=Yugi2x"
    )

# Create miner instance
twitch_miner = TwitchChannelPointsMiner(
    username=TWITCH_USERNAME,
    password=TWITCH_PASSWORD,
    claim_drops_startup=False,
    priority=[
        Priority.STREAK,
        Priority.DROPS,
        Priority.ORDER,
    ],
    logger_settings=LoggerSettings(
        save=True,
        console_level=logging.INFO,
        file_level=logging.DEBUG,
        emoji=True,
        less=False,
        colored=True,
        color_palette=ColorPalette(
            STREAMER_online="GREEN",
            streamer_offline="red",
            BET_wiN=Fore.MAGENTA,
        ),
    ),
    streamer_settings=StreamerSettings(
        make_predictions=False,
        follow_raid=True,
        claim_drops=True,
        watch_streak=True,
        chat=ChatPresence.ONLINE,
    ),
)

if __name__ == "__main__":
    print(f"\n{'=' * 50}")
    print(f"🎮 Twitch Channel Points Bot")
    print(f"{'=' * 50}")
    print(f"👤 Username: {TWITCH_USERNAME}")
    print(f"📺 Watching: {TARGET_CHANNEL}")
    print(f"🔍 Auto-detecting stream status...")
    print(f"{'=' * 50}\n")

    # Start mining - streamers go here, not in constructor
    twitch_miner.mine(
        [
            Streamer(
                TARGET_CHANNEL,
                settings=StreamerSettings(
                    make_predictions=False,
                    follow_raid=True,
                    claim_drops=True,
                    watch_streak=True,
                    chat=ChatPresence.ONLINE,
                ),
            ),
        ],
        followers=False,
        followers_order=FollowersOrder.ASC,
    )
