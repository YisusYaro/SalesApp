"""Constructs a authentication class ."""


class AuthenticationResult(object):
    """Classmethod to create a AuthenticationResult .

    Args:
        object ([type]): [description]
    """

    def __init__(self, _dict):
        """Initialize the class with the given _dict .

        Args:
            _dict ([type]): [description]
        """
        self.__dict__.update(_dict)

    def updateProperties(self, _dict):
        """Update this object s properties from the dictionary .

        Args:
            _dict ([type]): [description]
        """
        self.__dict__.update(_dict)
