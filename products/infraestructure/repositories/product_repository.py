from ulid import ULID
from products.infraestructure.models.product_model import ProductModel
from products.domain.product_factory import reconstitute

def getId():
  return str(ULID())

def save(product):
  PK = 'products'
  SK = product.id
  model = ProductModel(PK=PK, SK=SK, name=product.name, price=product.price, category= product.category)
  model.save() 
  return

def modelToProduct(model):
  return reconstitute(id=model.id, name=model.name, price=model.price, category=model.category)
  

