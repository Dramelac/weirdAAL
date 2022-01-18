'''
ECR functions for WeirdAAL
'''

import boto3
import botocore
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def ecr_describe_repositories():
    '''
    Use ecr describe_repositories function to list available repositories
    '''
    print("### Printing ECR Repositories ###")
    try:
        for region in regions:
            client = awsclient('ecr', region_name=region)
            response = client.describe_repositories()

            if response.get('repositories') is None:
                print("{} likely does not have ECR permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['repositories']) <= 0:
                print("[-] DescribeRepositories allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ECR Repositories ###" .format(region))
                for tables in response['repositories']:
                    pp.pprint(tables)
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
