# DALL-E 3 requires version 1.0.0 or later of the openai-python library.

import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv

load_dotenv()

# You will need to set these environment variables or edit the following values.
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("OPENAI_API_VERSION")
deployment = os.getenv("DEPLOYMENT_NAME")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=api_key,
)

result = client.images.generate(
    model=deployment,
    prompt="Futuristic neon city at night, cyberpunk style, floating vehicles, holographic advertisements, rain-slicked streets",
    n=1,
    style="vivid",
    quality="standard",

)


image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url)