from sellers.domain.sellers_factory import create
from sellers.infraestructure.repositories.seller_repository import getId, save, findByEmail

def registerSeller(name, email, password):

  seller = findByEmail(email)

  if(seller):
   return {
    'statusCode': 200,
   } 

  seller = create(id=getId(), name=name, email=email)

  seller.setPassword(password=password)

  save(seller)

  return {
    'statusCode': 201,
  }