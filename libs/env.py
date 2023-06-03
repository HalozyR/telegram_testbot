from os import getenv
from typing import Final

TELEGRAM_BOT_TOKEN: Final = getenv('TELEGRAM_BOT_TOKEN')
DATABASE_URL: Final = getenv('DATABASE_URL')
ADMIN_CHANNEL_ID = getenv('ADMIN_CHANNEL_ID', None)

if not TELEGRAM_BOT_TOKEN:
  raise Exception('Environment variable TELEGRAM_BOT_TOKEN is not set')
if not DATABASE_URL:
  raise Exception('Environment variable DATABASE_URL is not set')
if not ADMIN_CHANNEL_ID:
  raise Exception('Environment variable ADMIN_CHANNEL_ID is not set')
