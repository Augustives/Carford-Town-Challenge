from flask_restful import Resource
from flask_restful import reqparse

from hashlib import sha256

from api.utils.auth import generate_jwt_token


class LoginRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.__parser = self.__create_parser()
    self.route = self.__create_route()

  def __create_parser(self):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Missing username parameter in payload')
    parser.add_argument('password', type=str, required=True, help='Missing password parameter in payload')
    return parser

  def __create_route(self):
    user_service = self.__module_service.user_service
    parser = self.__parser
    class Login(Resource):
      def post(self):
        payload = parser.parse_args()

        user = user_service.find_user(payload['username'])
        if user is None:
          return {"message": "User not registered"}

        payload['password'] = sha256(payload['password'].encode('utf-8')).hexdigest()
        if payload['password'] != user.password:
          return {"message": "Invalid credentials"}, 401

        return {
          "message": "Logged in successfully",
          "token": str(generate_jwt_token(user.username))
        }

    return Login


class RegisterRoute:
  def __init__(self, model_service) :
    self.__module_service = model_service
    self.__parser = self.__create_parser()
    self.route = self.__create_route()

  def __create_parser(self):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Missing username parameter in payload')
    parser.add_argument('password', type=str, required=True, help='Missing password parameter in payload')
    return parser
  
  def __create_route(self):
    user_service = self.__module_service.user_service
    parser = self.__parser
    class Register(Resource):
      def post(self):
        payload = parser.parse_args()
        payload['password'] = sha256(payload['password'].encode('utf-8')).hexdigest()

        user = user_service.find_user(payload['username'])
        if user is not None:
          return {"message": "User already registered"}
        
        user_service.create_user(payload)
        return {"message": "User registered successfully"}

    return Register