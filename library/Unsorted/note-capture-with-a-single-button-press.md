---
title: "Note capture with a single button press"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm using Obsidian to store LLM outputs. I would ideally like to have the ability to press a single button on my keyboard which would:

- Create a new note with a specific template which is saved in Templater

So far I haven't been able to achieve this. I can configure a hotkey to create a new note using a Templater template, but it takes me to a template selection dropdown that I have to pass through

Is it possible to achieve what I want in one single button press?

# Output

To achieve the functionality of creating a new note with a specific template in Obsidian using a single button press, you can utilize the Templater plugin along with some configuration. Here’s how you can set it up:

## Steps to Create a New Note with a Specific Template Using a Single Hotkey

### 1. Install Necessary Plugins

- **Templater**: Ensure that the Templater plugin is installed and enabled in your Obsidian setup. This plugin allows for advanced templating capabilities.
- **QuickAdd** (Optional): This plugin can further automate and streamline the process.

### 2. Configure Templater

- **Template Setup**: Save your desired template in the Templater folder within your Obsidian vault.
- **Assign Hotkey**: In Templater settings, add your specific template to the "Template Hotkeys" section. This creates a command specifically for your template[2].

### 3. Create a Hotkey for Your Template

- Go to Obsidian's settings and navigate to the "Hotkeys" section.
- Search for the command related to your specific template (e.g., "Templater: Create new note from [Your Template Name]").
- Assign a hotkey to this command, ensuring it doesn't conflict with existing shortcuts[5].

### 4. Automate Note Creation

- Use the `tp.file.create_new()` function within Templater to automate the creation of a new note directly from the specified template without additional prompts[2].
  
  Example Templater script:
  ```markdown
  <%*
  const template = tp.file.find_tfile("YourTemplateName");
  await tp.file.create_new(template, "NewNoteName", true);
  %>
  ```

### 5. Use QuickAdd for Enhanced Automation (Optional)

- If using QuickAdd, configure it to create notes in specific folders with predefined templates, further streamlining the process[1][6].

### Conclusion

By following these steps, you can efficiently create new notes using a specific template with just one button press in Obsidian. This setup eliminates the need for manual selection from dropdowns, thereby enhancing your workflow efficiency.
 