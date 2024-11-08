---
title: "Adding open VS Code as easy access context in Dolphin"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I'd like to create "Open in VS Code" as one of the primary options in Dolphin when I navigate to a folder. How can I set this up as a context association?

# Output

You can add a custom context menu action to **Dolphin** (the KDE file manager) so that you can open folders directly in **Visual Studio Code (VS Code)**. Here’s how to set it up:

### **Steps to Add "Open in VS Code" to Dolphin's Context Menu**:

1. **Create a Custom Service Menu for Dolphin**:
   Dolphin uses **service menus** to add custom context menu options. You can create one for opening folders in VS Code.

2. **Navigate to the Service Menu Directory**:
   You need to create the custom service menu file in the appropriate directory:

   ```bash
   mkdir -p ~/.local/share/kservices5/ServiceMenus/
   ```

3. **Create the Service Menu File**:
   Create a new `.desktop` file for the service menu, which will add "Open in VS Code" to the context menu.

   ```bash
   nano ~/.local/share/kservices5/ServiceMenus/open-in-vscode.desktop
   ```

4. **Add the Following Content** to the file:

   ```ini
   [Desktop Entry]
   Type=Service
   ServiceTypes=KonqPopupMenu/Plugin, inode/directory
   Actions=openInVSCode
   Icon=code
   X-KDE-Priority=TopLevel

   [Desktop Action openInVSCode]
   Name=Open in VS Code
   Icon=code
   Exec=code "%f"
   ```

   ### **Explanation of the Fields**:
   - `Type=Service`: Specifies that this is a custom service.
   - `ServiceTypes=KonqPopupMenu/Plugin, inode/directory`: Tells Dolphin to display this menu item for directories.
   - `Actions=openInVSCode`: Defines the action that will be taken when the option is clicked.
   - `Exec=code "%f"`: The command to open the selected directory in VS Code. `%f` refers to the selected folder.

5. **Save the File** and Exit.

   In **nano**, press `Ctrl + O` to save the file, and then `Ctrl + X` to exit the editor.

6. **Restart Dolphin**:
   After creating the custom service menu, restart Dolphin to apply the changes:

   ```bash
   kquitapp5 dolphin
   dolphin &
   ```

### **Testing the New Option**:

1. Open **Dolphin** and **right-click** on any folder.
2. You should now see the option **"Open in VS Code"** in the context menu.
3. Click it, and the folder should open in VS Code.

### **Optional: Using VS Code's Insiders Version**:

If you're using the **Insiders** version of VS Code, you’ll need to adjust the `Exec` line in the `.desktop` file to point to the Insiders version:

```ini
Exec=code-insiders "%f"
```

### **Conclusion**:

Now you should be able to easily open any folder in Dolphin directly in VS Code with just a right-click! If you need further adjustments or have any questions, feel free to ask.