---
title: "Guide to installing SSH on new containers"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here's a detailed guide to help you install and configure **SSH**, **rsync**, and enable **root access with password connectivity** on your new Ubuntu LXC container.

### **1. Install SSH Server**

To install the **OpenSSH server** on your container, follow these steps:

1. **Update the package list**:
   ```bash
   sudo apt update
   ```

2. **Install the OpenSSH server**:
   ```bash
   sudo apt install openssh-server
   ```

3. **Verify SSH is installed**:
   You can check the status of the SSH service:
   ```bash
   sudo systemctl status ssh
   ```
   - If the output shows **"active (running)"**, SSH is already up.
   - If SSH is not running, start it:
     ```bash
     sudo systemctl start ssh
     ```

4. **Enable SSH to start on boot**:
   Ensure that the SSH service starts automatically on boot:
   ```bash
   sudo systemctl enable ssh
   ```

---

### **2. Install Rsync**

You can install `rsync` to efficiently transfer and synchronize files between different systems:

1. **Install rsync**:
   ```bash
   sudo apt install rsync
   ```

2. **Verify rsync installation**:
   Confirm that `rsync` is installed by checking the version:
   ```bash
   rsync --version
   ```

---

### **3. Enable Root Access and Password Connectivity**

By default, **root login** and **password authentication** may be disabled for SSH on Ubuntu. Here's how to enable them:

#### **Step 1: Allow Root Login**

1. **Edit the SSH configuration file**:
   Open the SSH configuration file (`sshd_config`) in your favorite editor:
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

2. **Find and modify the `PermitRootLogin` directive**:
   Look for this line:
   ```bash
   PermitRootLogin prohibit-password
   ```
   - Change it to:
     ```bash
     PermitRootLogin yes
     ```

3. **Enable Password Authentication**:
   Ensure password-based login is allowed. Look for the `PasswordAuthentication` directive, and set it to `yes`:
   ```bash
   PasswordAuthentication yes
   ```

4. **Save and exit** the file:
   - In `nano`, press `Ctrl + O` to save, then `Ctrl + X` to exit the editor.

5. **Restart the SSH service** to apply the changes:
   ```bash
   sudo systemctl restart ssh
   ```

#### **Step 2: Set a Root Password**

If the root account does not have a password set, you need to assign one:

1. **Set the root password**:
   ```bash
   sudo passwd root
   ```

2. **Enter the new password** when prompted.

---

### **4. Check Firewall Settings**

Ensure that your firewall allows incoming SSH connections.

1. If you're using **UFW**, allow SSH:
   ```bash
   sudo ufw allow ssh
   sudo ufw reload
   ```

2. If using `iptables`, check if SSH traffic is allowed:
   ```bash
   sudo iptables -L | grep ssh
   ```

---

### **5. Test SSH Access**

After setting up SSH, root login, and password authentication, you can test SSH access from another machine:

```bash
ssh root@<container-ip-address>
```

---

### Summary:

1. **Install SSH server**: `sudo apt install openssh-server`
2. **Install rsync**: `sudo apt install rsync`
3. **Enable root access and password login**:
   - Modify `/etc/ssh/sshd_config` to set `PermitRootLogin yes` and `PasswordAuthentication yes`
   - Restart SSH with `sudo systemctl restart ssh`
   - Set the root password: `sudo passwd root`
4. **Check firewall settings** to allow SSH traffic.

Let me know if you need further assistance!