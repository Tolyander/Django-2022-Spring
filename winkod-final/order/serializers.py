from rest_framework import serializers
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # fields = "__all__"
        exclude= ('user', )

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)    