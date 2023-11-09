from django.apps import AppConfig
from threading import Thread
import logging


class TelegramBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TelegramBot'
    
    def ready(self):
        from app.telegrambot import update_schedule, schedule_checker
        try:
            Thread(target=update_schedule).start()
            Thread(target=schedule_checker).start()
        except Exception as err:
            logging.error(f"Произошла ошибка: {err}")