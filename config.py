import os
from os import getenv

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_OWNER = os.getenv("BOT_OWNER")
REM_BG_API_KEY = os.getenv("REM_BG_API_KEY")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
MONGODB_URI = os.environ.get("MONGODB_URI")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY"))
