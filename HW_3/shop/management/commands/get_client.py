from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = "Get client details by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            self.stdout.write(f'{client}')
        else:
            self.stdout.write(f'Client with ID {pk} does not exist in the database')
