from django.core.management.base import BaseCommand
from shop.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create a new order in the database"

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID for the order')
        parser.add_argument('product_ids', nargs='+', type=int, help='Product IDs for the order')

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('client_id')
        product_ids = kwargs.get('product_ids')

        client = Client.objects.filter(pk=client_id).first()
        if client is None:
            self.stdout.write(f'Client with ID {client_id} does not exist in the database')
            return

        products = Product.objects.filter(pk__in=product_ids)
        if len(products) != len(product_ids):
            self.stdout.write('One or more products do not exist in the database')
            return

        insufficient_products = []
        for product in products:
            if product.count <= 0:
                insufficient_products.append(product.name)
                continue
            product.count -= 1
            product.save()

        if insufficient_products:
            for product_name in insufficient_products:
                self.stdout.write(f'Product {product_name} is out of stock')
            return

        total_amount = sum(product.price for product in products)
        order = Order.objects.create(customer=client, total_amount=total_amount)
        order.products.set(products)

        self.stdout.write(f'Order created successfully: {order}')
