import os
import jwt
from functools import wraps
from flask import request

SECRET = os.environ['JWT_SECRET']

def generate_jwt_token(username):
  key = SECRET
  return jwt.encode({"username": username}, key, algorithm="HS256")

def authentication_middleware(function=None):
  @wraps(function)
  def wrapper(*args, **kwargs):
    _ = function(*args, **kwargs)
    try:
      token = request.headers.environ['HTTP_AUTHORIZATION']
    except KeyError:
      return {"message": "Missing authorization token"}, 400
    try:
      jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
      return {"message": "Invalid authorization token"}, 401
    return _
  return wrapper