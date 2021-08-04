from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User


class RegisterAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='jacob@gmail.com', password='Top_secret')

    def test_register_user(self):
        data = {
            'email': 'test@gmail.com',
            'password': 'Passtest123'
        }
        response = self.client.post('/auth/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_existing_user(self):
        data = {
            'email': 'jacob@gmail.com',
            'password': 'Top_secret'
        }
        response = self.client.post('/auth/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
