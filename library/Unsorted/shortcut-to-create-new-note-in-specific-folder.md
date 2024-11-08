---
title: "Shortcut to create new note in specific folder"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Great. 90% of the use for my system is going to be saving prompt outputs into a specific folder. Can you think of the best workflow to achieve that? Ideally I'd like to split the prompt and output into separate folders. But as a starter, it would be useful to have something like a hotkey or shortcut that would allow me to create a new note in this specific folder in the vault

# Output
To create an efficient workflow for saving prompt outputs into a specific folder in your Obsidian vault, here’s a setup that should work well for your needs:

### **Step 1: Set Up Your Folder Structure**
   - **Prompts Folder**: Create a folder named `Prompts` in your vault where you will store all your prompt texts.
   - **Outputs Folder**: Create a folder named `Outputs` where you will save the corresponding outputs.

### **Step 2: Use the Templater Plugin**
   - **Install Templater**: Install the Templater plugin from the Obsidian community plugins.
   - **Create Templates**: Set up two templates:
     1. **Prompt Template**: A template for your prompts.
     2. **Output Template**: A template for your outputs, which could include metadata fields like the date, associated prompt ID, etc.

### **Step 3: Set Up QuickAdd Plugin**
   - **Install QuickAdd**: Install the QuickAdd plugin from the Obsidian community plugins.
   - **Create a Macro**: Set up a QuickAdd macro that:
     1. **Creates a New Prompt Note**: Automatically creates a new note in the `Prompts` folder using the Prompt Template.
     2. **Creates a New Output Note**: After the prompt is saved, automatically open a new note in the `Outputs` folder using the Output Template.

### **Step 4: Configure Hotkeys**
   - **Assign a Hotkey**: In Obsidian’s settings, assign a hotkey to trigger your QuickAdd macro. This allows you to quickly create new prompt and output notes with a single keypress.

### **Step 5: Automate Saving Workflow**
   - **QuickAdd Capture Workflow**:
     - **Press the Hotkey**: Press the assigned hotkey to trigger the workflow.
     - **Enter Prompt**: The macro prompts you to enter the prompt text, which is saved in the `Prompts` folder.
     - **Enter Output**: The macro then opens another note for the output, which you can fill out, and it saves to the `Outputs` folder.

### **Step 6: Link Prompts and Outputs (Optional)**
   - **Use Dataview or Links**: To link prompts and outputs, you can include a link to the corresponding prompt in the output note. For example:
     - In the Output Template, include a placeholder like `[[Prompts/{{prompt_title}}]]` to link back to the prompt note.

### **Bonus: Automate with AutoHotkey (if on Windows)**
   - If you’re using Windows, AutoHotkey can create more complex automation, but since you’re on Fedora, the above method using Obsidian plugins is the most native and efficient.

### **Example QuickAdd Workflow Setup**
   - **Macro Steps**:
     1. **New Prompt**: Create a note in the `Prompts` folder with the prompt text.
     2. **New Output**: Open a note in the `Outputs` folder for the output.
     3. **Link Notes**: (Optional) Add a backlink to the prompt in the output note.

This setup should provide a smooth and efficient way to manage your prompts and outputs, keeping them well-organized and easy to navigate. The hotkey-driven workflow will make it quick and easy to save and separate your data as you work.## Extracted Prompts
[[Prompts/Autocapture/Shortcut to create new note in specific folder.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Shortcut to create new note in specific folder.md#Prompt 1|Prompt 1]]
