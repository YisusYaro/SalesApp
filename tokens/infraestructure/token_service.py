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
        """Initialize the cognito - idp client .
        """
        self.client = boto3.client(
            'cognito-idp',
            region_name=os.environ.get('REGION')
        )
        self.clientId = os.environ.get('COGNITO')

    def signUp(self, email, password):
        """Signup for the user .

        Args:
            email ([type]): [description]
            password ([type]): [description]
        """
        try:
            self.client.sign_up(
                ClientId=self.clientId,
                Username=email,
                Password=password,
                )
        except ClientError:
            return
