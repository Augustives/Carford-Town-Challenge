import os
from hashlib import sha256

from api.models.user import UserModel
from api.models.car import CarModel
from api.models.person import PersonModel
from api.services.car_service import CarService

from api.services.person_service import PersonService
from api.services.user_service import UserService


class ModelService:
  def __init__(self, db):
    self.__db = db
    self.user_model, self.car_model, self.person_model = self.__create_all_models()
    self.user_service = UserService(self.__db, self.user_model)
    self.person_service = PersonService(self.__db, self.person_model)
    self.car_service = CarService(self.__db, self.car_model)

  def __create_all_models(self):
    user_model = UserModel(self.__db).model
    person_model = PersonModel(self.__db).model
    car_model = CarModel(self.__db).model

    self.__db.create_all()
    return user_model, car_model, person_model

  def generate_test_user(self):
    user = {
      "username": os.environ['TEST_USER_USERNAME'],
      "password": sha256(os.environ['TEST_USER_PASSWORD'].encode('utf-8')).hexdigest()
    }
    try:
      self.user_service.create_user(user)
    except Exception:
      self.__db.session.rollback()
