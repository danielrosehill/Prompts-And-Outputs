---
title: "Exporting list of Gitkraken Workspaces and their repos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


As of now, **GitKraken** doesn’t have a direct built-in feature for exporting a list of workspaces and repositories. However, you can manually gather this information by inspecting the workspace setup or by using a **scripted approach** via GitKraken's associated file structure.

Here are a few methods you can try:

### 1. **Manual Approach from GitKraken**
You can manually inspect each workspace in GitKraken and list the repositories:

- Open GitKraken.
- Navigate to **Workspaces**.
- Open each workspace and note down the repositories listed.
- You can then manually compile this into a CSV or text file.

### 2. **Using GitKraken’s Local File Configuration**
GitKraken stores local settings in configuration files, including workspaces and repositories. These files are typically stored locally on your machine, and you can extract information from them.

For example, on **Linux** or **Windows**, you may find the relevant files in:

- **Linux**: `~/.gitkraken`
- **Windows**: `C:\Users\<YourUsername>\.gitkraken`

You can look for JSON or configuration files that reference workspaces and repositories. Once located, you could parse these files (if they're in a readable format like JSON) using a script.

### 3. **Using GitKraken's API (GitHub, GitLab, etc.)**
If your workspaces are linked to Git services (like GitHub or GitLab), you could write a script using their APIs to extract repositories that are connected to a particular workspace.

For example, if your repositories are hosted on **GitHub**, you can use the **GitHub API** to list all the repositories in a particular organization or linked to your GitKraken account.

#### Example with GitHub API:
1. Authenticate with the **GitHub API**.
2. List all repositories in an organization or under your user account:
   ```bash
   curl -H "Authorization: token YOUR_GITHUB_TOKEN" https://api.github.com/user/repos
   ```

You can similarly do this for **GitLab**, **Bitbucket**, or other services your GitKraken workspaces are connected to.

### 4. **Export Repositories from GitHub (if applicable)**
If your repositories are hosted on **GitHub** and linked to GitKraken, you can use a GitHub API or GitHub CLI (`gh`) to list the repositories in an organization or under your account.

Example with GitHub CLI:
```bash
gh repo list <your-org-or-username> --limit 100
```

### 5. **Script to Export Workspaces from GitKraken Config**
If you’re comfortable with scripting and find the configuration files that GitKraken uses to store your workspace and repository data, you can write a custom script (in Python, for example) to extract and export the data into a CSV or text file.

#### Example Python Script (if JSON-based config):
```python
import json

# Open GitKraken config file
config_file = '/path/to/gitkraken/config.json'

with open(config_file, 'r') as file:
    data = json.load(file)

# Extract relevant workspace and repo information
workspaces = data.get('workspaces', [])

# Save the information to a CSV
with open('gitkraken_workspaces.csv', 'w') as csv_file:
    csv_file.write('Workspace, Repository\n')
    for workspace in workspaces:
        workspace_name = workspace.get('name')
        for repo in workspace.get('repositories', []):
            repo_name = repo.get('name')
            csv_file.write(f'{workspace_name}, {repo_name}\n')

print('Workspace list exported to gitkraken_workspaces.csv')
```

This example assumes the config file is in a JSON format, and the structure contains "workspaces" and "repositories."

### Conclusion
- For a manual approach, you can manually inspect and list repositories under each workspace within GitKraken.
- If you are comfortable with scripting, you can check GitKraken’s local configuration files or leverage GitHub/GitLab/Bitbucket APIs if your workspaces are linked to these services.
  
There isn't a direct "export" button in GitKraken, but with some automation, you can achieve a similar result. Let me know if you need help with any of the approaches!