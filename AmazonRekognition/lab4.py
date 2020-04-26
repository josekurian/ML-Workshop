from contextlib import closing
import boto3
import os

image = open("image2.jpg", 'rb');

translate = boto3.client('rekognition')
response = translate.detect_faces(
    Image={'Bytes': image.read()},
    Attributes= [ "ALL" ]
)

print(response);
