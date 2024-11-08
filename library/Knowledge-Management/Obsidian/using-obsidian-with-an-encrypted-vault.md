---
title: "Using Obsidian with an encrypted vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please provide an overview of how you can use Obsidian with the vault contents being encrypted, if this is possible. Could the sync with B2 still work? 

# Output

Using **Obsidian** with encrypted vault contents is possible, but it requires additional tools since Obsidian itself doesn't natively support encryption for vaults. Here's an overview of how you can achieve this, including how **Backblaze B2** syncing might still work:

### 1. **Encrypting Your Obsidian Vault**
To encrypt the contents of your Obsidian vault, you can use external encryption tools such as:

- **Cryptomator**: This is a popular, open-source tool that encrypts files and folders. You can create an encrypted vault using Cryptomator, store your Obsidian vault within it, and access the vault via Cryptomator's virtual drive.
  - **How It Works**: Cryptomator encrypts files on the fly, and when you open the vault, you’ll be able to access the files as if they’re stored in a regular folder. When the vault is closed, the contents are fully encrypted.
  - **Obsidian Compatibility**: You can point Obsidian to the Cryptomator drive (where the decrypted files are temporarily mounted) and work within your vault as usual. When you’re done, close the Cryptomator vault to encrypt the files again.

- **VeraCrypt**: Another open-source encryption tool that works similarly to Cryptomator. You create a secure volume (a virtual disk) that is encrypted, and you can mount and unmount it as needed. The Obsidian vault can be stored in this encrypted volume.
  - **How It Works**: Similar to Cryptomator, you’ll mount the encrypted volume when you want to work on your vault, and Obsidian will access the unencrypted version while the volume is mounted.
  
### 2. **Syncing with Backblaze B2**
If you want to sync your encrypted vault with **Backblaze B2** for cloud backups, here’s how it would work:

- **Encryption Tools and Syncing**: Both Cryptomator and VeraCrypt store encrypted files on your disk, and those files can be synced to the cloud. Since the contents are encrypted, the data stored on Backblaze B2 will remain secure even if Backblaze is compromised.
  - **Backblaze Integration**: You can use **rclone** to sync your encrypted files with Backblaze B2. Rclone supports syncing with B2 directly and can handle large files efficiently. If you're using Cryptomator or VeraCrypt, you would sync the **encrypted vault folder** (not the decrypted files) to Backblaze.
  - **Automation**: You can schedule rclone to automatically sync your encrypted vault with Backblaze at regular intervals, ensuring your backups are up-to-date while maintaining encryption.

### 3. **Workflow Overview**
1. **Create the Encrypted Vault**: Use Cryptomator or VeraCrypt to create an encrypted vault, and store your Obsidian notes inside the encrypted vault.
   
2. **Mount and Work**: When you need to work on your notes, mount the encrypted vault and point Obsidian to the decrypted contents (the virtual drive).

3. **Sync to B2**: Use **rclone** to sync the encrypted files (from the encrypted vault, not the decrypted version) to Backblaze B2 for cloud storage.

4. **Close the Vault**: Once you’re done, unmount the encrypted vault. The contents will remain securely encrypted both locally and in the cloud.

### 4. **Considerations**
- **Performance**: There may be a slight performance hit when working with encrypted files, but modern encryption tools like Cryptomator and VeraCrypt are optimized to minimize overhead.
- **Automation**: Ensure that the sync process with Backblaze B2 is automated to keep your backups consistent without needing manual intervention.

### Conclusion
Using **Obsidian** with encrypted vault contents is entirely feasible using tools like Cryptomator or VeraCrypt. You can continue syncing your encrypted vault to **Backblaze B2** using tools like **rclone**, ensuring your data remains secure both locally and in the cloud. While Obsidian doesn't handle encryption natively, these external solutions integrate well with the platform.