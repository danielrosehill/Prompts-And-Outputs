---
title: "Using Zenity to build a local app for Output Hub"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
So I Zenity was very good. I know we have explored this before, but would it be possible to build a Linux GUI using a tool like this that interfaced with the remote database in Supabase? In other words, a desktop application rather than a web UI

# Output
import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

# Supabase configuration
SUPABASE_URL = 'https://your-supabase-url.supabase.co'
SUPABASE_KEY = 'your-supabase-anon-key'
SUPABASE_TABLE = 'your-table-name'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GPT Workbench GUI")

        # Create a simple layout
        layout = QVBoxLayout()

        # Example label to display data
        self.label = QLabel("Fetching data...")
        layout.addWidget(self.label)

        # Fetch data from Supabase on startup
        self.fetch_data()

        # Set up the main window
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_data(self):
        # Fetch data from Supabase
        response = requests.get(f'{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}',
                                headers={
                                    'apikey': SUPABASE_KEY,
                                    'Authorization': f'Bearer {SUPABASE_KEY}'
                                })

        if response.status_code == 200:
            data = response.json()
            self.label.setText(f"Data fetched: {data}")
        else:
            self.label.setText(f"Error fetching data: {response.status_code}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())## Extracted Prompts
[[Prompts/Autocapture/Using Zenity to build a local app for Output Hub.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Using Zenity to build a local app for Output Hub.md#Prompt 1|Prompt 1]]
