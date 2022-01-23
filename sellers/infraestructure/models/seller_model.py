from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute


class SellerModel(Model):
    class Meta:
        table_name = 'App'
        region = 'us-east-1'
    PK = UnicodeAttribute(hash_key=True)
    SK = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    password = UnicodeAttribute()
