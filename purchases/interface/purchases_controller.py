"""Handler for creating new products ."""

import json

from purchases.application.generate_purchase_handler import \
    GeneratePurchaseHandler
from purchases.application.list_client_purchases import \
    ListClientPurchases
from shared.interface.items_response import ItemsResponse
from shared.interface.void_response import VoidResponse


def generate_purchase(event, context):
    """Generate a new purchase .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    GeneratePurchaseHandler().execute(
        client_id=body['client_id'],
        product_id=body['product_id'],
    )
    return VoidResponse.respond()


def get_client_purchases_list(event, context):
    client_id = event['pathParameters']['id']
    return ItemsResponse.respond(ListClientPurchases().execute(client_id))
