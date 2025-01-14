'''
dynamoDB functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys
import os

pp = pprint.PrettyPrinter(indent=5, width=80)

from libs.aws.aws_session import *


def list_dynamodb_tables():
    '''
    Use dynamodb list_tables function to list table names
    '''
    print("### Printing DynamoDB Tables ###")
    try:
        for region in regions:
            client = awsclient('dynamodb', region_name=region)
            response = client.list_tables()
            if response.get('TableNames') is None:
                print("{} likely does not have DynamoDB permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['TableNames']) <= 0:
                print("[-] ListTables allowed for {} but no results [-]" .format(region))
            else:
                print("### {} DynamoDB Tables ###" .format(region))
                for tables in response['TableNames']:
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


def list_dynamodb_tables_detailed():
    '''
    Use dynamodb list_tables function to list table names and also attempt to describe each table from list_tables()
    '''
    print("### Printing DynamoDB Tables ###")
    try:
        for region in regions:
            client = awsclient('dynamodb', region_name=region)
            response = client.list_tables()
            if response.get('TableNames') is None:
                print("{} likely does not have DynamoDB permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['TableNames']) <= 0:
                print("[-] ListTables allowed for {} but no results [-]" .format(region))
            else:
                print("### {} DynamoDB Tables ###" .format(region))
                for tables in response['TableNames']:
                    describe_table(tables, region)
        print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")


def describe_table(table, region):
    '''
    dynamodb attempt to read infromation from specified DynamoDB table
    '''
    print("### Describing DynamoDB Table: {} ###" .format(table))
    try:
        client = awsclient('dynamodb', region_name=region)
        response = client.describe_table(TableName=table)
        if response.get('Table') is None:
            print("{} likely does not have DynamoDB permissions\n" .format(AWS_ACCESS_KEY_ID))
        elif len(response['Table']) <= 0:
            print("[-] DescribeTable allowed for {} but no results [-]" .format(region))
        else:
            print("TableArn: {}" .format(response['Table']['TableArn']))
            print("AttributeDefinitions: {}" .format(response['Table']['AttributeDefinitions']))
            print("ProvisionedThroughput: {}" .format(response['Table']['ProvisionedThroughput']))
            print("TableSizeBytes: {}" .format(response['Table']['TableSizeBytes']))
            print("TableName: {}" .format(response['Table']['TableName']))
            print("TableStatus: {}" .format(response['Table']['TableStatus']))
            print("KeySchema: {}" .format(response['Table']['KeySchema']))
            print("ItemCount: {}" .format(response['Table']['ItemCount']))
            print("CreationDateTime: {}" .format(response['Table']['CreationDateTime']))
        print("\n")

    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'InvalidClientTokenId':
            sys.exit("{} : The AWS KEY IS INVALID. Exiting" .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDenied':
            print('{} : Does not have the required permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'AccessDeniedException':
            print('{} : Does not have the required DescribeTable permissions' .format(AWS_ACCESS_KEY_ID))
        elif e.response['Error']['Code'] == 'SubscriptionRequiredException':
            print('{} : Has permissions but isnt signed up for service - usually means you have a root account' .format(AWS_ACCESS_KEY_ID))
        else:
            print("Unexpected error: {}" .format(e))
    except KeyboardInterrupt:
        print("CTRL-C received, exiting...")
