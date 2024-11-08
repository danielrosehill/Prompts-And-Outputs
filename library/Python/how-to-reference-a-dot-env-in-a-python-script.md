---
title: "How to reference a dot env in a Python script"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

the variable I have in my dot env is ANTHROPIC_API_KEY Can you tell me how I can reference that in the python script?

# Output

To reference the `ANTHROPIC_API_KEY` variable from your `.env` file in Python, you can use the `python-dotenv` package. Here's how to modify the script to load the API key from the `.env` file:

1. First, install `python-dotenv` if you don't have it yet:

   ```bash
   pip install python-dotenv
   ```

2. Update your script to load the API key from the `.env` file:

```python
import os
import requests
import json
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Retrieve the API key from the .env file
API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Claude API endpoint
url = 'https://api.anthropic.com/v1/complete'

# Set the headers with your API key
headers = {
    'Content-Type': 'application/json',
    'x-api-key': API_KEY
}

# The prompt to generate the list of media organizations
prompt = """
Generate a list of 1,000 of the world's biggest media organizations. Provide only the name and country for each, in alphabetical order by country.
"""

# Set the request payload
data = {
    'prompt': prompt,
    'model': 'claude-2',  # Ensure you're using Claude 2 with a large token limit
    'max_tokens_to_sample': 100000,  # Request enough tokens to handle the full response
    'stop_sequences': ['\n']
}

# Make the request to the Claude API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Parse and print the response
media_list = response.json().get('completion', '').strip()
print(media_list)

# Optionally save the result to a file
with open('media_organizations_claude.txt', 'w') as f:
    f.write(media_list)
```

### Steps:
1. Make sure your `.env` file has the following line:

   ```
   ANTHROPIC_API_KEY=your_actual_api_key
   ```

2. The `dotenv` package will load the environment variables from the `.env` file, and you can reference the `ANTHROPIC_API_KEY` using `os.getenv('ANTHROPIC_API_KEY')`.

This will allow you to securely store and reference your API key from the `.env` file.