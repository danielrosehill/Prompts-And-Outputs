---
title: "Laying out menu on the left in MK Docs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To configure your MkDocs repository with a left navigation menu and prettified titles:

### Navigation Configuration
1. **Edit `mkdocs.yml`**: 
   Add a `nav` section to define the structure:
   ```yaml
   nav:
     - Home: index.md
     - Guide 1: guide1.md
     - Guide 2: guide2.md
   ```

### Prettifying Titles
2. **Use Markdown Headers**: In your Markdown files, use header syntax to define titles:
   ```markdown
   # Title of Your Page
   ## Subtitle
   ```

This will format the titles nicely when rendered. Make sure to run `mkdocs serve` to preview your changes!