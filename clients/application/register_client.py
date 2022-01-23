from clients.domain.client_factory import create
from clients.infraestructure.repositories.client_repository import getId, save, findByEmail

def registerClient(name, email, password):

  client = findByEmail(email)

  if(client):
   return {
    'statusCode': 200,
   } 

  client = create(id=getId(), name=name, email=email)

  client.setPassword(password=password)

  save(client)

  return {
    'statusCode': 201,
  }