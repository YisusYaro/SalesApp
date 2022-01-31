"""Create a model that will be used to store the DynamoDB model ."""

import os

from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.models import Model


class ProductModel(Model):
    """Create a summary for MetaArgs .

    Args:
        Model ([type]): [description]
    """

    class Meta(object):
        """Meta - function to parse the table .

        Args:
            object ([type]): [description]
        """

        table_name = os.environ.get('TABLE')
        region = os.environ.get('REGION')
    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    price = NumberAttribute()
    category = UnicodeAttribute()
    seller_id = UnicodeAttribute()
