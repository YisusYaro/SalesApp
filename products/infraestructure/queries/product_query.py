from products.infraestructure.models.product_model import ProductModel
from products.domain.product_factory import reconstitute

def find():
  models = ProductModel.query(hash_key='products');
  return modelsToProducts(models)

def modelsToProducts(models):
  products = []
  for model in models:
    products.append(reconstitute(id=model.SK, name=model.name, price=model.price, category=model.category))
  return products
