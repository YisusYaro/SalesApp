"""Creates a custom product handler ."""

from products.domain.product_factory import ProductFactory
from products.infraestructure.repositories.product_repository import \
    ProductRepository
from shared.infraestructure.data_structures.singleton import Singleton


class UpdateProductHandler(object, metaclass=Singleton):
    """Handler for update_product .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the use case ."""
        self.productRepository = ProductRepository()
        self.productFactory = ProductFactory()

    def execute(self, _id, name, price, category):
        """Update product details .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            price ([type]): [description]
            category ([type]): [description]

        Returns:
            [type]: [description]
        """
        product = self.productRepository.find_by_id(_id)

        if (not product):
            return {'statusCode': 400}

        product.updateProperties({
            'name': name,
            'price': price,
            'category': category,
        })

        self.productRepository.save(product)

        return {'statusCode': 200}
