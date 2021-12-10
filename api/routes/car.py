from flask_restful import Resource
from flask_restful import reqparse

from api.utils.auth import authentication_middleware
from api.utils.validate_car_fields import validate_creation, validate_delete, validate_patch

class CarRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.__parser = self.__create_parser()
    self.route = self.__create_route()

  def __create_parser(self):
    parser = reqparse.RequestParser()
    parser.add_argument('license_plate', type=str)
    parser.add_argument('type', type=str)
    parser.add_argument('color', type=str)
    parser.add_argument('owner_registry', type=str)
    return parser

  def __create_route(self):
    car_service = self.__module_service.car_service
    person_service = self.__module_service.person_service
    parser = self.__parser
    class Car(Resource):
      decorators = [authentication_middleware]
      def post(self):
        payload = parser.parse_args()
        validate = validate_creation(payload)
        if validate:
          return  validate, 400
        car = car_service.find_car(payload['license_plate'])
        if car is not None:
          return {"message": "License plate already registered"}, 400
        owner = person_service.find_person(payload['owner_registry'])
        if owner is None:
          return {"message": "Owner doesnt exist"}, 400
        if len(owner.cars) == 3:
          return {"message": "Selected owner already has 3 cars"}, 400
        car_service.create_car(payload)
        return {"message": "Car created successfully"}

      def patch(self):
        payload = parser.parse_args()
        validate = validate_patch(payload)
        if validate:
          return validate, 400
        car = car_service.find_car(payload['license_plate'])
        if car is None:
           return {"message": "Car not found"}
        car_service.patch_car(payload)
        return {"message": "Car data updated successfully"}

      def delete(self):
        payload = parser.parse_args()
        validate = validate_delete(payload)
        if validate:
          return validate, 400
        car = car_service.find_car(payload['license_plate'])
        if car is None:
           return {"message": "Car not found"}, 404
        car_service.delete_car(payload['license_plate'])
        return {"message": "Car deleted successfully"}

    return Car

class CarFindRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.route = self.__create_route()

  def __create_route(self):
    car_service = self.__module_service.car_service
    class CarFind(Resource):
      decorators = [authentication_middleware]
      def get(self, license_plate):
        car = car_service.find_car(license_plate)
        if car is None:
           return {"message": "Car not found"}, 404
        data = {
          "license_plate": car.license_plate,
          "type": car.type,
          "color": car.color,
          "owner_registry": car.owner_registry,
        }
        return {
          "message": "Car found successfully",
          "data": data
        }

    return CarFind