"""Authentication handler for the login process ."""

import json

from shared.infraestructure.data_structures.singleton import Singleton
from tokens.infraestructure.token_service import TokenService


class LoginHandler(object, metaclass=Singleton):
    """Class method for handling a login handler .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the service ."""
        self.tokenService = TokenService()

    def execute(self, email, password):
        """Execute the auth token .

        Args:
            email ([type]): [description]
            password ([type]): [description]

        Returns:
            [type]: [description]
        """
        auth = self.tokenService.auth(email=email, password=password)

        return {
            'statusCode': 200,
            'body': json.dumps(auth),
        }
