from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"
        depth=1

    code = serializers.ReadOnlyField()


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['codes']
        
    codes = serializers.ReadOnlyField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
