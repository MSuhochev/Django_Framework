from django.core.management.base import BaseCommand
from models_app.models import Client


class Command(BaseCommand):
    help = "Creating a new Client in database."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone', type=str, help='Client phone')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client(name=name, email=email, phone=phone, address=address)
        client.save()
        self.stdout.write(f'{client}')
