"""Handler for list of seller objects ."""

import json

from sellers.infraestructure.queries.seller_query import SellerQuery
from shared.infraestructure.data_structures.singleton import Singleton


class ListSellersHandler(object, metaclass=Singleton):
    """Class Handler for list sellers .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        self.sellerQuery = SellerQuery()

    def execute(self):
        """List all seller objects .

        Returns:
            [type]: [description]
        """
        sellers = self.sellerQuery.find()

        return {
            'statusCode': 200,
            'body': json.dumps(
                sellers, default=lambda seller: seller.__dict__,
            ),
        }
