import json
from sellers.infraestructure.queries.seller_query import find

def listSellers():

  sellers = find()

  return {
    'statusCode': 200,
    'body': json.dumps(sellers, default=lambda seller: seller.__dict__)
  }
