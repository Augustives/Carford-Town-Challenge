from flask_restful import Resource
from flask_restful import reqparse

from api.utils.auth import authentication_middleware
from api.utils.validate_person_fields import validate_creation, validate_delete, validate_patch

class PersonRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.__parser = self.__create_parser()
    self.route = self.__create_route()

  def __create_parser(self):
    parser = reqparse.RequestParser()
    parser.add_argument('registry', type=str)
    parser.add_argument('name', type=str)
    parser.add_argument('sale_opportunity', type=bool)
    return parser

  def __create_route(self):
    person_service = self.__module_service.person_service
    parser = self.__parser
    class Person(Resource):
      decorators = [authentication_middleware]
      def post(self):
        payload = parser.parse_args()
        validate = validate_creation(payload)
        if validate:
          return validate, 400
        person = person_service.find_person(payload['registry'])
        if person is not None:
          return {"message": "Person already registered"}
        person_service.create_person(payload)
        return {"message": "Person created successfully"}

      def patch(self):
        payload = parser.parse_args()
        validate = validate_patch(payload)
        if validate:
          return validate, 400
        person = person_service.find_person(payload['registry'])
        if person is None:
           return {"message": "Person not found"}, 404
        person_service.patch_person(payload)
        return {"message": "Person data updated successfully"}

      def delete(self):
        payload = parser.parse_args()
        validate = validate_delete(payload)
        if validate:
          return validate, 400
        person = person_service.find_person(payload['registry'])
        if person is None:
           return {"message": "Person not found"}, 404
        person_service.delete_person(payload['registry'])
        return {"message": "Person deleted successfully"}

    return Person

class PersonFindRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.route = self.__create_route()

  def __create_route(self):
    person_service = self.__module_service.person_service
    class PersonFind(Resource):
      decorators = [authentication_middleware]
      def get(self, person_registry):
        person = person_service.find_person(person_registry)
        if person is None:
           return {"message": "Person not found"}, 404
        data = {
          "registry": person.registry,
          "name": person.name,
          "sale_opportunity": str(person.sale_opportunity)
        }
        return {
          "message": "Person found successfully",
          "data": data
        }

    return PersonFind