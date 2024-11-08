---
title: "Creating links between associated Github repositories"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have a number of Github repositories that are related to one another.

For example, here's a repository that shares a GUI I created for saving prompts and outputs into my Obsidian vault for managing LLM outputs:

https://github.com/danielrosehill/Obsidian-Prompt-Output-Saver?tab=readme-ov-file

That's related to this repository which talks about the overall system:

https://github.com/danielrosehill/Obisidian-For-LLM-Capture

I prefer to create separate repos for the different parts of the system so I can work on the components independently

But perhaps you can think of ways that I can reflect the links in the repos themselves?


# Output

To reflect the relationships between your related GitHub repositories, you can implement several strategies that will help users understand the connections and navigate between the projects. Here are some effective methods:

## Cross-Repository References

In each repository's README file, you can create a section that lists related repositories[1]. For example:

**Related Repositories:**
- [Obsidian-Prompt-Output-Saver](https://github.com/danielrosehill/Obsidian-Prompt-Output-Saver): GUI for saving prompts and outputs into Obsidian vault
- [Obisidian-For-LLM-Capture](https://github.com/danielrosehill/Obisidian-For-LLM-Capture): Overview of the LLM output management system

This approach allows visitors to quickly understand the ecosystem of your projects and navigate to related repositories.

## GitHub Topics

Use consistent GitHub topics across your related repositories[3]. This helps in grouping and discovering related projects. For example, you could add topics like:
- obsidian-llm-management
- llm-output-capture
- obsidian-integration

## Project Documentation

Create a comprehensive project documentation that outlines the overall system architecture and how different repositories fit together[3]. You can host this documentation in one of the repositories or use GitHub Pages to create a dedicated website for the project.

## Use of Git Submodules

If there are components that are shared between repositories, you can use Git submodules to link them[2]. This allows you to include one repository as a subdirectory of another, which can be useful for shared libraries or common configurations.

## GitHub Issues and Pull Requests

When working on features that span multiple repositories, you can reference issues and pull requests across repositories using the `owner/repo#issue_number` syntax in comments[2]. For example: `danielrosehill/Obsidian-Prompt-Output-Saver#42`.

## Project Boards

Create a GitHub Project board that spans multiple repositories[4]. This can give you a high-level view of tasks and issues across your entire system, helping to manage the development process holistically.

## Consistent Naming and Branding

Use consistent naming conventions and branding across your repositories. This helps users identify that the repositories are part of the same project ecosystem[3].

By implementing these strategies, you can effectively communicate the relationships between your repositories while maintaining the flexibility to work on components independently. This approach will make it easier for users and contributors to understand and navigate your project ecosystem.

 




## Extracted Prompts
[[Prompts/Creating links between associated Github repositories.md#Prompt 1|Prompt 1]]
