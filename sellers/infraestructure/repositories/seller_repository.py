import imp
from os import name
from statistics import mode


import boto3
from ulid import ULID
from sellers.infraestructure.models.seller_model import SellerModel
from sellers.domain.sellers_factory import create, reconstitute

def getId():
  return str(ULID())

def save(seller):
  PK = 'sellers'
  SK = '{email}#{id}'.format(email=seller.email, id=seller.id)
  model = SellerModel(PK=PK, SK=SK, name=seller.name, password=seller.password)
  model.save() 
  return

def findByEmail(email):
  for model in SellerModel.query(
    hash_key='sellers',
    range_key_condition=SellerModel.SK.startswith(email),
    limit=1
  ):
    return modelToSeller(model)
  return False  

def modelToSeller(model):
  SK = model.SK.split('#')
  return reconstitute(id=SK[0], name=model.name, email=SK[1], password=model.password)
  

