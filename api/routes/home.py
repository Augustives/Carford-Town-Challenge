from flask_restful import Resource


class HomeRoute:
  def __init__(self, model_service):
      self.__model_service = model_service
      self.route = self.__create_route()

  def __create_route(self):
    class Home(Resource):
      def get(self):
        return {"message": "API Online"}

    return Home