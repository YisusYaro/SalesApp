"""Create a JSON object representing the item ."""
import json


class ItemResponse(object):
    """A class method for creating a Item class .

    Args:
        object ([type]): [description]
    """

    @classmethod
    def respond(cls, response_item):
        """Respond to the API .

        Args:
            response_item ([type]): [description]

        Returns:
            [type]: [description]
        """
        return {
            'statusCode': 200,
            'body': json.dumps({
                'item': response_item,
            }),
        }
