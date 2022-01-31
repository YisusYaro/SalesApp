"""Initialize seller with the given credentials .

Returns:
    [type]: [description]
"""

from sellers.infraestructure.repositories.seller_repository import \
    SellerRepository
from shared.exceptions.bad_request import BadRequestException
from shared.infraestructure.data_structures.singleton import Singleton


class GetSellerProfileHandler(object, metaclass=Singleton):
    """Generate a handler for the seller profile .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the object for the service ."""
        self.sellerRepository = SellerRepository()

    def execute(self, _id):
        """Finds the seller profile by id .

        Args:
            _id ([type]): [description]

        Raises:
            BadRequestException: [description]

        Returns:
            [type]: [description]
        """
        profile = self.sellerRepository.find_by_id(_id)

        if (not profile):
            raise BadRequestException()

        return profile
