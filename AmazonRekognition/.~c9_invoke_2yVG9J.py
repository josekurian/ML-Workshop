SOURCE_LANGUAGE = 'pl'
TARGET_LANGUAGE = 'en'

from contextlib import closing
import boto3
import os

# Reading a file
with open("text.txt", 'r') as myfile:
    content=myfile.read()
    
# Using Amazon Translate service to convert text
translate = boto3.client('rekognition')
response = client.detect_labels(
    Image={
        'Bytes': b'bytes',
        'S3Object': {
            'Bucket': 'string',
            'Name': 'string',
            'Version': 'string'
        }
    },
    MaxLabels=100,
    MinConfidence=0.8
)