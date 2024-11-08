---
title: "Using Qsplitter and Qt to build the ChatGPT and Obsidian app"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's explore the Qt app approach, especially if it wouldn't be that much more complicated than the Electron approach. How could we achieve this functionality suing it?

# Output

Using **Qt** to create a split-screen app with **Obsidian** on the left and **ChatGPT PWA** on the right can indeed be achieved in a way that is relatively straightforward, similar to an Electron app but leveraging native Linux toolkits. Since you are already using **Wayland**, **Qt** is well-supported for Wayland, and the **QSplitter** widget is ideal for the split-screen functionality.

Here’s how you can approach this:

### Steps to Create the Qt App:

1. **Install the Qt Development Environment**:
   - First, install the necessary Qt development tools. On Fedora, you can do this with:
   ```bash
   sudo dnf install qt5-qtbase qt5-qtbase-devel qt5-qtscript qt5-qtmultimedia qt5-qtsvg qt5-qtwebengine-devel
   ```

2. **Set Up the Project**:
   You can use **Qt Creator** (a GUI IDE for Qt), or simply work from the command line with a basic project structure. We’ll walk through a simple example with a main window using **QSplitter** to divide the screen.

3. **Create the Basic Qt Application**:
   This app will use a **QSplitter** to divide the window into two halves: one half will launch **Obsidian** as a native app, and the other half will load **ChatGPT** using a **QWebEngineView** to render the ChatGPT PWA.

4. **Code for the Qt App**:

   Here’s a basic example using **QSplitter** to create the split layout, embedding a native process on the left and the web browser (ChatGPT PWA) on the right.

```cpp
#include <QApplication>
#include <QSplitter>
#include <QWidget>
#include <QProcess>
#include <QVBoxLayout>
#include <QWebEngineView>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    // Create the main window
    QWidget *window = new QWidget;
    QVBoxLayout *layout = new QVBoxLayout(window);

    // Create a splitter for the split screen functionality
    QSplitter *splitter = new QSplitter(Qt::Horizontal);

    // Left pane: Launch Obsidian as a native process
    QWidget *leftWidget = new QWidget;
    QVBoxLayout *leftLayout = new QVBoxLayout(leftWidget);

    // Start the Obsidian process
    QProcess *obsidianProcess = new QProcess;
    obsidianProcess->start("obsidian");

    // Add a label or placeholder for the Obsidian process
    QLabel *obsidianLabel = new QLabel("Obsidian is running...");
    leftLayout->addWidget(obsidianLabel);
    splitter->addWidget(leftWidget);

    // Right pane: QWebEngineView for ChatGPT
    QWebEngineView *webView = new QWebEngineView;
    webView->setUrl(QUrl("https://chat.openai.com"));
    splitter->addWidget(webView);

    // Add the splitter to the main layout
    layout->addWidget(splitter);
    window->setLayout(layout);

    // Set window size
    window->resize(1600, 900);
    window->setWindowTitle("Obsidian + ChatGPT Split Screen");
    window->show();

    return app.exec();
}
```

### Key Components in the Code:

1. **QSplitter**: 
   - This widget allows you to divide the main window into resizable panes. One pane will run **Obsidian**, and the other will display **ChatGPT** via a web engine.

2. **QProcess**:
   - Used to launch the **Obsidian** desktop client as a native application. It will run separately but in the same window layout.

3. **QWebEngineView**:
   - This Qt class is part of the **Qt WebEngine** module and is used to display web content. Here, we use it to load the **ChatGPT PWA**.

### Building and Running the Qt Application:

1. **Compile the App**:
   To compile the app, you will need to have `qmake` and `make` set up. Here's how you can compile it from the command line:
   ```bash
   qmake -project
   qmake
   make
   ```

2. **Run the App**:
   Once built, you can run the resulting binary:
   ```bash
   ./yourappname
   ```

   You should now see a split-screen window with **Obsidian** running on the left (launched as a native process) and **ChatGPT** (in a webview) on the right.

### Advantages of the Qt Approach:

- **Native Performance**: Since Qt is a native toolkit for Linux, performance is optimal, and you avoid some of the overhead that comes with Electron apps.
- **Full Control Over Layout**: You can easily adjust the splitter, size, and layout of the windows.
- **Compatibility with Wayland**: Qt has excellent support for Wayland, so you won’t run into the window management limitations that you faced previously.

### Optional Improvements:
- **Error Handling**: Add error handling for launching Obsidian to display a message if the process fails.
- **Customization**: You can further customize the look and feel of the split-screen interface by adding custom themes or controls for resizing panes.
- **Two-Way Interactivity**: If you want to integrate more complex interaction between **Obsidian** and **ChatGPT**, you can extend this app to allow data sharing between the panes.

### Summary:
Creating a **Qt app** with **split-screen functionality** is a highly efficient and flexible solution for your needs. By using **QSplitter**, **QProcess**, and **QWebEngineView**, you can run **Obsidian** as a native app on the left and load the **ChatGPT PWA** on the right, all within a single window that’s compatible with **Wayland**.

This approach gives you full control over the interface and provides a native app experience, combining both local and web-based applications seamlessly.