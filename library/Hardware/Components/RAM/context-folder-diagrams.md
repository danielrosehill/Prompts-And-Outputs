---
title: "Context folder diagrams"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please create a few drafts of a mermaid diagram to explain the following flow in my Obsidian vault for managing LLM outputs.

The user saves contextual details into a context folder

The context folder and the prompts are sent to an LLM

The LLM returns an output that is captured in the outputs folder

The prompt is automatically copied and saved into the prompts folder

# Output

Certainly! I'll create a few drafts of Mermaid diagrams to explain the flow in your Obsidian vault for managing LLM outputs, including the context folder and LLM interaction. Here are three different approaches:

1. Simple Linear Flow:

```mermaid
graph LR
    A[User] -->|Saves context| B[Context Folder]
    A -->|Creates| C[Prompt]
    B --> D{LLM}
    C --> D
    D -->|Returns| E[Output]
    E -->|Saved to| F[Outputs Folder]
    C -->|Copied to| G[Prompts Folder]
```

2. Detailed Process Flow:

```mermaid
graph TD
    A[User] -->|Saves| B[Context Folder]
    A -->|Creates| C[Prompt]
    B --> D{LLM Process}
    C --> D
    D -->|Generates| E[Output]
    E -->|Saved to| F[Outputs Folder]
    C -->|Automatically copied| G[Prompts Folder]
    subgraph Obsidian Vault
    B
    C
    F
    G
    end
    subgraph External
    D
    end
```

3. Sequence Diagram:

```mermaid
sequenceDiagram
    actor User
    participant CF as Context Folder
    participant P as Prompt
    participant LLM as LLM API
    participant OF as Outputs Folder
    participant PF as Prompts Folder

    User->>CF: Saves contextual details
    User->>P: Creates prompt
    P->>LLM: Sends prompt
    CF->>LLM: Sends context
    LLM->>OF: Returns output
    P->>PF: Automatically copied
    OF->>User: Displays output
```

These diagrams provide different perspectives on the flow of your Obsidian vault management system for LLM outputs, including the context folder and LLM interaction. The first is a simple linear flow, the second provides more detail about the process and the structure of the Obsidian vault, and the third shows the sequence of events. You can choose the one that best represents your system or use them as a starting point for further refinement.

 




## Extracted Prompts
[[Prompts/Context folder diagrams.md#Prompt 1|Prompt 1]]
