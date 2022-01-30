"""Creates a custom product handler ."""

from products.domain.product_factory import ProductFactory
from products.infraestructure.repositories.product_repository import \
    ProductRepository
from shared.infraestructure.data_structures.singleton import Singleton


class CreateProductHandler(object, metaclass=Singleton):
    """Class method for creating a custom product handler .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the use case ."""
        self.productRepository = ProductRepository()
        self.productFactory = ProductFactory()

    def execute(self, name, price, category):
        """Create a new Product .

        Args:
            name ([type]): [description]
            price ([type]): [description]
            category ([type]): [description]

        Returns:
            [type]: [description]
        """
        product = self.productFactory.create(
            _id=self.productRepository.get_id(),
            name=name,
            price=price,
            category=category,
            )

        self.productRepository.save(product)

        return {
            'statusCode': 200,
        }
