---
title: "Best way to install fonts in bulk on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You are asking for the best way to install multiple fonts in Fedora, specifically after downloading about 50 fonts from Google Fonts, where each font is in its own folder with TTF files.

---

To install multiple fonts efficiently on Fedora, you can use a few methods to streamline the process. Since you have a large number of fonts, I'll outline how to install them all at once rather than manually installing each one.

### **Method 1: Install Fonts System-Wide (Available to All Users)**
If you want the fonts to be accessible to all users on the system, you can place them in the system fonts directory. You will need root privileges to do this.

1. **Open Terminal and Navigate to the Fonts Directory**
   - You’ll need to copy the fonts into the system fonts directory:
     ```bash
     sudo mkdir -p /usr/share/fonts/custom
     ```
2. **Copy All TTF Files to the System Fonts Directory**
   - Assuming you have your downloaded Google Fonts in a directory called `~/Downloads/google-fonts`, use the following command to copy all `.ttf` files:
     ```bash
     sudo cp ~/Downloads/google-fonts/**/*.ttf /usr/share/fonts/custom
     ```
   - The `**/*.ttf` pattern will recursively find all `.ttf` files in your downloaded directories and copy them.

3. **Update the Font Cache**
   - After copying the fonts, you’ll need to refresh the font cache so that the system recognizes the new fonts:
     ```bash
     sudo fc-cache -fv
     ```

### **Method 2: Install Fonts Locally (For Your User Only)**
If you prefer to install the fonts for just your user account (without needing root access), you can place them in a user-specific directory:

1. **Create a Local Fonts Directory (If It Doesn’t Exist)**
   - This is typically `~/.local/share/fonts` or `~/.fonts`:
     ```bash
     mkdir -p ~/.local/share/fonts
     ```
2. **Copy All TTF Files to Your Local Fonts Directory**
   - Use the following command to copy all `.ttf` files to your local fonts directory:
     ```bash
     cp ~/Downloads/google-fonts/**/*.ttf ~/.local/share/fonts
     ```

3. **Update the Font Cache**
   - Run the following command to refresh the font cache:
     ```bash
     fc-cache -fv
     ```

### **Method 3: Bulk Install Using GNOME Fonts (GUI Method)**
If you prefer using a graphical interface, Fedora provides a **Fonts** app where you can drag and drop fonts. However, this method is more manual and may not be as efficient if you have a large number of fonts.

1. **Open the Fonts App**
   - You can launch the **Fonts** app from the application menu by searching for **"Fonts."**
2. **Drag and Drop TTF Files**
   - Open the directory where your font files are stored.
   - Select all the `.ttf` files you want to install and drag them into the Fonts window.

### **Verifying Installed Fonts**
Once you have installed the fonts, you can verify that they are available on your system using the `fc-list` command:
```bash
fc-list | grep -i "<font name>"
```
Replace `<font name>` with part of the name of one of the fonts you installed to confirm it has been correctly installed.

### **Managing Fonts with Font Managers**
If you often install and manage a large number of fonts, you might want to consider using a **font manager**. A font manager can help you organize, preview, and activate/deactivate fonts easily.

1. **Font Manager for Linux**
   - You can install a tool called `font-manager` which provides a GUI for managing fonts on Linux:
     ```bash
     sudo dnf install font-manager
     ```
   - This tool allows you to view installed fonts, install new fonts, and organize them into collections.

### **Conclusion**
For the most efficient way to install multiple fonts, I recommend **Method 1 (System-Wide Installation)** if you need them available for all users, or **Method 2 (Local Installation)** if you only need them for yourself. Both approaches allow you to quickly bulk install fonts by copying them to the appropriate directory and refreshing the font cache. For users who prefer graphical methods, **dragging and dropping in the Fonts app** is an option, though it may be slower for bulk installs.