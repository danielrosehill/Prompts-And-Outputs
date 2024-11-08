---
title: "Setting up the class names in Qt Widget setup"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 
In the screen you're showing, you are defining the basic class information for your project. Here's what each field represents and how you should proceed:

### 1. **Class Name**:
   - This defines the name of the main window class for your application.
   - **Recommendation**: You can leave it as `MainWindow`, which is typical for a basic Qt application that has one main window. This is the standard naming convention and will be the class that handles your main window's UI.
   
### 2. **Base Class**:
   - This defines the parent class from which your window class will inherit. The default is `QMainWindow`, which provides a central widget, menu bar, toolbars, and status bars.
   - **Recommendation**: Leave this as `QMainWindow` since it is the most suitable for your application, providing you with the needed window structure.

### 3. **Header File (`.h`)**:
   - This is where the declaration of your `MainWindow` class and its functions will reside.
   - **Recommendation**: Keep the default name `mainwindow.h`.

### 4. **Source File (`.cpp`)**:
   - This is where the implementation of your `MainWindow` class will be written (the logic behind your UI).
   - **Recommendation**: Keep the default name `mainwindow.cpp`.

### 5. **Generate Form**:
   - This checkbox ensures that a `.ui` file will be created, which is where you will design the visual layout using Qt's drag-and-drop interface.
   - **Recommendation**: Keep this checked, as you will need the form for designing your app's interface visually.

### 6. **Form File (`.ui`)**:
   - This is the file where your visual interface design will be stored.
   - **Recommendation**: Keep the default name `mainwindow.ui`.

### Final Recommendations:
   - You can proceed with the default values on this screen:
     - Class Name: `MainWindow`
     - Base Class: `QMainWindow`
     - Header File: `mainwindow.h`
     - Source File: `mainwindow.cpp`
     - Form File: `mainwindow.ui`
   - After clicking "Next," you'll be able to move on to the next steps, where you’ll start adding the widgets (like **QSplitter** and **QWebEngineView**) to create the split-screen layout.