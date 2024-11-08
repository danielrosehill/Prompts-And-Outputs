---
title: "Streamline capture into Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Another Obsidian question. I would to create a hotkey that automatically begins a new note in a specific folder prepopulated with the format that I discussed earlier with heads for prompt and output. can you suggest how I could do this?

# Output

To create a hotkey in Obsidian that automatically begins a new note in a specific folder, prepopulated with the format for "Prompt" and "Output," you can use a combination of the **Templater** plugin and Obsidian’s built-in hotkey settings. Here’s how you can set this up:

### Step 1: Install the Templater Plugin
1. **Install Templater:**
   - Open Obsidian.
   - Go to `Settings` > `Community Plugins`.
   - Search for "Templater" and install it.
   - Enable the Templater plugin.

### Step 2: Create a Template for Your New Note
1. **Create a Template:**
   - Go to your designated templates folder in Obsidian (or create a new folder for templates).
   - Create a new markdown file for your template, e.g., `PromptOutputTemplate.md`.
   - Inside this file, add the following content:
     ```markdown
     ## Prompt

     ## Output
     ```
   - Save the template.

2. **Configure Templater:**
   - Go to `Settings` > `Templater`.
   - Set the "Template Folder Location" to the folder where you saved your template.

### Step 3: Set Up the Hotkey for the New Note
1. **Create a New Templater Script for the Note:**
   - Go to `Settings` > `Templater` > `User Scripts`.
   - Click `+` to create a new script.
   - Name it something like `New PromptOutput Note`.
   - Enter the following script:
     ```javascript
     // Templater script to create a new note in a specific folder

     // Define the folder where you want to save the note
     const folder = "Your/Specific/Folder";

     // Generate a unique file name for the note
     const date = tp.date.now("YYYY-MM-DD");
     const fileName = `Note ${date}.md`;

     // Set the file path
     const filePath = `${folder}/${fileName}`;

     // Create a new file in the specific folder using the template
     await tp.file.create_new(tp.file.find_tfile("PromptOutputTemplate"), filePath);
     ```

   - Replace `"Your/Specific/Folder"` with the actual path to the folder where you want to save your new notes.

2. **Assign a Hotkey:**
   - Go to `Settings` > `Hotkeys`.
   - Search for "Run User Script" in the Templater section.
   - Find your script `New PromptOutput Note` and assign it a hotkey, e.g., `Ctrl+N`.

### Step 4: Test the Hotkey
- Press the hotkey (`Ctrl+N` or whatever you set) to create a new note in the specified folder. The note should automatically be created with the "Prompt" and "Output" headings prepopulated.

### Summary
This setup allows you to quickly generate a new note in a specific folder with predefined content using a hotkey. The Templater plugin provides the flexibility to automate note creation in a way that fits your workflow perfectly.## Extracted Prompts
[[Prompts/Autocapture/Streamline capture into Obsidian.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Streamline capture into Obsidian.md#Prompt 1|Prompt 1]]
