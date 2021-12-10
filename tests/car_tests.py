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

# Creating dummy person
ints = random.sample(range(11), k=10)
random_registry = ''.join(str(int) for int in ints)
payload = {
  "registry": random_registry,
  "name": "Dummy"
  }
resp = session.post(f'{url}/person', json=payload)

# Creating ramdom car for the tests
random_license_plate = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))

# Car routes
class CarTest(unittest.TestCase):
  def test_a_create_car_missing_parameters(self):
    payload = {}
    resp = session.post(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing license_plate parameter in payload')

  def test_b_successfull_car_creation(self):
    payload = {
      "license_plate": random_license_plate,
      "type": "sedan",
      "color": "yellow",
      "owner_registry": random_registry
    }
    resp = session.post(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Car created successfully')

  def test_c_failing_to_find_car(self):
    resp = session.get(f'{url}/car/ZZZ999')
    self.assertEqual(resp.status_code, 404)
    self.assertEqual(resp.json()['message'], 'Car not found')

  def test_d_successfully_finding_car(self):
    resp = session.get(f'{url}/car/{random_license_plate}')
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Car found successfully')

  def test_e_patching_car_missing_parameter(self):
    payload = {"color": "yellow"}
    resp = session.patch(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing license_plate parameter in payload')

  def test_f_successfully_patching_car(self):
    payload = {
      "license_plate": random_license_plate,
      "color": "yellow"
    }
    resp = session.patch(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Car data updated successfully')

  def test_g_deleting_car_missing_parameter(self):
    payload = {}
    resp = session.delete(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 400)
    self.assertEqual(resp.json()['message'], 'Missing license_plate parameter in payload')
  
  def test_g_successfully_deleting_car(self):
    payload = {"license_plate": random_license_plate}
    resp = session.delete(f'{url}/car', json=payload)
    self.assertEqual(resp.status_code, 200)
    self.assertEqual(resp.json()['message'], 'Car deleted successfully')


if __name__ == '__main__':
  unittest.main(argv=['first-arg-is-ignored'], exit=False)