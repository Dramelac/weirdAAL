'''
Translate functions for WeirdAAL
'''

import boto3
import botocore
import pprint
import sys


pp = pprint.PrettyPrinter(indent=5, width=80)

from aws_session import *


def translate_text(text, source_lang, target_lang):
    '''
    Translate a block of text from source to target language
    Available languages: English (en), Arabic (ar), Chinese (Simplified) (zh), French (fr), German (de), Portuguese (pt), Spanish (es)
    http://boto3.readthedocs.io/en/latest/reference/services/translate.html
    '''
    try:
        for region in regions:
            client = boto3.client('translate', region_name=region)
            response = client.translate_text(Text=text, SourceLanguageCode=source_lang, TargetLanguageCode=target_lang)
            # print(response)
            if response.get('TranslatedText') is None:
                print("{} likely does not have Translate permissions\n" .format(AWS_ACCESS_KEY_ID))
            elif len(response['TranslatedText']) <= 0:
                print("[-] TranslateText allowed for {} but no results [-]" .format(region))
            else:
                print("### {}: Translated Text  ###\n" .format(region))
                print("Translated Text: {}".format(response['TranslatedText']))
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
