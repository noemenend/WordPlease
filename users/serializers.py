from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers


class UserListSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()


class UserSerializer(UserListSerializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        return self.update(user, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


    def validate_username(self, value):
        username = slugify(value)
        # validacion si estoy actualizando un usuario
        if self.instance is not None and self.instance.username != username and User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username '{0}' already exists".format(value))

        # validacion si estoy creando un usuario
        if self.instance is None and User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username '{0}' already exists".format(value))

        return username
