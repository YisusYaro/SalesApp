"""Script RegisterClientHandler Class ."""

from clients.domain.client_factory import ClientFactory
from clients.infraestructure.repositories.client_repository import \
    ClientRepository
from shared.infraestructure.data_structures.singleton import Singleton
from tokens.infraestructure.token_service import TokenService


class RegisterClientHandler(object, metaclass=Singleton):
    """Class for RegisterClientHandler use case .

    Args:
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the object for the service ."""
        self.clientFactory = ClientFactory()
        self.tokenService = TokenService()
        self.clientRepository = ClientRepository()

    def execute(self, name, email, password):
        """Register a new client .

        Args:
            name ([type]): [description]
            email ([type]): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        client = self.clientRepository.find_by_email(email)

        if (client):
            return

        client = self.clientFactory.create(
            _id=self.clientRepository.get_id(), name=name, email=email,
        )

        self.tokenService.sign_up(email=client.email, password=password)
        self.tokenService.add_to_group(email=client.email, group='clients')

        self.clientRepository.save(client)
