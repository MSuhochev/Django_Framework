from django.urls import path
from . import views
from .views import orders_list, find_order_form, add_product_form
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/<str:period>/', orders_list, name='orders_list'),
    path('find_orders/', find_order_form, name='find_order_form'),
    path('add_product/', add_product_form, name='add_product_form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)