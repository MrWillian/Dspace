from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class UserTestCase(APITestCase):

  def test_create_user(self):
    self.post_data = self.data_user_object()
    response = self.client.post('/api/v1/user/', self.post_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def test_get_user(self):
    self.post_data = self.data_user_object()
    self.client.post('/api/v1/user/', self.post_data, format='json')

    response = self.client.get('/api/v1/user/1/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_list_users(self):
    response = self.client.get('/api/v1/user/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def data_user_object(self):
    return {
      'id': 1,
      'username': 'test',
      'email': 'test@gmail.com',
      'password': '123456'
    }

  # def test_create_user_with_address(self):
  #   self.post_data = self.data_user_object()
  #   self.post_data_address = {
  #     "user_id": "1",
  #     "country": "Brazil",
  #     "state": "Sao Paulo",
  #     "city": "Sao Paulo",
  #     "place": "Rua Getulio",
  #     "latitude": "-13.0183823",
  #     "longitude": "-42.6983994"
  #   }
  #   response_user = self.client.post('/api/v1/user/', self.post_data, format='json')
  #   response_address = self.client.post('/api/v1/address/', self.post_data, format='json')
  #   self.assertEqual(response_user.status_code, status.HTTP_201_CREATED)
  #   self.assertEqual(response_address.status_code, status.HTTP_201_CREATED)
  