---
title: "Build a custom LLM access app"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use Fedora Linux as my desktop OS. There's a custom desktop GUI that I'd really like to build. Its purpose would be to group together some great online LLMs that I use all the time. So rather than having to visit the sites one by one, I could open up a window and access them side by side. I'd like this app to be either a quadrant /grid design. Or perhaps a sidebar and panel design. Can you think of how I might best implement this?

# Output

Creating a custom desktop application to group together online LLMs (Large Language Models) is an excellent idea for improving your workflow. Given your use of Fedora Linux, there are several approaches you could take to implement this. I'll outline two potential designs and suggest implementation methods.

## Design Options

### 1. Quadrant/Grid Design

This design would divide the application window into four equal sections, each containing a different LLM interface.

**Pros:**
- Equal space for each LLM
- Easy to compare outputs side-by-side
- Clean, symmetrical layout

**Cons:**
- Limited to four LLMs (unless you implement tabs or scrolling)
- May feel cramped on smaller screens

### 2. Sidebar and Panel Design

This design would feature a sidebar with a list of available LLMs, and a main panel that displays the selected LLM interface.

**Pros:**
- Can accommodate more LLMs in the sidebar
- Larger workspace for the active LLM
- Easy to switch between LLMs

**Cons:**
- Only one LLM visible at a time
- Requires more user interaction to compare outputs

## Implementation Methods

### 1. Electron Application

Electron is a framework for creating native applications with web technologies.

**Advantages:**
- Cross-platform compatibility
- Familiar web technologies (HTML, CSS, JavaScript)
- Easy to embed web content

**Implementation steps:**
1. Set up an Electron project
2. Create a main window with either a grid layout or sidebar/panel layout using HTML and CSS
3. Use Electron's BrowserView or webview tags to embed the LLM websites
4. Implement navigation and layout controls using JavaScript

### 2. Python with PyQt or GTK

Python with a GUI toolkit like PyQt or GTK is well-suited for desktop application development on Linux.

**Advantages:**
- Native look and feel on Linux
- Python's extensive libraries for web interaction
- Good performance

**Implementation steps:**
1. Set up a Python project with PyQt or GTK
2. Design the main window with either a grid layout or sidebar/panel layout
3. Use QWebEngineView (PyQt) or WebKit2 (GTK) to embed web content
4. Implement controls and navigation using Python

### 3. GNOME Extension

Since you're using Fedora, which typically comes with GNOME, you could create a GNOME extension.

**Advantages:**
- Deep integration with the GNOME desktop
- Lightweight and fast
- Can be toggled on/off easily

**Implementation steps:**
1. Set up a GNOME extension project
2. Use GJS (GNOME JavaScript) to create the UI
3. Implement either a grid or sidebar/panel layout
4. Use WebKit2 to embed web content

## Recommended Approach

Given your requirements and the Fedora Linux environment, I recommend using **Python with PyQt**. This approach offers a good balance of ease of development, performance, and integration with the Linux desktop.

Here's a basic outline of how you could implement this:

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class LLMApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LLM Dashboard")
        self.setGeometry(100, 100, 1200, 800)

        # Create main widget and layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        # Create sidebar
        sidebar = QVBoxLayout()
        llm_buttons = ["ChatGPT", "Claude", "Bard", "Perplexity"]
        for llm in llm_buttons:
            button = QPushButton(llm)
            button.clicked.connect(lambda checked, l=llm: self.load_llm(l))
            sidebar.addWidget(button)

        # Create main panel
        self.main_panel = QWebEngineView()

        # Add layouts to main layout
        main_layout.addLayout(sidebar, 1)
        main_layout.addWidget(self.main_panel, 4)

        # Set main widget and layout
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def load_llm(self, llm):
        urls = {
            "ChatGPT": "https://chat.openai.com/",
            "Claude": "https://www.anthropic.com/",
            "Bard": "https://bard.google.com/",
            "Perplexity": "https://www.perplexity.ai/"
        }
        self.main_panel.load(urls[llm])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LLMApp()
    window.show()
    sys.exit(app.exec_())
```

This code creates a basic sidebar and panel design. You can modify it to create a grid layout instead by adjusting the layout and adding multiple QWebEngineView widgets.

To run this application, you'll need to install PyQt5 and PyQtWebEngine:

```
sudo dnf install python3-pyqt5 python3-pyqt5-webengine
```

Remember to respect the terms of service of each LLM provider when embedding their content in your application. Some may require authentication or have restrictions on embedding.

 