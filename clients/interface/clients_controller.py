"""Interface Clients events handler ."""

import json

from clients.application.get_client_profile_handler import \
    GetClientProfileHandler
from clients.application.register_client_handler import RegisterClientHandler
from shared.exceptions.bad_request import BadRequestException
from shared.interface.bad_request_response import BadRequestResponse
from shared.interface.item_response import ItemResponse
from shared.interface.void_response import VoidResponse


def register_client(event, context):
    """Register a client to be run in a JSON format .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    try:
        RegisterClientHandler().execute(
            name=body['name'], email=body['email'], password=body['password'],
            )
    except BadRequestException:
        return BadRequestResponse.respond()

    return VoidResponse.respond()


def get_client_profile(event, context):
    object_id = event['pathParameters']['id']
    try:
        return ItemResponse.respond(
            GetClientProfileHandler().execute(object_id)
            )
    except BadRequestException:
        return BadRequestResponse.respond
