from django.core.management.base import BaseCommand
from shop.models import Order


class Command(BaseCommand):
    help = "Delete order from database by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()
        if order is not None:
            order.delete()
            self.stdout.write(f'Order with ID {pk} was deleted.')
        else:
            self.stdout.write(f'Order with ID {pk} does not exist in the database')
