import boto3
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

polly = boto3.client('polly')

try:
    response = polly.synthesize_speech(Text="¡Hola! ¿Que tal? ¡Estás escuchando esta grabación desde Amazon Polly!", OutputFormat="mp3", VoiceId="Mia")
except (BotoCoreError, ClientError) as error:
    print(error)sys.exit(-1)
else:ys.exit(-1)
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")