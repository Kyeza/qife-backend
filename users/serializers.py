from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']


class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SlugRelatedField(slug_field='key', read_only=True)

    class Meta:
        model = User
        fields = ['uuid', 'phone_number', 'user_type', 'location', 'auth_token']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data.get('phone_number'))

        if user:
            if validated_data.get('user_type'):
                user.user_type = validated_data.get('user_type')

            if validated_data.get('location'):
                user.location = validated_data.get('location')

        return user

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get('user_type')
        instance.location = validated_data.get('location')

        return instance


