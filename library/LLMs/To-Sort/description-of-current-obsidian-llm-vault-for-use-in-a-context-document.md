---
title: "Description of current Obsidian LLM vault for use in a context document"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please generate a short document which provides an outline of my Obsidian vault for LLM output managemnt. Note today's date. All paths are relative to the vault base of course

/Agents is a folder for storing configuration parameters for custom LLM agents (e.g. custom GPTs). These are saved in JSON, markdown, or both.

/Context is a context repository storing snippets of contextual information in order to pass these easily into LLM interactions. It's intended to scale up to be a large contextual data store that could be ideally polled by a GUI to combine context snippets from various individual files

/Outputs is a core system module and is used to store the outputs. /Outputs/Raw is where the original outputs are stored and this path is baked into some data entry GUIs I've created. /Outputs/Edited is intended as storage for edited outputs

/Prompts is my prompt library. I have created some automations for automatically extracting prompts from saved outputs. To distinguish between those and the prompts I hand author and engineer, the automatically extracted prompts go to /Prompts/Autocapture

/Templates for templates

/Scripts for scripts

/Reference for refernce data

/Analytics for vualt analytics generated by python scripts

# Output

Here's a short document outlining your Obsidian vault for LLM output management:

# Obsidian Vault Structure for LLM Output Management

**Date: October 3, 2024**

## Folder Structure

### /Agents
- Purpose: Store configuration parameters for custom LLM agents
- File formats: JSON, Markdown, or both

### /Context
- Purpose: Repository for contextual information snippets
- Intended use: Scalable data store for easy integration into LLM interactions
- Potential feature: GUI for combining context snippets from various files

### /Outputs
- Core system module for storing LLM outputs
- Subfolders:
  - **/Outputs/Raw**: Original outputs storage (integrated with data entry GUIs)
  - **/Outputs/Edited**: Storage for edited outputs

### /Prompts
- Purpose: Prompt library
- Subfolders:
  - **/Prompts/Autocapture**: Automatically extracted prompts from saved outputs
- Note: Hand-authored and engineered prompts stored in the main /Prompts directory

### /Templates
- Purpose: Storage for templates

### /Scripts
- Purpose: Storage for scripts

### /Reference
- Purpose: Storage for reference data

### /Analytics
- Purpose: Storage for vault analytics
- Generation method: Python scripts

## Key Features
- Automated prompt extraction from saved outputs
- Custom data entry GUIs integrated with /Outputs/Raw
- Potential for GUI-based context snippet combination

 