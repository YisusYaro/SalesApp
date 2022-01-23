from clients.domain.client import Client

def create(id, name, email):
  return Client({'id':id, 'name':name, 'email':email})

def reconstitute(id, name, email, password):
  return Client({'id':id, 'name':name, 'email':email, 'password':password})