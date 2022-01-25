import json
from sellers.application.register_seller import registerSeller
from sellers.application.list_sellers import listSellers

def registerSellerHandler(event, context):
  body = json.loads(event['body'])
  return registerSeller(name=body['name'], email=body['email'], password=body['password'])

def listSellersHandler(event, context):
  return listSellers()