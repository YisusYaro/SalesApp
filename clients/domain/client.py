import bcrypt
from clients.domain.error import Error

class Client(object):
  
  def __init__(self, _dict):
    self.__dict__.update(_dict)
  
  def setPassword(self, password):
    if(password == ''):
      raise Exception(Error.CAN_NOT_SET_PASSWORD)
    self.password = bcrypt.hashpw(password, bcrypt.gensalt())