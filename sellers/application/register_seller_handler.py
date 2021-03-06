"""Script register seller use case ."""

from sellers.domain.seller_factory import SellerFactory
from sellers.infraestructure.repositories.seller_repository import \
    SellerRepository
from shared.infraestructure.data_structures.singleton import Singleton
from tokens.infraestructure.token_service import TokenService
from tokens.infraestructure.user_exist_exception import UserExistException


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
        self.tokenService = TokenService()

    def execute(self, name, email, password):
        """Register a seller in the database .

        Args:
            name ([type]): [description]
            email ([type]): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        seller = self.sellerFactory.create(
            _id=self.sellerRepository.get_id(), name=name, email=email,
        )

        try:
            self.tokenService.sign_up(
                _id=seller.id,
                email=seller.email,
                password=password,
            )
        except UserExistException:
            return

        self.tokenService.add_to_group(email=seller.email, group='sellers')

        self.sellerRepository.save(seller)
