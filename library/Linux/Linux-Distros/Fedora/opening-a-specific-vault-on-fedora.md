---
title: "Opening a specific vault on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

whats the command using a linux computer to open obsidian with a specific vault?
I'm on fedora and my vault is at:
/home/daniel/Vaults/outputhub_vault/Output_Hub

# Output

To open Obsidian with a specific vault from the command line on your Fedora system, you can use the following command:

```bash
obsidian --vault /home/daniel/Vaults/outputhub_vault/Output_Hub
```

This will directly open Obsidian with your specified vault. If this doesn't work, try using the full path to the Obsidian executable, depending on how it was installed, like this:

```bash
/path/to/obsidian --vault /home/daniel/Vaults/outputhub_vault/Output_Hub
```
 