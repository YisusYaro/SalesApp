"""Handler for creating new products ."""

import json

from products.application.create_product_handler import CreateProductHandler
from products.application.list_products_handler import ListProductsHandler
from products.application.update_product_handler import UpdateProductHandler
from shared.exceptions.bad_request import BadRequestException
from shared.interface.bad_request_response import BadRequestResponse
from shared.interface.items_response import ItemsResponse
from shared.interface.void_response import VoidResponse


def create_product(event, context):
    """Create a new product .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    CreateProductHandler().execute(
        name=body['name'], price=body['price'], category=body['category'],
    )
    return VoidResponse.respond()


def list_products(event, context):
    """Show list of products .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    return ItemsResponse.respond(
        ListProductsHandler().execute(),
    )


def update_product(event, context):
    """Update a new Product .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    object_id = event['pathParameters']['id']
    body = json.loads(event['body'])
    try:
        UpdateProductHandler().execute(
            _id=object_id,
            name=body['name'],
            price=body['price'],
            category=body['category'],
            )
    except BadRequestException:
        return BadRequestResponse.respond()

    return VoidResponse.respond()
