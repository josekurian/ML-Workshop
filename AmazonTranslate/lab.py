SOURCE_LANGUAGE = 'pl'
TARGET_LANGUAGE = 'en'

from contextlib import closing
import boto3
import os

# Reading a file
with open("text.txt", 'r') as myfile:
    content=myfile.read()
    
# Using Amazon Translate service to convert text
translate = boto3.client('translate')
response = translate.translate_text(
    Text = content,
    SourceLanguageCode = SOURCE_LANGUAGE,
    TargetLanguageCode = TARGET_LANGUAGE
)

translatedText = response["TranslatedText"];

output = os.path.join(".", "translation.txt")
with open(output, "w") as file:
    file.write(translatedText)
file.close()

print("File Saved!");
