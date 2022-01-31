"""This method is used to create purchases objects ."""

from purchases.domain.purchase_factory import PurchaseFactory
from purchases.infraestructure.models.purchase_model import PurchaseModel
from shared.infraestructure.data_structures.singleton import Singleton


class PurchaseQuery(object, metaclass=Singleton):
    """Class method for creating a purchase query .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the purchaseFactory ."""
        self.purchaseFactory = PurchaseFactory()

    def find(self, client_id):
        """Find all purchases in the database .

        Returns:
            [type]: [description]
        """
        models = PurchaseModel.query(hash_key=client_id)
        return self.models_to_purchases(models)

    def models_to_purchases(self, models):
        """Convert a list of models into a list of Purchase objects .

        Args:
            models ([type]): [description]

        Returns:
            [type]: [description]
        """
        purchases = []
        for model in models:
            purchases.append(
                self.purchaseFactory.reconstitute(
                    {
                        'id': model.sk,
                        'client_id': model.pk,
                        'client_name': model.client_name,
                        'seller_name': model.seller_name,
                        'product_name': model.product_name,
                        'price': model.price,
                        'date': str(model.date),
                    }),
            )
        return purchases
