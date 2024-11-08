---
title: "Streamlining new repo creation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

When I start new Github repos, I tend to use the same folder structure over and over again. I would love to automate the creation process a bit. I use Gitkraken for repo mgmt which I generally like. Can you think of any way to speed up the new repo setup?

# Output

Creating a consistent folder structure for new GitHub repositories can indeed be automated to save time and ensure standardization. Here are a few ways you can speed up your new repo setup process, especially when using GitKraken:

## Use GitHub Repository Templates

GitHub offers a feature called repository templates that can significantly speed up your setup process[1]:

1. Create a repository with your desired folder structure and files.
2. Go to the repository settings and check "Template repository".
3. When creating a new repository, you can choose this template as a starting point.

GitKraken supports cloning from GitHub templates, making this process seamless[1].

## Utilize GitKraken's Init Feature

GitKraken's Init feature allows you to create a new repository with some basic structure[3]:

1. Click on "File > Init" or use the Init button in the Repo Management tab.
2. Choose a .gitignore template and a license.
3. GitKraken will create an initial commit with a README.md file.

While this doesn't create your full folder structure, it's a good starting point.

## Create a Script or Use GitHub CLI

You can create a script that sets up your folder structure:

1. Write a script (e.g., in Bash or PowerShell) that creates your desired folders and files.
2. Use GitHub CLI to create a new repository and push the initial structure.
3. Run this script whenever you need a new repository.

## Use GitKraken's Custom Actions

GitKraken allows you to create custom actions, which could potentially be used to automate repository setup[1]. While this feature is primarily for running scripts on existing repositories, you might be able to leverage it for initial setup tasks.

## Consider Using a Project Generator

Tools like Yeoman can generate project structures. While not directly integrated with GitKraken, you could:

1. Use a generator to create your folder structure locally.
2. Initialize a Git repository in that folder.
3. Open the repository in GitKraken.

## Leverage GitKraken's GitHub Integration

GitKraken's deep integration with GitHub can help streamline the process[5]:

1. Use GitKraken to create a new repository on GitHub.
2. Clone it locally.
3. Use GitKraken's file management features to quickly add your standard folders and files.
4. Commit and push these changes.

By combining these methods, you can significantly speed up your repository setup process. For the most seamless experience within GitKraken, using GitHub templates or enhancing GitKraken's Init feature with custom scripts might be your best options.

 