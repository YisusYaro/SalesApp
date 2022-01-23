import json
from clients.application.register_client import registerClient

def registerClientHandler(event, context):
  body = json.loads(event['body'])
  return registerClient(name=body['name'], email=body['email'], password=body['password'])