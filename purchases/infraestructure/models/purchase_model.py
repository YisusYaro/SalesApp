"""Create a model that will be used to store the DynamoDB model ."""

import os

from pynamodb.attributes import (NumberAttribute, UnicodeAttribute,
                                 UTCDateTimeAttribute)
from pynamodb.models import Model


class PurchaseModel(Model):
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
    client_name = UnicodeAttribute()
    seller_name = UnicodeAttribute()
    product_name = UnicodeAttribute()
    price = NumberAttribute()
    date = UTCDateTimeAttribute()
