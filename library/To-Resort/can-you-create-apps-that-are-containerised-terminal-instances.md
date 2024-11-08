---
title: "Can you create apps that are containerised terminal instances"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
on fedora is there any way to create "apps" that are containerised terminal instances kind of like how you can create PWAs for chrome apps? For instance I'd like to create a terminal instance that opened up with newsboat already open

# Output

Yes, on Fedora (or any Linux system), you can create "apps" that are essentially **containerized terminal instances** with specific applications like **Newsboat** running inside them. While this isn't exactly the same as **PWAs (Progressive Web Apps)** in a browser like Chrome, you can achieve something similar by using tools like **desktop shortcuts**, **wrappers around terminal commands**, and **containerization** tools (like **Docker** or **Podman**). Below are a few approaches that can give you a PWA-like experience for terminal-based applications:

### Approach 1: Using `.desktop` Files to Create "Apps"
On Linux, you can create **`.desktop` files**, which are essentially shortcuts that can open specific applications or run specific commands. This can be used to create terminal instances that open **Newsboat** or other terminal-based applications automatically.

#### Steps to Create a `.desktop` Shortcut:

1. **Create a `.desktop` file**:
   - Navigate to your local applications folder:
     ```bash
     cd ~/.local/share/applications/
     ```
   - Create a new `.desktop` file for your terminal app (for example, Newsboat):
     ```bash
     nano newsboat.desktop
     ```

2. **Add the following contents** to the `.desktop` file:
   ```ini
   [Desktop Entry]
   Name=Newsboat
   Comment=RSS Reader
   Exec=gnome-terminal -- bash -c "newsboat; exec bash"
   Icon=utilities-terminal
   Terminal=false
   Type=Application
   Categories=Utility;Application;
   ```

   - **Name**: This is the name that will appear in your application launcher.
   - **Exec**: This is the command that will be executed when the "app" is launched. Here, it opens `gnome-terminal` and automatically runs `newsboat`. After Newsboat is closed, `exec bash` keeps the terminal open.
   - **Icon**: You can specify an icon here, but `utilities-terminal` is a generic terminal icon.
   - **Terminal=false**: This is important since `gnome-terminal` is already handling the terminal instance.
   - **Categories**: You can organize this under categories like "Utility."

3. **Make the `.desktop` file executable**:
   ```bash
   chmod +x ~/.local/share/applications/newsboat.desktop
   ```

4. **Launch the "app"**:
   - You should now see **Newsboat** as an application in your **app launcher** (GNOME, KDE, etc.).
   - Clicking on it will open a new terminal instance with Newsboat running automatically.

### Approach 2: Use a Script to Launch a Containerized Terminal Instance
If you want to **containerize** your terminal apps (e.g., run them isolated from the system), you can use **Podman** or **Docker** to create lightweight containers for terminal applications like **Newsboat**.

#### Example using **Podman**:

1. **Create a Dockerfile** for Newsboat:
   Create a directory for your containerized Newsboat setup:
   ```bash
   mkdir ~/newsboat-container
   cd ~/newsboat-container
   ```

   Create a `Dockerfile`:
   ```bash
   nano Dockerfile
   ```

2. **Add the following to the Dockerfile**:
   ```Dockerfile
   FROM fedora:latest

   RUN dnf install -y newsboat && dnf clean all

   CMD ["newsboat"]
   ```

   - This installs **Newsboat** in a minimal **Fedora** container.

3. **Build the container**:
   Build the Docker or Podman image:
   ```bash
   podman build -t newsboat-app .
   ```

4. **Create a launcher script**:
   Create a script to launch the containerized app with **Podman** or **Docker**:
   ```bash
   nano ~/launch-newsboat.sh
   ```

5. **Add the following content** to the script**:
   ```bash
   #!/bin/bash
   podman run --rm -it newsboat-app
   ```

6. **Make the script executable**:
   ```bash
   chmod +x ~/launch-newsboat.sh
   ```

7. **Create a `.desktop` file for the containerized Newsboat**:
   Follow the same steps as in **Approach 1**, but change the **Exec** line to run the launcher script:
   ```ini
   Exec=gnome-terminal -- bash -c "~/launch-newsboat.sh; exec bash"
   ```

8. **Run your app**:
   You can now launch the containerized Newsboat "app" from your **application launcher**.

### Approach 3: Use `tmux` or `screen` to Start Custom Terminal Sessions
Another approach is to use **`tmux`** or **`screen`** to start a pre-configured terminal session. This isn’t containerized, but it gives you a persistent or scripted terminal environment where Newsboat opens automatically.

1. **Install `tmux`**:
   ```bash
   sudo dnf install tmux
   ```

2. **Create a Script to Start Newsboat in `tmux`**:
   ```bash
   nano ~/start-newsboat.sh
   ```

3. **Add the following content**:
   ```bash
   #!/bin/bash
   tmux new-session -d -s newsboat_session "newsboat"
   tmux attach -t newsboat_session
   ```

4. **Make the script executable**:
   ```bash
   chmod +x ~/start-newsboat.sh
   ```

5. **Create a `.desktop` file** to launch this script:
   Follow the steps in **Approach 1** to create a `.desktop` file and point the **Exec** line to this script:
   ```ini
   Exec=gnome-terminal -- bash -c "~/start-newsboat.sh; exec bash"
   ```

6. **Launch the "app"**:
   Your app will now open **tmux** and automatically start a session with **Newsboat** running.

### Approach 4: Use a Systemd Service to Auto-Launch a Terminal App
You can also create a **Systemd service** that starts a terminal application like **Newsboat** on demand, but that might be overkill for your use case. The `.desktop` file solution is simpler for managing terminal apps with ease.

---

### Conclusion:
The most straightforward way to create a terminal "app" in Fedora is by creating a **`.desktop` file** that launches a terminal instance with the desired application (like **Newsboat**) already running. If you want isolation, you can containerize the app using **Podman** or **Docker** and still launch it through a `.desktop` file or shell script.

Each of these methods gives you a similar "app-like" experience in your application launcher, making it easy to open terminal-based tools quickly.