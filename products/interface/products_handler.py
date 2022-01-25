import json
from products.application.create_product import createProduct
from products.application.list_products import listProducts

def createProductHandler(event, context):
  body = json.loads(event['body'])
  return createProduct(name=body['name'], price=body['price'], category=body['category'])

def listProductsHandler(event, context):
  return listProducts()