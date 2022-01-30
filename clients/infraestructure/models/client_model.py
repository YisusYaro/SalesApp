"""Script to Create a client pynamo model ."""
import os

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class ClientModel(Model):
    """Create a client pynamo model class .

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
