from rest_framework import serializers
from .models import User, UserConfig


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        UserConfig.objects.create(user=user)
        return user


class UserRLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfig
        fields = ["languague", "theme"]


class UserResponse(serializers.ModelSerializer):
    config = UserConfigSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "config"]
