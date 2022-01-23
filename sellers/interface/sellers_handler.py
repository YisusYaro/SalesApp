import json
from sellers.application.register_seller import registerSeller

def register_seller_handler(event, context):
  body = json.loads(event['body'])
  return registerSeller(name=body['name'], email=body['email'], password=body['password'])