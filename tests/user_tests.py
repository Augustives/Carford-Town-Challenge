import unittest
import requests
import string
import random
import os

# Flask Server URL
url = os.environ['FLASK_URL']

# Creating session
session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})

# Creating ramdom user for the tests
random_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))

# User routes
class UserTest(unittest.TestCase):
  def test_a_create_user_with_missing_parameter(self):
    payload = {"username": "admin"}
    resp = session.post(f'{url}/register', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(str(resp.json()['message']), "{'password': 'Missing password parameter in payload'}" )
    payload = {"paswword": "admin"}
    resp = session.post(f'{url}/register', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(str(resp.json()['message']), "{'username': 'Missing username parameter in payload'}")
  
  def test_b_successfull_user_creation(self):
    payload = {
      "username": random_username,
      "password": random_password
    }
    resp = session.post(f'{url}/register', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'User registered successfully')


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)