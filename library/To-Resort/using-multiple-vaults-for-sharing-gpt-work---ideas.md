---
title: "Using multiple vaults for sharing GPT work - ideas"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you suggest some ways I could link multiple Obsidian vaults together? Here's an example: I have an Obsidian vault that captures all my work with ChatGPT. I have folders for prompts, outputs, and more. I've created another vault to push to Github to share my prompt library. I would like to share my prompts folder there but I don't want to have to administer separate vaults all the time. I'd like to copy my prompts from this vault to the other (and then prune a few and then share publicly). Any suggestions?

# Output

Here are some ways to link multiple Obsidian vaults together while syncing or sharing content like your **prompts folder** between them:

### 1. **Symlinks (Symbolic Links)**
   - **Create symlinks** from the prompts folder in your main vault (ChatGPT prompts) to the other vault. This way, you can maintain one folder and the changes will automatically reflect in both vaults.
   - On Mac/Linux: `ln -s /path/to/folder /path/to/other/vault`
   - On Windows: Use the `mklink /D` command.

### 2. **Obsidian Sync or Git**
   - Use **Obsidian Sync** for syncing specific folders between multiple vaults.
   - If you prefer Git, **create a separate branch** in your main vault for sharing public prompts. Push that branch to GitHub without pushing the entire vault.

### 3. **Third-Party Sync Solutions**
   - Use a sync tool like **Syncthing** or **Dropbox** to sync your prompts folder between multiple vaults.
   - These tools allow you to select specific folders to sync across different devices or vaults without needing to manage the entire vault.

### 4. **Folder Duplication with Automation**
   - Use a tool like **rsync** (for Mac/Linux) or **robocopy** (Windows) to automate copying your prompts folder from the main vault to the GitHub vault. Set up scheduled tasks to keep the folders updated.

### 5. **Obsidian Workspaces Plugin**
   - Utilize Obsidian's **Workspaces plugin** to switch between different setups within a single vault, allowing easy toggling between your full prompt library and a trimmed-down version for public sharing.

These methods allow you to maintain a single workflow while seamlessly managing your prompt folder between multiple vaults.