---
title: "Python GUI for saving prompts and sending them through LLM API"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here's another idea.

Could you generate a Python GUI.

Here are the functions I would like incorporated.

The user can enter the text of a prompt. This should be a multi line field
The user can enter the title of the prompt. this should be a single line field.

The user can configure two folders:

The first folder is where the prompts will be stored.
The second folder is where the outputs will be stored. 

The user can also enter their OpenAI API key.

The GUI should have the ability to retain these settings between sessions. So these variables can be written to a memory file. 

The functionality of the GUI should be as follows

The user enters a prompt text. And when ready to execute it, he clicks a button that says Run Prompt

There is a terminal output display field in the UI where the user can monitor the progress of the jobs which the GUI runs.

When the user executes the prompt, it gets sent to the OpenAI API via its API.

When the API returns with an output, the output should be written to the outputs folder. the file name should be the title that the user entered with hyphens replacing spaces

the prompt should be written to the prompts folder with the same file name

when this process completes successfully the terminal output pane should provide a success message and then the output should clear

after the user sends a prompt for execution, the prompt pane should clear so that the user can use it again to send a new prompt

# Output

Certainly! I can help you create a Python GUI with the functionality you described. Here's a script that implements the features you requested using tkinter for the GUI and the OpenAI API for sending prompts:

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import openai

class PromptGUI:
    def __init__(self, master):
        self.master = master
        master.title("Prompt Executor")
        master.geometry("800x600")

        self.load_settings()

        # Prompt Title
        tk.Label(master, text="Prompt Title:").pack(pady=5)
        self.title_entry = tk.Entry(master, width=50)
        self.title_entry.pack()

        # Prompt Text
        tk.Label(master, text="Prompt Text:").pack(pady=5)
        self.prompt_text = tk.Text(master, height=10, width=60)
        self.prompt_text.pack()

        # Folders
        tk.Button(master, text="Set Prompts Folder", command=self.set_prompts_folder).pack(pady=5)
        tk.Button(master, text="Set Outputs Folder", command=self.set_outputs_folder).pack(pady=5)

        # API Key
        tk.Label(master, text="OpenAI API Key:").pack(pady=5)
        self.api_key_entry = tk.Entry(master, width=50, show="*")
        self.api_key_entry.pack()

        # Run Button
        tk.Button(master, text="Run Prompt", command=self.run_prompt).pack(pady=10)

        # Terminal Output
        tk.Label(master, text="Terminal Output:").pack(pady=5)
        self.terminal_output = tk.Text(master, height=10, width=60, state='disabled')
        self.terminal_output.pack()

        self.load_saved_settings()

    def load_settings(self):
        self.settings = {
            "prompts_folder": "",
            "outputs_folder": "",
            "api_key": ""
        }

    def save_settings(self):
        with open("settings.json", "w") as f:
            json.dump(self.settings, f)

    def load_saved_settings(self):
        try:
            with open("settings.json", "r") as f:
                self.settings = json.load(f)
            self.api_key_entry.insert(0, self.settings["api_key"])
        except FileNotFoundError:
            pass

    def set_prompts_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.settings["prompts_folder"] = folder
            self.save_settings()

    def set_outputs_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.settings["outputs_folder"] = folder
            self.save_settings()

    def run_prompt(self):
        title = self.title_entry.get()
        prompt = self.prompt_text.get("1.0", tk.END).strip()
        api_key = self.api_key_entry.get()

        if not title or not prompt or not api_key:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        self.settings["api_key"] = api_key
        self.save_settings()

        self.update_terminal("Sending prompt to OpenAI API...")

        try:
            openai.api_key = api_key
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content

            filename = title.replace(" ", "-") + ".txt"
            
            with open(os.path.join(self.settings["prompts_folder"], filename), "w") as f:
                f.write(prompt)
            
            with open(os.path.join(self.settings["outputs_folder"], filename), "w") as f:
                f.write(output)

            self.update_terminal("Prompt executed successfully!")
            self.clear_fields()
        except Exception as e:
            self.update_terminal(f"Error: {str(e)}")

    def update_terminal(self, message):
        self.terminal_output.config(state='normal')
        self.terminal_output.insert(tk.END, message + "\n")
        self.terminal_output.config(state='disabled')
        self.terminal_output.see(tk.END)

    def clear_fields(self):
        self.title_entry.delete(0, tk.END)
        self.prompt_text.delete("1.0", tk.END)

root = tk.Tk()
gui = PromptGUI(root)
root.mainloop()
```

This script creates a GUI with the following features:

1. A single-line entry field for the prompt title
2. A multi-line text field for the prompt text
3. Buttons to set the prompts and outputs folders
4. An entry field for the OpenAI API key (masked for security)
5. A "Run Prompt" button to execute the prompt
6. A terminal output display field to show progress and results

The script also implements:

- Saving and loading settings (folders and API key) between sessions using a JSON file
- Sending the prompt to the OpenAI API
- Writing the prompt and output to their respective folders
- Clearing the prompt fields after successful execution
- Displaying success messages and errors in the terminal output

To use this script:

1. Make sure you have the `openai` library installed (`pip install openai`)
2. Replace `"gpt-3.5-turbo"` with the specific model you want to use if needed
3. Run the script, and the GUI will appear
4. Set your folders and API key
5. Enter a prompt title and text, then click "Run Prompt"

The script will save your settings (except the prompt itself) between sessions, so you won't need to re-enter them every time you run the application.

 




## Extracted Prompts
[[Prompts/Python GUI for saving prompts and sending them through LLM API.md#Prompt 1|Prompt 1]]
