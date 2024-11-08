---
title: "Configuring a submodule repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm interested in the submodule approach. In the example that I gave, I would like my output saving GUI to be a submodule of the main Obsidian Vault project. How would I set that up?

# Output

To set up your Obsidian-Prompt-Output-Saver as a submodule of your main Obisidian-For-LLM-Capture project, you can follow these steps:

1. First, navigate to your main project directory (Obisidian-For-LLM-Capture) in your terminal:

```bash
cd path/to/Obisidian-For-LLM-Capture
```

2. Add the Obsidian-Prompt-Output-Saver repository as a submodule:

```bash
git submodule add https://github.com/danielrosehill/Obsidian-Prompt-Output-Saver
```

This command will clone the Obsidian-Prompt-Output-Saver repository into a new directory within your main project[2].

3. Commit the changes:

```bash
git add .
git commit -m "Added Obsidian-Prompt-Output-Saver as a submodule"
```

4. Push the changes to your remote repository:

```bash
git push
```

After completing these steps, your Obsidian-Prompt-Output-Saver will be a submodule of the main Obisidian-For-LLM-Capture project[3].

Some important points to remember:

- A new .gitmodules file will be created in your main project, containing the submodule information[3].
- The submodule will point to a specific commit in the Obsidian-Prompt-Output-Saver repository[3].
- When other developers clone your main repository, they'll need to initialize and update the submodule:

```bash
git submodule init
git submodule update
```

Or they can clone the repository with the --recurse-submodules flag:

```bash
git clone --recurse-submodules https://github.com/danielrosehill/Obisidian-For-LLM-Capture
```

This approach allows you to keep the GUI component as a separate repository while still integrating it closely with your main project. It also makes it easier to manage updates and maintain the independence of the two projects[4].

 




## Extracted Prompts
[[Prompts/Configuring a submodule repo.md#Prompt 1|Prompt 1]]
