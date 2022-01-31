"""Initialize client with the given credentials .

Returns:
    [type]: [description]
"""

from clients.infraestructure.repositories.client_repository import \
    ClientRepository
from shared.infraestructure.data_structures.singleton import Singleton
from shared.exceptions.bad_request import BadRequestException


class GetClientProfileHandler(object, metaclass=Singleton):
    """Generate a handler for the client profile .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the object for the service ."""
        self.clientRepository = ClientRepository()

    def execute(self, _id):
        """Execute the ExecuteClient with the _id .

        Args:
            _id ([type]): [description]

        Returns:
            [type]: [description]
        """
        profile = self.clientRepository.find_by_id(_id)

        if (not profile):
            raise BadRequestException()

        return profile
