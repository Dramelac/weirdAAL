'''
EMR functions for WeirdAAL
'''

import boto3
import botocore
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def list_clusters():
    '''
    List EMR Clusters
    '''
    print("### Printing EMR Clusters ###")
    try:
        for region in regions:
            client = awsclient('emr', region_name=region)
            response = client.list_clusters()

            if response.get('Clusters') is None:
                print("{} likely does not have EMR permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Clusters']) <= 0:
                print("[-] ListClusters allowed for {} but no results [-]" .format(region))
            else:
                print("### {} EMR Clusters ###" .format(region))
                for app in response['Clusters']:
                    pp.pprint(app)
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


def list_security_configurations():
    '''
    List EMR Security Configurations
    '''
    print("### Printing EMR Security Configuration ###")
    try:
        for region in regions:
            client = awsclient('emr', region_name=region)
            response = client.list_security_configurations()
            # print(response)

            if response.get('SecurityConfigurations') is None:
                print("{} likely does not have EMR permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['SecurityConfigurations']) <= 0:
                print("[-] ListSecurityConfigurations allowed for {} but no results [-]" .format(region))
            else:
                print("### {} EMR Security Configuration ###" .format(region))
                for app in response['SecurityConfigurations']:
                    pp.pprint(app)
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
