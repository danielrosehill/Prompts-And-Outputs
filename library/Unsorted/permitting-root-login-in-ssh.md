---
title: "Permitting root login in SSH"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To allow other computers to **SSH into the root account** on a Linux system, you need to adjust the SSH server's configuration. By default, many Linux distributions disable SSH access for the root user for security reasons. Here's how you can enable it:

### **Steps to Allow SSH Access for the Root User**

#### 1. **Edit the SSH Configuration File**

You need to modify the SSH server configuration file (`sshd_config`) to allow root login.

1. Open the SSH configuration file using your favorite text editor (e.g., `nano`, `vim`, etc.):
   ```bash
   sudo nano /etc/ssh/sshd_config
   ```

2. Look for the following line:
   ```bash
   PermitRootLogin prohibit-password
   ```

   - **Change it** to:
     ```bash
     PermitRootLogin yes
     ```

   This will allow the root user to log in via SSH using a password. 

3. **Optional (Enable Password Authentication)**:
   If password authentication is disabled for SSH, you also need to ensure it is enabled. Look for the following line in the same file:
   ```bash
   PasswordAuthentication no
   ```

   - **Change it** to:
     ```bash
     PasswordAuthentication yes
     ```

4. Save the changes and exit the text editor (in `nano`, you can press `Ctrl + O` to save and `Ctrl + X` to exit).

#### 2. **Restart the SSH Service**

After making changes to the SSH configuration, you need to restart the SSH service to apply the changes:

```bash
sudo systemctl restart ssh
```

#### 3. **Ensure the Root Account Has a Password**

If the root account does not have a password, set one with the following command:

```bash
sudo passwd root
```

Enter a new password for the root user when prompted.

#### 4. **Check Firewall Settings**

Ensure that the **firewall** (if enabled) allows SSH access:

- If you're using **UFW** (Uncomplicated Firewall), you can allow SSH with:
  ```bash
  sudo ufw allow ssh
  sudo ufw reload
  ```

- If using **iptables**, ensure there are rules allowing SSH traffic:
  ```bash
  sudo iptables -L | grep ssh
  ```

#### 5. **Test the Root SSH Access**

Now, you should be able to SSH into the system as the root user from another machine using the following command:

```bash
ssh root@<your_server_ip>
```

### Important Security Considerations:
- **Allowing root login over SSH** can be a security risk. It is generally recommended to use **non-root users with `sudo` privileges** to perform administrative tasks.
- If you must allow root SSH access, consider using **key-based authentication** rather than password-based authentication for better security.
  
To enforce key-based authentication for root:
1. Disable password-based login for root:
   ```bash
   PermitRootLogin prohibit-password
   ```

2. Copy the SSH public key to the root account's `~/.ssh/authorized_keys` file, and ensure permissions are set correctly:
   ```bash
   chmod 700 ~/.ssh
   chmod 600 ~/.ssh/authorized_keys
   ```

### Conclusion:
1. Modify the **`sshd_config`** to allow root login (`PermitRootLogin yes`).
2. Enable **password authentication** (`PasswordAuthentication yes`) if necessary.
3. Restart the SSH service to apply the changes.
4. Ensure the **root account** has a password, and test the connection.

Let me know if you need further assistance or have more questions!