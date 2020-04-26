from contextlib import closing
import boto3
import os

# Reading a file
with open("image2.jpg", 'rb') as image:

    # Using Amazon Translate service to convert text
    translate = boto3.client('rekognition')
    response = translate.recognize_celebrities(
        Image={'Bytes': image.read()},
    )
    
    print("Celebrity: " + response["CelebrityFaces"][0]["Name"]);