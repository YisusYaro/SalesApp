import json
from products.application.create_product import createProduct

def createProductHandler(event, context):
  body = json.loads(event['body'])
  return createProduct(name=body['name'], price=body['price'], category=body['category'])