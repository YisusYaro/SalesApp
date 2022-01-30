"""A class method to create a token service for use in the cognito service ."""

import os

import boto3
from botocore.exceptions import ClientError

from shared.infraestructure.data_structures.singleton import Singleton


class TokenService(object, metaclass=Singleton):
    """Class method to create a new TokenService class .

    Args:
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the cognito - idp client ."""
        self.client = boto3.client(
            'cognito-idp',
            region_name=os.environ.get('REGION'),
        )
        self.client_id = os.environ.get('COGNITO')

    def sign_up(self, email, password):
        """Signup for the user .

        Args:
            email ([type]): [description]
            password ([type]): [description]
        """
        try:
            self.client.sign_up(
                ClientId=self.client_id,
                Username=email,
                Password=password,
                )
        except ClientError:
            return

    def add_to_group(self, email, group):
        """Add a user to a group .

        Args:
            email ([type]): [description]
            group ([type]): [description]
        """
        self.client.admin_add_user_to_group(
            UserPoolId='us-east-1_9HZVao1gk',
            Username=email,
            GroupName=group,
        )
