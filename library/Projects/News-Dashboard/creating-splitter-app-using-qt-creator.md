---
title: "Creating splitter app using Qt Creator"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Let's consider using Qt Creator. It seems like a useful application. Could you revise your previous output on how to create the ChatGPT and Obsidian splitter app based on the new assumption that I will be using this tool to build the utility?

# Output

Great! Using **Qt Creator** simplifies the process of developing the **Obsidian + ChatGPT splitter app** because it provides an integrated development environment (IDE) for designing and coding the app. Here’s a step-by-step guide on how to build your split-screen application using **Qt Creator**.

### 1. **Install Qt Creator and Required Dependencies**
First, make sure you have **Qt Creator** and the necessary **Qt WebEngine** module installed.

On **Fedora**, you can install everything with:
```bash
sudo dnf install qt-creator qt5-qtbase qt5-qtbase-devel qt5-qtwebengine qt5-qtwebengine-devel
```

This will install the Qt Creator IDE and the dependencies needed to work with **QWebEngineView** (for embedding ChatGPT) and other basic Qt components.

### 2. **Create a New Project in Qt Creator**
1. Open **Qt Creator** and select **New Project**.
2. Choose **Qt Widgets Application**.
3. Set the project name (e.g., `ObsidianChatGPTApp`) and the location where you want to save the project.
4. Select your Qt kit (default should work) and click **Next**.
5. Set the class name for the main window (e.g., `MainWindow`) and finish creating the project.

### 3. **Set Up the Split-Screen Layout in `mainwindow.ui`**
1. In **Qt Creator**, go to the **Design** mode. This opens the **mainwindow.ui** file, which represents your application's graphical interface.
2. You will see a blank window in the design area. Drag a **QSplitter** widget from the **Widget Box** on the left into your main window.
   - This **QSplitter** will allow you to split the window into two panes.
3. Drag two **QWidget** elements into the **QSplitter**—one for **Obsidian** (left pane) and one for **ChatGPT** (right pane).

### 4. **Configure the Left Pane for Obsidian**
The left pane will be a placeholder for launching the native **Obsidian** desktop application.

1. Click on the first widget inside the **QSplitter** (left pane).
2. Add a **QLabel** to the widget (from the **Widget Box**) and set the text to something like **"Obsidian (Running as Native App)"**. This is just a placeholder for the app’s UI.
3. You will launch the **Obsidian** app programmatically when the app starts (code step later).

### 5. **Configure the Right Pane for ChatGPT (QWebEngineView)**
1. Select the second widget inside the **QSplitter** (right pane).
2. Drag and drop a **QWebEngineView** widget from the **Widget Box** into the right pane. This will be used to load the **ChatGPT PWA**.

### 6. **Code: Load ChatGPT and Launch Obsidian**

Now switch to **Edit** mode in **Qt Creator** and modify the code in `mainwindow.cpp` to:
- Launch **Obsidian** using **QProcess**.
- Load the **ChatGPT PWA** in the **QWebEngineView**.

**`mainwindow.cpp` Code**:
```cpp
#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QProcess>
#include <QWebEngineView>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Launch Obsidian as a native application in the left pane
    QProcess *obsidianProcess = new QProcess(this);
    obsidianProcess->start("obsidian");

    // Load ChatGPT PWA in the QWebEngineView (right pane)
    QWebEngineView *webView = ui->webEngineView; // QWebEngineView in the right pane
    webView->setUrl(QUrl("https://chat.openai.com"));
}

MainWindow::~MainWindow()
{
    delete ui;
}
```

### 7. **Build and Run the Project**
1. In **Qt Creator**, click **Build** > **Build Project** to compile your application.
2. Once built, click **Run** to execute the application.

You should see the split-screen layout:
- On the left side: A label indicating that **Obsidian** is running as a native app (while the actual app runs as a separate process).
- On the right side: **ChatGPT** loaded inside the **QWebEngineView** widget.

### 8. **Customize the Layout**
To improve the user experience, you can further adjust the layout:
- **Resizable Splitter**: By default, the **QSplitter** allows resizing. If you want to lock the ratio, adjust its properties in the **Properties Panel**.
- **Default Size Ratio**: You can set the initial size ratio of the two panes in the `mainwindow.cpp` file:
  
```cpp
ui->splitter->setSizes({800, 800});  // Adjust the initial width ratio between Obsidian and ChatGPT
```

### 9. **Final Steps and Considerations**:
- **Error Handling**: Ensure that you handle the case where **Obsidian** is not installed or fails to start.
- **Performance**: Since you are using **QWebEngineView** to load an external web resource (ChatGPT), you might want to handle network errors and loading states in the web view.

### Open Source Considerations
As discussed previously, you can open-source this project while respecting OpenAI's terms of service by ensuring you:
- Mention that you’re embedding the **ChatGPT PWA**.
- Include links to OpenAI's terms of service for users interacting with ChatGPT.

### Conclusion
By using **Qt Creator**, you can easily design the UI for your split-screen app with **Obsidian** on the left and **ChatGPT** on the right. This approach provides a native experience on Linux with full control over the layout, and it’s highly customizable for your specific use case.