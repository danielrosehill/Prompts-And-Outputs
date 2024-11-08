---
title: "Submodule addition script"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you write me a script which will run at the base of the repository It will recurse through this list of repos which is at Management/Repos/repos.txt And it will add every repo in the list as a submodule If the repo is already a submodule, it can just skip it

# Output

Certainly! I can provide you with a Bash script that will accomplish this task. Here's a script that will read the `repos.txt` file, recursively add each repository as a submodule if it's not already present, and skip those that are already submodules:

```bash
#!/bin/bash

# Path to the repos.txt file
REPOS_FILE="Management/Repos/repos.txt"

# Check if the repos file exists
if [ ! -f "$REPOS_FILE" ]; then
    echo "Error: $REPOS_FILE not found!"
    exit 1
fi

# Read each line from the repos.txt file
while IFS= read -r repo_url; do
    # Skip empty lines and comments
    [[ -z "$repo_url" || "$repo_url" =~ ^#.*$ ]] && continue

    # Extract the repo name from the URL
    repo_name=$(basename "$repo_url" .git)

    # Check if the submodule already exists
    if git submodule status | grep -q "$repo_name"; then
        echo "Submodule $repo_name already exists. Skipping..."
    else
        echo "Adding submodule: $repo_name"
        git submodule add "$repo_url"
        if [ $? -eq 0 ]; then
            echo "Successfully added $repo_name as a submodule."
        else
            echo "Failed to add $repo_name as a submodule."
        fi
    fi
done < "$REPOS_FILE"

echo "Finished processing all repositories."
```

To use this script:

1. Save it as `add_submodules.sh` in the root directory of your main repository.

2. Make the script executable:
   ```
   chmod +x add_submodules.sh
   ```

3. Run the script:
   ```
   ./add_submodules.sh
   ```

This script does the following:

1. It defines the path to your `repos.txt` file.
2. It checks if the file exists.
3. It reads the file line by line, skipping empty lines and comments (lines starting with #).
4. For each repository URL:
   - It extracts the repository name.
   - It checks if the repository is already a submodule.
   - If it's not a submodule, it adds it using `git submodule add`.
   - It provides feedback on the success or failure of each operation.

Remember to commit the changes after running the script, as adding submodules will modify your `.gitmodules` file and create new entries in your repository.

Also, ensure you have the necessary permissions to add these repositories as submodules. If any of the repositories are private, you'll need to have the appropriate access rights.

Citations:
[1] https://www.wolframalpha.com/input?input=%22repos.txt%22+file+format+specification