---
title: "Model prompt collection device Google Drive implementation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please create a how to guide explaining how to set up a very simple model GUI for storing and saving prompt outputs. 

The user would set up a repository with folders called Agents, Prompts and Outputs. 

In the Prompts folder would be two subfolders called Drafting and Run

As soon as a prompt moved from the Drafting to the Run folder, a script would trigger using the Anthropic API to run the prompt. 

The output from that prompt run would be collected in Outputs and the filename would be the same as that of the prompt.

So long as the program is open, the script would sync every 15 minutes with a Google Drive folder.

Agents would sync with /Angents in the remote
Prompts/Run would sync with /Prompts in the remote and 
/Outputs would sync with /Outputs

# Output

Here's a how-to guide for setting up a simple GUI model for storing and saving prompt outputs with the features you've described:

## How to Set Up a Simple GUI for Managing Prompts and Outputs

### Step 1: Set Up the Repository Structure

1. Create a main folder for your project, e.g., "PromptManager"
2. Inside the main folder, create three subfolders:
   - "Agents"
   - "Prompts"
   - "Outputs"
3. Inside the "Prompts" folder, create two more subfolders:
   - "Drafting"
   - "Run"

Your folder structure should look like this:

```
PromptManager/
├── Agents/
├── Prompts/
│   ├── Drafting/
│   └── Run/
└── Outputs/
```

### Step 2: Install Required Libraries

Install the necessary Python libraries by running the following command in your terminal:

```bash
pip install PyQt5 watchdog anthropic google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Step 3: Set Up Google Drive API

1. Go to the Google Cloud Console (https://console.cloud.google.com/)
2. Create a new project
3. Enable the Google Drive API for your project
4. Create credentials (OAuth 2.0 Client ID) for a desktop application
5. Download the client configuration file and rename it to `credentials.json`
6. Place the `credentials.json` file in your project's root directory

### Step 4: Create the GUI Application

Create a new Python file called `prompt_manager.py` in your main project folder and add the following code:

```python
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileSystemModel, QTreeView, QLabel
from PyQt5.QtCore import QDir, QTimer
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import anthropic
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import time

SCOPES = ['https://www.googleapis.com/auth/drive.file']

class PromptManager(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_file_watcher()
        self.setup_sync_timer()
        self.drive_service = self.get_drive_service()

    def initUI(self):
        layout = QVBoxLayout()

        # File system model and view
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.currentPath()))
        layout.addWidget(self.tree)

        # Output display
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_display)

        self.setLayout(layout)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Prompt Manager')
        self.show()

    def setup_file_watcher(self):
        self.observer = Observer()
        event_handler = PromptHandler(self)
        self.observer.schedule(event_handler, os.path.join(QDir.currentPath(), "Prompts", "Run"), recursive=False)
        self.observer.start()

    def setup_sync_timer(self):
        self.sync_timer = QTimer(self)
        self.sync_timer.timeout.connect(self.sync_with_google_drive)
        self.sync_timer.start(15 * 60 * 1000)  # 15 minutes in milliseconds

    def get_drive_service(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return build('drive', 'v3', credentials=creds)

    def run_prompt(self, prompt_file):
        with open(prompt_file, 'r') as file:
            prompt_content = file.read()

        client = anthropic.Client(os.environ["ANTHROPIC_API_KEY"])
        response = client.completion(
            prompt=f"Human: {prompt_content}\n\nAssistant:",
            model="claude-v1",
            max_tokens_to_sample=300,
        )

        output_file = os.path.join(QDir.currentPath(), "Outputs", os.path.basename(prompt_file))
        with open(output_file, 'w') as file:
            file.write(response.completion)

        self.output_display.setText(response.completion)

    def sync_with_google_drive(self):
        try:
            self.sync_folder("Agents", "Agents")
            self.sync_folder("Prompts/Run", "Prompts")
            self.sync_folder("Outputs", "Outputs")
            self.output_display.append("Synced with Google Drive successfully.")
        except Exception as e:
            self.output_display.append(f"Error syncing with Google Drive: {str(e)}")

    def sync_folder(self, local_folder, remote_folder):
        local_path = os.path.join(QDir.currentPath(), local_folder)
        for root, dirs, files in os.walk(local_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_file_path, local_path)
                remote_file_path = os.path.join(remote_folder, relative_path)
                self.upload_file(local_file_path, remote_file_path)

    def upload_file(self, local_file_path, remote_file_path):
        file_metadata = {'name': os.path.basename(remote_file_path), 'parents': [self.get_or_create_folder(os.path.dirname(remote_file_path))]}
        media = MediaFileUpload(local_file_path, resumable=True)
        self.drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    def get_or_create_folder(self, folder_path):
        folders = folder_path.split('/')
        parent_id = 'root'
        for folder in folders:
            query = f"name='{folder}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
            results = self.drive_service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
            if not results['files']:
                file_metadata = {
                    'name': folder,
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [parent_id]
                }
                folder = self.drive_service.files().create(body=file_metadata, fields='id').execute()
                parent_id = folder.get('id')
            else:
                parent_id = results['files'][0]['id']
        return parent_id

class PromptHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_created(self, event):
        if not event.is_directory:
            self.app.run_prompt(event.src_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PromptManager()
    sys.exit(app.exec_())
```

### Step 5: Set Up the Anthropic API Key

Before running the application, make sure to set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Anthropic API key.

### Step 6: Run the Application

Run the application by executing the following command in your terminal:

```bash
python prompt_manager.py
```

## How to Use the Prompt Manager

1. **First-time setup**: When you run the application for the first time, it will open a browser window for you to authenticate with your Google account. Follow the prompts to grant the necessary permissions.

2. **Create a new prompt**: Create a new text file in the "Prompts/Drafting" folder with your desired prompt content.

3. **Move prompt to Run folder**: When you're ready to run the prompt, simply move the file from the "Drafting" folder to the "Run" folder.

4. **Automatic prompt execution**: The application will automatically detect the new file in the "Run" folder and execute the prompt using the Anthropic API.

5. **View output**: The output from the prompt will be displayed in the GUI's output text area and saved in the "Outputs" folder with the same filename as the prompt.

6. **Automatic Google Drive sync**: The application will automatically sync the following folders with Google Drive every 15 minutes while the program is running:
   - "Agents" folder syncs with "/Agents" in Google Drive
   - "Prompts/Run" folder syncs with "/Prompts" in Google Drive
   - "Outputs" folder syncs with "/Outputs" in Google Drive

7. **Manage files**: Use the file tree view in the GUI to easily navigate and manage your agents, prompts, and outputs.

This application provides a basic framework for managing prompts and outputs, with automatic execution of prompts moved to the "Run" folder and periodic syncing with Google Drive. You can further enhance it by adding features like editing prompts directly in the GUI, displaying file contents, or implementing more advanced prompt processing options.
 




## Extracted Prompts
[[Prompts/Model prompt collection device Google Drive implementation.md#Prompt 1|Prompt 1]]
