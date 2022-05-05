from rest_framework import serializers
from product.models import Product
from product.models import Category

class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
       model = Category
       fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
       model = Product
       fields = "__all__"

class ImageCreateSerializer(serializers.Serializer):
    image = serializers.ImageField(label='Photo', max_length=100, read_only=False)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    def create(self, validated_data):
        return ItemImage.objects.create(**validated_data)