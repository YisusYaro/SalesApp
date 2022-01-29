from clients.domain.error import Error

class Client(object):
  
  def __init__(self, _dict):
    self.__dict__.update(_dict)
  