---
title: "Running Python scripts within Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I think you said before that there was a way to run python scripts in Obsidian if the scripts were saved within the vault. Could you teach me how to do that please?
# Output


Certainly! You can run Python scripts within Obsidian using the Python Scripter plugin. Here's how to set it up and use it:

## Installation and Setup

1. Open Obsidian and go to Settings > Community plugins.
2. Search for "Python Scripter" and install the plugin.
3. Enable the plugin after installation.

## Configuration

1. Go to the Python Scripter settings.
2. Set the path to your Python scripts folder. By default, it uses a folder within your Obsidian vault: `.obsidian/scripts/python`.
3. Optionally, you can specify the Python executable path if needed.

## Creating and Running Scripts

1. Create a new Python script in the designated folder (e.g., `.obsidian/scripts/python/my_script.py`).
2. Write your Python code in the script file.
3. To run the script:
   - Use the command palette (Ctrl/Cmd + P)
   - Type "Python Scripter: Run"
   - Select your script from the list

## Example Usage

Here's a simple example:

1. Create a file named `hello_world.py` in your scripts folder with this content:

```python
print("Hello from Obsidian!")
```

2. In Obsidian, open the command palette and type "Python Scripter: Run".
3. Select `hello_world.py` from the list.
4. You should see the output "Hello from Obsidian!" in a popup.

## Advanced Features

- You can use "magic commands" in your scripts to access Obsidian-specific information:
  - `@vault_path`: Inserts the vault path
  - `@note_path`: Inserts the current note's path
- For scripts you want to run frequently, you can create a button in your notes:

```markdown
```run-python
print("This script runs directly from the note!")
```

Remember to restart Obsidian after making changes to the plugin settings for them to take effect[1][4].

This setup allows you to leverage Python's power within your Obsidian workflow, enabling you to create custom tools and automations tailored to your note-taking needs.

Citations:
[1] https://forum.obsidian.md/t/runing-a-python-script-with-templater/62282
[2] https://forum.obsidian.md/t/python-scripter-add-your-custom-python-scripts-to-obsidian-as-commands/66010
[3] https://www.youtube.com/watch?v=wdlS9Mif4Vg
[4] https://github.com/twibiral/obsidian-execute-code
[5] https://pypi.org/project/obsidiantools/
[6] https://www.reddit.com/r/ObsidianMD/comments/uv9blx/execute_code_in_your_notes/
[7] https://www.youtube.com/watch?v=gRPBAKiu37Y
[8] https://forum.obsidian.md/t/help-for-a-python-script/68863










## Extracted Prompts
[[Prompts/Running Python scripts within Obsidian.md#Prompt 1|Prompt 1]]
