'''
ElasticBeanstalk functions for WeirdAAL
'''

import boto3
import botocore
import os
import pprint
import sys

pp = pprint.PrettyPrinter(indent=5, width=80)

from aws_session import *


def elasticbeanstalk_describe_applications():
    '''
    Elasticbeanstalk Describe Applications
    '''
    print("### Printing ElasticBeanstalk Applications ###")
    try:
        for region in regions:
            client = boto3.client('elasticbeanstalk', region_name=region)
            response = client.describe_applications()
            # print(response)

            if response.get('Applications') is None:
                print("{} likely does not have ElasticBeanstalk permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Applications']) <= 0:
                print("[-] DescribeApplications allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ElasticBeanstalk Applications ###" .format(region))
                for app in response['Applications']:
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


def elasticbeanstalk_describe_application_versions():
    '''
    Elasticbeanstalk Describe Application versions
    '''
    print("### Printing ElasticBeanstalk Applications Versions ###")
    try:
        for region in regions:
            client = boto3.client('elasticbeanstalk', region_name=region)
            response = client.describe_application_versions()
            # print(response)

            if response.get('ApplicationVersions') is None:
                print("{} likely does not have ElasticBeanstalk permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['ApplicationVersions']) <= 0:
                print("[-] DescribeApplicationVersions allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ElasticBeanstalk Application Versions ###" .format(region))
                for app in response['ApplicationVersions']:
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


def elasticbeanstalk_describe_configuration_options():
    '''
    Elasticbeanstalk Describe Configuration options
    Currently not working
    '''
    print("### Printing ElasticBeanstalk Configuration Options ###")
    try:
        for region in regions:
            client = boto3.client('elasticbeanstalk', region_name=region)
            response = client.describe_configuration_options()
            # print(response)

            if response.get('Options') is None:
                print("{} likely does not have ElasticBeanstalk permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Options']) <= 0:
                print("[-] DescribeConfigurationOptions allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ElasticBeanstalk Configuration Options ###" .format(region))
                # if response['PlatformArn'] is None:
                #    pass
                # else:
                #    print("PlatformArn: {}" .format(response['PlatformArn']))

                print("SolutionStackName: {}" .format(response['SolutionStackName']))
                pp.pprint("Options: {}" .format(response['Options']))
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


def elasticbeanstalk_describe_environments():
    '''
    Elasticbeanstalk Describe Environments
    '''
    print("### Printing ElasticBeanstalk Environments ###")
    try:
        for region in regions:
            client = boto3.client('elasticbeanstalk', region_name=region)
            response = client.describe_environments()
            # print response

            if response.get('Environments') is None:
                print("{} likely does not have ElasticBeanstalk permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Environments']) <= 0:
                print("[-] DescribeEnvironments allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ElasticBeanstalk Environments ###" .format(region))
                for enviro in response['Environments']:
                    pp.pprint(enviro)
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


def elasticbeanstalk_describe_events():
    '''
    Elasticbeanstalk Describe Events
    '''
    print("### Printing ElasticBeanstalk Environments ###")
    try:
        for region in regions:
            client = boto3.client('elasticbeanstalk', region_name=region)
            response = client.describe_events()
            # print(response)

            if response.get('Events') is None:
                print("{} likely does not have ElasticBeanstalk permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['Events']) <= 0:
                print("[-] DescribeEvents allowed for {} but no results [-]" .format(region))
            else:
                print("### {} ElasticBeanstalk Events ###" .format(region))
                for events in response['Events']:
                    pp.pprint(events)
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
