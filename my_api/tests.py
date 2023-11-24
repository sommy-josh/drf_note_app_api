from django.test import TestCase
from .models import NoteApp
from django.urls import reverse
from rest_framework import status

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import response

class NoteTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.note=NoteApp.objects.create(
            title='First Note',
            body='A body of text here'
        )
    def test_model_content(self):
        self.assertEqual(self.note.title, 'First Note')
        self.assertSetEqual(self.note.body,'A body of text here')
        self.assertEqual(str(self.note), 'First Note')
