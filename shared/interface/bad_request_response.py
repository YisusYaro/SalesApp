"""Return a 400 error response ."""


class BadRequestResponse(object):
    """Return a 400 error response that can be used to render a 400 error code .

    Args:
        object ([type]): [description]

    Returns:
        [type]: [description]
    """

    @classmethod
    def respond(cls):
        """Return a JSON response that can be used to render a 400 error code .

        Returns:
            [type]: [description]
        """
        return {'statusCode': 400}
