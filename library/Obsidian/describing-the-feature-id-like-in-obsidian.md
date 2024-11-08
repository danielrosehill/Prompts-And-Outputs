---
title: "Describing the feature I'd like in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you attempt to describe the feature that I'm looking for. When I'm navigating through a folder of notes, I'd like to be able to press a button (or use a keyboard shortcut) that will bring me to the "next" note. "Next" in this context would be the next note by creation date, from newest to oldest. 

# Output

It sounds like you're looking for a **sequential navigation feature** that allows you to move through notes in a folder based on their **creation date**, from newest to oldest. The specific feature you're describing would:

1. Allow you to press a **button** or use a **keyboard shortcut** to jump to the next note.
2. The "next" note would be defined by its **creation date**, specifically moving through notes from **newest to oldest**.
3. Ideally, the process would allow you to cycle through the entire folder of notes in a time-ordered fashion.

This type of feature would be especially useful for reviewing notes or going through a backlog in a systematic, chronological way without needing to manually navigate through folders or lists.

### Key characteristics of this feature:
- **One-click/one-shortcut navigation** between notes.
- **Sequential navigation** based on the **creation date** of the notes, specifically from the most recent to the oldest.
- Works within a **specific folder** or set of notes.

### Possible ways to implement it:
- A **keyboard shortcut** that could be pressed repeatedly to move through the next note in the time-ordered sequence.
- A **"Next Note" button** that appears in the UI of the note editor, which will dynamically change based on the creation date of the note you're currently viewing.

Some note editors, like **Zettlr** and **Trilium Notes**, provide hierarchical or structured navigation features but may require customization or plugin use to achieve this specific behavior. **Obsidian**, with its strong plugin ecosystem, could potentially support such a feature with the right customization (e.g., via Templater or Dataview with creation date filters).