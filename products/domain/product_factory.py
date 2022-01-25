from products.domain.product import Product

def create(id, name, price, category):
  return Product({'id':id, 'name':name, 'price':price, 'category':category})

def reconstitute(id, name, price, category):
  return Product({'id':id, 'name':name, 'price':price, 'category':category})
