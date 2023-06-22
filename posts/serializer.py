from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    emphasis = serializers.BooleanField(required=False)
    image = serializers.ImageField()
    description = serializers.CharField()
    content = serializers.JSONField()
    created_at = serializers.DateTimeField(read_only=True)
    update_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)