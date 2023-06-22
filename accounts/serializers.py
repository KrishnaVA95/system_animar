from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # shift = serializers.ChoiceField(
    #     choices=ShiftOptions.choices, default=ShiftOptions.DEFAULT
    # )
    email = serializers.EmailField(max_length=127)
    # first_name = serializers.CharField(max_length=127)
    # last_name = serializers.CharField(max_length=127)
    username = serializers.CharField(max_length=127)
    password = serializers.CharField(max_length=127, write_only=True)

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance