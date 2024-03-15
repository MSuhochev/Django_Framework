from django.core.management.base import BaseCommand
from shop.models import Client


class Command(BaseCommand):
    help = "Update client details by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='New client name')
        parser.add_argument('email', type=str, help='New client email')
        parser.add_argument('phone', type=str, help='New client phone')
        parser.add_argument('address', type=str, help='New client address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.name = name
            client.email = email
            client.phone = phone
            client.address = address
            client.save()
            self.stdout.write(f'Client details updated successfully: {client}')
        else:
            self.stdout.write(f'Client with ID {pk} does not exist in the database')
