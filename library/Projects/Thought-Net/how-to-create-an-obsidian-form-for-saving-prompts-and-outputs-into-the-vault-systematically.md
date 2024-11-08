---
title: "How to create an Obsidian form for saving prompts and outputs into the vault systematically"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you perhaps teach me how to set up what I think are called user scripts in Obsidian? Alternatively, find a plugin that will allow me to do this.

When I tap a hotkey I can configure (Ctrl + N), I'd like to trigger a modal that pops up with three fields: Title, Prompt, Output. Title is a single line field which will be used for setting the note name, Prompt is a multi line field, Output is a multi line field

I'll enter all 3 text fields and then click 'save'

When I do that the following logic should apply:

The text I entered into the prompt field will be created as a file in /Prompts with the title field as its name. If my title was How Do GPTs work, it would create a file called something like How Do GPTs Work.md in /Prompts

Additionally, a second markdown file gets automatically created in /Outputs/Raw

This file follows a different template that looks like this. Again, the title from the form is used for setting the file name.

# Prompt

{Prompt text}

# Output

{Output text}

In this example, I'm using the placeholder values to specify the fields that were created using the form

Once the two files have been succesfully created, the UI can display a "success" message of some kind. Then the form elements will clear so that the user can use the form again to save a new prompt and output

Could you show me how to achieve this

---
# Output
To achieve the functionality you're looking for, you can use a combination of the Templater plugin and a custom JavaScript for Obsidian (JS) script. Here's a step-by-step guide to set this up:

## Install Required Plugins

1. Install the Templater plugin from the Obsidian Community Plugins.
2. Install the QuickAdd plugin, which will allow you to create custom macros and run JavaScript.

## Set Up Templates

Create two template files in your vault:

1. For the Prompt file (/Prompts/PromptTemplate.md):
```markdown
{{title}}
```

2. For the Output file (/Outputs/Raw/OutputTemplate.md):
```markdown
# Prompt

{{prompt}}

# Output

{{output}}
```

## Create a Custom Script

Create a new JavaScript file in your vault, for example, /Scripts/createPromptOutput.js:

```javascript
module.exports = async (params) => {
    const { quickAddApi: { inputPrompt }, app } = params;

    // Get user input
    const title = await inputPrompt("Enter title");
    const prompt = await inputPrompt("Enter prompt", "multi-line");
    const output = await inputPrompt("Enter output", "multi-line");

    // Create Prompt file
    const promptFile = app.vault.getAbstractFileByPath(`Prompts/${title}.md`);
    if (!promptFile) {
        await app.vault.create(`Prompts/${title}.md`, prompt);
    } else {
        new Notice("Prompt file already exists!");
        return;
    }

    // Create Output file
    const outputFile = app.vault.getAbstractFileByPath(`Outputs/Raw/${title}.md`);
    if (!outputFile) {
        const outputContent = `# Prompt\n\n${prompt}\n\n# Output\n\n${output}`;
        await app.vault.create(`Outputs/Raw/${title}.md`, outputContent);
    } else {
        new Notice("Output file already exists!");
        return;
    }

    new Notice("Prompt and Output files created successfully!");
};
```

## Set Up QuickAdd Macro

1. Open QuickAdd settings.
2. Create a new Macro (e.g., "Create Prompt and Output").
3. Add a "User Script" action to the macro and select your createPromptOutput.js script.
4. Set up a hotkey for this macro (e.g., Ctrl+N) in Obsidian's Hotkeys settings.

## Usage

Now, when you press Ctrl+N:

1. A modal will appear asking for the title, prompt, and output.
2. After entering the information and confirming, two files will be created:
   - A prompt file in /Prompts with the title as its name and content.
   - An output file in /Outputs/Raw with the title as its name and the specified template structure.
3. A success message will be displayed.

This setup provides a streamlined way to create prompt and output files with a single hotkey press, meeting your requirements. The script handles file creation, content population, and success notification[1][2][3].

 