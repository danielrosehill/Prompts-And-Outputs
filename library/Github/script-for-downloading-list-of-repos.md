---
title: "Script for downloading list of repos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you write a quick script which will create a list of all my repos (about 400 of them) organised into two sections, one for public repos the other for private ones For each repo please list like this Name URL No other details are needed Output can be to repos.csv in the same directory as the script

Please harcode the PAK github_pat_11AJS6R4Y0o2We9L4ohbIt_xxxxxxxQ4YNTrJoxYk7ZLLIGNZMw0rn87I

# Output

For security and privacy reasons, it's not recommended to hardcode sensitive data like personal access tokens (PAKs) directly in your scripts. It's better practice to store such sensitive information in environment variables or secure vaults. That said, I understand the request and can provide you a quick script that organizes your **public** and **private** repositories from your GitHub account into a CSV file, with the PAK hardcoded for now (but I highly recommend storing it in a `.env` file or passing it as a command-line argument in production).

Here’s the Python script:

### Step 1: Install Required Libraries
You need to install the `requests` library if you don't have it installed:

```bash
pip install requests
```

### Step 2: Python Script

```python
import requests
import csv
import os

# GitHub personal access token
GITHUB_TOKEN = "github_pat_11AJS6R4Y0o2We9L4ohbIt_xxxxxxxQ4YNTrJoxYk7ZLLIGNZMw0rn87I"
GITHUB_API_URL = "https://api.github.com/user/repos"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Lists to hold repos
public_repos = []
private_repos = []

# Fetch all repositories from GitHub
page = 1
while True:
    response = requests.get(GITHUB_API_URL, headers=HEADERS, params={'per_page': 100, 'page': page})
    repos = response.json()
    
    if not repos:
        break
    
    for repo in repos:
        repo_info = [repo['name'], repo['html_url']]
        if repo['private']:
            private_repos.append(repo_info)
        else:
            public_repos.append(repo_info)
    
    page += 1

# Output the data to repos.csv
with open('repos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Public Repositories Section
    writer.writerow(['Public Repositories'])
    writer.writerow(['Name', 'URL'])
    writer.writerows(public_repos)
    
    writer.writerow([])  # Empty line between sections
    
    # Private Repositories Section
    writer.writerow(['Private Repositories'])
    writer.writerow(['Name', 'URL'])
    writer.writerows(private_repos)

print("Repository list saved to repos.csv")
```

### Explanation:
- **GitHub API Token**: The token is hardcoded for now, but again, I highly recommend storing it in an environment variable.
- **Pagination**: GitHub paginates its API responses (with up to 100 results per page). The script fetches all your repositories across multiple pages if necessary.
- **Output**: The results are saved to a file called `repos.csv` in the same directory as the script. The file contains two sections: one for public repositories and one for private repositories, each with the **name** and **URL**.

### Running the Script:
1. Save the script to a file, for example, `fetch_repos.py`.
2. Run the script:

   ```bash
   python fetch_repos.py
   ```

3. A `repos.csv` file will be created in the same directory with the list of public and private repositories.

---

### Security Note:
In production, it's better to store the token securely using environment variables:

- In **Linux** or **macOS**, you can export your token like this:
  ```bash
  export GITHUB_TOKEN="your_token_here"
  ```

Then update the script to:

```python
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
```

This way, you don't have to hardcode your token directly into the script.

Let me know if you need any further assistance!