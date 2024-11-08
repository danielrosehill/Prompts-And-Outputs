---
title: "Additional security for Fedora endpoint"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking about additional ways to protect your **Fedora** computer beyond just running antivirus software.

Besides running an antivirus program, there are several additional layers of protection you can implement to secure your Fedora workstation. These measures will help protect your system from a wide range of threats, including malware, unauthorized access, data breaches, and network attacks.

### 1. **Enable and Configure the Firewall**
   Fedora comes with **firewalld** pre-installed, which is a dynamic firewall manager offering easy control over your system's network security.

   - **Check if firewalld is running**:
     ```bash
     sudo systemctl status firewalld
     ```
   - **Enable firewalld if it's not active**:
     ```bash
     sudo systemctl enable --now firewalld
     ```
   - **Configure firewall rules**: You can use the **firewall-cmd** utility to add rules and open or close specific ports. For example, to allow SSH:
     ```bash
     sudo firewall-cmd --add-service=ssh --permanent
     sudo firewall-cmd --reload
     ```
   - **GUFW**: If you prefer a graphical interface, install **GUFW**, a user-friendly GUI for managing the firewall.
     ```bash
     sudo dnf install gufw
     ```

### 2. **Keep Your System Updated**
   - **Regular Updates**: Keeping your system up-to-date ensures that you have the latest security patches and fixes for vulnerabilities. Fedora’s package manager (DNF) makes this process easy.
     ```bash
     sudo dnf update
     ```
   - Enable automatic updates:
     ```bash
     sudo dnf install dnf-automatic
     sudo systemctl enable --now dnf-automatic.timer
     ```

### 3. **Use SELinux (Security-Enhanced Linux)**
   - **SELinux** is a mandatory access control (MAC) security mechanism that limits processes’ capabilities and access to files and other resources on your system.
   - Fedora comes with **SELinux** enabled by default. You can check its status by running:
     ```bash
     sudo sestatus
     ```
   - If SELinux is not in enforcing mode, you can enable it by editing the configuration file:
     ```bash
     sudo nano /etc/selinux/config
     ```
     Change `SELINUX=permissive` to `SELINUX=enforcing`, then reboot the system.
   - **SELinux Troubleshooter**: If you encounter issues with SELinux, Fedora has a built-in **SELinux Troubleshooter** that helps diagnose and resolve policy violations.
     ```bash
     sudo dnf install setroubleshoot
     ```

### 4. **Use Disk Encryption**
   - **Full-Disk Encryption** (FDE) is essential to protect your data in case your device is lost or stolen. Fedora offers full-disk encryption via **LUKS** (Linux Unified Key Setup).
   - If you didn’t enable disk encryption during installation, you can encrypt specific partitions or external drives using **LUKS**:
     ```bash
     sudo cryptsetup luksFormat /dev/sdX
     sudo cryptsetup luksOpen /dev/sdX my_encrypted_drive
     ```
   - Consider encrypting sensitive files or directories using **GnuPG** (GPG).

### 5. **Configure Secure SSH Access**
   - **Disable Password Authentication**: Use **SSH key-based authentication** instead of passwords to prevent brute-force attacks.
     - Generate SSH keys:
       ```bash
       ssh-keygen -t rsa
       ```
     - Copy your public key to the remote machine:
       ```bash
       ssh-copy-id user@remote_host
       ```
     - Disable password login by editing `/etc/ssh/sshd_config`:
       ```
       PasswordAuthentication no
       ```
     - Restart SSH service:
       ```bash
       sudo systemctl restart sshd
       ```
   - **Limit SSH Access**: Allow SSH only from specific IPs, or change the default SSH port (22) to a non-standard port to reduce exposure to automated attacks.

### 6. **Use a Password Manager**
   - Use a password manager like **Bitwarden**, **KeePassXC**, or **1Password** to securely store and manage your passwords. Password managers can generate strong passwords and reduce the risk of using weak or reused passwords.
   - **KeePassXC** is available on Fedora:
     ```bash
     sudo dnf install keepassxc
     ```

### 7. **Use Two-Factor Authentication (2FA)**
   - Enable **2FA** on all services and accounts where it is available, especially for system-critical applications such as email, SSH access, and sensitive websites.
   - **SSH with 2FA**: You can enable **two-factor authentication** for SSH using **Google Authenticator**:
     ```bash
     sudo dnf install google-authenticator
     google-authenticator
     ```

### 8. **Audit Your System with Lynis**
   - **Lynis** is a security auditing tool for Linux systems. It scans your system for security vulnerabilities and misconfigurations, providing recommendations for hardening.
   - Install and run Lynis:
     ```bash
     sudo dnf install lynis
     sudo lynis audit system
     ```

### 9. **Use Intrusion Detection Systems (IDS)**
   - Consider using **AIDE (Advanced Intrusion Detection Environment)** to detect unauthorized changes to the filesystem.
     - Install and initialize AIDE:
       ```bash
       sudo dnf install aide
       sudo aide --init
       sudo cp /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
       ```
     - To check for changes later:
       ```bash
       sudo aide --check
       ```

### 10. **Install Fail2Ban**
   - **Fail2Ban** helps protect your system by blocking IP addresses that show signs of malicious activity, such as repeated failed login attempts.
   - Install and configure Fail2Ban:
     ```bash
     sudo dnf install fail2ban
     sudo systemctl enable --now fail2ban
     ```
   - Configure Fail2Ban by editing `/etc/fail2ban/jail.local` to protect services like SSH.

### 11. **Browser Security**
   - **Harden your browser**: Use privacy extensions like **uBlock Origin** (adblocker), **HTTPS Everywhere** (force HTTPS connections), and **Privacy Badger** (prevent tracking).
   - Use **firejail** to sandbox your browser:
     ```bash
     sudo dnf install firejail
     firejail firefox
     ```

### 12. **Disable Unnecessary Services**
   - Run the following command to list services and disable those that are unnecessary:
     ```bash
     systemctl list-unit-files --type=service --state=enabled
     ```
   - Disable any unneeded services:
     ```bash
     sudo systemctl disable service_name
     ```

### 13. **Regular Backups**
   - Use tools like **rsync** or **Timeshift** to create regular backups of your important files.
   - Set up automatic backups with tools like **Deja Dup**:
     ```bash
     sudo dnf install deja-dup
     ```

### 14. **Use a VPN for Network Security**
   - Use a **VPN** to encrypt your internet connection and protect your privacy when browsing, especially on unsecured networks.
   - Fedora has built-in support for **OpenVPN**, **WireGuard**, and other VPN clients:
     ```bash
     sudo dnf install wireguard-tools
     ```

### 15. **Use AppArmor or SELinux Profiles for Additional Security**
   - Consider fine-tuning SELinux policies for applications that have higher risks. Alternatively, install **AppArmor** for application sandboxing if you prefer.

---

### Conclusion:
In addition to running antivirus software, you can significantly improve the security of your Fedora workstation by enabling a firewall, keeping your system updated, utilizing SELinux, encrypting your disks, securing SSH access, and implementing two-factor authentication. Regular system audits using tools like **Lynis** and intrusion detection with **AIDE** or **Fail2Ban** will further enhance your security posture.

Let me know if you'd like assistance setting up any of these tools!