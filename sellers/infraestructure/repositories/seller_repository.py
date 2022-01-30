"""Script seller repository ."""

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
        pk = 'sellers'
        sk = '{email}#{id}'.format(email=seller.email, id=seller.id)
        model = SellerModel(
            pk=pk,
            sk=sk,
            name=seller.name,
            )
        model.save()

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
        sk = model.sk.split('#')
        return self.sellerFactory.reconstitute(
            _id=sk[0], name=model.name, email=sk[1],
            )
