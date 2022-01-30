"""Log in to the user ."""

import json

from tokens.aplication.login_handler import LoginHandler
from tokens.infraestructure.unauthorized_exception import UnauthorizedException


def login(event, context):
    """Log in to the user .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])

    try:
        return LoginHandler().execute(
            email=body['email'],
            password=body['password'],
            )
    except UnauthorizedException:
        return {'statusCode': 400}
