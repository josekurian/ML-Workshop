from contextlib import closing
import boto3
import os

# Reading a file
with open("image1.jpg", 'rb') as image:

    # Using Amazon Translate service to convert text
    translate = boto3.client('rekognition')
    response = translate.detect_labels(
        Image={'Bytes': image.read()},
        MaxLabels=100,
        MinConfidence=0.95
    )
    
    for label in response["Labels"]:
        print(label);