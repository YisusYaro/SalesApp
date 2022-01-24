from itertools import product
from products.domain.product_factory import create
from products.infraestructure.repositories.product_repository import getId, save

def createProduct(name, price, category):

  product = create(id=getId(), name=name, price=price, category=category)

  save(product)

  return {
    'statusCode': 200,
  }