SOURCE_LANGUAGE = 'pl'
TARGET_LANGUAGE = 'en'

from contextlib import closing
import boto3
import os

# Reading a file
with open("text1.txt", 'r') as myfile:
    content=myfile.read()
    
# Using Amazon Translate service to convert text
comprehend = boto3.client('comprehend')
response = comprehend.detect_dominant_language(
    Text = content
)

language = response["Languages"];
print("Text in : " + str(language));
