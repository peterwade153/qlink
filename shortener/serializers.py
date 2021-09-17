from django.db import IntegrityError
from rest_framework import serializers

from .models import Url


class ShortenerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        read_only_fields = ['id', 'user']
        fields = read_only_fields + ['original_url', 'short_url']

    def create(self, validated_data):
        try:
            instance = Url(
                original_url=validated_data['original_url'],
                user=validated_data['user']
            )
            instance.save()
            return instance
        except IntegrityError:
            raise serializers.ValidationError({'error': 'URL short version already created.'})
