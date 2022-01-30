"""Script seller factory ."""

from sellers.domain.seller import Seller
from shared.infraestructure.data_structures.singleton import Singleton


class SellerFactory(object, metaclass=Singleton):
    """Class Seller Factory .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def create(self, _id, name, email):
        """Create a new seller .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Seller({'id': _id, 'name': name, 'email': email})

    def reconstitute(self, _id, name, email):
        """Reconstruct a seller .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Seller({'id': _id, 'name': name, 'email': email})
