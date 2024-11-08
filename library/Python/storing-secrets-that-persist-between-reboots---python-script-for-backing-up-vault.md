---
title: "Storing secrets that persist between reboots - Python script for backing up vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd like all the parameters to be saved so that the user doesn't have to repeat these between sessions. Maybe dot env doesn't make the most sense. Can you think of the best way to store these variables? The storage should persist between reboots. Please adjust accordingly.
# Output

Based on your requirements, storing the parameters in a configuration file that persists between sessions and reboots would be more appropriate than using environment variables or a .env file. A common and user-friendly approach is to use a JSON file to store these settings. Here's how we can modify the script to implement this:

1. We'll create a `config.json` file to store the user's settings.
2. We'll add methods to read from and write to this file.
3. We'll update the UI to load saved settings and save new settings.

Here's the modified script:

```python
import sys
import os
import tarfile
import json
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit, QLabel, QFileDialog,
                             QTextEdit, QMessageBox)
from PyQt5.QtCore import QThread, pyqtSignal
import b2sdk.v2 as b2

CONFIG_FILE = 'config.json'

class BackupThread(QThread):
    # ... (BackupThread class remains unchanged)

class LLMVaultBackupUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.config = self.load_config()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LLM Vault Backup Utility')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Folder selection
        self.create_folder_input(layout, "Agent Folder:", "agent_folder")
        self.create_folder_input(layout, "Prompt Folder:", "prompt_folder")
        self.create_folder_input(layout, "Output Folder:", "output_folder")
        self.create_folder_input(layout, "Snapshot Folder:", "snapshot_folder")

        # B2 configuration
        self.create_text_input(layout, "B2 Key ID:", "b2_key_id")
        self.create_text_input(layout, "B2 Key Secret:", "b2_key_secret")
        self.create_text_input(layout, "B2 Bucket Name:", "b2_bucket_name")

        # Create snapshot button
        self.create_snapshot_btn = QPushButton('Create Snapshot and Upload to B2')
        self.create_snapshot_btn.clicked.connect(self.create_snapshot)
        layout.addWidget(self.create_snapshot_btn)

        # Terminal output
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        layout.addWidget(QLabel("Process Output:"))
        layout.addWidget(self.terminal_output)

        self.setLayout(layout)

    def create_folder_input(self, layout, label_text, attribute_name):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel(label_text))
        line_edit = QLineEdit(self.config.get(attribute_name, ''))
        setattr(self, attribute_name, line_edit)
        h_layout.addWidget(line_edit)
        browse_btn = QPushButton('Browse')
        browse_btn.clicked.connect(lambda: self.browse_folder(attribute_name))
        h_layout.addWidget(browse_btn)
        layout.addLayout(h_layout)

    def create_text_input(self, layout, label_text, attribute_name):
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel(label_text))
        line_edit = QLineEdit(self.config.get(attribute_name, ''))
        setattr(self, attribute_name, line_edit)
        h_layout.addWidget(line_edit)
        layout.addLayout(h_layout)

    def browse_folder(self, attribute_name):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            getattr(self, attribute_name).setText(folder)
            self.save_config()

    def create_snapshot(self):
        agent_folder = self.agent_folder.text()
        prompt_folder = self.prompt_folder.text()
        output_folder = self.output_folder.text()
        snapshot_folder = self.snapshot_folder.text()
        b2_key_id = self.b2_key_id.text()
        b2_key_secret = self.b2_key_secret.text()
        b2_bucket_name = self.b2_bucket_name.text()

        if not all([agent_folder, prompt_folder, output_folder, snapshot_folder, b2_key_id, b2_key_secret, b2_bucket_name]):
            QMessageBox.warning(self, "Input Error", "All fields must be filled.")
            return

        self.save_config()

        self.backup_thread = BackupThread(agent_folder, prompt_folder, output_folder, snapshot_folder, b2_key_id, b2_key_secret, b2_bucket_name)
        self.backup_thread.update_signal.connect(self.update_terminal)
        self.backup_thread.finished_signal.connect(self.backup_finished)
        self.backup_thread.start()
        self.create_snapshot_btn.setEnabled(False)

    def update_terminal(self, message):
        self.terminal_output.append(message)

    def backup_finished(self, success):
        self.create_snapshot_btn.setEnabled(True)
        if success:
            QMessageBox.information(self, "Success", "Snapshot created and uploaded to B2 successfully!")
        else:
            QMessageBox.critical(self, "Error", "Failed to create snapshot or upload to B2. Check the process output for details.")

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        config = {
            'agent_folder': self.agent_folder.text(),
            'prompt_folder': self.prompt_folder.text(),
            'output_folder': self.output_folder.text(),
            'snapshot_folder': self.snapshot_folder.text(),
            'b2_key_id': self.b2_key_id.text(),
            'b2_key_secret': self.b2_key_secret.text(),
            'b2_bucket_name': self.b2_bucket_name.text()
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LLMVaultBackupUtility()
    ex.show()
    sys.exit(app.exec_())
```

