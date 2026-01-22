# -*- coding: utf-8 -*-

import logging
import os
import requests

# Auto-load .env file if it exists (for running without Docker)
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Loaded .env file")
except ImportError:
    pass

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
CLIENT_ID = os.getenv("CLIENT_ID", "").strip()
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "").strip()


def get_access_token(client_id: str, client_secret: str) -> str:
    """Generate access token using client credentials."""
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": "channel:read:redemptions chat:read chat:edit user:read:email"
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token: {response.text}")


# Validate configuration
if not TWITCH_USERNAME:
    raise ValueError(
        "❌ ERROR: TWITCH_USERNAME is not set.\n"
        "Create a .env file with:\n"
        "  TWITCH_USERNAME=your_username\n"
        "  TARGET_CHANNEL=Yugi2x"
    )

# If password not set but client credentials are, generate token automatically
if not TWITCH_PASSWORD and CLIENT_ID and CLIENT_SECRET:
    print("🔑 Generating access token from client credentials...")
    TWITCH_PASSWORD = "oauth:" + get_access_token(CLIENT_ID, CLIENT_SECRET)
    print("✅ Access token generated successfully!")
elif TWITCH_PASSWORD and not TWITCH_PASSWORD.startswith("oauth:"):
    print("⚠️  Warning: TWITCH_PASSWORD should start with 'oauth:'. Adding prefix...")
    TWITCH_PASSWORD = "oauth:" + TWITCH_PASSWORD
elif not TWITCH_PASSWORD:
    raise ValueError(
        "❌ ERROR: TWITCH_PASSWORD is not set.\n"
        "Either:\n"
        "  1. Set TWITCH_PASSWORD with your OAuth token\n"
        "  2. Set CLIENT_ID and CLIENT_SECRET to auto-generate token"
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
        emoji=False,  # Disabled - avoids emoji library compatibility issues
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