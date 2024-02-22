from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from category.models import Category
from category.tests import get_user_token
from note.models import Note


class NoteAPITest(APITestCase):
    def setUp(self) -> None:
        self.user, self.token = get_user_token('John')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        self.category = Category.objects.create(title='test')
        self.note = Note.objects.create(title='test', owner=self.user, category=self.category)

    def test_get_all_notes(self):
        response = self.client.get(reverse('note:note-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_notes_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('note:note-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_note(self):
        response = self.client.get(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_note_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_note_not_found(self):
        self.user, self.token = get_user_token('Jane')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.get(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_put_note(self):
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.put(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_note_not_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.put(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_note_not_found(self):
        self.user, self.token = get_user_token('Jane')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.put(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_note(self):
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.patch(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_note_not_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.patch(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_note_not_found(self):
        self.user, self.token = get_user_token('Jane')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        data = {'title': 'test', 'category': self.category.pk}
        response = self.client.patch(reverse('note:note-detail', args=[self.note.id]), data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_note(self):
        response = self.client.delete(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_note_not_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_note_not_found(self):
        self.user, self.token = get_user_token('Jane')
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        response = self.client.delete(reverse('note:note-detail', args=[self.note.id]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
