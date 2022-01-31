"""Create a new purchase model for the purchase model ."""

from ulid import ULID

from purchases.domain.purchase_factory import PurchaseFactory
from purchases.infraestructure.models.purchase_model import PurchaseModel
from shared.infraestructure.data_structures.singleton import Singleton


class PurchaseRepository(object, metaclass=Singleton):
    """Creates a purchase repository class .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the purchase repository ."""
        self.purchaseFactory = PurchaseFactory()

    def get_id(self):
        """Get the id .

        Returns:
            [type]: [description]
        """
        return str(ULID())

    def save(self, purchase):
        """Save a purchase model .

        Args:
            purchase ([type]): [description]
        """
        print(purchase.__dict__)
        model = PurchaseModel(
            pk=purchase.client_id,
            sk=purchase.id,
            client_name=purchase.client_name,
            seller_name=purchase.seller_name,
            product_name=purchase.product_name,
            price=purchase.price,
            date=purchase.date,
        )
        model.save()

    def model_to_purchase(self, model):
        """Convert a model to a purchase .

        Args:
            model ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.purchaseFactory.reconstitute(
            {
                '_id': model.sk,
                'client_id': model.client_id,
                'client_name': model.client_name,
                'seller_name': model.product.name,
                'product_name': model.product_name,
                'price': model.price,
            },
        )
