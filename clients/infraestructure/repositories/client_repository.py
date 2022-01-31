"""Create a client repository for a given model ."""

from pynamodb.exceptions import DoesNotExist
from ulid import ULID

from clients.domain.client_factory import ClientFactory
from clients.infraestructure.models.client_model import ClientModel
from shared.infraestructure.data_structures.singleton import Singleton


class ClientRepository(object, metaclass=Singleton):
    """Construct a client repository for the given model .

    Args:
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the client ."""
        self.clientFactory = ClientFactory()

    def get_id(self):
        """Generate the UUID .

        Returns:
            [ULID]: [Universally Unique Lexicographically Sortable Identifier]
        """
        return str(ULID())

    def save(self, client):
        """Save a client to the database .

        Args:
            client ([type]): [description]
        """
        model = ClientModel(
            pk='clients',
            sk=client.id,
            name=client.name,
            email=client.email,
        )
        model.save()

    def find_by_id(self, _id):
        """Find a client by id .

        Args:
            _id ([type]): [description]

        Returns:
            [type]: [description]
        """
        model = None
        try:
            model = ClientModel.get(hash_key='clients', range_key=_id)
        except DoesNotExist:
            return False
        return self.model_to_client(model)

    def find_by_email(self, email):
        """Find client by email address .

        Args:
            email ([type]): [description]

        Returns:
            [type]: [description]
        """
        for model in ClientModel.query(
            hash_key='clients',
            range_key_condition=ClientModel.sk.startswith(email),
            limit=1,
        ):
            return self.model_to_client(model)

        return False

    def model_to_client(self, model):
        """Convert a PySB model into a client object .

        Args:
            model ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.clientFactory.reconstitute(
            _id=model.sk, name=model.name, email=model.email,
        )
