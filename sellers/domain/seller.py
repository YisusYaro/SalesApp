"""Script for creating a seller class ."""


class Seller(object):
    """Class method for creating a seller class .

    Args:
        object ([type]): [description]
    """

    def __init__(self, _dict):
        """Initialize the class with the given _dict .

        Args:
            _dict ([type]): [description]
        """
        self.__dict__.update(_dict)
