from django.core.management.base import BaseCommand
from app.telegrambot import Run, PrintSessions

class Command(BaseCommand):
    help = 'Run Telegrambot command'

    def handle(self, *args, **kwargs):
        try:
            Run()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))

