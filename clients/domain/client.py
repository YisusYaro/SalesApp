"""Script Client ."""


class Client(object):
    """Generates a client class for the given object .

    Args:
        object ([type]): [description]
    """

    def __init__(self, _dict):
        """Initialize the class with the given _dict .

        Args:
            _dict ([type]): [description]
        """
        self.__dict__.update(_dict)
