'''
Datapipleine functions for WeirdAAL
'''

import boto3
import botocore
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def datapipeline_list_pipelines():
    '''
    Function to use the datapipeline boto3 library to list available pipelines
    '''
    print("### Printing Data Pipeline Pipelines ###")
    try:
        for region in regions:
            client = boto3.client('datapipeline', region_name=region)
            response = client.list_pipelines()
            print("### {} Data Pipelines ###" .format(region))
            if response.get('pipelineIdList') is None:
                print("{} likely does not have Data Pipeline permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['pipelineIdList']) <= 0:
                print("[-] ListPipelines allowed for {} but no results [-]" .format(region))
            else:
                print("### {} Data Pipelines ###" .format(region))
                for pipes in response['pipelineIdList']:
                    pp.pprint(pipes)
                    print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Is NOT a root key' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
