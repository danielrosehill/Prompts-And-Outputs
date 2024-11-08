---
title: "Enforcing system wide preference for dark mode themes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm really liking the dark mode theme on KDE but some apps (like VS Code) don't seem to have it. Is the only option to configure dark mode on an app by app basis? Or are there any additional settings that can be changed to try to enforce a more system wide preference for dark mode themes if they are available

# Output
In KDE Plasma, there are a few options to encourage apps to adopt the system-wide dark theme, though some apps may still require manual adjustments:

### 1. **Set Global Theme to Dark Mode**
   - In **System Settings > Appearance > Global Theme**, select a dark theme as the default. This will apply a dark theme to most KDE/Qt applications automatically.

### 2. **GTK Application Style Settings**
   - Many apps, like VS Code, are GTK-based and don’t automatically follow the Qt/KDE theme.
   - Go to **System Settings > Appearance > Application Style > Configure GNOME/GTK Application Style** and select a dark theme (such as **Adwaita-dark** or a dark Breeze variant).
   - This should make most GTK applications, including VS Code, follow a dark mode if available.

### 3. **Force Dark Mode for Electron Apps (like VS Code)**
   - Electron-based apps, such as VS Code, often have their own theming options. You can set `GTK_THEME=Adwaita:dark` as an environment variable for such apps to enforce a dark theme.
   - For VS Code specifically, add the following line to `/usr/share/applications/code.desktop` under the `[Desktop Entry]` section:
     ```ini
     Exec=env GTK_THEME=Adwaita:dark code %U
     ```

### 4. **Using KDE’s Night Color for Reduced Blue Light**
   - For additional eye comfort, you can enable **Night Color** under **Display and Monitor > Night Color** to reduce blue light, which complements dark mode by adjusting color warmth.

While these steps help enforce dark mode across many apps, some may still need individual configuration. However, these settings should give you better consistency across your KDE desktop environment.