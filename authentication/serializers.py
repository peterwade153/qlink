from rest_framework import serializers

from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['id']
        fields = read_only_fields + ['email', 'password']

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        return User.objects.create_user(
            email=email,
            password=password
        )