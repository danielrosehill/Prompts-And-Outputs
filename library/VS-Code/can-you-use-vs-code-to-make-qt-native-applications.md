---
title: "Can you use VS Code to make Qt native applications"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

So you can make a Qt native app using VS Code? Could I just use VS Code to make my splitter app for Obsidian and ChatGPT?
# Output

Yes, you can absolutely use **Visual Studio Code (VS Code)** to develop a **Qt native application**, including your splitter app for **Obsidian** and **ChatGPT**. VS Code is highly flexible and can be set up with the necessary tools to build and manage **Qt** projects, though it doesn't provide the built-in, integrated visual design features of **Qt Creator**.

Here’s how you can set up **VS Code** for developing your **Qt** splitter app:

### 1. **Install the Necessary Extensions in VS Code**:
   VS Code is not a full-fledged IDE for Qt by default, but with a few extensions, you can get it working for Qt development.

   - **C++ Extension**: You'll need the **C++ extension** for syntax highlighting, IntelliSense, and debugging. Install the [C/C++ extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) from the VS Code marketplace.
   
   - **Qt for Visual Studio Code**: This extension adds **Qt**-specific features to VS Code, such as **qmake** integration and easier access to **Qt Designer** for `.ui` files. You can install it from [Qt Visual Studio Tools](https://marketplace.visualstudio.com/items?itemName=twxs.qt-tools).

   - **CMake Tools (if using CMake)**: If you're using **CMake** as your build system (which is common for Qt projects), you'll want to install the **CMake Tools** extension. You can find it [here](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools).

### 2. **Set Up a New Qt Project in VS Code**:
   You'll need to manually configure some settings for your project, as VS Code won’t generate these automatically like Qt Creator does.

   **Steps**:
   1. Create a folder for your project.
   2. Initialize a Git repository inside that folder (if needed):
      ```bash
      git init
      ```

   3. If using **CMake** as the build system, you'll need a **CMakeLists.txt** file in your project root to specify how to build your Qt project. Here's an example for your splitter app:

      ```cmake
      cmake_minimum_required(VERSION 3.5)
      project(ObsidianChatGPTApp)

      set(CMAKE_CXX_STANDARD 11)

      find_package(Qt5 COMPONENTS Widgets WebEngineWidgets REQUIRED)

      add_executable(ObsidianChatGPTApp main.cpp)

      target_link_libraries(ObsidianChatGPTApp Qt5::Widgets Qt5::WebEngineWidgets)
      ```

   4. Create the **main.cpp** file in your project directory (similar to what we did earlier). For example:

      ```cpp
      #include <QApplication>
      #include <QSplitter>
      #include <QProcess>
      #include <QWebEngineView>
      #include <QLabel>
      #include <QVBoxLayout>

      int main(int argc, char *argv[]) {
          QApplication app(argc, argv);

          // Create a main window
          QWidget *window = new QWidget;
          QVBoxLayout *layout = new QVBoxLayout(window);

          // Create a splitter for the split screen functionality
          QSplitter *splitter = new QSplitter(Qt::Horizontal);

          // Left pane: Launch Obsidian as a native process
          QWidget *leftWidget = new QWidget;
          QVBoxLayout *leftLayout = new QVBoxLayout(leftWidget);
          QProcess *obsidianProcess = new QProcess;
          obsidianProcess->start("obsidian");
          QLabel *obsidianLabel = new QLabel("Obsidian Running...");
          leftLayout->addWidget(obsidianLabel);
          splitter->addWidget(leftWidget);

          // Right pane: Load ChatGPT using QWebEngineView
          QWebEngineView *webView = new QWebEngineView;
          webView->setUrl(QUrl("https://chat.openai.com"));
          splitter->addWidget(webView);

          layout->addWidget(splitter);
          window->setLayout(layout);
          window->resize(1600, 900);
          window->show();

          return app.exec();
      }
      ```

### 3. **Configure Build Tasks**:
   To make building and running your project smoother in VS Code, you'll need to configure build tasks for compiling your project.

   1. Create a **tasks.json** file under the `.vscode/` directory. Here’s an example configuration for using **CMake**:

      ```json
      {
          "version": "2.0.0",
          "tasks": [
              {
                  "label": "Build Qt Project",
                  "type": "shell",
                  "command": "cmake --build .",
                  "group": {
                      "kind": "build",
                      "isDefault": true
                  },
                  "problemMatcher": ["$gcc"]
              }
          ]
      }
      ```

   This task will invoke **CMake** to build your Qt project.

### 4. **Debugging Configuration**:
   Configure debugging by creating a **launch.json** file in the `.vscode/` directory:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Launch Qt Application",
               "type": "cppdbg",
               "request": "launch",
               "program": "${workspaceFolder}/ObsidianChatGPTApp", 
               "args": [],
               "stopAtEntry": false,
               "cwd": "${workspaceFolder}",
               "environment": [],
               "externalConsole": false,
               "MIMode": "gdb",
               "setupCommands": [
                   {
                       "description": "Enable pretty-printing for gdb",
                       "text": "-enable-pretty-printing",
                       "ignoreFailures": true
                   }
               ],
               "preLaunchTask": "Build Qt Project",
               "miDebuggerPath": "/usr/bin/gdb",
               "setupCommands": [
                   {
                       "text": "enable-pretty-printing",
                       "description": "Enable pretty printing",
                       "ignoreFailures": true
                   }
               ],
               "logging": {
                   "trace": true,
                   "traceResponse": true
               },
               "targetArchitecture": "x64",
               "internalConsoleOptions": "openOnSessionStart",
               "MIMode": "gdb",
               "miDebuggerPath": "/usr/bin/gdb",
               "stopAtEntry": false,
               "environment": []
           }
       ]
   }
   ```

### 5. **Build and Run**:
   Once you have your **tasks.json** and **launch.json** set up, you can build and run your Qt project in VS Code.

   - **To build the project**: Press `Ctrl+Shift+B` (or open the Command Palette and type `Run Build Task`).
   - **To run the project**: Press `F5` to launch the application with debugging.

### 6. **Install Dependencies**:
   Make sure you have the necessary Qt libraries installed on your system:
   ```bash
   sudo dnf install qt5-qtbase qt5-qtwebengine qt5-devel
   ```

### Pros and Cons of Using VS Code vs Qt Creator:

#### **Pros of VS Code**:
   - **Highly customizable**: You can add or remove extensions to fit your workflow.
   - **Wide language support**: If you’re using multiple languages (e.g., Python, JavaScript), VS Code allows you to work on various parts of a project in a single environment.
   - **Lightweight**: VS Code is lighter than Qt Creator and can be faster for smaller projects.
   - **Familiar interface**: If you’re already used to VS Code for other projects, it can be convenient to stick with a single environment.

#### **Cons of VS Code**:
   - **No integrated UI designer**: Qt Creator’s **Qt Designer** for `.ui` files provides a seamless drag-and-drop interface for designing UIs. With VS Code, you’ll either need to write the UI code by hand or use **Qt Designer** separately.
   - **Manual configuration**: You’ll need to set up things like build tasks, launch configurations, and project structure manually, whereas Qt Creator handles these automatically for you.

### Conclusion:
You can absolutely use **VS Code** to build your splitter app for **Obsidian** and **ChatGPT**. With the right extensions and configurations, it becomes a powerful environment for **Qt** development. However, keep in mind that **VS Code** won’t offer the built-in visual tools that **Qt Creator** provides (like the UI designer). If you’re comfortable with manually configuring your project and prefer a lighter, more flexible editor, **VS Code** is a solid option.