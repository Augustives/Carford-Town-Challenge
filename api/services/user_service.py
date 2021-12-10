class UserService:
  def __init__(self, db, user_model):
    self.__db = db
    self.__user_model = user_model

  def create_user(self, data):
    user = self.__user_model(**data)
    self.__db.session.add(user)
    self.__db.session.commit()

  def find_user(self, username):
    return self.__user_model.query.filter(self.__user_model.username == username).first()

  def patch_user(self, data):
    user = self.__user_model.query.filter(self.__user_model.username == data['username']).first()
    user.password = data['password']
    self.__db.session.commit()

  def delete_user(self, username):
    self.__user_model.query.filter(self.__user_model.username == username).delete()
    self.__db.session.commit()