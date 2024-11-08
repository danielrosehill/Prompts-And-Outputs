---
title: "Creating split views with multiple panes in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there a file manager for Fedora (KDE Plasma) that can support creating a split view with 3 folders open (or 4)

# Output

Yes, there are several file managers on Fedora (with KDE Plasma) that support split views, and some of them can handle more than two folders open at the same time. Here are some options:

### 1. **Krusader**
Krusader is a powerful file manager designed for KDE Plasma, and it supports multi-pane views.

- **Key Features**:
  - Split view support with multiple panes.
  - Tabs within each pane for additional flexibility.
  - Highly configurable and supports advanced file management features like mounting/unmounting, archive management, etc.
  
- **How to install**:
  ```bash
  sudo dnf install krusader
  ```

- **How to Use**:
  - Open Krusader.
  - By default, it opens with two panes. You can create new tabs in each pane or use the "Vertical Split" feature for additional panes.

### 2. **Dolphin** (Default KDE File Manager)
Dolphin is the default file manager for KDE Plasma and supports split views natively. However, it only supports **two panes** at once but you can open multiple tabs within each pane.

- **Key Features**:
  - Split view (two panes only).
  - Tabs for managing multiple folders.
  
- **How to use**:
  - Open Dolphin.
  - Press `F3` to open a split view with two panes.
  - You can open multiple tabs in each pane by pressing `Ctrl+T`.

If you're content with tabs within two panes, Dolphin is highly configurable and can give you access to multiple directories with quick tab switching.

### 3. **Konqueror**
Konqueror is another KDE-based file manager that is very versatile and supports multi-pane views, including splitting into 3 or more views.

- **Key Features**:
  - Multi-pane support (more than 2 panes).
  - Tabs for multiple folders within panes.
  - Web browsing functionality (optional).

- **How to install**:
  ```bash
  sudo dnf install konqueror
  ```

- **How to use**:
  - Open Konqueror.
  - Right-click on the window or use the menu to open additional panes (`View > Split View`).

### 4. **Q-Dir (via Wine)**
If you're open to using **Wine** (Windows compatibility layer), you can try **Q-Dir**, a lightweight file manager for Windows that supports up to 4 panes in one view. 

- **Key Features**:
  - Support for up to 4 folders open simultaneously.
  - Lightweight and highly configurable.
  
- **How to install**:
  1. Install Wine:
     ```bash
     sudo dnf install wine
     ```
  2. Download Q-Dir from the [official site](https://www.softwareok.com/?Download=Q-Dir).
  3. Run the downloaded `.exe` file using Wine:
     ```bash
     wine Q-Dir.exe
     ```

- **How to use**:
  - Open Q-Dir with Wine.
  - The default view supports 4 panes, and you can manage multiple directories at once.

### Conclusion:
- For **3 or 4 pane views**: **Krusader** and **Konqueror** are the best native options for KDE Plasma on Fedora.
- If you are okay with just **2 panes with tabs**, **Dolphin** is a good, fast, and integrated choice.
- **Q-Dir** (via Wine) is a good lightweight option if you're open to using a non-native application.

Among these, **Krusader** is the most powerful and flexible file manager that natively supports multiple panes, making it ideal for power users.