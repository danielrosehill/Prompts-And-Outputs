---
title: "Cloning helper GUIs into repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

What's the best way to do what I'm trying to do. I have a few helper GUIs that are related to my github repository

Their paths are set out in /Repo-Setup/repos.txt

Currently they are:

https://github.com/danielrosehill/LLM-Obsidian-Vault-Backup-Utility.git
https://github.com/danielrosehill/Obsidian-LLM-Vault-Management-GUI.git
https://github.com/danielrosehill/Obsidian-Prompt-Output-Saver.git


I'd like to create a script in my repo. when it runs, it should clone these to a directory in the repo called /GUIs/Active

# Output

Based on your requirements, I can suggest a script that will clone the specified repositories into a designated directory within your main repository. Here's how you can achieve this:

1. Create a new bash script in the root of your repository, let's call it `clone_guis.sh`.

2. Make the script executable:

```bash
chmod +x clone_guis.sh
```

3. Here's the content for the `clone_guis.sh` script:

```bash
#!/bin/bash

# Set script to exit on any error
set -e

# Change to the directory containing this script
cd "$(dirname "$0")"

# Create the GUIs/Active directory if it doesn't exist
mkdir -p GUIs/Active

# Read the repos from the file
REPOS_FILE="Repo-Setup/repos.txt"

# Check if the repos file exists
if [ ! -f "$REPOS_FILE" ]; then
    echo "Error: $REPOS_FILE not found!"
    exit 1
fi

# Clone or update each repository
while IFS= read -r repo
do
    # Extract the repo name from the URL
    repo_name=$(basename "$repo" .git)
    
    # Check if the repository already exists
    if [ -d "GUIs/Active/$repo_name" ]; then
        echo "Updating $repo_name..."
        cd "GUIs/Active/$repo_name"
        git pull
        cd ../../..
    else
        echo "Cloning $repo_name..."
        git clone "$repo" "GUIs/Active/$repo_name"
    fi
done < "$REPOS_FILE"

echo "All repositories have been cloned or updated successfully."
```

This script does the following:

1. It creates a `GUIs/Active` directory in your repository if it doesn't already exist.

2. It reads the repository URLs from `/Repo-Setup/repos.txt`.

3. For each repository URL:
   - If the repository already exists in `GUIs/Active`, it updates it using `git pull`.
   - If the repository doesn't exist, it clones it into `GUIs/Active`.

To use this script:

1. Ensure that `/Repo-Setup/repos.txt` exists and contains the repository URLs, one per line.

2. Run the script from the root of your repository:

```bash
./clone_guis.sh
```

This approach has several advantages:

- It's flexible: You can easily add or remove repositories by editing the `repos.txt` file.
- It's idempotent: You can run the script multiple times without issues. It will update existing repositories and clone new ones.
- It keeps your helper GUIs organized in a specific directory within your main repository.

Remember to add the `GUIs/Active` directory to your `.gitignore` file if you don't want to track these cloned repositories in your main repository's version control.

This solution provides an efficient way to manage and update your related helper GUIs within your main repository structure.

Citations:
[1] https://github.com/danielrosehill/LLM-Obsidian-Vault-Backup-Utility.g