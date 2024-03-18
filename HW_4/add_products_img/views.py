from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from add_products_img.models import Order, Client, Product
from .forms import FindOrdersForm, AddProductForm


def index(request):
    data = {
        'title': 'главная',
    }
    return render(request, 'add_products_img/index.html', context=data)


def about(request):
    data = {
        'title': 'о себе',
    }
    return render(request, 'add_products_img/about.html', context=data)


def orders_list(request, client_id, period):
    # Получаем клиента по его ID
    client = get_object_or_404(Client, pk=client_id)

    today = timezone.now()
    start_date = None

    # Определяем начальную дату в зависимости от выбранного периода
    if period == 'week':
        period_ru = "7 дней"
        start_date = today - timedelta(days=7)
    elif period == 'month':
        period_ru = "месяц"
        start_date = today - timedelta(days=30)
    elif period == 'year':
        period_ru = "год"
        start_date = today - timedelta(days=365)

    # Получаем все заказы клиента за выбранный период
    orders = Order.objects.filter(customer=client, date_ordered__gte=start_date)

    # Создаем множество для хранения уникальных товаров
    unique_products = set()

    # Получаем все уникальные товары из заказов за выбранный период
    for order in orders:
        unique_products.update(order.products.all())

    # Сортируем товары по времени добавления
    ordered_products = sorted(unique_products, key=lambda x: x.add_date, reverse=True)

    context = {
        'title': 'лист заказов',
        'ordered_products': ordered_products,
        'period': period.capitalize(),
        'period_ru': period_ru,
        'client': client,
    }

    return render(request, 'add_products_img/orders_list.html', context)


def find_order_form(request):
    if request.method == 'POST':
        form = FindOrdersForm(request.POST)
        if form.is_valid():
            client_id = form.cleaned_data['pk']
            period = form.cleaned_data['period']
            # обрабатываем данные
            client = Client.objects.filter(pk=client_id).first()
            if client is not None:
                return orders_list(request, client_id, period)
    else:
        form = FindOrdersForm()
    return render(request, 'add_products_img/find_order_form.html', {'form': form})


def add_product_form(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']

            # Сохраняем изображение в папке media
            fs = FileSystemStorage(location='media/')
            filename = fs.save(image.name, image)

            # Получаем путь к сохраненному файлу
            product_img = fs.url(filename)

            # Создаем экземпляр Product с указанием пути к изображению
            product = Product.objects.create(name=name, description=description, price=price,
                                             count=count, product_img=product_img)

            context = {'image': image, 'product': product}
            return render(request, 'add_products_img/added_product.html', context)
    else:
        form = AddProductForm()
    return render(request, 'add_products_img/add_product_form.html', {'form': form})
