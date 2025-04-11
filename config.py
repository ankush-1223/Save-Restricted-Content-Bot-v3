# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("BQGuUuYAO-EmNta9fAqfwSJHaSw1CF3aayO1d0dit0kkHXVhnRdlNJxSB-AObhxXwDn7GadKnHtRsi3ZmV7mThMK5IigC7uqygoeGCd_s5FK4m9eecFeaAM0A9CSgd15cjboUuRJwRhMpz2gMzdL8fcnX6UylWxpBfOSgYVzOCIiJDc3Z0D3O8QJVhCPvwmzJuvJbzc-Ejq9a6aknDHUxBX40ZfWw3gwWBxuQvT7yTyMRsD4e14R_JNgJJ8ac08_JUqNLhR0lPzhyCziDYJgLXYySBDZnCUn5yJU_4NdtQXy6pM3brS24gqaAs-zPslMJ-rzbQpZrHQayGE4KSGqwM2wHbk95AAAAAHAmuyJAA", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "") # for session encryption
IV_KEY = os.getenv("IV_KEY", "") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "9999"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "9999"))
