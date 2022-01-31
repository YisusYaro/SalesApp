"""Interface Sellers events handler ."""

import json

from sellers.application.list_sellers_handler import ListSellersHandler
from sellers.application.register_seller_handler import RegisterSellerHandler
from shared.interface.items_response import ItemsResponse
from shared.exceptions.bad_request import BadRequestException
from shared.interface.bad_request_response import BadRequestResponse
from shared.interface.void_response import VoidResponse


def register_seller(event, context):
    """Register a new seller .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    try:
        RegisterSellerHandler().execute(
            name=body['name'], email=body['email'], password=body['password'],
            )
    except BadRequestException:
        return BadRequestResponse.respond()

    return VoidResponse.respond()


def list_sellers(event, context):
    """List all sellers .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    return ItemsResponse.respond(ListSellersHandler().execute())
