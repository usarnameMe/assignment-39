from unittest import TestCase

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Note


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_register(self):
        url = reverse('register')
        data = {'username': 'testuser2', 'password': 'testpassword2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("logout")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class NoteTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.note = Note.objects.create(title="Test Title", body="Test Body", user=self.user)

    def test_create_note(self):
        url = reverse('notes')
        data = {'title': 'Test Title 2', 'body': 'Test Body 2', 'slug': 'test-title-2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_notes_list(self):
        url = reverse('notes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_note_detail(self):
        url = reverse('note_detail', kwargs={'pk': self.note.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_note(self):
        url = reverse('note_detail', kwargs={'pk': self.note.id})
        data = {'title': 'Updated Test Title', 'body': 'Updated Test Body'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class NoteModelTest(TestCase):
    def setUp(self):
        # Create a user for testing Note creation
        self.user = User.objects.create_user(username="sampleuser", password="samplepassword")

    def test_note_creation(self):
        note = Note.objects.create(title="Sample Note", body="This is a test.", user=self.user)
        self.assertEqual(note.title, "Sample Note")