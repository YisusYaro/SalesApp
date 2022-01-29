from shared.infraestructure.data_structures.singleton import Singleton
from clients.infraestructure.repositories.client_repository import ClientRepository
from clients.domain.client_factory import ClientFactory
from tokens.infraestructure.token_service import TokenService

class RegisterClientHandler(metaclass=Singleton):
    
  def __init__(self):
    self.clientFactory = ClientFactory()
    self.tokenService = TokenService()
    self.clientRepository = ClientRepository()

  def execute(self, name, email, password):

    client = self.clientRepository.findByEmail(email)

    if(client):
      return {
        'statusCode': 200,
      } 

    client = self.clientFactory.create(id=self.clientRepository.getId(), name=name, email=email)
    
    self.tokenService.signUp(email=client.email, password=password)

    self.clientRepository.save(client)

    return {
      'statusCode': 200,
    }