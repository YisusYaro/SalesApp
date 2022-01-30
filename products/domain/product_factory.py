"""Generate a product factory ."""

from products.domain.product import Product
from shared.infraestructure.data_structures.singleton import Singleton


class ProductFactory(object, metaclass=Singleton):
    """Generate a product factory .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def create(self, _id, name, price, category):
        """Create a Product .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            price ([type]): [description]
            category ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Product(
            {'id': _id, 'name': name, 'price': price, 'category': category},
            )

    def reconstitute(self, _id, name, price, category):
        """Reconstruct a Product .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            price ([type]): [description]
            category ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Product(
            {'id': _id, 'name': name, 'price': price, 'category': category},
            )
