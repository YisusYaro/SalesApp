"""Create a Singleton class ."""


class Singleton(type):
    """Create a Singleton class .

    Args:
        type ([type]): [description]

    Returns:
        [type]: [description]
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call the method if it is not already instantiated .

        Returns:
            [type]: [description]
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls,
                ).__call__(*args, **kwargs)
        return cls._instances[cls]
