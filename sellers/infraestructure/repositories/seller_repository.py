"""Script seller repository ."""

from pynamodb.exceptions import DoesNotExist
from ulid import ULID

from sellers.domain.seller_factory import SellerFactory
from sellers.infraestructure.models.seller_model import SellerModel
from shared.infraestructure.data_structures.singleton import Singleton


class SellerRepository(object, metaclass=Singleton):
    """Class method for creating a seller repository .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the repository ."""
        self.sellerFactory = SellerFactory()

    def get_id(self):
        """Get the uid of the object .

        Returns:
            [type]: [description]
        """
        return str(ULID())

    def save(self, seller):
        """Save a seller .

        Args:
            seller ([type]): [description]
        """
        model = SellerModel(
            pk='sellers',
            sk=seller.id,
            name=seller.name,
            email=seller.email,
            )
        model.save()

    def find_by_id(self, _id):
        """Find a client by id .

        Args:
            _id ([type]): [description]

        Returns:
            [type]: [description]
        """
        model = None
        try:
            model = SellerModel.get(hash_key='sellers', range_key=_id)
        except DoesNotExist:
            return False
        return self.model_to_seller(model)

    def find_by_email(self, email):
        """Find a seller by email address .

        Args:
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        for model in SellerModel.query(
            hash_key='sellers',
            range_key_condition=SellerModel.sk.startswith(email),
            limit=1,
        ):
            return self.modelToSeller(model)

        return False

    def model_to_seller(self, model):
        """Convert a model to a seller model .

        Args:
            model ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.sellerFactory.reconstitute(
            _id=model.sk, name=model.name, email=model.email,
            )
