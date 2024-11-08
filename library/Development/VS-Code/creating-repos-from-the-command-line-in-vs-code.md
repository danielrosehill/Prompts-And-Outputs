---
title: "Creating repos from the command line in VS Code"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you teach me how to create new repositories in Github entirely from the command line in VS Code?

I'd like to be able to create both public and private repos, so please provide instructions for both

# Output

Certainly! I'll guide you through the process of creating new GitHub repositories entirely from the command line in VS Code, including instructions for both public and private repositories.

## Creating GitHub Repositories from VS Code Command Line

To create GitHub repositories from the VS Code command line, you'll need to use the GitHub CLI (gh) tool. Here's how to set it up and create repositories:

1. Install GitHub CLI:
   If you haven't already, install the GitHub CLI. You can download it from the official GitHub CLI website or use a package manager.

2. Authenticate GitHub CLI:
   Open the VS Code terminal and run:
   ```
   gh auth login
   ```
   Follow the prompts to authenticate with your GitHub account.

3. Create a new repository:
   Navigate to the directory where you want to create the repository, then use the following command:

   For a public repository:
   ```
   gh repo create <repo-name> --public
   ```

   For a private repository:
   ```
   gh repo create <repo-name> --private
   ```

   Replace `<repo-name>` with your desired repository name.

4. Additional options:
   - To add a description: `--description "Your description here"`
   - To add a README file: `--add-readme`
   - To specify a gitignore template: `--gitignore <template-name>`
   - To specify a license: `--license <license-name>`

5. Clone the repository locally:
   After creating the repository, you can clone it to your local machine:
   ```
   gh repo clone <your-username>/<repo-name>
   ```

6. Initialize the local repository:
   If you're starting with local files, navigate to your project directory and run:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   ```

7. Push your code:
   Link your local repository to the remote one and push your code:
   ```
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```

## Examples

Creating a public repository with a README and description:
```
gh repo create my-public-repo --public --add-readme --description "This is my new public repository"
```

Creating a private repository with a specific gitignore template:
```
gh repo create my-private-repo --private --gitignore Node
```

By using these commands, you can create and set up GitHub repositories entirely from the VS Code command line, without needing to use the GitHub website. This method gives you full control over the repository creation process and allows for easy integration into your development workflow[1][3].

 