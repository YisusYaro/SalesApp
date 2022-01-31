"""Handler for ListProducts ."""

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
        """Execute the query and return the results .

        Returns:
            [type]: [description]
        """
        return self.productQuery.find()
