---
title: "Quick repo launchers and workflow optimisation"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

To manage your **20 GitHub repositories** more effectively, especially when switching between multiple projects throughout the day, you could consider tools and workflows that provide a **centralized launcher**, a **visual overview**, and a **more streamlined process for opening and managing repos** in VS Code. Here are some suggestions to improve your setup:

### 1. **VS Code Workspace Files**
   - **Overview**: Instead of manually switching between individual repositories, you could use **workspace files** (`.code-workspace`). A VS Code workspace can include multiple folders (in your case, repositories), which allows you to switch contexts more seamlessly.
   - **How to Use**: Create a `.code-workspace` file that includes all your active repositories for the day. You can open a workspace, and all your repositories will be loaded in VS Code, each in its own section.
   - **Why It’s Helpful**: This allows you to launch multiple repositories in a single VS Code window, providing an organized overview without constant toggling.

### 2. **GitAhead or Fork (GUI Git Clients)**
   - **Overview**: **GitAhead** or **Fork** are **Git GUI clients** that provide a visual overview of your repositories, including which ones are currently active. You can quickly open any repository in VS Code from the GUI.
   - **How to Use**: Use GitAhead to monitor all repositories you’re working with. It has a clear UI for browsing, and you can launch VS Code from there.
   - **Why It’s Helpful**: These tools act as a central hub for all your repositories, giving you the ability to quickly open, manage, and track the repositories, along with a clear view of which ones are currently in use.

### 3. **VS Code "Repository Manager" (Custom Solution)**
   - **Create a Custom Launcher**: If you’re comfortable with a bit of scripting, you can create a **custom Python or Bash script** to act as a "launcher window." This script can:
     - Display all your GitHub repositories in a simple GUI using something like **Tkinter** (for Python).
     - Provide buttons for opening each repository in VS Code.
     - Track which repositories are currently open by monitoring the processes.
   - **Why It’s Helpful**: This would provide a quick launcher tailored to your workflow, and you could always modify it to add more features as you need.

### 4. **Raycast (MacOS) or Albert (Linux)**
   - **Overview**: If you’re using **MacOS**, **Raycast** is an app launcher that can be configured to run custom scripts, making it easy to create a command to open repositories in VS Code. For **Linux**, **Albert** can be used similarly.
   - **How to Use**: Set up Raycast or Albert to list and launch your repositories in VS Code with a few keystrokes.
   - **Why It’s Helpful**: This provides a **lightweight** and **keyboard-driven** way to switch between repositories without opening multiple programs or interfaces.

### 5. **GitLens Extension in VS Code**
   - **Overview**: **GitLens** is a popular VS Code extension for enhancing Git capabilities. It provides a **repository explorer** directly in VS Code.
   - **How to Use**: Install GitLens and use the repository explorer to get a clear list of all repositories you’ve cloned. You can switch between repositories directly in the VS Code sidebar.
   - **Why It’s Helpful**: It integrates directly into VS Code, eliminating the need for external applications and giving you a clear overview of all repositories in one place.

### 6. **Obsidian for Managing Repository Links**
   - **Overview**: Since you’re already using **Obsidian**, you could create a note that acts as a **repository dashboard**, listing all your repos with quick commands to open them in VS Code.
   - **How to Use**: Create a list in Obsidian with each repository name and include an embedded command link to open the repository in VS Code. You can even organize them by project type, priority, or status.
   - **Why It’s Helpful**: This approach provides you with a familiar interface for managing all your links and notes in one place, and it’s easy to integrate into your daily workflow.

### 7. **Tiling Window Managers (if using Linux)**
   - **Overview**: If you’re on Linux, using a **tiling window manager** like **i3** or **bspwm** can greatly simplify managing multiple VS Code windows, each open to a different repository.
   - **How to Use**: Configure the tiling manager to place each VS Code instance in a dedicated part of your screen, which makes navigating between repositories fast and intuitive.
   - **Why It’s Helpful**: It gives you a visual, organized layout, reducing the mental overhead of tracking which repositories are open.

### 8. **Multi-VS Code Instance with Named Sessions**
   - **Overview**: You can use named sessions for **VS Code** instances, each dedicated to a specific set of repositories.
   - **How to Use**: When opening VS Code, add a suffix to each session window (`code --user-data-dir <directory>`). This allows each instance to maintain its own set of open projects.
   - **Why It’s Helpful**: This lets you work with multiple isolated sessions, each tailored to a different LLM project or group of repositories.

### Summary:
- **VS Code Workspaces** are great for managing multiple repositories within one window.
- **GitAhead** or **Fork** provide a visual overview and easy switching between repos.
- **Raycast** (MacOS) or **Albert** (Linux) can be used as quick launchers to access repos.
- **Obsidian** can serve as a centralized dashboard for repository links.
- **Tiling window managers** are very useful if you’re on Linux and want an organized multi-window workflow.

Depending on your preferences, a combination of **VS Code Workspaces** for easy switching, **GitLens** for quick repository access, and **Obsidian** for an overview might work well to keep things organized. Let me know if you’d like more information on setting up any of these!

