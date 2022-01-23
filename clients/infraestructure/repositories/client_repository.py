from ulid import ULID
from clients.infraestructure.models.client_model import ClientModel
from clients.domain.client_factory import reconstitute

def getId():
  return str(ULID())

def save(client):
  PK = 'clients'
  SK = '{email}#{id}'.format(email=client.email, id=client.id)
  model = ClientModel(PK=PK, SK=SK, name=client.name, password=client.password)
  model.save() 
  return

def findByEmail(email):
  for model in ClientModel.query(
    hash_key='clients',
    range_key_condition=ClientModel.SK.startswith(email),
    limit=1
  ):
    return modelToClient(model)
  return False  

def modelToClient(model):
  SK = model.SK.split('#')
  return reconstitute(id=SK[0], name=model.name, email=SK[1], password=model.password)
  

