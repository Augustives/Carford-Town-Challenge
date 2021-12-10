class UserModel():
  def __init__(self, db):
    self.__db = db
    self.model = self.__generate_model()
    
  def __generate_model(self):
    db = self.__db
    class User(db.Model):
      username = db.Column(db.String(50), unique=True, nullable=False, primary_key=True)
      password = db.Column(db.String(500), unique=True, nullable=False)

    return User