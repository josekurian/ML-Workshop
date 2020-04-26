SOURCE_LANGUAGE = 'pl'
TARGET_LANGUAGE = 'en'

from contextlib import closing
import boto3
import os

# Reading a file
with open("text2.txt", 'r') as myfile:
    content=myfile.read()
    
# Using Amazon Translate service to convert text
comprehend = boto3.client('comprehend')
response = comprehend.detect_dominant_language(
    Text = content
)

language = response["Languages"][0]["LanguageCode"];

response = comprehend.detect_sentiment(
    Text = content,
    LanguageCode = language
)

print("Sentiment: " + response["Sentiment"]);

print("Details:");
print(response["SentimentScore"]);