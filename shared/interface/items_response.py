"""Returns a response object for the items_list ."""

import json


class ItemsResponse(object):
    """Generate a new ItemResponse class .

    Args:
        object ([type]): [description]
    """

    @classmethod
    def respond(cls, items_list):
        """Build a JSON response .

        Args:
            items_list ([type]): [description]

        Returns:
            [type]: [description]
        """
        return {
            'statusCode': 200,
            'body': json.dumps({'items': json.loads(
                json.dumps(
                    items_list,
                    default=lambda list_item: list_item.__dict__,
                    ),
                )},
                ),
        }
