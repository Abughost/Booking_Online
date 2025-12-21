from aiogram import Bot, Dispatcher
from django.apps import AppConfig

from root.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

class BotConfig(AppConfig):
    name = 'bot'
    default_auto_field = 'django.db.models.BigAutoField'