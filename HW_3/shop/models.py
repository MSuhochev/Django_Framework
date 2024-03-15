from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    registr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, register_date: {self.registr_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Product_name: {self.name}, price: {self.price}, count: {self.count}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer}, total_amount: {self.total_amount}, date_ordered: {self.date_ordered}'

