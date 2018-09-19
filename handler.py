"""
Example of AWS Lambda with Auth0 in Python.
"""

import os
import json
from auth0.v3.management import Auth0
from auth0.v3.exceptions import Auth0Error


def get_user_profile(event, _context):
    """
    Gets the user profile from Auth0 by a given user_id.
    """

    auth0 = Auth0(os.getenv('AUTH0_DOMAIN'), os.getenv('AUTH0_TOKEN'))
    user_id = event['pathParameters']['user_id']

    try:
        user_profile = auth0.users.get(user_id)
        response = {
            'statusCode': 200,
            'body': json.dumps(user_profile)
        }
    except Auth0Error as err:
        response = {
            'statusCode': err.status_code,
            'body': err.message
        }

    return response
