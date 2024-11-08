---
title: "How would you define the current storage format programatically"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

If you were to define the current format I'm storing these templates in, how would you do so? The file name is a title describing the knowledge gleaned in the session

# Output

Based on the provided details, here’s a definition of the format you’re currently using to store these templates in Obsidian:

### Structure Definition

1. **File Name as Title**:
   - The file name itself acts as the **primary title**, summarizing the knowledge or topic covered in the session. This title is often descriptive and unique, indicating the purpose or insight gained.

2. **Markdown Document Content**:
   - **Prompt Section**: 
     - The document starts with a **prompt** that outlines the question, directive, or problem that initiated the session.
     - The prompt is typically written as free text and might not have a distinct section header, though it could begin with phrases like “Let’s think about…” or “Explore…”

   - **Output Section**:
     - Following the prompt, the **output** is structured into several sections, often with **section headers** prefixed by “##” (Markdown syntax for headers).
     - Each section header (e.g., “Step 1: Install Neo4j on Ubuntu”) marks a sub-topic or step within the output. 
     - The content under each header provides detailed explanations, steps, or information relevant to the section’s topic.
     - There’s typically a logical progression from one section to the next, representing an organized answer or guide in response to the initial prompt.

3. **Metadata (Implied)**:
   - Though not explicitly stated, **metadata** might include:
     - **Creation Date**: Implicit in the file’s metadata or file system.
     - **Tags**: Likely applied within Obsidian as part of your organization but not present directly in the Markdown file.
   - These metadata elements are useful for sorting and filtering when analyzing or querying the files programmatically.

### Example Structure Summary

1. **File Name**: Descriptive title summarizing the knowledge topic.
2. **Markdown Content**:
   - **Prompt**: Initial question or directive.
   - **Output**:
     - **Section 1**: Sub-header with content.
     - **Section 2**: Sub-header with content.
     - Additional sections as needed, each addressing a specific aspect or step.

### Suggested Formal Name for Format
You might call this format **“Markdown Prompt-Output Template”**, with the following key components:
   - **Title**: File name as a descriptive title.
   - **Prompt**: Opening statement or query.
   - **Output Sections**: Header-separated sections with structured information in response to the prompt.

This format captures both the purpose of each document (knowledge retention and structured exploration) and makes it ready for potential data extraction, analysis, and transformation into a database-friendly format.