'''
dynamoDBstreams functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import os
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def list_dynamodbstreams():
    '''
    Use list_streams function in dynamodbstreams to list available streams
    '''
    print("### Printing DynamoDBstreams ###")
    try:
        for region in regions:
            client = boto3.client('dynamodbstreams', region_name=region)
            response = client.list_streams()
            if response.get('Streams') is None:
                print("{} likely does not have DynamoDB permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Streams']) <= 0:
                print("[-] ListStreams allowed for {} but no results [-]" .format(region))
            else:
                print("### {} DynamoDB Streams ###" .format(region))
                for streams in response['Streams']:
                    pp.pprint(streams)
                    print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
