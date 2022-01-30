"""Script register seller use case ."""

from sellers.domain.seller_factory import SellerFactory
from sellers.infraestructure.repositories.seller_repository import \
    SellerRepository
from shared.infraestructure.data_structures.singleton import Singleton


class RegisterSellerHandler(object, metaclass=Singleton):
    """Class register seller handler .

    Args:
        object ([type]): [description]
        metclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the handler ."""
        self.sellerRepository = SellerRepository()
        self.sellerFactory = SellerFactory()

    def execute(self, name, email, password):
        """Register a seller in the database .

        Args:
            name ([type]): [description]
            email ([type]): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        seller = self.sellerRepository.find_by_email(email)

        if (seller):
            return {'statusCode': 200}

        seller = self.sellerFactory.create(
            _id=self.sellerRepository.get_id(), name=name, email=email,
            )

        self.sellerRepository.save(seller)

        return {'statusCode': 200}
