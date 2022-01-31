"""Generate a purchase factory ."""

from purchases.domain.purchase import Purchase
from shared.infraestructure.data_structures.singleton import Singleton


class PurchaseFactory(object, metaclass=Singleton):
    """Creates a new purchase factory .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def create(self, create_dict):
        """Create a purchase object .

        Args:
            create_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Purchase(create_dict)

    def reconstitute(self, reconstitute_dict):
        """Return a new Purchase object with the given dictionary .

        Args:
            reconstitute_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Purchase(reconstitute_dict)
