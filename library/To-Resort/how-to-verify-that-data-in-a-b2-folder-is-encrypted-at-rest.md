---
title: "How to verify that data in a B2 folder is encrypted at rest"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please tell me how I can verify that the contents of a directory in B2 are encrypted at rest i used this command: rclone lsf yourbusinessb2:danielnotepad --dirs-only And vaultdata is showing up correctly This is my sync folder containing the vault and I am hoping that everything within it is encfypted

# Clarification based on first response

No. I'm not using rclone to sync with B2. That's being handled by the remote sync plugin. What I would like to do is do a spot check to make sure that the data I can see in the server is not in plain text

# Output


Got it! Since you're not using `rclone` for encryption and the **remote sync plugin** (likely Obsidian's "Remote Sync" plugin or a similar tool) is handling the sync with Backblaze B2, you'd like to ensure that the data on the **B2 server** is not stored in plain text.

Here’s how you can **spot-check** to ensure your data is not visible in plain text on **Backblaze B2**:

### **Steps for Spot Checking Data Encryption on Backblaze B2:**

1. **Login to Your Backblaze B2 Account**:
   - Go to [Backblaze B2](https://secure.backblaze.com/) and log in to your account.

2. **Navigate to the Bucket Containing Your Data**:
   - Once logged in, go to **Buckets** and find the bucket containing your `danielnotepad` directory (or the bucket where your Obsidian vault is stored).
   
3. **Browse the Bucket**:
   - Navigate to the folder or files you want to spot-check, such as `danielnotepad/vaultdata/`.
   
4. **Download a File**:
   - Download one or more files (preferably a **Markdown file** or any text-based file) from the server to your local system.
   
5. **Open the File Locally**:
   - Open the downloaded file using a simple text editor (e.g., **Notepad**, **Kate**, **Sublime Text**) and check if the contents are in plain text or unreadable (i.e., encrypted).

### **What to Look For**:

- **If the file contents are unreadable** (e.g., garbled or encoded), this means the data is **encrypted** on the server.
- **If the file is in plain text** (e.g., a readable Markdown file or other plaintext), the data is **not encrypted at rest**.

### **Confirming Encryption**:
If the file appears garbled or unreadable, the sync plugin you're using is encrypting the data before uploading it to Backblaze B2. If it's in plain text, this means the data is stored as-is (without encryption) on the server.

### **Note**: 
If you're expecting encryption, check the plugin or method you're using for synchronization to confirm whether it supports **client-side encryption**. Not all sync plugins encrypt data before uploading to the cloud. If encryption is crucial for your workflow, make sure the plugin you're using has encryption features, or consider using **rclone** or another tool for client-side encryption.

### **Encryption Recommendations**:
If you find that the data is in plain text and want to encrypt it before uploading, you can:

- **Use rclone with encryption**: Set up an encrypted `rclone` remote for Backblaze B2 and sync your data using this encrypted remote.
- **Use the Obsidian Vault Encryption Plugin**: There are encryption-related plugins for Obsidian that encrypt the contents of the vault locally before syncing them to remote services.

Let me know if you need further assistance in checking or configuring encryption!