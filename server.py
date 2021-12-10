import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from api.services.model_service import ModelService

from api.routes.home import HomeRoute
from api.routes.user import LoginRoute, RegisterRoute
from api.routes.car import CarFindRoute, CarRoute
from api.routes.person import PersonFindRoute, PersonRoute


class Server():
  def __init__(self):
    load_dotenv()
    self.__app = Flask(__name__)
    self.__add_configs()
    self.__api = Api(self.__app)
    self.__db = SQLAlchemy(self.__app)
    
    self.__model_service = ModelService(self.__db)
    self.__model_service.generate_test_user()

  def __enter__(self):
    print('Server is running')
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    print('Server closed')

  def __add_configs(self):
    self.__app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

  def __add_routes(self):
    self.__api.add_resource(HomeRoute(self.__model_service).route, '/')
    self.__api.add_resource(LoginRoute(self.__model_service).route, '/login')
    self.__api.add_resource(RegisterRoute(self.__model_service).route, '/register')
    self.__api.add_resource(PersonRoute(self.__model_service).route, '/person')
    self.__api.add_resource(PersonFindRoute(self.__model_service).route, '/person/<string:person_registry>')
    self.__api.add_resource(CarRoute(self.__model_service).route, '/car')
    self.__api.add_resource(CarFindRoute(self.__model_service).route, '/car/<string:license_plate>')

  def run(self):
    self.__add_routes()
    self.__app.run(host='0.0.0.0', port=os.environ['PORT'], debug=True)

if __name__ == '__main__':
  with Server() as server:
    server.run()