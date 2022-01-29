from sellers.domain.seller import Seller

def create(id, name, email):
  return Seller({'id':id, 'name':name, 'email':email})

def reconstitute(id, name, email):
  return Seller({'id':id, 'name':name, 'email':email})