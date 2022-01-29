import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class ProductModel(Model):
    class Meta:
        table_name = os.environ.get('TABLE')
        region = os.environ.get('REGION')
    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    price = NumberAttribute()
    category = UnicodeAttribute()