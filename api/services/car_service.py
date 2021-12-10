from psycopg2 import IntegrityError


class CarService:
  def __init__(self, db, car_model):
    self.__db = db
    self.__car_model = car_model

  def create_car(self, data):
    car = self.__car_model(**data)
    self.__db.session.add(car)
    self.__db.session.commit()

  def find_car(self, license_plate):
    return self.__car_model.query.filter(self.__car_model.license_plate == license_plate).first()

  def patch_car(self, data):
    car = self.__car_model.query.filter(self.__car_model.license_plate == data['license_plate']).first()
    car.type = data['type'] if data['type'] != None else car.type
    car.color = data['color'] if data['color'] != None else car.color
    car.owner = data['owner_registry'] if data['owner_registry'] != None else car.owner_registry
    self.__db.session.commit()

  def delete_car(self, license_plate):
    self.__car_model.query.filter(self.__car_model.license_plate == license_plate).delete()
    self.__db.session.commit()