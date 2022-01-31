"""Log in to the user ."""

import json

from shared.interface.bad_request_response import BadRequestResponse
from shared.interface.item_response import ItemResponse
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
        return ItemResponse.respond(
            LoginHandler().execute(
                email=body['email'],
                password=body['password'],
                ))
    except UnauthorizedException:
        return BadRequestResponse.respond()
