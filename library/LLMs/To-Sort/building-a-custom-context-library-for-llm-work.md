---
title: "Building a custom context library for LLM work"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
When I prompt LLMs I frequently need to provide the same set of details to provide context.

A good example is the "Output Hub" system  that we're discussing which I'm working on. It's a system for saving prompts and outputs into a knowledge base type tool that humans can then edit and improve upon.

As I'm working with a lot of different LLMs and accessing them via different means, I'm beginning to find that I need some kind of context repository. My idea is that I'll have files with contexts for key projects that I can copy and paste when required into an LLM (as many web UIs allow users to do this).

What do you think of this idea? Are there any frameworks that exist for this purpose already? If not, can you think of how I might best structure and implement my custom contextual library for LLM work?

# Output
The idea of creating a context repository for LLM interactions is excellent and can significantly streamline your workflow. It's particularly useful for complex, ongoing projects like your "Output Hub" system. Here's my analysis of your idea and some suggestions for implementation:

Benefits of a Context Repository:
1. Consistency: Ensures you're providing the same context across different LLM interactions.
2. Efficiency: Saves time by avoiding rewriting or remembering complex context details.
3. Versioning: Allows you to track changes in project context over time.
4. Collaboration: Enables sharing of context with team members or across different devices.

Existing Frameworks:
While there isn't a widely-adopted, standardized framework specifically for managing LLM contexts, some tools and approaches that could be adapted for this purpose include:

1. Prompt Engineering Tools: Some prompt engineering platforms offer features for saving and reusing prompt templates, which could include context.
2. Knowledge Management Tools: Apps like Obsidian or Notion can be used to store and organize context snippets.
3. Version Control Systems: Git can be used to version and manage context files.

Implementing a Custom Contextual Library:
Given your specific needs, a custom solution might be the best approach. Here's a suggested structure and implementation:

1. File Structure:
   ```
   contexts/
   ├── projects/
   │   ├── output_hub.md
   │   ├── project_x.md
   │   └── project_y.md
   ├── domains/
   │   ├── ai_ethics.md
   │   └── software_architecture.md
   └── general/
       ├── personal_background.md
       └── technical_skills.md
   ```

2. File Format:
   Use Markdown (.md) files for easy readability and potential integration with other tools. Structure each file with clear sections:

   ```markdown
   # Project: Output Hub

   ## Overview
   [Brief project description]

   ## Key Components
   - Component 1
   - Component 2

   ## Current Status
   [Current state of the project]

   ## Goals
   [Project objectives]

   ## Technical Details
   [Relevant technical information]
   ```

3. Implementation:
   a. Python Script: Create a simple Python script to manage and access your contexts:

   ```python
   import os
   import pyperclip

   CONTEXTS_DIR = "path/to/contexts"

   def list_contexts():
       for root, dirs, files in os.walk(CONTEXTS_DIR):
           for file in files:
               if file.endswith(".md"):
                   print(os.path.join(root, file))

   def read_context(file_path):
       with open(file_path, 'r') as file:
           return file.read()

   def copy_to_clipboard(content):
       pyperclip.copy(content)
       print("Context copied to clipboard!")

   # Usage
   list_contexts()
   file_path = input("Enter the context file path: ")
   context = read_context(file_path)
   copy_to_clipboard(context)
   ```

   b. GUI Application: For a more user-friendly approach, you could create a simple GUI using PyQt5 (similar to the LLMVaultBackupUtility in your provided code):

   ```python
   import sys
   from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QTextEdit
   from PyQt5.QtCore import Qt
   import os

   class ContextManager(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()

       def initUI(self):
           layout = QVBoxLayout()

           self.context_list = QListWidget()
           self.populate_context_list()
           layout.addWidget(self.context_list)

           self.context_display = QTextEdit()
           self.context_display.setReadOnly(True)
           layout.addWidget(self.context_display)

           copy_button = QPushButton('Copy to Clipboard')
           copy_button.clicked.connect(self.copy_context)
           layout.addWidget(copy_button)

           self.setLayout(layout)
           self.setGeometry(300, 300, 600, 400)
           self.setWindowTitle('Context Manager')

           self.context_list.itemClicked.connect(self.display_context)

       def populate_context_list(self):
           for root, dirs, files in os.walk(CONTEXTS_DIR):
               for file in files:
                   if file.endswith(".md"):
                       self.context_list.addItem(os.path.join(root, file))

       def display_context(self, item):
           with open(item.text(), 'r') as file:
               self.context_display.setText(file.read())

       def copy_context(self):
           QApplication.clipboard().setText(self.context_display.toPlainText())

   if __name__ == '__main__':
       app = QApplication(sys.argv)
       ex = ContextManager()
       ex.show()
       sys.exit(app.exec_())
   ```

This implementation provides a structured way to organize your contexts, makes them easily accessible, and allows for quick copying into LLM interfaces. You can further enhance this system by adding features like context editing, version control integration, or even direct API integration with LLM providers to automatically include relevant context in your prompts.

 




## Extracted Prompts
[[Prompts/Building a custom context library for LLM work.md#Prompt 1|Prompt 1]]
