from sellers.domain.error import Error

class Seller:

  def __init__(self, _dict):
    self.__dict__.update(_dict)