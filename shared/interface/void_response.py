"""Create a dummy response ."""


class VoidResponse(object):
    """Create a dummy response .

    Args:
        object ([type]): [description]

    Returns:
        [type]: [description]
    """

    @classmethod
    def respond(cls):
        """Create a response .

        Returns:
            [type]: [description]
        """
        return {'statusCode': 200}
