'''
Config functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys

from aws_session import *

pp = pprint.PrettyPrinter(indent=5, width=80)


def describe_configuration_recorders(region):
    '''
    Describe Config recorders
    '''
    try:
        client = boto3.client("config", region_name=region)

        response = client.describe_configuration_recorders()
        region_name = "Region: %s\n" % region
        print(region_name)
        print("=" * len(region_name))
        if not response['ConfigurationRecorders']:
            print("No Recordings Found\n")
        else:
            for r in response['ConfigurationRecorders']:
                for k, v in r.items():
                    print("%s: %s" % (k, v))
                print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'UnrecognizedClientException':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def describe_configuration_rules(region):
    '''
    Describe Config rules
    '''
    try:
        client = boto3.client("config", region_name=region)

        response = client.describe_config_rules()
        region_name = "Region: %s" % region
        print(region_name)
        print("=" * len(region_name))
        if not response['ConfigRules']:
            print("No Rules Found\n")
        else:
            for r in response['ConfigRules']:
                for k, v in r.items():
                    print("%s: %s" % (k, v))
                print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'UnrecognizedClientException':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def delete_rule(rule_name, region):
    '''
    Attempt to delete the specified Config Rule
    '''
    try:
        client = boto3.client("config", region_name=region)
        client.delete_config_rule(ConfigRuleName=rule_name)
        print("Successfully deleted %s from %s!" % (rule_name, region))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'UnrecognizedClientException':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def delete_recorder(recorder_name, region):
    '''
    Attempt to delete the specified Config recorder
    '''
    try:
        client = boto3.client("config", region_name=region)
        client.delete_configuration_recorder(ConfigurationRecorderName=recorder_name)
        print("Successfully deleted %s from %s!" % (recorder_name, region))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'UnrecognizedClientException':
            sys.exit("The AWS KEY IS INVALID. Exiting")
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('[-] {} : does not have config access. Did you check first?' .format(AWS_ACCESS_KEY_ID))
            pass
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def list_all_config_rules():
    '''
    Get config rules for each region
    '''
    for region in regions:
        describe_configuration_rules(region)


def list_all_config_recorders():
    '''
    Get recorders for each region
    '''
    for region in regions:
        describe_configuration_recorders(region)


def delete_config_rule(rule_name, region):
    '''
    delete config rule (makes sure you passed a rule name)
    '''
    if rule_name:
        delete_rule(rule_name, region)


def delete_config_recorder(recorder_name, region):
    '''
    delete config recorder (makes sure you passed a recorder name)
    '''
    if recorder_name:
        delete_recorder(recorder_name, region)
