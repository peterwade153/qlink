from rest_framework import status

from . import BaseAPITestCase, UrlFactory


class ShortenerAPITestCase(BaseAPITestCase):

    def test_create_short_link(self):
        data = {
            'original_url': 'https://hakibenita.com/django-nested-transaction',
        }
        res = self.login_user()
        token = res.data['key']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post('/api/shortener/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_short_link(self):
        UrlFactory(
            original_url='https://hakibenita.com/django-transaction',
            user=self.user
        )
        data = {
            'original_url': 'https://hakibenita.com/django-transaction',
        }
        res = self.login_user()
        token = res.data['key']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post('/api/shortener/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
