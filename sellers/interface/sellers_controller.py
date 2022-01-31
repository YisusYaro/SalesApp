"""Interface Sellers events handler ."""

import json

from sellers.application.list_sellers_handler import ListSellersHandler
from sellers.application.register_seller_handler import RegisterSellerHandler
from shared.interface.items_response import ItemsResponse


def register_seller(event, context):
    """Register a new seller .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    return RegisterSellerHandler().execute(
        name=body['name'],
        email=body['email'],
        password=body['password'],
    )


def list_sellers(event, context):
    """List all sellers .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    return ItemsResponse.respond(ListSellersHandler().execute())
