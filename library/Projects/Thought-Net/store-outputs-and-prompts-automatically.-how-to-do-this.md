---
title: "Store outputs and prompts automatically. How to do this"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


---
Prompt: "I would like to devise a system for storing prompt outputs in Obsidian (or another note/knowledge manager) which supports the following functionalities: the user fills out an input form with three fields: title, prompt, output. The form parses this information. The prompt is saved into a prompt library folder. The output is saved into a prompt output folder. And the title is used to name the file in the output folder. The output file includes a link to the prompt and vice versa. All these documents are created automatically after the user completes the form. Any tools that could implement this easily?"
---
To implement this system in Obsidian (or another note/knowledge manager), you can leverage a combination of Obsidian plugins and tools that allow for form creation, automation, and linking. Here’s how you can do it:

### 1. **Obsidian with Templater and Dataview Plugins**
   - **Templater Plugin**: This allows you to create templates and automate the creation of notes based on user input.
   - **Dataview Plugin**: This plugin enables the creation of dynamic queries and links between notes, making it easier to manage and link your prompt and output files.

   **Steps:**
   - **Step 1: Create a Form Template with Templater**
     - Design a template with three fields: `title`, `prompt`, and `output`.
     - Use Templater’s prompts to capture user input when creating a new note.
     - Example Templater script:
       ```markdown
       ---
       title: <%* tR = tp.prompt("Title") %>
       prompt: <%* pR = tp.prompt("Enter Prompt") %>
       output: <%* oR = tp.prompt("Enter Output") %>
       ---
       # <%= tR %>

       - **Prompt:** [[Prompts/<%= tR %>]]
       - **Output:** [[Outputs/<%= tR %>]]

       # Prompt
       <%= pR %>

       # Output
       <%= oR %>
       ```

   - **Step 2: Automate File Creation**
     - Create two separate templates for prompts and outputs that automatically create links between each other.
     - When you fill out the form, the output is saved in the `Outputs` folder with the title as the filename.
     - The prompt is saved in the `Prompts` folder, and both notes link to each other.

   - **Step 3: Use Dataview for Organization**
     - Use Dataview queries to generate dynamic lists of prompts and outputs, making it easy to navigate between them.

### 2. **Alternative: Logseq with Custom Templates**
   - **Logseq** is another knowledge manager that could implement this system using custom templates and properties.
   - **Steps:**
     - Create a custom template for prompts and outputs, using Logseq's block properties to link them.
     - Automate the creation of these templates through custom queries or scripts.

### 3. **Alternative: Notion with Database Templates**
   - **Notion** could also implement this system using its database functionality.
   - **Steps:**
     - Set up a database with three fields: `Title`, `Prompt`, and `Output`.
     - Create a template that automatically fills out the `Prompt` and `Output` fields and saves them in their respective folders.
     - Use Notion's linking functionality to connect the prompt to the output and vice versa.

### Tools Summary:
- **Obsidian**: Use Templater and Dataview for maximum customization and automation.
- **Logseq**: Use custom templates and block properties.
- **Notion**: Use database templates and linked databases for an intuitive setup.

These tools will allow you to implement the system you described with varying degrees of automation and flexibility. Obsidian with Templater and Dataview might offer the most customizable and scriptable solution for your needs.