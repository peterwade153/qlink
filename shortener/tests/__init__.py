import factory
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from shortener.models import Url


class UrlFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Url


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test123',
            email='test@gmail.com',
            password='password123'
        )
        self.user.is_active = True
        self.user.save()

    def login_user(self):
        data = {
            'email': 'test@gmail.com',
            'password': 'password123'
        }
        return self.client.post('/auth/login/', data)
