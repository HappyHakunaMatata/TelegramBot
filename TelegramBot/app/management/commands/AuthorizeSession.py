from django.core.management.base import BaseCommand
from app.telegrambot import GetAllMembers
import asyncio

class Command(BaseCommand):
    help = 'Run Telegrambot command'

    def handle(self, *args, **kwargs):
        try:
            asyncio.run(GetAllMembers())
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
