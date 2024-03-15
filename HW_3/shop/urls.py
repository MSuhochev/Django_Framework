from django.urls import path
from . import views
from .views import orders_list, find_order_form

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/<str:period>/', orders_list, name='orders_list'),
    path('find_orders/', find_order_form, name='find_order_form'),
]
