from curses import meta
from shared.infraestructure.data_structures.singleton import Singleton
from clients.domain.client import Client


class ClientFactory(metaclass=Singleton):

  def create(self, id, name, email):
    return Client({'id':id, 'name':name, 'email':email})

  def reconstitute(self, id, name, email):
    return Client({'id':id, 'name':name, 'email':email})