class PersonService:
  def __init__(self, db, person_model):
    self.__db = db
    self.__person_model = person_model

  def create_person(self, data):
    person = self.__person_model(**data)
    self.__db.session.add(person)
    self.__db.session.commit()

  def find_person(self, registry):
    return self.__person_model.query.filter(self.__person_model.registry == registry).first()

  def patch_person(self, data):
    person = self.__person_model.query.filter(self.__person_model.registry == data['registry']).first()
    person.name = data['name'] if data['name'] != None else person.name
    person.sale_opportunity = data['sale_opportunity'] if data['sale_opportunity'] != None else person.sale_opportunity
    self.__db.session.commit()

  def delete_person(self, registry):
    self.__person_model.query.filter(self.__person_model.registry == registry).delete()
    self.__db.session.commit()