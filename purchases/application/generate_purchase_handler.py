"""Creates a custom purchase handler ."""

from clients.infraestructure.repositories.client_repository import \
    ClientRepository
from products.infraestructure.repositories.product_repository import \
    ProductRepository
from purchases.domain.purchase_factory import PurchaseFactory
from purchases.infraestructure.repositories.purchase_repository import \
    PurchaseRepository
from sellers.infraestructure.repositories.seller_repository import \
    SellerRepository
from shared.infraestructure.data_structures.singleton import Singleton


class GeneratePurchaseHandler(object, metaclass=Singleton):
    """Class method for creating a new purchase handler .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the use case ."""
        self.purchaseRepository = PurchaseRepository()
        self.clientRepository = ClientRepository()
        self.productRepository = ProductRepository()
        self.sellerRepository = SellerRepository()
        self.purchaseFactory = PurchaseFactory()

    def execute(self, client_id, product_id):
        """Create a new Product instance .

        Args:
            client_id ([type]): [description]
            product_id ([type]): [description]
        """

        client = self.clientRepository.find_by_id(client_id)
        product = self.productRepository.find_by_id(product_id)
        seller = self.sellerRepository.find_by_id(product.seller_id)

        purchase = self.purchaseFactory.create(
            {
                'id': self.purchaseRepository.get_id(),
                'client_id': client.id,
                'client_name': client.name,
                'seller_name': seller.name,
                'product_name': product.name,
                'price': product.price,
            })

        self.purchaseRepository.save(purchase)
