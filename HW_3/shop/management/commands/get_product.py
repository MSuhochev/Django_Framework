from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Get product details by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'Product with ID {pk} does not exist in the database')
