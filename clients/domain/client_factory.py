"""Script ClientFactory ."""
from clients.domain.client import Client
from shared.infraestructure.data_structures.singleton import Singleton


class ClientFactory(object, metaclass=Singleton):
    """Factory for create or reconstitute a client .

    Args:
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def create(self, _id, name, email):
        """Create a client .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Client({'id': _id, 'name': name, 'email': email})

    def reconstitute(self, _id, name, email):
        """Reconstitute a client with the given name and email address .

        Args:
            _id ([type]): [description]
            name ([type]): [description]
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        return Client({'id': _id, 'name': name, 'email': email})
