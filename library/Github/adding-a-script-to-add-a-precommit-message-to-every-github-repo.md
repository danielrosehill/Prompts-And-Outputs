---
title: "Adding a script to add a precommit message to every Github repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

You previously showed me a way I can add a default commit message to a git repo by adding a hook. is there a way that I could recurse through every repo in /Git (and subfolders). For every Git repo found, i'd like to add this into the .git folder within it

# Output

Yes, you can create a script that recursively goes through each Git repository in a specified directory (like `/Git` and its subfolders) and adds a `prepare-commit-msg` hook to each repository's `.git/hooks` directory. Below is a shell script that accomplishes this task.

### Bash Script to Add a Default Commit Message Hook

1. **Create a Shell Script**:
   You can create a shell script (e.g., `add_commit_hook.sh`) with the following content:

   ```bash
   #!/bin/bash

   # Define the commit message
   COMMIT_MSG="Update"

   # Find all directories with a .git subdirectory
   find /Git -type d -name ".git" | while read gitdir; do
       # Determine the path to the hooks directory
       hooks_dir="$gitdir/hooks"
       
       # Create the prepare-commit-msg hook script
       echo -e "#!/bin/sh\n\necho \"$COMMIT_MSG\" > \"\$1\"" > "$hooks_dir/prepare-commit-msg"
       
       # Make the hook executable
       chmod +x "$hooks_dir/prepare-commit-msg"
       
       echo "Added prepare-commit-msg hook to $gitdir"
   done
   ```

2. **How It Works**:
   - The script uses the `find` command to search for directories named `.git` starting from the `/Git` directory.
   - For each `.git` directory found, it creates a `prepare-commit-msg` hook that sets a default commit message.
   - The hook script is made executable with `chmod +x`.

3. **Run the Script**:
   - Save the script to a file (e.g., `add_commit_hook.sh`).
   - Make the script executable:
     ```bash
     chmod +x add_commit_hook.sh
     ```
   - Run the script:
     ```bash
     ./add_commit_hook.sh
     ```

### Important Notes:
- **Backup Your Repositories**: It's always a good idea to back up your repositories before running scripts that modify them.
- **Adjust Permissions**: Ensure that the script has the appropriate permissions to write to the `.git/hooks` directories.
- **Test the Script**: Consider testing the script in a single repository first to confirm it works as expected.

This script will automate the process of adding the default commit message hook to every Git repository in the specified directory and its subfolders.