import json

def seller_authorizers(event, context):
    token = event['authorizationToken']
    method_arn = event['methodArn']

    if(token=='allow'):
        return generate_auth_response('user', 'Allow', method_arn)
    else:
        return generate_auth_response('user', 'Deny', method_arn)


def generate_auth_response(principal_id, effect, method_arn):
    policy_document = generate_policy_document(
        effect=effect, method_arn=method_arn)

    return {
        principal_id,
        policy_document,
    }


def generate_policy_document(effect, method_arn):

    return {
        'Version': '2020-10-17',
        'Statement': [{
            'Action': 'execute-api:Invoke',
            'Effect': effect,
            'Resource': method_arn,
        }],
    }
