---
title: "Simultaneously pushing multiple Git repos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have 4 github repos in a directory. is there any way to do a git add ., config, push on all 4 of them simutlaneously?

# Output

Yes, you can automate the `git add .`, `git commit`, and `git push` commands for multiple Git repositories in a directory by writing a simple **bash script**. This script will recursively find all repositories in the directory and perform the necessary Git commands on each one.

Here’s how you can do it:

### **Steps to Automate `git add .`, `git commit`, and `git push` for Multiple Repos:**

1. **Create the Bash Script**:
   Save this script in a file, such as `git-multi-push.sh`:

```bash
#!/bin/bash

# Define the base directory where your repositories are located
BASE_DIR="/path/to/your/repositories"  # Change this to the directory containing your Git repos

# Define a commit message
COMMIT_MSG="Automated commit"

# Find all the .git directories within the base directory
find "$BASE_DIR" -type d -name ".git" | while read -r git_dir; do
    # Get the parent directory (repository root)
    repo_dir=$(dirname "$git_dir")
    
    echo "[INFO] Entering repository: $repo_dir"
    
    # Change to the repository directory
    cd "$repo_dir" || exit
    
    # Add all changes
    echo "[INFO] Running git add . in $repo_dir"
    git add .
    
    # Commit changes
    echo "[INFO] Committing changes in $repo_dir"
    git commit -m "$COMMIT_MSG"
    
    # Push to remote
    echo "[INFO] Pushing changes in $repo_dir"
    git push
    
    echo "[INFO] Done with repository: $repo_dir"
    echo "---------------------------------"
done
```

### **Explanation of the Script:**

- **BASE_DIR**: The base directory where all your repositories are located. Change `/path/to/your/repositories` to the path where your 4 repositories are located.
- The script uses `find` to recursively locate `.git` directories, which are the indicators of a Git repository.
- For each repository:
  - `git add .`: Stages all changes.
  - `git commit -m "Automated commit"`: Commits the changes with a specified message (you can modify the message).
  - `git push`: Pushes the changes to the remote repository.

### **Make the Script Executable**:
Once the script is created, make it executable:

```bash
chmod +x git-multi-push.sh
```

### **Run the Script**:
Run the script to automatically add, commit, and push changes for all your repositories:

```bash
./git-multi-push.sh
```

### **Customize the Commit Message**:
If you want to specify a custom commit message every time, you can modify the script to accept a commit message as an argument:

```bash
#!/bin/bash

# Define the base directory where your repositories are located
BASE_DIR="/path/to/your/repositories"

# Check if a commit message is passed, otherwise use a default message
COMMIT_MSG=${1:-"Automated commit"}

# Find all the .git directories within the base directory
find "$BASE_DIR" -type d -name ".git" | while read -r git_dir; do
    # Get the parent directory (repository root)
    repo_dir=$(dirname "$git_dir")
    
    echo "[INFO] Entering repository: $repo_dir"
    
    # Change to the repository directory
    cd "$repo_dir" || exit
    
    # Add all changes
    echo "[INFO] Running git add . in $repo_dir"
    git add .
    
    # Commit changes
    echo "[INFO] Committing changes in $repo_dir"
    git commit -m "$COMMIT_MSG"
    
    # Push to remote
    echo "[INFO] Pushing changes in $repo_dir"
    git push
    
    echo "[INFO] Done with repository: $repo_dir"
    echo "---------------------------------"
done
```

Now, you can specify the commit message when running the script:

```bash
./git-multi-push.sh "Updated files with latest changes"
```

### **Benefits**:
- **Automates multi-repo Git management**: This script will automatically handle multiple repositories in a directory without the need for manual intervention.
- **Works for multiple repositories**: Even if you add more repositories in the future, the script will work on all of them.

Let me know if you need further adjustments or explanations!