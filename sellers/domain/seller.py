import bcrypt
from sellers.domain.error import Error

class Seller:

  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email
  
  def __init__(self, id, name, email, password):
    self.id = id
    self.name = name
    self.email = email
    self.password = password

  def setPassword(self, password):
    if(password == ''):
      raise Exception(Error.CAN_NOT_SET_PASSWORD)
    self.password = bcrypt.hashpw(password, bcrypt.gensalt())