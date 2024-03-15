from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from shop.models import Order, Client
from .forms import FindOrdersForm



def index(request):
    data = {
        'title': 'главная',
    }
    return render(request, 'shop/index.html', context=data)


def about(request):
    data = {
        'title': 'о себе',
    }
    return render(request, 'shop/about.html', context=data)


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

    return render(request, 'shop/orders_list.html', context)


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
    return render(request, 'shop/find_order_form.html', {'form': form})
