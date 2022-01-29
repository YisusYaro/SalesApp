from ulid import ULID
from shared.infraestructure.data_structures.singleton import Singleton
from clients.infraestructure.models.client_model import ClientModel
from clients.domain.client_factory import ClientFactory


class ClientRepository(metaclass=Singleton):

  def __init__(self):
    self.clientFactory = ClientFactory()

  def getId(self):
    return str(ULID())

  def save(self, client):
    PK = 'clients'
    SK = '{email}#{id}'.format(email=client.email, id=client.id)
    model = ClientModel(PK=PK, SK=SK, name=client.name)
    model.save()
    return

  def findByEmail(self, email):
    for model in ClientModel.query(
      hash_key='clients',
      range_key_condition=ClientModel.SK.startswith(email),
      limit=1
    ):
      return self.__modelToClient(model)
    return False  

  def __modelToClient(self, model):
    SK = model.SK.split('#')
    return self.clientFactory.reconstitute(id=SK[0], name=model.name, email=SK[1])
    

