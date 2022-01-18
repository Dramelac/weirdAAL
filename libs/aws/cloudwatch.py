'''
Cloudwatch functions for WeirdAAL
'''

import boto3
import botocore
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from aws_session import *


def cloudwatch_describe_alarms():
    '''
    Describe CloudWatch alarms
    '''
    print("### Printing Cloudwatch Alarm Information ###")
    try:
        for region in regions:
            client = boto3.client('cloudwatch', region_name=region)

            response = client.describe_alarms()
            print("### {} Alarms ###" .format(region))
            for alarm in response['MetricAlarms']:
                pp.pprint(alarm)
        print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Is NOT a root key' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'OptInRequired':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def cloudwatch_describe_alarm_history():
    '''
    Describe CloudWatch Alarm History
    '''
    print("### Printing Cloudwatch Alarm History Information ###")
    try:
        for region in regions:
            client = boto3.client('cloudwatch', region_name=region)

            response = client.describe_alarm_history()
            # print(response)
            if response.get('AlarmHistoryItems') is None:
                print("{} likely does not have cloudwatch permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['AlarmHistoryItems']) <= 0:
                print("[-] DecribeAlarmHistory allowed for {} but no results [-]" .format(region))
            else:
                print("### {} Alarm History ###" .format(region))
                for history_item in response['AlarmHistoryItems']:
                    pp.pprint(history_item)
        print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Is NOT a root key' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'OptInRequired':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def cloudwatch_list_metrics():
    '''
    List CloudWatch metrics
    '''
    print("### Printing Cloudwatch List Metrics ###")
    try:
        for region in regions:
            client = boto3.client('cloudwatch', region_name=region)

            response = client.list_metrics()
            # print(response)
            if response.get('Metrics') is None:
                print("{} likely does not have cloudwatch permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Metrics']) <= 0:
                print("[-] ListMetrics allowed for {} but no results [-]" .format(region))
            else:
                print("### Listing Metrics for {} ###" .format(region))
                for metrics in response['Metrics']:
                    pp.pprint(metrics)
        print("\n")
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Is NOT a root key' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'OptInRequired':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
