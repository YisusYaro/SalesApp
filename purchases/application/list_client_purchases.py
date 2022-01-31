"""Creates a custom purchase handler ."""

from purchases.infraestructure.queries.purchase_query import PurchaseQuery
from shared.infraestructure.data_structures.singleton import Singleton


class ListClientPurchases(object, metaclass=Singleton):
    """Returns a list of client purchases .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the use case ."""
        self.purchaseQuery = PurchaseQuery()

    def execute(self, client_id):
        """Execute the query and return all the purchases .

        Args:
            client_id ([type]): [description]

        Raises:
            BadRequestException: [description]

        Returns:
            [type]: [description]
        """
        return self.purchaseQuery.find(client_id)
