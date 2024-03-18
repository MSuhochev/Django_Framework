from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    registr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Имя клиента: {self.name}, email: {self.email}, тел: {self.phone}, дата регистрации: {self.registr_date}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_img = models.ImageField(upload_to='', max_length=30, null=True, blank=True)
    count = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Наименование продукта: {self.name},\n цена: {self.price},\n количество: {self.count}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказчик: {self.customer},\n общая сумма: {self.total_amount},\n дата заказа: {self.date_ordered}'

