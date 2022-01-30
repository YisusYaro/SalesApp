"""Handler for ListProducts ."""

import json

from products.infraestructure.queries.product_query import ProductQuery
from shared.infraestructure.data_structures.singleton import Singleton


class ListProductsHandler(object, metaclass=Singleton):
    """Handler for ListProducts .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the object ."""
        self.productQuery = ProductQuery()

    def execute(self):
        """Execute the query and return the results as JSON .

        Returns:
            [type]: [description]
        """
        products = self.productQuery.find()

        return {
            'statusCode': 200,
            'body': json.dumps(
                products, default=lambda seller: seller.__dict__,
                ),
        }
