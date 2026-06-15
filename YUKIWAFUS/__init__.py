import logging
import os
from pyrogram import Client

# 1. Setup the standard logging configuration properly
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

LOGGER = logging.getLogger("YUKIWAFUS")

# Helper function for modules that try to fetch custom sub-loggers
def get_custom_logger(name: str):
    return logging.getLogger(name)


# 2. Load API credentials from Environment Variables (Coolify) or config file
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Fallback check if you use a local config.py file instead of env variables
if not API_ID or not API_HASH or not BOT_TOKEN:
    try:
        import config
        API_ID = getattr(config, "API_ID", None)
        API_HASH = getattr(config, "API_HASH", None)
        BOT_TOKEN = getattr(config, "BOT_TOKEN", None)
    except ImportError:
        LOGGER.error("Could not find API_ID, API_HASH, or BOT_TOKEN in Environment or config.py!")


# 3. Setup and initialize the Telegram Bot Client (app)
LOGGER.info("Initializing Telegram Client (app)...")

app = Client(
    name="YUKIWAFUS",
    api_id=int(API_ID) if API_ID else None,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Force Python to use the real core LOGGER object directly
import YUKIWAFUS

YUKIWAFUS.LOGGER.info(f"Modules found: {ALL_MODULES}")
