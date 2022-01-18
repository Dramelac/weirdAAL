'''
RDS functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def describe_db_instances():
    '''
    RDS describe DB instances
    '''
    print("### Printing RDS DB instances  ###")
    try:
        for region in regions:
            client = awsclient(
                'rds',
                region_name=region
            )

            response = client.describe_db_instances()
            # print(response)
            if response.get('DBInstances') is None:
                print("{} likely does not have RDS permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['DBInstances']) <= 0:
                print("[-] DescribeDBInstances allowed for {} but no results [-]" .format(region))
            else:
                print("### {} RDS DB Instances ###" .format(region))
                for r in response['DBInstances']:
                    for i in r['Instances']:
                        pp.pprint(i)
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
