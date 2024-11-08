---
title: "Attempt to prompt for generating TUI for entering prompts and outputs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm wondering if you might be able to help me create a terminal application that could run on Fedora Linux. If you can, please generate the full code in one codeblock.

## Instructions

Firstly, the terminal program will need to be able to determine the location of the base of my Obsidian vault. I would ideally like this information to be stored in persistent memory so that I can access the terminal UI between multiple sessions. 

Here's the functionality I'd like to the TUI to have:

## Desired Features: 

The TUI should provide a simple form element allowing text to be entered for three fields: Title, Prompt, Output. 

Title is a single line field which will be used for setting the note name, Prompt is a multi line field, Output is a multi line field. I would be pasting long content pastes in markdown format into both prompt and output.

I'll enter all 3 text fields and then click 'save'

When I do that the following logic should apply:

The text I entered into the prompt field will be created as a file in /Prompts with the title field as its name. I'm providing the path for the prompts folder relative to the base of the Obisidian vault.

If my title was How Do GPTs work, it would create a file called something like How Do GPTs Work.md in /Prompts

Additionally, a second markdown file gets automatically created in /Outputs/Raw. I'm providing the path for the prompts folder relative to the base of the Obisidian vault.

This second markdown file that is generated follows a slightly different template:

-> Its filename remains that of the title set by the user

For its body text, it follows a template like this:

# Prompt

{prompttext}

# Output

{outputtext}

The text the user entered for propmt is {prompttext} and the text the user entered for output is {outputtext}

This TUI is designed to speed up repetitive data entry. so as soon as the form is submitted and the two markdown files are created:

1) A quick success message will display
2) The 3 data entry fields will clear so that the form can be reused

---

# Output

Here's a Python script that creates a terminal application with the functionality you described. This script uses the `urwid` library for the terminal user interface and `appdirs` for managing persistent data storage. The code is designed to run on Fedora Linux and includes all the features you requested.

```python
import urwid
import os
import json
from appdirs import user_data_dir

# Constants
APP_NAME = "ObsidianVaultManager"
APP_AUTHOR = "YourName"

class ObsidianVaultManager:
    def __init__(self):
        self.vault_path = self.load_vault_path()
        self.title = urwid.Edit(("Prompt", "Title: "))
        self.prompt = urwid.Edit(("Prompt", "Prompt:\n"), multiline=True)
        self.output = urwid.Edit(("Prompt", "Output:\n"), multiline=True)
        self.save_button = urwid.Button("Save", on_press=self.save_data)
        self.status_text = urwid.Text("")

        self.main_widget = urwid.Pile([
            urwid.AttrMap(self.title, 'edit'),
            urwid.Divider(),
            urwid.AttrMap(self.prompt, 'edit'),
            urwid.Divider(),
            urwid.AttrMap(self.output, 'edit'),
            urwid.Divider(),
            urwid.AttrMap(self.save_button, 'button'),
            urwid.Divider(),
            self.status_text
        ])

        self.frame = urwid.Frame(urwid.Filler(self.main_widget, valign='top'))
        self.palette = [
            ('edit', 'light gray', 'dark blue'),
            ('button', 'black', 'light gray'),
            ('status', 'yellow', 'dark blue'),
        ]

    def load_vault_path(self):
        data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
        config_file = os.path.join(data_dir, 'config.json')
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                return config.get('vault_path', '')
        else:
            return self.set_vault_path()

    def set_vault_path(self):
        vault_path = input("Enter the base path of your Obsidian vault: ")
        data_dir = user_data_dir(APP_NAME, APP_AUTHOR)
        os.makedirs(data_dir, exist_ok=True)
        config_file = os.path.join(data_dir, 'config.json')
        
        with open(config_file, 'w') as f:
            json.dump({'vault_path': vault_path}, f)
        
        return vault_path

    def save_data(self, button):
        title = self.title.edit_text.strip()
        prompt_text = self.prompt.edit_text.strip()
        output_text = self.output.edit_text.strip()

        if not title or not prompt_text or not output_text:
            self.status_text.set_text(('status', "All fields must be filled"))
            return

        # Save prompt file
        prompt_dir = os.path.join(self.vault_path, "Prompts")
        os.makedirs(prompt_dir, exist_ok=True)
        prompt_file = os.path.join(prompt_dir, f"{title}.md")
        with open(prompt_file, 'w') as f:
            f.write(prompt_text)

        # Save output file
        output_dir = os.path.join(self.vault_path, "Outputs", "Raw")
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{title}.md")
        with open(output_file, 'w') as f:
            f.write(f"# Prompt\n\n{prompt_text}\n\n# Output\n\n{output_text}")

        self.status_text.set_text(('status', "Files saved successfully"))
        self.clear_fields()

    def clear_fields(self):
        self.title.edit_text = ""
        self.prompt.edit_text = ""
        self.output.edit_text = ""

    def run(self):
        loop = urwid.MainLoop(self.frame, self.palette, unhandled_input=self.handle_input)
        loop.run()

    def handle_input(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

if __name__ == "__main__":
    app = ObsidianVaultManager()
    app.run()
```

To use this script, you'll need to install the required libraries. You can do this by running:

```
pip install urwid appdirs
```

This script does the following:

1. It uses `appdirs` to manage persistent storage of the Obsidian vault path.
2. On first run, it will prompt you to enter the base path of your Obsidian vault.
3. It creates a simple TUI with three fields: Title, Prompt, and Output.
4. When you click "Save", it creates two markdown files:
   - One in the `/Prompts` directory with the content of the Prompt field.
   - Another in the `/Outputs/Raw` directory with both Prompt and Output content.
5. After saving, it displays a success message and clears the fields for the next entry.
6. You can exit the application by pressing 'q' or 'Q'.

To run the script, save it as a `.py` file (e.g., `obsidian_vault_manager.py`) and run it from the terminal:

```
python obsidian_vault_manager.py
```

This script should work on Fedora Linux and provide the functionality you described. Remember to adjust the `APP_AUTHOR` constant to your name or organization.