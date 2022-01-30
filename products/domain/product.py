"""Constructs a product class from a dictionary of _dict_ ."""


class Product(object):
    """A product class .

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
