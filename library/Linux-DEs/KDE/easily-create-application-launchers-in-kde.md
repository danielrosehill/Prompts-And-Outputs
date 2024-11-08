---
title: "Easily create application launchers in KDE"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

can you recommend any application for easily creating application launchers in fedora linux. i'm using kde plasma

# Output

For KDE Plasma on Fedora Linux, there are a few options that integrate well with the desktop environment for creating application launchers:

### 1. **KMenuEdit**
   - **Description**: KMenuEdit is the default menu editor for KDE Plasma. It allows you to create, modify, and delete application launchers easily.
   - **Usage**:
     1. Right-click on the application launcher icon in your panel or desktop.
     2. Select "Edit Applications."
     3. In KMenuEdit, navigate to the category where you want to add the launcher.
     4. Click "New Item" and fill in the details such as the name, command (path to your executable or script), and icon.
     5. Save your changes, and the new launcher will appear in your application menu.

### 2. **Plasma Application Launcher Widget**
   - **Description**: You can directly add custom launchers to your panel or desktop using the Plasma widgets.
   - **Usage**:
     1. Right-click on your desktop or panel.
     2. Select "Add Widgets."
     3. Choose "Application Launcher" or "Application Menu" and drag it to your desktop or panel.
     4. Right-click the new launcher, select "Configure," and add the command for your script or application.

### 3. **Manually Creating a .desktop File**
   - **Description**: Similar to the GNOME method, you can manually create `.desktop` files for KDE Plasma.
   - **Steps**:
     1. **Create a .desktop file**: Open a text editor and create a new file, for example, `myapp.desktop`.
     2. **Add content**:
        ```ini
        [Desktop Entry]
        Name=MyApp
        Exec=/path/to/myapp
        Icon=/path/to/icon.png
        Type=Application
        Terminal=false
        ```
     3. **Save the file**: Save it in `~/.local/share/applications/` for it to be available in your application menu or `~/Desktop/` to create a desktop launcher.
     4. **Usage**: After saving, you can double-click the launcher on your desktop, or it will appear in the application menu under the specified category.

### 4. **MenuLibre (If you prefer a GUI)**
   - **Description**: Although MenuLibre is not native to KDE, it’s a universal menu editor that can work with KDE Plasma as well.
   - **Installation**:
     ```bash
     sudo dnf install menulibre
     ```
   - **Usage**: Launch MenuLibre, and it provides a graphical interface to create and edit application launchers, which will appear in your KDE menu.

### 5. **Application Launcher from Kickoff**
   - **Description**: You can also create launchers directly from the Kickoff Application Launcher.
   - **Usage**:
     1. Open the Kickoff menu and navigate to the location where you want the new entry.
     2. Right-click on an empty area within the category or menu.
     3. Choose "Add Application" or "Add New Item."
     4. Fill in the necessary details like name, command, and icon.
     5. Save, and the launcher will appear in the menu.

These tools and methods should allow you to easily create and manage application launchers within KDE Plasma on Fedora Linux.## Extracted Prompts
[[Prompts/Autocapture/Easily create application launchers in KDE.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Easily create application launchers in KDE.md#Prompt 1|Prompt 1]]
