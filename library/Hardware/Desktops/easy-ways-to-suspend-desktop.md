---
title: "Easy ways to suspend desktop"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

On Fedora, is there a quicker way of getting the computer to go into a suspend/hibernation state when you stap away? I've looked into setting up a keyboard shortcut. Perhaps there are desktop widgets too? KDE Plasma + Wayland

# Output

On **Fedora with KDE Plasma on Wayland**, there are indeed several ways to quickly put your computer into a suspend or hibernation state when you step away. Here are a few options you can explore:

### 1. **Setting up a Keyboard Shortcut**
This is a quick and efficient method. You can set up a custom keyboard shortcut to trigger suspend or hibernate by following these steps:

1. **Open System Settings**:
   - Navigate to **System Settings** → **Shortcuts**.

2. **Create a New Custom Shortcut**:
   - Click on **Custom Shortcuts** on the left side.
   - Click the **+ Add Action** button → **Command/URL**.

3. **Configure the Command**:
   - Name the shortcut (e.g., "Suspend Shortcut").
   - In the **Action** section, set the command for suspend:
     - For **suspend**: `systemctl suspend`
     - For **hibernate**: `systemctl hibernate`
   - In the **Trigger** section, assign your desired key combination (e.g., `Ctrl + Alt + S`).

4. **Save** your new shortcut.

Now, whenever you press the assigned keys, your computer will go into suspend or hibernate mode.

### 2. **Using Desktop Widgets**
If you prefer using a widget, KDE Plasma has a variety of widgets that can be placed on your desktop or panel to suspend your system:

1. **Add a Sleep/Suspend Widget**:
   - Right-click on your desktop or panel and select **Add Widgets**.
   - Search for keywords like “**Sleep**,” “**Suspend**,” or “**Hibernate**.”
   - Some popular widgets include **Shutdown Control** or **Sleep Button**, which let you quickly put your system into suspend or hibernation.
   - Drag the widget to your desktop or panel for quick access.

### 3. **Set Power Management Settings**
If you want your computer to suspend automatically when you step away, you can configure **Power Management** settings to trigger suspend after a period of inactivity.

1. **Open System Settings**:
   - Go to **System Settings** → **Power Management**.

2. **Configure Inactivity Behavior**:
   - Set the time after which the computer should automatically suspend.
   - Adjust settings for both on **Battery** and **AC** power.

These methods should streamline the process for quickly suspending or hibernating your system.