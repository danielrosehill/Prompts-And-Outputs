---
title: "Automating new private repo creation in VS Code"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

My question is whether this awkward process could be chained into an automation. I would like to simplify this to:

-> I'd like to create a new repo
-> Let's give the new folder this name and store it here
-> Now's let's initiate the remote and link the project

Can all/any of this be chained/automated as I've described

# Output

Yes, it's definitely possible to automate the process of creating a new GitHub repository and setting it up locally using VS Code. Here's how you can streamline the workflow you've described:

## Automating GitHub Repository Creation in VS Code

### Step 1: Create a Custom VS Code Task

1. Open your VS Code workspace or folder.
2. Create a `.vscode` folder if it doesn't exist.
3. Inside the `.vscode` folder, create a `tasks.json` file.
4. Add the following task configuration:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Create GitHub Repo and Initialize",
      "type": "shell",
      "command": "${command:workbench.action.terminal.new}",
      "args": [
        "${command:workbench.action.terminal.sendSequence}",
        {
          "text": "#!/bin/bash\n\necho 'Enter new repo name:'\nread REPO_NAME\n\necho 'Enter local folder path:'\nread FOLDER_PATH\n\nmkdir -p \"$FOLDER_PATH/$REPO_NAME\"\ncd \"$FOLDER_PATH/$REPO_NAME\"\n\ngit init\n\ngh repo create \"$REPO_NAME\" --public --source=. --remote=origin\n\necho 'Repository created and initialized!'\n"
        }
      ]
    }
  ]
}
```

### Step 2: Install GitHub CLI

If you haven't already, install GitHub CLI (`gh`) on your system. You can find installation instructions at https://cli.github.com/

### Step 3: Authenticate GitHub CLI

Run `gh auth login` in your terminal and follow the prompts to authenticate with your GitHub account.

### Step 4: Run the Automated Task

1. Open the Command Palette in VS Code (Ctrl+Shift+P or Cmd+Shift+P on Mac).
2. Type "Tasks: Run Task" and select it.
3. Choose the "Create GitHub Repo and Initialize" task.

This task will:
- Prompt you for a new repository name
- Ask for the local folder path where you want to create the project
- Create the folder and initialize a Git repository
- Create a new GitHub repository with the same name
- Link the local repository to the remote GitHub repository

## Additional Customization

You can further customize this task to:
- Set default values for the repository name or folder path
- Add initial files like README.md or .gitignore
- Configure repository settings (e.g., private/public)
- Add collaborators or set up branch protection rules

By using this method, you've effectively chained the process into a single automated task, simplifying the creation of new GitHub repositories directly from VS Code[1][3][5].
 