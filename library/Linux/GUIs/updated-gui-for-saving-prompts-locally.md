---
title: "Updated GUI for saving prompts locally"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

please make one more change. there should be  a "Save Config" button which allows the user to update the prompt and output paths if required. Please make this change and the previous one and regenerate the whole program

# Output

Certainly! I'll incorporate the "Save Config" button along with the previous changes to preserve formatting. Here's the updated and complete Python GUI application with all the requested features:

```python
import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QTextEdit, QPushButton, 
                             QLabel, QFileDialog, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSettings

class ObsidianSaverGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.loadSettings()

    def initUI(self):
        self.setWindowTitle('Obsidian Prompt Saver')
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # Folder configuration
        folder_layout = QHBoxLayout()
        self.prompt_folder = QLineEdit()
        self.output_folder = QLineEdit()
        folder_layout.addWidget(QLabel('Prompts Folder:'))
        folder_layout.addWidget(self.prompt_folder)
        folder_layout.addWidget(QPushButton('Browse', clicked=lambda: self.browse_folder('prompt')))
        folder_layout.addWidget(QLabel('Outputs Folder:'))
        folder_layout.addWidget(self.output_folder)
        folder_layout.addWidget(QPushButton('Browse', clicked=lambda: self.browse_folder('output')))
        main_layout.addLayout(folder_layout)

        # Save Config button
        save_config_button = QPushButton('Save Config')
        save_config_button.clicked.connect(self.save_config)
        main_layout.addWidget(save_config_button)

        # Input fields
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText('Enter title')
        main_layout.addWidget(QLabel('Title:'))
        main_layout.addWidget(self.title_input)

        self.prompt_input = QTextEdit()
        self.prompt_input.setAcceptRichText(True)
        self.prompt_input.setPlaceholderText('Enter prompt')
        main_layout.addWidget(QLabel('Prompt:'))
        main_layout.addWidget(self.prompt_input)

        self.output_input = QTextEdit()
        self.output_input.setAcceptRichText(True)
        self.output_input.setPlaceholderText('Enter output')
        main_layout.addWidget(QLabel('Output:'))
        main_layout.addWidget(self.output_input)

        # Save button
        save_button = QPushButton('Save To Vault')
        save_button.clicked.connect(self.save_to_vault)
        main_layout.addWidget(save_button)

        # Terminal output
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        main_layout.addWidget(QLabel('Status:'))
        main_layout.addWidget(self.terminal_output)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Set styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
            QLineEdit, QTextEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def browse_folder(self, folder_type):
        folder = QFileDialog.getExistingDirectory(self, f"Select {folder_type.capitalize()} Folder")
        if folder:
            if folder_type == 'prompt':
                self.prompt_folder.setText(folder)
            else:
                self.output_folder.setText(folder)

    def save_config(self):
        self.saveSettings()
        self.terminal_output.append("Configuration saved successfully.")

    def save_to_vault(self):
        title = self.title_input.text().strip()
        prompt = self.prompt_input.toPlainText()  # Keep all formatting
        output = self.output_input.toPlainText()  # Keep all formatting

        if not all([title, prompt, output, self.prompt_folder.text(), self.output_folder.text()]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled and folders selected.")
            return

        try:
            # Save prompt file
            prompt_file_path = os.path.join(self.prompt_folder.text(), f"{title}.md")
            with open(prompt_file_path, 'w', encoding='utf-8') as f:
                f.write(prompt)  # Write prompt as-is

            # Save output file
            output_file_path = os.path.join(self.output_folder.text(), f"{title}.md")
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(f"# Prompt\n\n{prompt}\n\n# Output\n\n{output}\n\n")
                f.write(f"[[{os.path.basename(prompt_file_path)}]]")

            # Update prompt file with link to output
            with open(prompt_file_path, 'a', encoding='utf-8') as f:
                f.write(f"\n\n[[{os.path.basename(output_file_path)}]]")

            self.terminal_output.append(f"Successfully saved files for '{title}'")
            self.clear_inputs()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
            self.terminal_output.append(f"Error: {str(e)}")

    def clear_inputs(self):
        self.title_input.clear()
        self.prompt_input.clear()
        self.output_input.clear()

    def loadSettings(self):
        settings = QSettings('ObsidianSaver', 'FolderSettings')
        self.prompt_folder.setText(settings.value('prompt_folder', ''))
        self.output_folder.setText(settings.value('output_folder', ''))

    def saveSettings(self):
        settings = QSettings('ObsidianSaver', 'FolderSettings')
        settings.setValue('prompt_folder', self.prompt_folder.text())
        settings.setValue('output_folder', self.output_folder.text())

def main():
    app = QApplication(sys.argv)
    ex = ObsidianSaverGUI()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
```

This updated version includes the following changes:

1. Added a "Save Config" button that allows users to update the prompt and output paths.
2. Modified the `save_to_vault` function to preserve formatting in both prompt and output.
3. Set `setAcceptRichText(True)` for both prompt and output QTextEdit widgets to handle formatted text properly.

The "Save Config" button calls the `save_config` method, which saves the current folder configurations and displays a success message in the terminal output.

To use this application, you'll need to create a `requirements.txt` file with the following content:

```
PyQt6==6.4.0
```

And here's an updated `README.md` file with setup and usage instructions:

```markdown
# Obsidian Prompt Saver

A Python GUI application for saving prompts and outputs to an Obsidian vault.

## Setup Instructions

1. Ensure you have Python 3.7+ installed on your system.
2. Clone this repository or download the source code.
3. Navigate to the project directory in your terminal.
4. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python obsidian_saver.py
   ```
2. Configure the folders for prompts and outputs by clicking the "Browse" buttons.
3. Click "Save Config" to save the folder configurations.
4. Enter a title, prompt, and output in the respective fields.
5. Click "Save To Vault" to create the markdown files in your Obsidian vault.
6. Check the status pane for success messages or any errors.

## Features

- Separate folders for prompts and outputs
- Automatic creation of bidirectional links between prompt and output files
- Data persistence for folder configurations
- Modern and user-friendly interface
- Input validation and error handling
- Preservation of text formatting in prompts and outputs

## Requirements

- Python 3.7+
- PyQt6

For a complete list of dependencies, see `requirements.txt`.
```

This implementation provides a robust foundation for the Obsidian Prompt Saver application with the requested features and changes. You may want to add more error handling, implement unit tests, and further optimize the code based on your specific needs.

Citations:
[1] https://pplx-res.cloudinary.com/image/upload/v1727636192/user_uploads/fxnjtyfqy/image.jpg

[[Outputs/Updated GUI for saving prompts locally]]