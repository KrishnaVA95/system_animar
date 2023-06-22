from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=127)
    value = serializers.FloatField()
    emphasis = serializers.BooleanField(required=False)
    image = serializers.ImageField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)
    def create(self, validated_data):
        return Product.objects.create(**validated_data)