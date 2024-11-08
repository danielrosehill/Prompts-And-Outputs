---
title: "Screen locker for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here’s a list of **screen locking utilities** that work with **Fedora** running **KDE Plasma**, and some also support **fingerprint reader integration** for unlocking the device:

### 1. **KDE Plasma’s Built-in Screen Locker**
   - **Description**: KDE Plasma comes with a **built-in screen locker** that integrates well with fingerprint authentication on Fedora. It’s the default lock screen utility for KDE, and it supports both password and fingerprint unlock (provided fingerprint authentication is enabled).
   - **How to Enable Fingerprint Authentication**:
     1. Go to **System Settings** > **Users**.
     2. Click on your user account and set up your **fingerprint** under **Fingerprint Login**.
     3. Once enabled, your fingerprint will work to unlock the screen.
   - **Link**: [KDE Plasma Lock Screen](https://userbase.kde.org/Plasma)

### 2. **SDDM (Simple Desktop Display Manager)**
   - **Description**: **SDDM** is the default display and lock screen manager for KDE Plasma on Fedora. It supports fingerprint login via **PAM** (Pluggable Authentication Modules).
   - **How to Enable Fingerprint Unlock**:
     1. Ensure **fprintd** (Fingerprint PAM module) is installed:
        ```bash
        sudo dnf install fprintd-pam
        ```
     2. Register your fingerprint using:
        ```bash
        fprintd-enroll
        ```
     3. Enable fingerprint unlocking by editing `/etc/pam.d/sddm` and adding `pam_fprintd.so` to the PAM authentication stack.
   - **Link**: [SDDM](https://github.com/sddm/sddm)

### 3. **XSecureLock**
   - **Description**: **XSecureLock** is an alternative screen locker designed to be lightweight and compatible with various desktop environments, including KDE Plasma. It can be configured to use fingerprint unlocking via PAM.
   - **Fingerprint Integration**: XSecureLock can work with **PAM** to unlock the device using fingerprint authentication if configured properly with **fprintd**.
   - **Install on Fedora**:
     ```bash
     sudo dnf install xsecurelock
     ```
   - **Link**: [XSecureLock GitHub](https://github.com/google/xsecurelock)

### 4. **i3lock**
   - **Description**: **i3lock** is a simple screen locker that works well with Fedora and KDE Plasma. While it doesn’t natively support fingerprint unlocking, it can be configured with **PAM** to work with **fprintd** for fingerprint authentication.
   - **How to Integrate Fingerprint Unlock**:
     1. Install **i3lock**:
        ```bash
        sudo dnf install i3lock
        ```
     2. Integrate **fprintd** by configuring the PAM stack, similar to SDDM.
   - **Link**: [i3lock GitHub](https://github.com/i3/i3lock)

### 5. **LightDM**
   - **Description**: **LightDM** is another popular display manager that is compatible with KDE Plasma. Like SDDM, it supports **fingerprint authentication** via PAM integration.
   - **Setup Fingerprint Unlock**:
     1. Install **LightDM**:
        ```bash
        sudo dnf install lightdm
        ```
     2. Configure **fprintd** for fingerprint authentication with LightDM.
   - **Link**: [LightDM](https://github.com/canonical/lightdm)

### 6. **betterlockscreen**
   - **Description**: **betterlockscreen** is a highly customizable lock screen tool that works with various window managers and desktop environments, including KDE Plasma. It can be configured with **PAM** to support fingerprint unlocking.
   - **Installation on Fedora**:
     ```bash
     sudo dnf install betterlockscreen
     ```
   - **Fingerprint Unlock Setup**: Follow the same steps as for i3lock to configure **PAM** for fingerprint integration.
   - **Link**: [betterlockscreen GitHub](https://github.com/pavanjadhaw/betterlockscreen)

### 7. **Light Locker**
   - **Description**: **Light Locker** is a lightweight screen locker designed for Xfce, but it also works with KDE Plasma. It can be configured to use fingerprint unlocking with **PAM**.
   - **Installation**:
     ```bash
     sudo dnf install light-locker
     ```
   - **PAM Integration**: Like with other PAM-based tools, configure **fprintd** for fingerprint unlocking.
   - **Link**: [Light Locker GitHub](https://github.com/the-cavalry/light-locker)

### General Fingerprint Setup on Fedora
For any screen locker to support **fingerprint unlocking**, you need to set up fingerprint authentication using **fprintd**:
1. Install the **fprintd** package if it's not already installed:
   ```bash
   sudo dnf install fprintd fprintd-pam
   ```
2. Enroll your fingerprint:
   ```bash
   fprintd-enroll
   ```
3. Integrate fingerprint authentication into your lock screen by modifying the relevant **PAM** configuration files, such as `/etc/pam.d/sssd`, `/etc/pam.d/login`, or `/etc/pam.d/sddm`.

These screen lockers should integrate well with **Fedora** and **KDE Plasma**, and with some configuration, they can support **fingerprint unlocking** via **fprintd** and **PAM**.