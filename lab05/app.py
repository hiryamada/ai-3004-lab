import os
from urllib.request import urlopen, Request
import base64
from pathlib import Path
from dotenv import load_dotenv

# Add references
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential

def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
        # Get configuration settings 
        load_dotenv()

        endpoint = os.getenv("ENDPOINT_URL")
        model_deployment = os.getenv("DEPLOYMENT_NAME")
        subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

        # Initialize Azure OpenAI client with key-based authentication
        openai_client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=subscription_key,
            api_version="2025-01-01-preview",
        )

        # Initialize prompts
        system_message = "You are an AI assistant in a grocery store that sells fruit. You provide detailed answers to questions about produce."
        prompt = ""

        # Loop until the user types 'quit'
        while True:
            prompt = input("\nAsk a question about the image\n(or type 'quit' to exit)\n")
            if prompt.lower() == "quit":
                break
            elif len(prompt) == 0:
                    print("Please enter a question.\n")
            else:
                print("Getting a response ...\n")


                # Get a response to image input
                image_url = "https://github.com/MicrosoftLearning/mslearn-ai-vision/raw/refs/heads/main/Labfiles/gen-ai-vision/orange.jpeg"
                image_format = "jpeg"
                request = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
                image_data = base64.b64encode(urlopen(request).read()).decode("utf-8")
                data_url = f"data:image/{image_format};base64,{image_data}"

                response = openai_client.chat.completions.create(
                    model=model_deployment,
                    messages=[
                        {"role": "system", "content": system_message},
                        { "role": "user", "content": [  
                            { "type": "text", "text": prompt},
                            { "type": "image_url", "image_url": {"url": data_url}}
                        ] } 
                    ]
                )
                print(response.choices[0].message.content)                    


    except Exception as ex:
        print(ex)


if __name__ == '__main__': 
    main()