'''
Pricing functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from aws_session import *


def pricing_describe_services():
    '''
    Using pricing service describe services
    '''
    try:
        for region in regions:
            client = boto3.client('pricing', region_name=region)
            response = client.describe_services()
            print(response)
            if response.get('Services') is None:
                print("{} likely does not have Pricing permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Services']) <= 0:
                print("[-] Describe Pricing Services allowed for {} but no results [-]" .format(region))
            else:
                print("### {} Services  ###" .format(region))
                for tables in response['ServiceCode']:
                    pp.pprint(tables)
                    print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'UnauthorizedOperation':
            print('{} : (UnauthorizedOperation) when calling the Pricing DescribeServices' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print(e)
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
