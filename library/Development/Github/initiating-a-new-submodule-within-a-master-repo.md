---
title: "Initiating a new submodule within a master repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say that I have a "master" repository for a project. I want to set up a new repository but straight away I want that to be set up as a submodule of the master repository. I'd want to 1) set up a remote, 2) clone that to a folder within the master repo . Can this be done automatically?

# Output

Yes, it’s possible to set up a new repository as a submodule of a master repository and automate the process. You can accomplish this by creating a script or using a few Git commands within VS Code or a terminal. Here's how you can set it up:

### Steps to Automate:
1. **Create the Remote Repository**: You’ll need to create the new repository on GitHub (or any other Git provider).
2. **Add the New Repository as a Submodule**: Initialize the new repository as a submodule within the master repository.
3. **Clone the Submodule into the Master Repository**: Automatically clone the newly created repository as a submodule inside the master repo.

### Full Process to Automate:

#### 1. **Create a New Remote Repository**
This step would typically be manual unless you automate repository creation via the GitHub API, GitLab API, or GitHub CLI (`gh`).

**Using GitHub CLI (`gh`)**:
```bash
gh repo create your-username/new-repo-name --public --confirm
```

This creates a new repository directly on GitHub.

#### 2. **Add the Repository as a Submodule and Clone It**
Once you have the remote repository created, you can run a script or set of commands that adds the repository as a submodule to your master repository.

```bash
# Navigate to your master repository
cd path/to/master-repo

# Add the new repository as a submodule
git submodule add https://github.com/your-username/new-repo-name.git path/to/submodule-folder

# Initialize and update the submodule
git submodule update --init --recursive
```

This will:
1. Add the newly created repository as a submodule to your master repo.
2. Clone the submodule into the specified folder.

#### Full Script for Automation:
Here’s a simple shell script that automates the entire process:

```bash
#!/bin/bash

# Variables
GITHUB_USERNAME="your-username"
NEW_REPO_NAME="new-repo-name"
MASTER_REPO_PATH="/path/to/master-repo"
SUBMODULE_FOLDER="path/to/submodule-folder"

# Step 1: Create a new repository on GitHub using the GitHub CLI
gh repo create "$GITHUB_USERNAME/$NEW_REPO_NAME" --public --confirm

# Step 2: Navigate to the master repository
cd "$MASTER_REPO_PATH" || exit

# Step 3: Add the new repository as a submodule
git submodule add https://github.com/"$GITHUB_USERNAME"/"$NEW_REPO_NAME".git "$SUBMODULE_FOLDER"

# Step 4: Initialize and update the submodule
git submodule update --init --recursive

echo "Submodule $NEW_REPO_NAME added and cloned into $SUBMODULE_FOLDER"
```

This script does the following:
- Automatically creates a new repository using the GitHub CLI.
- Adds that repository as a submodule within your master repository.
- Initializes and clones the submodule into the specified folder inside the master repo.

### Automation in **VS Code**:
You can integrate this script into **VS Code** using tasks or a custom script:

1. **Create a Task in VS Code**:
   In your project’s `.vscode/tasks.json` file, you can add a task to run this automation:

   ```json
   {
     "version": "2.0.0",
     "tasks": [
       {
         "label": "Add Submodule",
         "type": "shell",
         "command": "./add_submodule.sh",
         "group": {
           "kind": "build",
           "isDefault": true
         },
         "problemMatcher": []
       }
     ]
   }
   ```

2. **Run the Task**:
   Now you can run the task from the Command Palette (`Ctrl+Shift+P`) by searching for "Tasks: Run Task" and selecting "Add Submodule". This will run the script inside your VS Code environment.

### Conclusion:
By using the GitHub CLI or Git APIs, you can automate the process of creating a new repository, adding it as a submodule to a master repo, and cloning it into a specific folder. This process can be further automated with a shell script or configured as a task in VS Code to streamline development.