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

    def test_get_short_links(self):
        res = self.login_user()
        token = res.data['key']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.get('/api/shortener/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_visit_shortened_url(self):
        url = UrlFactory(
            original_url='https://hakibenita.com/django-transaction',
            user=self.user
        )
        response = self.client.get(f'/api/{url.short_url}')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_visit_non_existing_shortened_url(self):
        response = self.client.get('/api/QJHNDIJ2as')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
