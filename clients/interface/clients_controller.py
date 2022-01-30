"""Interface Clients events handler ."""

import json

from clients.application.register_client_handler import RegisterClientHandler


def register_client(event, context):
    """Register a client to be run in a JSON format .

    Args:
        event ([type]): [description]
        context ([type]): [description]

    Returns:
        [type]: [description]
    """
    body = json.loads(event['body'])
    return RegisterClientHandler().execute(
        name=body['name'], email=body['email'], password=body['password'],
        )
