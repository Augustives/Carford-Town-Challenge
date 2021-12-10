import unittest
import requests
import os
import random
import string

# Flask Server URL
url = os.environ['FLASK_URL']

# Created user to login in routes
test_user_username = os.environ['TEST_USER_USERNAME']
test_user_password = os.environ['TEST_USER_PASSWORD']

# Creating session
session = requests.Session()
session.headers.update({'Content-Type': 'application/json'})
payload = {
      "username": test_user_username,
      "password": test_user_password
    }
resp = session.post(f'{url}/login', json=payload)
session.headers.update({'Authorization': resp.json()['token']})

# Creating ramdom person for the tests
ints = random.sample(range(11), k=10)
random_registry = ''.join(str(int) for int in ints)
random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))

# Person routes
class PersonTest(unittest.TestCase):
  def test_a_create_person_missing_parameters(self):
    payload = {}
    resp = session.post(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing registry parameter in payload')

  def test_b_successfull_person_creation(self):
    payload = {
      "registry": random_registry,
      "name": random_name
      }
    resp = session.post(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Person created successfully')

  def test_c_failing_to_find_person(self):
    resp = session.get(f'{url}/person/99')
    self.assertEqual(resp.status_code, 404)
    self.assertEqual(resp.json()['message'], 'Person not found')

  def test_d_successfully_finding_person(self):
    resp = session.get(f'{url}/person/{random_registry}')
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Person found successfully')

  def test_e_patching_person_missing_parameter(self):
    payload = {"name": "Patch Test"}
    resp = session.patch(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing registry parameter in payload')

  def test_f_successfully_patching_person(self):
    payload = {
      "registry": random_registry,
      "name": random_name
    }
    resp = session.patch(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Person data updated successfully')

  def test_g_deleting_person_missing_parameter(self):
    payload = {}
    resp = session.delete(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing registry parameter in payload')
  
  def test_g_successfully_deleting_person(self):
    payload = {"registry": random_registry}
    resp = session.delete(f'{url}/person', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Person deleted successfully')


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)