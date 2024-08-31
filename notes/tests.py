from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteAPITests(APITestCase):

    def test_create_note(self):
        """
        Ensure we can create a new note.
        """
        url = reverse('create_note')
        data = {'title': 'Test Note', 'body': 'This is a test note'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_fetch_note(self):
        """
        Ensure we can fetch a note by its ID.
        """
        note = Note.objects.create(title='Fetch Note', body='This is a note to fetch')
        url = reverse('fetch_note', kwargs={'pk': note.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Fetch Note')
        self.assertEqual(response.data['body'], 'This is a note to fetch')

    def test_query_notes(self):
        """
        Ensure we can query notes by title substring.
        """
        Note.objects.create(title='Query Note 1', body='This is note 1')
        Note.objects.create(title='Query Note 2', body='This is note 2')
        url = reverse('query_notes')
        response = self.client.get(url, {'title': 'Query'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_note(self):
        """
        Ensure we can update an existing note.
        """
        note = Note.objects.create(title='Update Note', body='This is a note to update')
        url = reverse('update_note', kwargs={'pk': note.id})
        data = {'title': 'Updated Note', 'body': 'This note has been updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Note')
        self.assertEqual(response.data['body'], 'This note has been updated')

    def test_fetch_nonexistent_note(self):
        """
        Ensure fetching a non-existent note returns a 404 error.
        """
        url = reverse('fetch_note', kwargs={'pk': 999})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_update_nonexistent_note(self):
        """
        Ensure updating a non-existent note returns a 404 error.
        """
        url = reverse('update_note', kwargs={'pk': 999})
        data = {'title': 'Non-existent Note', 'body': 'This note does not exist'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
