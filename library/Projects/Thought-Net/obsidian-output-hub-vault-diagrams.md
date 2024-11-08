---
title: "Obsidian output hub vault diagrams"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please create some mermaid diagrams that might help to explain how I'm using an Obsidian vault to store and manage LLM outputs. There are three core folders: agents, outputs, prompts When outputs are saved, the prompts are extracted and copied into the prompt library by a Python script Links are created between prompts and outputs The whole vault is synced to B2 object storage in the cloud

# Output

Certainly! I'll create some Mermaid diagrams to help explain how you're using an Obsidian vault to store and manage LLM outputs, based on the information you've provided. Here are the diagrams:

1. Obsidian Vault Structure:

```mermaid
graph TD
    A[Obsidian Vault] --> B[Agents Folder]
    A --> C[Outputs Folder]
    A --> D[Prompts Folder]
    C --> E[Output Files]
    D --> F[Prompt Files]
    E -.-> |Links| F
```

This diagram shows the basic structure of your Obsidian vault with the three core folders and the links between outputs and prompts.

2. Output Processing Workflow:

```mermaid
graph LR
    A[New Output] --> B[Save to Outputs Folder]
    B --> C{Python Script}
    C --> D[Extract Prompt]
    D --> E[Copy to Prompts Folder]
    C --> F[Create Link]
    F --> G[Link Output to Prompt]
```

This diagram illustrates the process of saving a new output, extracting the prompt, and creating links between them.

3. Sync Process with B2:

```mermaid
graph TD
    A[Obsidian Vault] --> B{Sync Process}
    B --> C[Agents Folder]
    B --> D[Outputs Folder]
    B --> E[Prompts Folder]
    C --> F[B2 Object Storage]
    D --> F
    E --> F
    F --> G[Cloud Backup]
```

This diagram shows how the entire vault is synced to B2 object storage in the cloud.

4. Overall System Flow:

```mermaid
sequenceDiagram
    participant User
    participant ObsidianVault
    participant PythonScript
    participant B2Storage

    User->>ObsidianVault: Save new output
    ObsidianVault->>PythonScript: Trigger processing
    PythonScript->>ObsidianVault: Extract and save prompt
    PythonScript->>ObsidianVault: Create links
    ObsidianVault->>B2Storage: Sync vault contents
    B2Storage-->>User: Provide cloud backup
```

This sequence diagram shows the overall flow of the system, from saving a new output to syncing with B2 storage.

These diagrams provide a visual representation of how your Obsidian vault is structured and used to manage LLM outputs, including the process of extracting prompts, creating links, and syncing to B2 object storage.
 




## Extracted Prompts
[[Prompts/Obsidian output hub vault diagrams.md#Prompt 1|Prompt 1]]
