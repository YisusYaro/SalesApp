import os
import boto3
from shared.infraestructure.data_structures.singleton import Singleton


class TokenService(metaclass=Singleton):
  
  def __init__(self):
    self.client = boto3.client(
      'cognito-idp', 
      region_name=os.environ.get('REGION')
      )
    self.clientId = os.environ.get('COGNITO_ID') 

  def signUp(self, email, password):
    self.client.sign_up(
      ClientId=self.clientId,
      Username=email,
      Password=password
      )




