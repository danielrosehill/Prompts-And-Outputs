---
title: "Locking and unlocking with the fingerprint reader"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To set up your **DigitalPersona U.are.U 4500** fingerprint reader on **Fedora Linux** with **KDE Plasma on Wayland**, follow these steps to install and configure the required software to unlock and lock your desktop using the device.

### Step 1: Install Required Packages
You'll need to install the fingerprint drivers and utilities for Fedora. These are available through the package manager.

1. **Install `fprintd` and `libfprint`**:
   Open a terminal and run the following commands:
   ```bash
   sudo dnf install fprintd libfprint fprintd-pam
   ```

   - `fprintd`: A fingerprint management service.
   - `libfprint`: The driver library for fingerprint readers.

### Step 2: Verify Fingerprint Reader Detection

Once the drivers are installed, you should check if your **U.are.U 4500** fingerprint reader is detected by the system.

1. **List the fingerprint devices**:
   ```bash
   fprintd-enroll --list-devices
   ```

   This should return a list of recognized fingerprint readers. If your device shows up here, it means the system has detected it and the necessary drivers are installed.

### Step 3: Enroll Your Fingerprint

Now, you need to enroll your fingerprint so the system can use it for authentication.

1. **Enroll your fingerprint**:
   Run the following command to begin enrolling your fingerprint:
   ```bash
   fprintd-enroll
   ```

2. Follow the on-screen instructions to scan your fingerprint multiple times until enrollment is complete.

### Step 4: Enable Fingerprint Authentication for Login and Unlocking

You need to configure **PAM (Pluggable Authentication Modules)** so that fingerprint authentication is used for locking and unlocking the desktop.

#### a. **Configure PAM for KDE Plasma Lock Screen**

PAM is responsible for handling authentication in most Linux environments, including KDE Plasma. You’ll need to enable fingerprint authentication in the PAM configuration files for login and the lock screen.

1. **Edit PAM configuration for login (`gdm-password`)**:
   Since KDE Plasma still relies on the `gdm-password` service (even with SDDM as the display manager), add fingerprint authentication:

   Open the PAM configuration file:
   ```bash
   sudo nano /etc/pam.d/gdm-password
   ```

2. **Add the following line** at the top of the file to enable fingerprint authentication:
   ```bash
   auth    sufficient    pam_fprintd.so
   ```

3. **Edit PAM configuration for SDDM (lock screen)**:
   Open the PAM configuration file for `sddm`:
   ```bash
   sudo nano /etc/pam.d/sddm
   ```

4. **Add the same line** at the top of this file as well:
   ```bash
   auth    sufficient    pam_fprintd.so
   ```

This will enable fingerprint authentication for both login and the lock screen.

#### b. **Configure PAM for Sudo (Optional)**

If you want to use your fingerprint for `sudo` commands as well, you can add the following to the `sudo` PAM configuration file:

1. **Edit the PAM configuration file for `sudo`**:
   ```bash
   sudo nano /etc/pam.d/sudo
   ```

2. **Add the fingerprint line**:
   ```bash
   auth    sufficient    pam_fprintd.so
   ```

This will allow you to authenticate `sudo` commands using your fingerprint.

### Step 5: Test Fingerprint Unlock and Lock

Once the configurations are in place, test your setup by locking the screen and attempting to unlock it using your fingerprint.

1. **Lock your screen**:
   You can use the shortcut `Super + L` (Super is the Windows key) or the system menu to lock your screen.

2. **Unlock with your fingerprint**:
   Place your finger on the **DigitalPersona U.are.U 4500** fingerprint reader. If the setup is successful, the screen should unlock without requiring your password.

### Step 6: Troubleshooting

If fingerprint unlocking doesn't work, try the following steps:

1. **Check PAM configuration**: Make sure you've correctly added the fingerprint authentication line (`auth sufficient pam_fprintd.so`) to the right PAM files (`gdm-password`, `sddm`).
2. **Check system logs**: Review system logs for errors related to `fprintd` by running:
   ```bash
   journalctl -xe | grep fprintd
   ```
3. **Test with other utilities**: Use the following command to test if your fingerprint reader works independently of the lock screen:
   ```bash
   fprintd-verify
   ```
   This will prompt you to verify your fingerprint.

### Step 7: Reboot the System

Finally, reboot your system to ensure all changes take effect:
```bash
sudo reboot
```

---

### Summary of Commands:
1. Install necessary packages:
   ```bash
   sudo dnf install fprintd libfprint fprintd-pam
   ```
2. Enroll your fingerprint:
   ```bash
   fprintd-enroll
   ```
3. Add fingerprint authentication to PAM:
   ```bash
   sudo nano /etc/pam.d/gdm-password
   sudo nano /etc/pam.d/sddm
   ```
   Add `auth sufficient pam_fprintd.so` to both files.
4. Test the setup by locking and unlocking the screen.

By following these steps, you should be able to lock and unlock your Fedora desktop running KDE Plasma with the **DigitalPersona U.are.U 4500** fingerprint reader.