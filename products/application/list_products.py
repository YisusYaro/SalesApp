import json
from products.infraestructure.queries.product_query import find

def listProducts():

  products = find()

  return {
    'statusCode': 200,
    'body': json.dumps(products, default=lambda seller: seller.__dict__)
  }
