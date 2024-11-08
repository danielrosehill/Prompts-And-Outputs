---
title: "Creating a GUI to run vault management scripts"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm running a few python scripts manually in order to fix up files in my obsidian vault and generate reports. we talked previously about running them in the background. another idea i had was to create a simple gui for running them. could that be done easily? this is the current content of my scripts folder in the obsidian vault

# Output
Creating a simple GUI to run your Python scripts can definitely make the process more user-friendly, especially if you find yourself running these scripts frequently. There are several ways to create a basic GUI for this purpose. Here are a couple of approaches you could take:

### **1. **Using Tkinter (Built-in Python Library)
   - **Tkinter** is a standard Python library for creating GUIs. It's relatively simple to use and doesn't require any additional installations. You can create buttons for each script and a basic interface to run them.

   **Example Script:**

   ```python
   import tkinter as tk
   import subprocess

   # Function to run a script
   def run_script(script_name):
       subprocess.run(['python3', script_name])

   # Create the main window
   root = tk.Tk()
   root.title("Obsidian Vault Script Runner")

   # Buttons for each script
   btn_vault_report = tk.Button(root, text="Run Vault Report", command=lambda: run_script('vault_report.py'))
   btn_vault_report.pack(pady=10)

   btn_extract_prompts = tk.Button(root, text="Run Extract Prompts", command=lambda: run_script('extract-prompts.py'))
   btn_extract_prompts.pack(pady=10)

   btn_structure_creator = tk.Button(root, text="Run Structure Creator", command=lambda: run_script('structure-creator.py'))
   btn_structure_creator.pack(pady=10)

   # Start the Tkinter loop
   root.mainloop()
   ```

   **How to Use:**
   - Save this script (e.g., `script_runner.py`) in your `Scripts` folder.
   - Run `script_runner.py` to open the GUI window.
   - Click on the buttons to run the corresponding scripts.

### **2. **Using PyQt or PySide (For a More Advanced GUI)
   - **PyQt** and **PySide** are more advanced libraries for building GUIs in Python. They offer more features and allow for more complex interfaces, though they require more setup.

   **Example Basic Setup:**

   ```python
   from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
   import subprocess
   import sys

   class ScriptRunner(QWidget):
       def __init__(self):
           super().__init__()
           self.initUI()

       def initUI(self):
           layout = QVBoxLayout()

           # Buttons
           btn_vault_report = QPushButton('Run Vault Report', self)
           btn_vault_report.clicked.connect(lambda: self.run_script('vault_report.py'))
           layout.addWidget(btn_vault_report)

           btn_extract_prompts = QPushButton('Run Extract Prompts', self)
           btn_extract_prompts.clicked.connect(lambda: self.run_script('extract-prompts.py'))
           layout.addWidget(btn_extract_prompts)

           btn_structure_creator = QPushButton('Run Structure Creator', self)
           btn_structure_creator.clicked.connect(lambda: self.run_script('structure-creator.py'))
           layout.addWidget(btn_structure_creator)

           self.setLayout(layout)
           self.setWindowTitle('Obsidian Vault Script Runner')
           self.show()

       def run_script(self, script_name):
           subprocess.run(['python3', script_name])

   def main():
       app = QApplication(sys.argv)
       ex = ScriptRunner()
       sys.exit(app.exec_())

   if __name__ == '__main__':
       main()
   ```

   **How to Use:**
   - Install PyQt5 with `pip install PyQt5`.
   - Save the script and run it to open the GUI.

### **3. **Automating the GUI Run**
   - **Batch Script or Shortcut**: If you want to simplify running your GUI, you could create a batch script (on Windows) or a shell script (on Linux) to automatically launch the GUI, and then just double-click the script to open the interface.
   - **Startup**: You can also add this GUI to start automatically when your system boots if you’re running it frequently.

### **Conclusion**
Creating a simple GUI using Tkinter or PyQt will make it easier to manage and run your Python scripts without manually executing them each time. Tkinter is the quickest and easiest way to get started, but if you need more advanced features, PyQt or PySide offers more power and flexibility. Both methods will allow you to streamline your workflow, making it more efficient and user-friendly.## Extracted Prompts
[[Prompts/Autocapture/Creating a GUI to run vault management scripts.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Creating a GUI to run vault management scripts.md#Prompt 1|Prompt 1]]
