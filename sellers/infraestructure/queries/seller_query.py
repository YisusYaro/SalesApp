"""Script class seller queries ."""

from sellers.domain.seller_factory import SellerFactory
from sellers.infraestructure.models.seller_model import SellerModel
from shared.infraestructure.data_structures.singleton import Singleton


class SellerQuery(object, metaclass=Singleton):
    """Class seller query .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the factory ."""
        self.sellerFactory = SellerFactory()

    def find(self):
        """Find all the sellers .

        Returns:
            [type]: [description]
        """
        models = SellerModel.query(hash_key='sellers')
        return self.models_to_sellers(models)

    def models_to_sellers(self, models):
        """Convert a list of strings to a list of seller objects .

        Args:
            models ([type]): [description]

        Returns:
            [type]: [description]
        """
        sellers = []
        for model in models:
            sk = model.sk.split('#')
            sellers.append(
                self.sellerFactory.reconstitute(
                    _id=sk[1], name=model.name, email=sk[0],
                    ),
                )
        return sellers
