from django.shortcuts import render, redirect
from rest_framework import generics

from cart.cart import Cart

from order.serializers import OrderCreateSerializer, OrderSerializer
from .models import Order, OrderItem


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all() 

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return OrderCreateSerializer
        return OrderSerializer

def start_order(request):
    cart = Cart(request)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        zipcode = request.POST.get('zipcode')
        place = request.POST.get('place')
        phone = request.POST.get('phone')

        order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, zipcode=zipcode, place=place)

        for item in cart:
            product = item['product']
            quantity = int(item['quantity'])
            price = product.price * quantity

            item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

        return redirect('myaccount')
    return redirect('cart')