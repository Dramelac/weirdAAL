'''
SESv2 functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

# https://docs.amazonaws.cn/en_us/general/latest/gr/ses.html
regions = ['us-east-1', 'us-west-2', 'ap-south-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1', 'us-gov-west-1']

from libs.aws.aws_session import *


def list_email_identities():
    '''
    SES List Email Identities
    '''
    print("### Printing SES Identities  ###")
    try:
        for region in regions:
            client = awsclient(
                'sesv2',
                region_name=region
            )

            response = client.list_email_identities()
            # print(response)
            if response.get('EmailIdentities') is None:
                print("{} likely does not have SESv2 permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['EmailIdentities']) <= 0:
                print("[-] ListEmailIdentities allowed for {} but no results [-]" .format(region))
            else:
                print("### {} SES Email Identities ###" .format(region))
                for r in response['EmailIdentities']:
                    pp.pprint(r)
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