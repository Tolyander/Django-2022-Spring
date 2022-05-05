from django.urls import path

from .views import start_order, OrderList

urlpatterns = [
    path('start_order/', start_order, name='start_order'),
    path('orders/', OrderList.as_view())
]