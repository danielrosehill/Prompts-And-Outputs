---
title: "How does using encryption via a plugin differ from storing the vault in an encrypted vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. But I'd love to know how this works. E2E is working which is what's important. But I'm not using an encrypted local vault as we discussed yesterday. I can read my vault contents on my local machine normally as if they were regular files. So at what point is the encryption actually taking place?

# Output

Great question! It sounds like you're seeing **end-to-end encryption (E2EE)** in action, where your **local vault** is in plaintext, but the data stored on Backblaze B2 is encrypted. Let’s break down where and how this encryption likely occurs:

### **1. Client-Side Encryption in the Syncing Process**

In your setup, it seems that the **sync plugin or tool** you're using is responsible for encrypting your data **before it gets uploaded to the cloud** (Backblaze B2). This is typical of tools that offer **end-to-end encryption (E2EE)**. Here's how it works:

- **Local Vault (Plaintext)**: On your local machine (e.g., your Android device or desktop), the vault files are stored in **plain text**. This means you can access, read, and modify these files normally without encryption. This is convenient because it allows you to use your vault as if it were just a regular folder of files.
  
- **Sync Process (Encryption Happens Here)**: When you use a sync plugin (like Obsidian’s Remote Sync or another third-party syncing tool), it steps in during the **syncing process** to encrypt the files **before uploading** them to the cloud storage provider (Backblaze B2 in this case). Encryption happens:
  - The **plugin encrypts the file contents** and possibly the file names.
  - The encrypted files are then **uploaded to the cloud** (Backblaze B2) as unreadable garbled data, protecting them from anyone who might try to access your cloud storage.

- **Cloud Storage (Encrypted)**: The data stored in Backblaze B2 (or any remote storage) is **already encrypted** by the time it reaches the cloud. So, even if someone were to access your B2 storage, they would only see the **encrypted files** (as in your screenshot), which are unreadable without the decryption key.

### **2. Decryption Happens When Syncing Back to Your Local Machine**

The encryption and decryption are handled entirely by the sync plugin or tool, **transparently** to you. This means:

- When the data is downloaded back to your local machine, the sync plugin **decrypts the data** on the fly, so you always have access to the readable, plain-text files locally.
- You’re essentially working with plaintext files locally, but as soon as you sync, the files are encrypted, transferred, and stored securely in the cloud.

### **Why You Can Read Files Locally**:
You can read and work with the files locally as plaintext because the **encryption only happens during the sync process**, not when the files are stored locally on your machine. When the sync plugin downloads files from the cloud, it decrypts them so that you can continue working with them in their original, readable form.

### **3. Encryption Key Management**:
The encryption keys used for encrypting and decrypting your vault contents are typically managed by the sync tool or plugin. Commonly:
- **Keys are stored locally** on your device, ensuring that only you (or devices with the keys) can decrypt the files.
- The **keys never leave your device**, meaning the cloud provider (Backblaze B2) or any third party does not have access to them.
- If you're syncing between multiple devices (e.g., desktop and Android), both devices have access to the decryption key.

### **4. Encryption Layers**:
The encryption you’re seeing is **client-side encryption**. There are two potential encryption layers here:
- **Client-side encryption**: Your sync plugin encrypts the files on your local machine before uploading them. The keys for this encryption reside on your local machine, providing **end-to-end encryption**.
- **Server-side encryption**: Backblaze B2 itself provides **server-side encryption** (which is on by default) to encrypt data once it arrives on their servers. However, since the files are already encrypted by the client (via the sync plugin), B2 would just encrypt the already-encrypted files, adding an extra layer of protection.

### **5. What is Actually Happening:**
1. **Local plaintext vault**: You work with plaintext files on your local device (laptop/phone).
2. **Encryption during sync**: When the files are synced (uploaded) to Backblaze B2 via your sync plugin, they are **encrypted client-side**.
3. **Encrypted data on B2**: The data stored in Backblaze B2 is already encrypted by the time it reaches the cloud.
4. **Decryption upon download**: When you download files via the sync tool, the files are **decrypted** back into plaintext so you can use them.

### **6. Example Tools that Work This Way**:
- **Obsidian Sync**: If you’re using Obsidian’s built-in sync tool with encryption enabled, this is exactly how it works. It encrypts your files before they are uploaded to Obsidian’s servers (or another cloud provider like B2).
- **Syncthing (with encryption)**: This open-source tool also offers encrypted synchronization, making sure that files are encrypted before they leave your device and are decrypted only when they reach a trusted device.
- **rclone (with crypt)**: rclone can also do this with its `crypt` feature, but in your case, it’s likely the sync plugin (like Obsidian Sync) doing the encryption.

---

### **Summary:**
- The **encryption** happens **during the sync process** by your sync plugin.
- Your **local vault is not encrypted**, so you can read the files as normal.
- **Files are encrypted** before they are uploaded to **Backblaze B2**, ensuring that the data is protected in the cloud.
- When you sync the data back to another device (or the same device), the plugin **decrypts the files** for local use.

This process provides you with the convenience of working with plaintext files locally while ensuring the safety of your data in the cloud through encryption.

Let me know if you’d like to explore any specific aspect of this process further!