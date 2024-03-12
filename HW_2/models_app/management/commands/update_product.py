from django.core.management.base import BaseCommand
from models_app.models import Product

class Command(BaseCommand):
    help = "Update product details by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='New product name')
        parser.add_argument('description', type=str, help='New product description')
        parser.add_argument('price', type=float, help='New product price')
        parser.add_argument('count', type=int, help='New product count')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        count = kwargs.get('count')

        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.name = name
            product.description = description
            product.price = price
            product.count = count
            product.save()
            self.stdout.write(f'Product details updated successfully: {product}')
        else:
            self.stdout.write(f'Product with ID {pk} does not exist in the database')
