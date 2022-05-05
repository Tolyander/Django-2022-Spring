from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from product.serializers import ProductSerializer

from .models import Product


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product.html', {'product': product})

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer