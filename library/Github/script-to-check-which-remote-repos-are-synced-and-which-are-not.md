---
title: "Script to check which remote repos are synced and which are not"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Would it be possible to write a script which lists all the git repositories in my Git folder (recursing into the subdirectories). Then reviews the list of remote repos in my account. Then produces a report stating which remote repos I don't have in my local structure?

# Output

Yes, it's absolutely possible to write a script that will:

1. **List all Git repositories in your `/Git` folder** by recursively searching into subdirectories.
2. **Review all remote repositories in your GitHub account**.
3. **Compare the two lists** and generate a report identifying which remote repositories are missing in your local `/Git` folder.

### Here's a step-by-step outline of how this can be done:

### 1. **List all Local Git Repositories in the `/Git` Folder**

We will search for `.git` directories recursively inside the `/Git` folder and retrieve the corresponding remote URLs.

### 2. **Retrieve All Repositories from Your GitHub Account**

We will use the **GitHub API** or **GitHub CLI** (`gh`) to list all repositories under your GitHub account.

### 3. **Compare Local Repos with Remote Repos**

Finally, we will compare the local repositories' URLs with the list of remote repositories and produce a report indicating which remote repositories are missing from the local `/Git` folder.

---

### Script to Perform These Actions

#### Prerequisites:
- **GitHub CLI (`gh`)** or the **GitHub API**. If you don't have GitHub CLI installed, install it using:
  ```bash
  sudo dnf install gh
  ```
- **Git** should be installed on your system.

#### The Script:
```bash
#!/bin/bash

# Define the base directory where your repositories are located
BASE_DIR=~/Git

# Output file for the report
REPORT_FILE="missing_repos_report.txt"

# GitHub username and API token (use GitHub CLI or API for authentication)
GITHUB_USER="your-github-username"

# Function to get all local Git repos and their remote URLs
get_local_repos() {
    echo "Fetching local repositories from $BASE_DIR..."
    
    # Create or clear the report file
    > "$REPORT_FILE"
    
    # Find all local Git repositories and get their remote URLs
    find "$BASE_DIR" -type d -name ".git" | while read -r repo; do
        repo_dir=$(dirname "$repo")
        repo_url=$(git -C "$repo_dir" remote get-url origin 2>/dev/null)
        if [ -n "$repo_url" ]; then
            echo "$repo_url"
        fi
    done
}

# Function to get all remote GitHub repos for the user
get_remote_repos() {
    echo "Fetching remote repositories from GitHub..."

    # Use GitHub CLI to get all remote repositories under your account
    gh repo list "$GITHUB_USER" --limit 1000 --json name,url --jq '.[].url'
}

# Function to compare and find missing repositories
find_missing_repos() {
    local_repos=$(get_local_repos)
    remote_repos=$(get_remote_repos)

    echo "Comparing local and remote repositories..."

    # Loop over the remote repositories and check if they are present in the local list
    for remote_repo in $remote_repos; do
        if ! echo "$local_repos" | grep -q "$remote_repo"; then
            echo "Missing repository locally: $remote_repo"
            echo "$remote_repo" >> "$REPORT_FILE"
        fi
    done
}

# Run the comparison
find_missing_repos

echo "Report generated: $REPORT_FILE"
```

### Explanation of the Script:
1. **get_local_repos**: 
   - This function scans your `/Git` directory recursively, finding all `.git` directories.
   - It retrieves the remote URL for each local repository using `git remote get-url origin`.

2. **get_remote_repos**:
   - This function uses the **GitHub CLI** (`gh repo list`) to list all repositories in your GitHub account.
   - You need to replace `your-github-username` with your actual GitHub username.
   - If you want to use the **GitHub API** instead of the CLI, you can modify this function accordingly.

3. **find_missing_repos**:
   - This function compares the list of local repositories to the list of remote repositories.
   - Any remote repository that is **not** found in the local list is added to the report (`missing_repos_report.txt`).

### How to Use:
1. **Install the GitHub CLI**:
   - If not already installed, install **GitHub CLI** (`gh`), authenticate it using `gh auth login`, and grant it access to your repositories.

2. **Run the Script**:
   Save the script as `check_missing_repos.sh` and make it executable:
   ```bash
   chmod +x check_missing_repos.sh
   ```
   
   Then run the script:
   ```bash
   ./check_missing_repos.sh
   ```

3. **Report Output**:
   - After running, the script will generate a file called `missing_repos_report.txt`, listing any repositories that are in your GitHub account but **missing** from your local `/Git` folder.

### Customizations:
- You can **filter repositories** if you only want to check specific ones, e.g., only public repositories, or filter by organization.
- Modify the **report file location** or format (e.g., CSV or JSON) if necessary.

### **Efficiency**:
- The script only compares the URLs of repositories, so it won’t use much data. It’s efficient because it just fetches the list of repositories and compares their URLs.
- Since it uses **GitHub CLI**, it can handle large lists of repositories (up to 1000) easily.

### **Enhancements**:
1. **Filtering**: Add filtering options if you have certain categories of repositories you don’t want to include in the comparison (e.g., archived repos).
2. **Syncing**: If you want, the script can be extended to **automatically clone** missing repositories after identifying them.
3. **Scheduling**: You can run this script periodically (via cron) to ensure your local structure is always synced with your remote repositories.

---

This script will help you track and manage repositories across your local machine and GitHub, ensuring you're aware of any remote repositories you haven't yet cloned locally. Let me know if you'd like further assistance!