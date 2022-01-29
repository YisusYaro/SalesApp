import json
from clients.application.register_client_handler import RegisterClientHandler


def registerClient(event, context):
  body = json.loads(event['body'])
  return RegisterClientHandler().execute(name=body['name'], email=body['email'], password=body['password'])