---
title: "Command for launching Obsidian to a specific vault folder"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You're asking for the command to launch a specific vault in Obsidian, located at `/home/daniel/Vaults/outputhub_vault/Output_Hub`.

You can launch a specific vault in Obsidian using the `obsidian://` URL scheme. To open your vault at `/home/daniel/Vaults/outputhub_vault/Output_Hub`, you would use the following URL format:

```bash
obsidian://open?vault=Output_Hub
```

If you're launching from the command line and want to directly reference the vault's location, you can use the `xdg-open` command to trigger Obsidian with the correct URL scheme:

```bash
xdg-open "obsidian://open?vault=Output_Hub"
```

Alternatively, if you prefer launching directly from the filesystem path, and assuming Obsidian is installed with the command-line option enabled, use:

```bash
obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub
```

This will open **Obsidian** directly into the **Output_Hub** vault. Let me know if this works or if you'd like further adjustments!