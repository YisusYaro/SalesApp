"""Generate a authentication result factory ."""

from tokens.domain.authentication_result import AuthenticationResult
from shared.infraestructure.data_structures.singleton import Singleton


class AuthenticationResultFactory(object, metaclass=Singleton):
    """Constructs an authentication result class .

    Args:
        object ([type]): [description]
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def create(self, create_dict):
        """Creates an AuthenticationResult object .

        Args:
            create_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        return AuthenticationResult(create_dict)

    def reconstitute(self, reconstitute_dict):
        """AI is creating summary for reconstitute

        Args:
            reconstitute_dict ([type]): [description]

        Returns:
            [type]: [description]
        """
        return AuthenticationResult(reconstitute_dict)
