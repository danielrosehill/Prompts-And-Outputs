---
title: "Access fedora remotely"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To access your Fedora Linux desktop from your Android phone in an unattended manner, with the ability to lock the screen, put the computer to sleep, and turn it off, I recommend the following tools:

1. RustDesk (Remote Desktop)

Overview: RustDesk is an open-source alternative to popular remote desktop solutions like TeamViewer and AnyDesk. It allows remote access with no need for third-party cloud servers. You can set it up for unattended access, meaning no login prompts are required on the desktop.

Key Features:

Unattended access to your Fedora system from your Android device.

Easy setup for screen locking and putting the computer to sleep.

Open-source with strong security protocols.


Setup Steps:

1. Install RustDesk on Fedora using a package manager or by downloading it from RustDesk’s official website.


2. Install the Android app from the Google Play Store.


3. Set up unattended access by configuring a password or secure key.




2. VNC (Virtual Network Computing)

Overview: VNC is a widely used tool that allows remote desktop access. You can use a VNC server on your Fedora Linux and connect using a VNC client from your Android phone.

Key Features:

Full control of the desktop remotely, including locking the screen, putting the computer to sleep, and shutting it down.

Can be configured for unattended access by storing a password for automatic login.


Setup Steps:

1. Install a VNC server on your Fedora system, such as TigerVNC or x11vnc.


2. Install a VNC viewer on your Android device, such as VNC Viewer from RealVNC.


3. Configure VNC on Fedora to allow unattended access with a stored password.




3. SSH with Termux (for Command-line Control)

Overview: If you’re comfortable with command-line access, you can use SSH to remotely control your Fedora system and execute commands to lock the screen, suspend the system, or shut it down.

Key Features:

Complete control via terminal commands.

You can easily script common actions like locking the screen or putting the system to sleep.


Setup Steps:

1. Install openssh-server on Fedora and enable SSH access.


2. Install Termux or any SSH client on your Android device.


3. Use SSH commands to control the computer:

Lock screen: loginctl lock-session

Suspend: systemctl suspend

Shutdown: systemctl poweroff





4. RDP (Remote Desktop Protocol) with xRDP

Overview: RDP provides a remote desktop experience and can be configured for unattended access. With xRDP, you can access Fedora from an Android device with an RDP client.

Key Features:

Full desktop access with the ability to manage power states.

Easy to configure for unattended logins.


Setup Steps:

1. Install xrdp on Fedora using the package manager.


2. Install a Remote Desktop client on your Android device (e.g., Microsoft Remote Desktop).


3. Set up unattended access with pre-stored credentials.




These solutions offer various levels of remote control, and you can select the one that best fits your preference for either GUI (RustDesk, VNC, RDP) or terminal control (SSH).