Key changes in this version:

1. We've added a `CONFIG_FILE` constant to specify the name of our configuration file.

2. The `load_config()` method reads the configuration from the JSON file if it exists, or returns an empty dictionary if it doesn't.

3. The `save_config()` method saves the current state of all input fields to the JSON file.

4. In the `__init__` method, we load the configuration before initializing the UI.

5. When creating input fields, we now populate them with values from the loaded configuration.

6. The `browse_folder()` method now calls `save_config()` after updating a folder path.

7. The `create_snapshot()` method calls `save_config()` before starting the backup process.

This approach allows the user's settings to persist between sessions and reboots. The configuration is stored in a `config.json` file in the same directory as the script. This file will be created the first time the user runs the program and saves settings.

Remember to handle the B2 credentials securely. While this method is more convenient for users, it's not the most secure way to store sensitive information like API keys. For a production environment, you might want to consider using a more secure method for storing the B2 credentials.

# Input

The problem is that I want to share this script on Github. If the JSON is generated in the script folder, that will of course be a problem. Can you think of some solution? Perhaps the secrets can be saved in a local file path that is not in the repo?

# Output

You're absolutely right to be concerned about sharing sensitive information on GitHub. Storing secrets in a local file path outside of the repository is an excellent solution to this problem. Here's how we can modify the script to achieve this:

1. Use a configuration file to specify the path to the secrets file.
2. Store the secrets file in a location outside of the repository.
3. Add the configuration file and the secrets file to .gitignore.

Here's a step-by-step implementation:

1. Create a configuration file named `config.json` in your project directory:

```json
{
    "secrets_file_path": "/path/to/your/secrets/secrets.json"
}
```

Replace `/path/to/your/secrets/` with an actual path on your local machine that is outside of the repository.

2. Modify the script to use this configuration:

```python
import json
import os

def load_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def get_secrets():
    config = load_config()
    secrets_path = config['secrets_file_path']
    
    if not os.path.exists(secrets_path):
        raise FileNotFoundError(f"Secrets file not found at {secrets_path}")
    
    with open(secrets_path, 'r') as secrets_file:
        return json.load(secrets_file)

def save_secrets(secrets):
    config = load_config()
    secrets_path = config['secrets_file_path']
    
    os.makedirs(os.path.dirname(secrets_path), exist_ok=True)
    
    with open(secrets_path, 'w') as secrets_file:
        json.dump(secrets, secrets_file, indent=4)

class LLMVaultBackupUtility(QWidget):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.secrets = get_secrets()
        self.initUI()

    # ... (rest of the class implementation)

    def save_config(self):
        config = {
            'agent_folder': self.agent_folder.text(),
            'prompt_folder': self.prompt_folder.text(),
            'output_folder': self.output_folder.text(),
            'snapshot_folder': self.snapshot_folder.text(),
            'b2_key_id': self.b2_key_id.text(),
            'b2_key_secret': self.b2_key_secret.text(),
            'b2_bucket_name': self.b2_bucket_name.text()
        }
        self.secrets.update(config)
        save_secrets(self.secrets)

    def load_config(self):
        return self.secrets

# ... (rest of the script)
```

3. Update your `.gitignore` file to exclude both the configuration and secrets files:

```
config.json
/path/to/your/secrets/secrets.json
```

This approach offers several benefits:

1. The secrets file is stored outside the repository, preventing accidental commits.
2. The configuration file (which doesn't contain sensitive information) can be shared, allowing other developers to set up their own secrets file location.
3. The script remains portable and can be shared safely on GitHub.

When using this script:
1. Each developer would need to create their own `config.json` file pointing to their local secrets file.
2. The `secrets.json` file would be created automatically when the user saves the configuration for the first time.
3. Subsequent runs of the script will load the existing secrets and update them as needed.

This solution keeps your sensitive data secure while allowing the script to be shared and collaborated on through GitHub.

# Input

I'm using Fedora Linux. My home user is /home/user/daniel. But as I'm sharing this on Github, I'd like the program to run on other people's computers too. So let's have the program create something like /home/user/secrets/obsidian-to-b2.json for secret storage. If it doesn't exist, the script should create it

# Output






## Extracted Prompts
[[Prompts/Storing secrets that persist between reboots - Python script for backing up vault.md#Prompt 1|Prompt 1]]
