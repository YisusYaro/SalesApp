"""Script RegisterClientHandler Class ."""

from clients.domain.client_factory import ClientFactory
from clients.infraestructure.repositories.client_repository import \
    ClientRepository
from shared.infraestructure.data_structures.singleton import Singleton
from tokens.infraestructure.token_service import TokenService
from tokens.infraestructure.user_exist_exception import UserExistException


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
        """Execute a new client .

        Args:
            name ([type]): [description]
            email ([type]): [description]
            password ([type]): [description]
        """
        client = self.clientFactory.create(
            _id=self.clientRepository.get_id(), name=name, email=email,
        )

        try:
            self.tokenService.sign_up(
                _id=client.id,
                email=client.email,
                password=password,
            )
        except UserExistException:
            return

        self.tokenService.add_to_group(email=client.email, group='clients')

        self.clientRepository.save(client)
