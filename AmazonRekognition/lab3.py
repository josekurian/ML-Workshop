from contextlib import closing
import boto3
import os

# Reading a file
image1 = open("image2.jpg", 'rb');
image2 = open("image3.jpg", 'rb');

translate = boto3.client('rekognition')
response = translate.compare_faces(
    SourceImage={'Bytes': image1.read()},
    TargetImage={'Bytes': image2.read()},
    SimilarityThreshold=0.90
)

print("Similarity: " + str(response["FaceMatches"][0]["Similarity"]));