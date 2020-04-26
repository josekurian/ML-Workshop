POLLY_VOICE = 'Maja'

from contextlib import closing
import boto3
import os

# Reading a file
with open("text.txt", 'r') as myfile:
    content=myfile.read().replace('\n', ' ')
    
# Using Amazon Polly service to convert text to speech
polly = boto3.client('polly')
response = polly.synthesize_speech(
    OutputFormat = 'mp3',
    Text = content,
    TextType = 'text',
    VoiceId = POLLY_VOICE
)

# Save audio on local directory
if "AudioStream" in response:
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(".", "audio.mp3")
        with open(output, "wb") as file:
            file.write(stream.read())
file.close()
    
print("File Saved!");
