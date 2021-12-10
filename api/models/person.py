class PersonModel():
  def __init__(self, db):
    self.__db = db
    self.model = self.__generate_model()
    
  def __generate_model(self):
    db = self.__db
    class Person(db.Model):
      registry = db.Column(db.String(11), unique=True, primary_key=True, nullable=False)
      name = db.Column(db.String(30), nullable=False,)
      sale_opportunity = db.Column(db.Boolean, unique=False, default=True)
      cars = db.relationship('Car', backref='person', passive_deletes=True)

    return Person