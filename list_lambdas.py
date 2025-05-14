import boto3

def lambda_handler(event, context):
    lambda_client = boto3.client('lambda', region_name='eu-north-1')

    paginator = lambda_client.get_paginator('list_functions')
    result = []

    for page in paginator.paginate():
        for function in page['Functions']:
            result.append({
                'FunctionName': function['FunctionName'],
                'Runtime': function['Runtime'],
                'Handler': function['Handler'],
                'LastModified': function['LastModified']
            })

    # This is what Lambda will return
    return result
