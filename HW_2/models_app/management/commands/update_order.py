from django.core.management.base import BaseCommand
from models_app.models import Order, Client, Product


class Command(BaseCommand):
    help = "Update order details by ID"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')
        parser.add_argument('client_id', type=int, help='New client ID for the order')
        parser.add_argument('product_ids', nargs='+', type=int, help='New product IDs for the order')
        parser.add_argument('total_amount', type=float, help='New total amount for the order')

    def handle(self, *args, **kwargs):
        order_id = kwargs.get('order_id')
        client_id = kwargs.get('client_id')
        product_ids = kwargs.get('product_ids')
        total_amount = kwargs.get('total_amount')

        order = Order.objects.filter(pk=order_id).first()
        if order is None:
            self.stdout.write(f'Order with ID {order_id} does not exist in the database')
            return

        client = Client.objects.filter(pk=client_id).first()
        if client is None:
            self.stdout.write(f'Client with ID {client_id} does not exist in the database')
            return

        products = Product.objects.filter(pk__in=product_ids)
        if len(products) != len(product_ids):
            self.stdout.write('One or more products do not exist in the database')
            return

        order.customer = client
        order.total_amount = total_amount
        order.products.set(products)
        order.save()
        self.stdout.write(f'Order details updated successfully: {order}')
