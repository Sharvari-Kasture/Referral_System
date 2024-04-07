from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

class UserRegistrationTestCase(TestCase):
    def test_user_registration(self):
        client = APIClient()
        data = {'name': 'Test User', 'email': 'test@example.com', 'password': 'test123'}
        response = client.post('/user-registration/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserDetailsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='test123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_details(self):
        response = self.client.get('/user-details/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
