import unittest

from auth_tests import AuthTest
from user_tests import UserTest
from person_tests import PersonTest
from car_tests import CarTest

# Using a developmente database is recommneded to run the tests

# Tests
t1 = unittest.TestLoader().loadTestsFromTestCase(AuthTest)
t2 = unittest.TestLoader().loadTestsFromTestCase(UserTest)
t3 = unittest.TestLoader().loadTestsFromTestCase(PersonTest)
t4 = unittest.TestLoader().loadTestsFromTestCase(CarTest)



# Creating suite
routes_tests = unittest.TestSuite([t1, t2, t3, t4])

if __name__ == '__main__':
  unittest.TextTestRunner().run(routes_tests)