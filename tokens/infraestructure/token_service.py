"""A class method to create a token service for use in the cognito service ."""

import os

import boto3

from shared.exceptions.bad_request import BadRequestException
from shared.infraestructure.data_structures.singleton import Singleton
from tokens.domain.authentication_result_factory import \
    AuthenticationResultFactory
from tokens.infraestructure.unauthorized_exception import UnauthorizedException
from tokens.infraestructure.user_exist_exception import UserExistException


class TokenService(object, metaclass=Singleton):
    """Class method to create a new TokenService class .

    Args:
        metaclass ([type], optional): [description]. Defaults to Singleton.
    """

    def __init__(self):
        """Initialize the cognito - idp client ."""

        self.authenticationResultFactory = AuthenticationResultFactory()

        self.client = boto3.client(
            'cognito-idp',
            region_name=os.environ.get('REGION'),
        )
        self.client_id = os.environ.get('COGNITO')

    def sign_up(self, _id, email, password):
        """Signs up a user with the given email address .

        Args:
            email ([type]): [description]
            password ([type]): [description]

        Raises:
            BadRequestException: [description]
        """
        try:
            self.client.sign_up(
                ClientId=self.client_id,
                Username=email,
                Password=password,
                UserAttributes=[
                    {
                        'Name': 'custom:identifier',
                        'Value': _id,
                    },
                ],
            )
        except (
            self.client.exceptions.InvalidPasswordException,
            self.client.exceptions.InvalidParameterException,
        ):
            raise BadRequestException()
        except self.client.exceptions.UsernameExistsException:
            raise UserExistException()

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

    def auth(self, email, password):
        """Authenticate using the Web API .

        Args:
            email ([type]): [description]
            password ([type]): [description]

        Raises:
            UnauthorizedException: [description]

        Returns:
            [type]: [description]
        """
        try:
            auth = self.client.initiate_auth(
                ClientId=self.client_id,
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': email,
                    'PASSWORD': password,
                },
            )
        except self.client.exceptions.NotAuthorizedException:
            raise UnauthorizedException()

        return self.cognito_result_to_authentication_result(
            auth.get('AuthenticationResult'),
            )

    def cognito_result_to_authentication_result(self, cognito_result):
        """Convert a cognito result to a cognito authentication result .

        Args:
            cognito_result ([type]): [description]

        Returns:
            [type]: [description]
        """
        return self.authenticationResultFactory.reconstitute({
            'AccessToken': cognito_result.get('AccessToken'),
            'ExpiresIn': cognito_result.get('ExpiresIn'),
            'TokenType': cognito_result.get('TokenType'),
            'RefreshToken': cognito_result.get('RefreshToken'),
            'IdToken': cognito_result.get('IdToken'),
        })
