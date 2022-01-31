"""Handler for list of seller objects ."""

from sellers.infraestructure.queries.seller_query import SellerQuery
from shared.infraestructure.data_structures.singleton import Singleton


class ListSellersHandler(object, metaclass=Singleton):
    """Class Handler for list sellers .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the query object ."""
        self.sellerQuery = SellerQuery()

    def execute(self):
        """Execute all seller queries .

        Returns:
            [type]: [description]
        """
        return self.sellerQuery.find()
