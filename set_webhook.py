import asyncio
import os

import django

from bot.config import bot
from root.settings import NGROK_URL

def set_webhook():
    bot.remove_webhook()
    webhook_ulr = f"{NGROK_URL}/bot/webhook"

    status = bot.set_webhook(webhook_ulr)
    print('ok' if status else webhook_ulr)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")
django.setup()

set_webhook()