# exmample code by Matt Rodgers matrodge@cisco.com
# NOTE: the variables, such as urls, model version, etc. may change at anytime
# rendering this script semi-useless. Caveat emptor
import os
from dotenv import load_dotenv
import json
import openai
from openai import AzureOpenAI
import requests
import base64

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables with error checking
client_id = os.getenv("AZURE_OPENAI_CLIENT_ID")
if not client_id:
    raise ValueError("Missing environment variable: AZURE_OPENAI_CLIENT_ID")

client_secret = os.getenv("AZURE_OPENAI_CLIENT_SECRET")
if not client_secret:
    raise ValueError("Missing environment variable: AZURE_OPENAI_CLIENT_SECRET")

openai.api_type = "azure"

# Specify the API version
api_version = "2023-12-01-preview"
openai.api_version = api_version

# OAuth2 token endpoint
token_url = "https://id.cisco.com/oauth2/default/v1/token"
llm_endpoint = "https://chat-ai.cisco.com"

# Payload for the token request
payload = "grant_type=client_credentials"

# Encode Client ID and Secret to Base64 for Basic Authorization header
auth_key = base64.b64encode(f"{client_id}:{client_secret}".encode("utf-8")).decode("utf-8")

# Headers for the token request
headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {auth_key}",
}

# Make a POST request to retrieve the token
try:
    token_response = requests.post(token_url, headers=headers, data=payload)
    token_response.raise_for_status()  # Raises HTTPError if the status is 4xx or 5xx
except requests.exceptions.RequestException as e:
    print(f"Failed to retrieve token: {e}")
    exit(-1)

# Parse the token from the response
token_data = token_response.json()
token = token_data.get("access_token")
if not token:
    print("Failed to retrieve access token from response.")
    exit(-1)

app_key = "hackathon-explore-35-team-4"

# Initialize the AzureOpenAI client with the obtained token
client = AzureOpenAI(
    azure_endpoint=llm_endpoint,
    api_key=token,
    api_version=api_version,
)

# Prepare the user parameter for the API call
model = "gpt-35-turbo"
user_param = json.dumps({"appkey": app_key})

# History of messages to be sent to the model
message_with_history = [
    {"role": "system", "content": "You are a chatbot"},
    {"role": "user", "content": "who is the president of the USA."},
]

# Make the API call to get a completion from the language model
try:
    response = client.chat.completions.create(
        messages=message_with_history,
        model=model,
        user=user_param,
    )
except Exception as e:
    print(f"Failed to get a response from the model: {e}")
    exit(-1)

# Print the prompt and response
print(f"\nYour prompt: {message_with_history}\n")
print(f"\nThe LLM response: {response.choices[0].message.content}\n")

# Print detailed response fields
print("The detailed response fields...\n")
if isinstance(response, dict):
    response_json = json.dumps(response, indent=4)
    print(response_json)
else:
    for attr in dir(response):
        if not attr.startswith("__") and not callable(getattr(response, attr)):
            print(f"    {attr}: {getattr(response, attr)}\n")