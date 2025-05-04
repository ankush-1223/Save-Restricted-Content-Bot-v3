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
# Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1778732890	PREF	f6=40000000&tz=Asia.Calcutta&f7=100
.youtube.com	TRUE	/	TRUE	1744174524	GPS	1
.youtube.com	TRUE	/	TRUE	1775708890	__Secure-1PSIDTS	sidts-CjEB7pHptZ43Bc57MsK-iEoc5am4c-3ahAi9pN-atc9yxG5vYkX8aa_vZlJFnmzE6KK3EAA
.youtube.com	TRUE	/	TRUE	1775708890	__Secure-3PSIDTS	sidts-CjEB7pHptZ43Bc57MsK-iEoc5am4c-3ahAi9pN-atc9yxG5vYkX8aa_vZlJFnmzE6KK3EAA
.youtube.com	TRUE	/	FALSE	1778732890	HSID	A9K6YQ07FeMQSI-dB
.youtube.com	TRUE	/	TRUE	1778732890	SSID	Ag0P4ilnpPz9D96Qb
.youtube.com	TRUE	/	FALSE	1778732890	APISID	Dn-cSIKW7HsjPtmZ/A-sZADhcoyQRBiVGo
.youtube.com	TRUE	/	TRUE	1778732890	SAPISID	Sx0NC40uKBiARjCo/AZLNz2IMR_OKDbWTN
.youtube.com	TRUE	/	TRUE	1778732890	__Secure-1PAPISID	Sx0NC40uKBiARjCo/AZLNz2IMR_OKDbWTN
.youtube.com	TRUE	/	TRUE	1778732890	__Secure-3PAPISID	Sx0NC40uKBiARjCo/AZLNz2IMR_OKDbWTN
.youtube.com	TRUE	/	FALSE	1778732890	SID	g.a000vgg02B0yvCpPvZmT2z9IQ7l0V7C-98m9624X9PvA5BXZd9rMpnwhAuN22bxQqZKEqYw_4AACgYKASQSARISFQHGX2MifQwa_ezwjNAFGkSo1eYFRhoVAUF8yKpShdytacofE-NiIEKS9pb70076
.youtube.com	TRUE	/	TRUE	1778732890	__Secure-1PSID	g.a000vgg02B0yvCpPvZmT2z9IQ7l0V7C-98m9624X9PvA5BXZd9rMdW9a9chB-qWPUKyL1JRlRAACgYKAd0SARISFQHGX2MiUVpV0jQ_eRSCCXuIoFSthBoVAUF8yKqnBZAqcWAfhceMK9BOQE4O0076
.youtube.com	TRUE	/	TRUE	1778732890	__Secure-3PSID	g.a000vgg02B0yvCpPvZmT2z9IQ7l0V7C-98m9624X9PvA5BXZd9rMapQRNZqr9ZlEI9NqKqj9bwACgYKAScSARISFQHGX2MiMWOyHgpqgsdJYAeWWAJAaxoVAUF8yKpWS0bxDbdENiX32mhfg6VK0076
.youtube.com	TRUE	/	TRUE	1778732890	LOGIN_INFO	AFmmF2swRQIgMubwaOTxHkhm5ymrE6jgrdLJOfgr2vqLyNaIpeXLZT0CIQCcA1HdnUV5l2aG_EjRtHRYKwmSUH0qDNvg8wL9JSLqhA:QUQ3MjNmd0ZxQldWWTROZkZyd2I2R1Q0d3JJWnd4Tm5sQy1HX2ZmZGZXQW9ETzdRZTNEeUU3VnljR0NmbmE0NlY1cHNFSEdMXy1JWm14b1NacTlubGtSUFVDTmpYblVMQjRQU1NYSXBrMVlCbGJtYS1RU1duaGRDV3NFWFBjUXowSTB5eG1LeU5wRjFPek5EMnd4Y3N6TWpsLVB1Y2w0SUt3
.youtube.com	TRUE	/	FALSE	1775708940	SIDCC	AKEyXzU0zq6wNoVr7fGD2tyeFp1fWCvQ48hocWfcwfwn7qOqXfBg8vVt6JfvrDr5cHZBteDBYw
.youtube.com	TRUE	/	TRUE	1775708940	__Secure-1PSIDCC	AKEyXzUioA-FA-F1BRRJxaYytaU79h5scryoOr9_-tdzfZYBifN__z0sxpfUFwGpX_LGmIu9
.youtube.com	TRUE	/	TRUE	1775708940	__Secure-3PSIDCC	AKEyXzWRxa8bOfyPTvzYtck9mKH7c7RPghRJPE1gS_QBmy4q5IbCnnIBVRpFajaTlhJLBHoizA

"""

API_ID = os.getenv("API_ID", "")
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "") # for session encryption
IV_KEY = os.getenv("IV_KEY", "") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "99"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "9999"))
