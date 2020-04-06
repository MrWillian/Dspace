from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTestCase(APITestCase):

  def test_create_user(self):
    self.post_data = {
      'username': 'test',
      'email': 'test@gmail.com',
      'password': '123456'
    }

    return self.client.post('/api/user/', self.post_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_list_users(self):
    response = self.client.get('/api/user/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
   