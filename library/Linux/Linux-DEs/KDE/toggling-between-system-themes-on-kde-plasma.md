---
title: "Toggling between system themes on KDE Plasma"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


For before calls etc
Yes, KDE Plasma offers several ways to quickly and easily toggle between themes. Here are a few methods:

### 1. **Global Theme Shortcut in System Settings**
   - **System Settings > Appearance > Global Theme**: Here, you can preview and switch between themes. Plasma themes can include dark and light modes, so if you have one of each, you can switch here.
   - **Quick Access**: To make switching faster, consider adding System Settings to your favorites or creating a desktop shortcut to open directly to the Global Theme page.

### 2. **Custom Shortcut with `lookandfeeltool`**
   - KDE provides the `lookandfeeltool` command-line tool to apply themes, making it easy to create shortcuts to toggle between two or more themes:
   - **Command**: Open a terminal and try:
     ```bash
     lookandfeeltool -a <theme-name>
     ```
   - **Example**: If you have Breeze Dark and Breeze Light installed, you can toggle between them by setting shortcuts for:
     ```bash
     lookandfeeltool -a org.kde.breezedark.desktop
     lookandfeeltool -a org.kde.breeze.desktop
     ```
   - **Create Keyboard Shortcuts**: Go to **System Settings > Shortcuts > Custom Shortcuts**, create a new custom shortcut for each command, and assign a keyboard shortcut to each theme toggle.

### 3. **KDE Store Widgets for Quick Access**
   - KDE's widget library (from the KDE Store) includes theme switchers and night/light mode toggle widgets. Some popular options include:
     - **Plasma Light/Dark Switch**: A widget that allows quick switching between light and dark themes.
     - **Night Color Control**: If you’re switching themes to manage screen brightness, Night Color (night mode) can also help by adjusting screen warmth.

### 4. **Scripts with Global Theme Switchers**
   - For a more custom approach, you could create a bash script to cycle between themes and assign a shortcut to run the script:
     ```bash
     #!/bin/bash
     current_theme=$(lookandfeeltool --list | grep -o "org.kde.breezedark\|org.kde.breeze")

     if [ "$current_theme" = "org.kde.breezedark" ]; then
       lookandfeeltool -a org.kde.breeze.desktop
     else
       lookandfeeltool -a org.kde.breezedark.desktop
     fi
     ```

This should provide you with a seamless, quick way to toggle themes on KDE Plasma without navigating through settings each time.