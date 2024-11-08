---
title: "What's a good basic standard of encryption to use today"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Alright. You've got me sold. So in 2024 what's a good basic standard of encryption I could use if I wanted to encrypt some of my data at rest

# Output

Great to hear you're sold on the value of encryption! In 2024, there are several widely accepted standards for encrypting data at rest that are both secure and practical for most users. Here’s a basic guide on what encryption algorithms and tools to use:

### **Basic Standard of Encryption for 2024: AES-256**

The **Advanced Encryption Standard (AES-256)** is the most widely recommended and secure symmetric encryption algorithm available. It's used by governments, militaries, and large enterprises globally to protect data. Here's why:

- **AES-256**: This means AES with a 256-bit key length, offering a very high level of security. It would take an enormous amount of computing power and time to break AES-256 with a brute force attack (essentially infeasible with current technology).
- **Widely Adopted**: AES-256 is a standard in tools like full-disk encryption, file encryption, and cloud encryption services. It's the default encryption for many modern applications.
  
### **How to Use AES-256 Encryption for Data at Rest**

Here are some tools and methods you can use to encrypt your data at rest using AES-256:

#### **1. Full-Disk Encryption (FDE) for Your Computer**
Encrypting your entire hard drive ensures that if your device is lost or stolen, no one can access your files without the encryption key or password.

- **Linux (Fedora)**: 
  - **LUKS (Linux Unified Key Setup)**: This is the default disk encryption system for most Linux distributions, including Fedora. When setting up Fedora, you can choose to encrypt the entire disk using LUKS with AES-256. It ensures that all data at rest is encrypted.
    - To check if LUKS is active or to set it up post-installation: 
      ```
      sudo cryptsetup luksFormat /dev/sdX
      ```
    - Use LUKS with **dm-crypt** to handle your encryption transparently once the system is unlocked at boot.

- **Windows**: 
  - **BitLocker**: BitLocker uses AES-256 by default on supported systems and provides full-disk encryption. It's easy to set up through Windows Security Settings.
  
- **macOS**: 
  - **FileVault**: Apple's FileVault uses XTS-AES-128 encryption (AES with a 256-bit key length is also available) to encrypt the entire disk. It’s built into macOS and can be enabled from System Preferences.

#### **2. File-Level Encryption**
If you don’t want to encrypt your entire disk but just specific files or folders, there are a variety of tools that use AES-256 encryption:

- **VeraCrypt** (cross-platform):
  - VeraCrypt is a highly respected tool for creating encrypted containers or full disk encryption. It uses AES-256 (or other encryption algorithms like Serpent or Twofish if you prefer) to encrypt files, folders, or even entire partitions.
  - You can create a secure “vault” (an encrypted container) that stores sensitive data, which you can mount like a normal drive when you need access.
  
- **gocryptfs** (Linux):
  - **gocryptfs** is a FUSE-based file system encryption tool that encrypts individual files with AES-256. It’s simple and lightweight, designed for Linux users who need efficient, file-based encryption.
  
- **Cryptomator** (cross-platform, cloud-focused):
  - Cryptomator encrypts files and folders before they are synced to cloud storage providers like Dropbox, Google Drive, or Backblaze B2. It uses AES-256 to ensure that your files remain private, even if someone gains access to your cloud storage.
  
- **7-Zip** (cross-platform):
  - 7-Zip allows you to compress and encrypt files using AES-256. While it's primarily a compression tool, its encryption feature is useful for securing individual files or archives.

#### **3. Encrypted Cloud Storage**
Many cloud storage services offer end-to-end encryption (E2EE) or allow you to encrypt files before uploading them. This ensures that even if someone gains access to your cloud storage, your files are unreadable without the decryption key.

- **Tresorit** (cross-platform):
  - A cloud storage service that uses zero-knowledge, AES-256 encryption by default. Tresorit’s focus is on privacy, and even they cannot access your data.

- **Sync.com** (cross-platform):
  - Sync.com provides E2EE with AES-256, ensuring your files are encrypted before they leave your device and are stored encrypted on their servers.

- **Cryptomator** (mentioned earlier) can be used to add an encryption layer to any cloud storage provider, ensuring that your data remains encrypted before uploading to services like Dropbox or Google Drive.

#### **4. Mobile Encryption for Android**
Since you're using Android devices, it's important to ensure your mobile data is encrypted as well.

- **Android Full-Disk Encryption**:
  - Most modern Android devices come with full-disk encryption enabled by default (using AES-256). You can verify this in your device’s security settings.
  
- **Cryptomator** (Android app):
  - Cryptomator also has an Android app that allows you to encrypt files and folders before uploading them to cloud services.

#### **5. Password Management with Encryption**
Your encryption is only as strong as your key management. Storing encryption keys, passwords, and recovery phrases securely is essential.

- **Bitwarden** (cross-platform, open-source):
  - Bitwarden is a popular password manager that encrypts your passwords using AES-256. It stores your credentials in an encrypted vault, keeping your sensitive information safe.
  
- **KeePassXC** (cross-platform, open-source):
  - KeePassXC is another widely respected password manager that uses AES-256 encryption to secure your passwords in a local database.

### **Best Practices for Encryption in 2024**
1. **Use Strong Passwords or Passphrases**: 
   - Encryption is only as strong as your password or encryption key. Use a long, random password or passphrase to protect your encrypted data. You can use a password manager like Bitwarden to generate and store strong passwords.
   
2. **Enable Two-Factor Authentication (2FA)**:
   - Always enable 2FA where possible, especially for cloud services that store encrypted data (e.g., Tresorit, Sync.com). This adds an extra layer of security in case someone tries to access your account.

3. **Keep Software Up to Date**:
   - Security vulnerabilities in outdated software can undermine even the best encryption systems. Make sure that your operating system and encryption tools are always up to date.

4. **Backup Your Encrypted Data**:
   - Always have backups of your encrypted data, but ensure the backup is also encrypted. Losing access to your encryption key or corrupted storage could result in data loss if you don't have secure backups.

5. **Audit and Test Your Setup**:
   - Periodically test your encrypted data to ensure that you can decrypt it correctly. Also, review your setup to make sure you’re following the latest best practices.

### Conclusion
In 2024, **AES-256** remains the gold standard for encrypting data at rest. Tools like **LUKS**, **VeraCrypt**, **gocryptfs**, **Cryptomator**, and **Bitwarden** make it easy to implement strong encryption on your Fedora system, Android devices, and cloud storage. By combining these tools with strong password management, regular updates, and backups, you can ensure that your data remains safe and private.