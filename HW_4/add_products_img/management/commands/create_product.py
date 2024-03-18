from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Create a new product in the database"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('count', type=int, help='Product count')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        count = kwargs.get('count')

        product = Product.objects.create(name=name, description=description, price=price, count=count)
        self.stdout.write(f'Product created successfully: {product}')
