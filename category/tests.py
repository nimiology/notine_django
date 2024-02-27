from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from category.models import Category


def get_user_token(username):
    user = get_user_model().objects.create(username=username, password='1234')
    refresh = RefreshToken.for_user(user)
    return user, f'Bearer {refresh.access_token}'


class CategoryAPITest(APITestCase):
    def setUp(self) -> None:
        self.user, self.token = get_user_token('John')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.category = Category.objects.create(owner=self.user, title='test')

    def test_categories_get(self):
        response = self.client.get(reverse('category:category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], Category.objects.count())

    def test_category_get_not_found(self):
        self.user, self.token = get_user_token('Jane')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.get(reverse('category:category-detail', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_category_get(self):
        response = self.client.get(reverse('category:category-detail', kwargs={'pk': self.category.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_unique(self):
        response = self.client.post(reverse('category:category-list',), data={'title': self.category.title})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
