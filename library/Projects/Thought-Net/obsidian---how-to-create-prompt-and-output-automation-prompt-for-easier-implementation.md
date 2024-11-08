---
title: "Obsidian - how to create prompt and output automation prompt for easier implementation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Could you perhaps teach me how to set up what I think are called user scripts in Obsidian? Alternatively, find a plugin that will allow me to do this. I'll describe the automation I'd like to configure below. Avoid suggesting the Quick Add plugin. Try to find one plugin that can do all of this if possible and try to find whichever approach is the easiest.

Here's my spec:

When I tap a hotkey I can configure (Ctrl + N), I'd like to trigger a modal that pops up with three fields: Title, Prompt, Output. Title is a single line field which will be used for setting the note name, Prompt is a multi line field, Output is a multi line field

I'll enter all 3 text fields and then click 'save'

When I do that the following logic should apply:

The text I entered into the prompt field will be created as a file in /Prompts with the title field as its name. If my title was How Do GPTs work, it would create a file called something like How Do GPTs Work.md in /Prompts

Additionally, a second markdown file gets automatically created in /Outputs/Raw

This file follows a different template that looks like this. Again, the title from the form is used for setting the file name.

# Output

Based on your requirements, I recommend using the Templater plugin for Obsidian. It's a powerful and flexible plugin that can handle custom scripts and automate note creation. Here's how you can set up your desired automation using Templater:

## Setting up Templater

1. Install the Templater plugin from the Community Plugins section in Obsidian settings.
2. Enable the plugin after installation.

## Creating User Scripts

To create the custom modal and handle the note creation, you'll need to set up a user script:

1. In your Obsidian vault, create a folder called `Scripts` (or any name you prefer).
2. In Templater settings, set the "Script files folder" to the folder you just created.
3. Create a new JavaScript file in the Scripts folder, e.g., `createNotes.js`.

## Writing the Script

Here's a script that should accomplish what you're looking for:

```javascript
async function createNotes(tp) {
    // Create modal for user input
    const { title, prompt, output } = await tp.system.prompt(
        "Create Notes",
        "Title,Prompt,Output",
        "split",
        true
    );

    if (!title || !prompt || !output) return;

    // Create prompt file
    const promptFileName = `Prompts/${title}.md`;
    await tp.file.create_new(prompt, promptFileName);

    // Create output file
    const outputFileName = `Outputs/Raw/${title}.md`;
    const outputContent = `# ${title}\n\n## Prompt\n\n${prompt}\n\n## Output\n\n${output}`;
    await tp.file.create_new(outputContent, outputFileName);

    // Open the output file
    const outputFile = tp.file.find_tfile(outputFileName);
    if (outputFile) {
        await tp.file.open(outputFile);
    }
}

module.exports = createNotes;
```

## Setting up the Template

1. Create a new template file, e.g., `CreateNotes.md`.
2. Add the following content to the template:

```
<% await tp.user.createNotes(tp) %>
```

## Configuring the Hotkey

1. Go to Obsidian Settings > Hotkeys.
2. Search for "Templater: Open Insert Template modal".
3. Assign the hotkey Ctrl+N to this command.

## Usage

1. Press Ctrl+N to open the Templater modal.
2. Select your `CreateNotes` template.
3. Fill in the Title, Prompt, and Output fields in the modal that appears.
4. Click "Save" or press Enter.

This setup will create the Prompt file in the `/Prompts` folder and the Output file in the `/Outputs/Raw` folder with the specified structure.

Remember to create the `/Prompts` and `/Outputs/Raw` folders in your vault if they don't already exist.

This solution uses a single plugin (Templater) and provides a relatively simple way to achieve your desired automation. The user script handles the custom modal and file creation logic, while Templater takes care of executing the script and integrating it with Obsidian.

 