class CarModel():
  def __init__(self, db):
    self.__db = db
    self.model = self.__generate_model()
    
  def __generate_model(self):                                                                                                                                                                                                    
    db = self.__db
    class Car(db.Model):
      license_plate = db.Column(db.String(6), primary_key=True, unique=True, nullable=False)
      type = db.Column(db.String(30), nullable=False)
      color = db.Column(db.String(30), default=True)
      owner_registry = db.Column(db.String(11), db.ForeignKey("person.registry", ondelete='CASCADE'))

    return Car