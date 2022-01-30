"""This method is used to create products objects from the products model ."""

from products.domain.product_factory import ProductFactory
from products.infraestructure.models.product_model import ProductModel
from shared.infraestructure.data_structures.singleton import Singleton


class ProductQuery(object, metaclass=Singleton):
    """Class method for creating a product query .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the productFactory ."""
        self.productFactory = ProductFactory()

    def find(self):
        """Find all products in the database .

        Returns:
            [type]: [description]
        """
        models = ProductModel.query(hash_key='products')
        return self.models_to_products(models)

    def models_to_products(self, models):
        """Convert a list of models into a list of Product objects .

        Args:
            models ([type]): [description]

        Returns:
            [type]: [description]
        """
        products = []
        for model in models:
            products.append(
                self.productFactory.reconstitute(
                    _id=model.sk,
                    name=model.name,
                    price=model.price,
                    category=model.category,
                    ),
            )
        return products
