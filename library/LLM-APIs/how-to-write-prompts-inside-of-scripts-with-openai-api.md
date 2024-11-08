---
title: "How to write prompts inside of scripts with OpenAI API"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Original script:

```
import os

import requests

from openai import OpenAI

from dotenv import load_dotenv

  

# Load environment variables

load_dotenv()

  

# Get environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

  

# Get environment variables

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

  

# Set up GitHub API

GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

  

# Set up OpenAI API

  

def get_all_repositories():

all_repos = []

page = 1

while True:

response = requests.get(

f"{GITHUB_API_URL}?page={page}&per_page=100",

headers={"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

)

if response.status_code != 200:

raise Exception(f"Failed to fetch repositories: {response.status_code}")

  

repos = response.json()

if not repos:

break

  

all_repos.extend(repos)

page += 1

  

return all_repos

  

def generate_index(repos):

repo_list = "\n".join([f"- {repo['name']}: {repo['description'] or 'No description'}" for repo in repos])

prompt = f"Generate a markdown index for the following GitHub repositories:\n\n{repo_list}\n\nPlease organize them by category and add a brief description for each category."

  

response = client.chat.completions.create(model="gpt-3.5-turbo",

messages=[

{"role": "system", "content": "You are a helpful assistant that creates well-organized markdown indexes for GitHub repositories."},

{"role": "user", "content": prompt}

])

  

return response.choices[0].message.content

  

def main():

if not all([GITHUB_USERNAME, GITHUB_TOKEN, OPENAI_API_KEY]):

raise ValueError("Missing required environment variables. Please check your .env file.")

  

repos = get_all_repositories()

print(f"Found {len(repos)} repositories")

  

index = generate_index(repos)

  

filename = "github_repo_index.md"

with open(filename, "w") as f:

f.write(index)

  

print(f"Index generated and saved to {filename}")

  

# Verify file contents

with open(filename, "r") as f:

content = f.read()

print(f"File contents ({len(content)} characters):")

print(content[:500] + "..." if len(content) > 500 else content)

  

if __name__ == "__main__":

main()
```

My prompt:

