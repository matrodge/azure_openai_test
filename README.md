# Azure OpenAI Chat Example

This Python script, `azure_openai_chat_example.py`, demonstrates how to authenticate with Azure, use the OpenAI API to send a chat message, and receive a response from the chatbot model.

## Prerequisites

Before running this script, you will need:

- Python 3 installed on your system
- An Azure account with access to OpenAI services, talk to the BridgeIT API team for this
- Client ID and Client Secret for Azure OpenAI authentication (This is what the BridgeIT API team will give you)

## Installation

Clone this repository or download the `azure_openai_chat_example.py` file directly. To install the required dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Configuration

You need to create a .env file in the same directory as the script with the following content:

AZURE_OPENAI_CLIENT_ID=your_client_id_here
AZURE_OPENAI_CLIENT_SECRET=your_client_secret_here
Replace your_client_id_here and your_client_secret_here with your actual Azure OpenAI credentials.

## Usage

To run the script, navigate to the directory containing azure_openai_chat_example.py and execute the following command:

```bash
python azure_openai_chat_example.py
```

The script will authenticate with Azure, send a predefined chat message (which you can change if you'd like) to the OpenAI API 3.5 turbo, and print the chatbot's response to the console.

## Features

1. Authentication with Azure OpenAI using client credentials
2. Sending chat messages to a pre-trained OpenAI GPT-3.5 model
3. Retrieving and displaying the model's response

## Support
If you encounter any issues or have questions, please feel free to open an issue in the repository, or contact matrodge@cisco.com

## Contributing
Contributions to this script are welcome. Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License.