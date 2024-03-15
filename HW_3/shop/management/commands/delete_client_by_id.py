from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = "Delete client from database by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
            self.stdout.write(f'Client {pk} was delete.')
        else:
            self.stdout.write(f'Client with {pk} not exist in database')
