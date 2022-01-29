from sellers.infraestructure.models.seller_model import SellerModel
from sellers.domain.sellers_factory import reconstitute

def find():
  models = SellerModel.query(hash_key='sellers');
  return modelsToSellers(models)

def modelsToSellers(models):
  sellers = []
  for model in models:
    SK = model.SK.split('#')
    sellers.append(reconstitute(id=SK[1], name=model.name, email=SK[0]))
  return sellers
