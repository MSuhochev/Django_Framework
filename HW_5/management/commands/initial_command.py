from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Greetings with initial commands."

    def handle(self, *args, **kwargs):
        self.stdout.write("Hello my dear friend!")
