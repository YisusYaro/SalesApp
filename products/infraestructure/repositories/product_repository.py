"""Create a new product model for the product model ."""

from ulid import ULID

from products.domain.product_factory import ProductFactory
from products.infraestructure.models.product_model import ProductModel
from shared.infraestructure.data_structures.singleton import Singleton
from pynamodb.exceptions import DoesNotExist


class ProductRepository(object, metaclass=Singleton):
    """Creates a product repository class .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the product repository ."""
        self.productFactory = ProductFactory()

    def get_id(self):
        """Get the id .

        Returns:
            [type]: [description]
        """
        return str(ULID())

    def save(self, product):
        """Save a product model .

        Args:
            product ([type]): [description]
        """
        pk = 'products'
        sk = product.id
        model = ProductModel(
            pk=pk,
            sk=sk,
            name=product.name,
            price=product.price,
            category=product.category,
            seller_id=product.seller_id,
            )
        model.save()

    def find_by_id(self, _id):
        """Find a product by its ID .

        Args:
            _id ([type]): [description]

        Returns:
            [type]: [description]
        """
        model = None
        try:
            model = ProductModel.get(hash_key='products', range_key=_id)
        except DoesNotExist:
            return False
        return self.model_to_product(model)

    def model_to_product(self, model):
        """Convert a model to a product .

        Args:
            model ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.productFactory.reconstitute(
            _id=model.sk,
            name=model.name,
            price=model.price,
            category=model.category,
            seller_id=model.seller_id,
            )
