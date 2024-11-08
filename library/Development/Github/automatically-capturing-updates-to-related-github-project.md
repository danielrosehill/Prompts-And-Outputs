---
title: "Automatically capturing updates to related Github project"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

What I'd really like to achieve is that whenever I update the prompt saving GUI, the updated repo is automatically pulled into the master repo for the project. Is there any way to do that?

# Output

To automatically update the main repository (Obisidian-For-LLM-Capture) whenever you make changes to the submodule repository (Obsidian-Prompt-Output-Saver), you can set up a GitHub Actions workflow in the submodule repository. This workflow will trigger an update in the main repository whenever changes are pushed to the submodule. Here's how you can achieve this:

1. In the Obsidian-Prompt-Output-Saver repository (submodule), create a new GitHub Actions workflow file:

```yaml
name: Update Parent Repository

on:
  push:
    branches:
      - main  # or your default branch name

jobs:
  update-parent:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger parent repository update
        run: |
          curl -X POST \
          -H "Authorization: token ${{ secrets.PAT }}" \
          -H "Accept: application/vnd.github.v3+json" \
          https://api.github.com/repos/danielrosehill/Obisidian-For-LLM-Capture/dispatches \
          -d '{"event_type": "update_submodule", "client_payload": {"submodule": "Obsidian-Prompt-Output-Saver"}}'
```

2. In the Obisidian-For-LLM-Capture repository (main project), create another workflow file:

```yaml
name: Update Submodule

on:
  repository_dispatch:
    types: [update_submodule]

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
        with:
          token: ${{ secrets.PAT }}
          submodules: recursive
      
      - name: Update submodule
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git submodule update --remote --merge
          git commit -am "Update submodule Obsidian-Prompt-Output-Saver"
          git push
```

3. Create a Personal Access Token (PAT) with repo scope and add it as a secret named `PAT` to both repositories.

This setup will:
1. Trigger an action in the submodule repository whenever you push changes to it.
2. That action will send a repository dispatch event to the main repository.
3. The main repository will then update the submodule reference, commit, and push the changes.

This approach allows you to keep your repositories separate while automating the update process. Remember to adjust the repository names and branch names in the workflow files to match your actual setup.

 




## Extracted Prompts
[[Prompts/Automatically capturing updates to related Github project.md#Prompt 1|Prompt 1]]
