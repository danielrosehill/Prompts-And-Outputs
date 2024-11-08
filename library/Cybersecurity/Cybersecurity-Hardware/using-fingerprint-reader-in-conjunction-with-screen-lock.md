---
title: "Using fingerprint reader in conjunction with screen lock"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To use your **fingerprint reader** (such as the DigitalPersona 4500) in conjunction with a screen lock to unlock the display on Fedora Linux, follow these steps:

### 1. **Ensure Fingerprint Reader is Set Up**
Make sure that your fingerprint reader is properly installed and set up on Fedora, as described in the previous steps (using `fprintd` and `libfprint`).

### 2. **Install and Enable Fingerprint Authentication**
You need to enable fingerprint authentication to use it with the screen lock:

#### a. **Install Fingerprint Authentication Packages**
Make sure you have the necessary packages installed:
   ```bash
   sudo dnf install fprintd-pam libfprint
   ```

#### b. **Enroll Your Fingerprint**
Enroll your fingerprint to link it to your user account:

   1. Open a terminal and run:
      ```bash
      fprintd-enroll
      ```
   2. Follow the prompts to scan your fingerprint and complete the enrollment process.

### 3. **Enable Fingerprint Authentication for Login and Screen Unlock**

#### a. **Using the GUI (Gnome Settings)**

1. **Go to Settings**: Open the "Settings" app.
2. **Access User Settings**: Navigate to **Users**.
3. **Enable Fingerprint Login**: Find your user account and enable the **Fingerprint Login** option.
4. **Add Fingerprint**: You may be prompted to scan your fingerprint if you haven't already.

#### b. **Using PAM (Pluggable Authentication Modules) for CLI**
To enable fingerprint authentication for login and screen unlocking, Fedora uses PAM (Pluggable Authentication Modules). PAM configuration files control how the system handles authentication.

1. Edit the PAM configuration to enable fingerprint-based login:
   
   Open the configuration file for `gdm` (the login manager) and `login` (the terminal login):
   
   ```bash
   sudo nano /etc/pam.d/gdm-password
   sudo nano /etc/pam.d/login
   ```

2. In both files, add the following line at the top to prioritize fingerprint authentication:
   ```bash
   auth      sufficient    pam_fprintd.so
   ```

3. Save and exit the editor (`Ctrl + O` to save, `Ctrl + X` to exit).

4. Now, when you lock your screen, you can unlock it using your fingerprint.

### 4. **Test Fingerprint Authentication for Screen Unlock**

1. Lock your screen using the shortcut `Super + L` (Super is usually the Windows key).
2. On the lock screen, try using your fingerprint to unlock the screen.
   
   If fingerprint authentication is set up correctly, you should be able to unlock the display without entering a password.

### 5. **Enable Fingerprint Unlock for Sudo (Optional)**
If you want to use your fingerprint for sudo access as well, you can configure it for system-wide authentication:

1. Edit the `sudo` PAM configuration file:
   ```bash
   sudo nano /etc/pam.d/sudo
   ```

2. Add the following line at the top:
   ```bash
   auth       sufficient    pam_fprintd.so
   ```

3. Save the changes and exit.

Now, you can authenticate `sudo` commands using your fingerprint as well.

### 6. **Restart the System**
Restart the system to ensure all configurations take effect:
```bash
sudo reboot
```

### Summary of Commands:
1. Install fingerprint-related packages:
   ```bash
   sudo dnf install fprintd-pam libfprint
   ```
2. Enroll your fingerprint:
   ```bash
   fprintd-enroll
   ```
3. Configure PAM:
   - Edit `/etc/pam.d/gdm-password` and `/etc/pam.d/login` to include:
     ```bash
     auth      sufficient    pam_fprintd.so
     ```
4. Test by locking your screen (`Super + L`) and unlocking with your fingerprint.

This setup should allow you to unlock the screen and authenticate using your fingerprint reader in Fedora Linux.