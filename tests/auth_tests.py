import unittest
import requests
import os

# Flask Server URL
url = os.environ['FLASK_URL']

# Creating session
session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})

# Created user to login in routes
test_user_username = os.environ['TEST_USER_USERNAME']
test_user_password = os.environ['TEST_USER_PASSWORD']

# Auth routes
class AuthTest(unittest.TestCase):
  def test_a_missing_jwt_token(self):
    resp = session.get(f'{url}/person/1')
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing authorization token')

  def test_b_invalid_jwt_token(self):
    header = {'Authorization': 'INVALID_TOKEN'}
    resp = session.get(f'{url}/person/1', headers=header)
    self.assertEqual(resp.status_code, 401)
    self.assertEqual(resp.json()['message'], 'Invalid authorization token')

  def test_c_successfull_login(self):
    payload = {
      "username": test_user_username,
      "password": test_user_password
    }
    resp = session.post(f'{url}/login', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Logged in successfully')


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)