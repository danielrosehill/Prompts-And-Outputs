---
title: "How to use private files in a public repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I mean though if I want to use this repo from another computer. I'll need all the files in the repo. But I still don't want them to be accessible to others

# Output

If you want to sync **all files** (including the private ones) across multiple machines, but **keep them hidden from others** who may access the repository, you'll need to take a slightly different approach. Since Git by itself doesn't support "private files" in a public repo, you have two main options to achieve this:

### Option 1: Use **Encrypted Files**
You can store sensitive files or folders in the repository in an **encrypted format**, ensuring that only those who have the decryption key (like you on your other machines) can access and decrypt them.

- **How it works**: Files are stored in the repository but **encrypted**, making them unreadable to others without the correct key.

#### Tools for Encryption in Git:

1. **git-crypt**:
   - `git-crypt` allows you to automatically **encrypt certain files** in the repository using symmetric encryption.
   - You and trusted collaborators can decrypt and work with the files, but to others, the files appear as encrypted blobs.
   
   **Setup Process**:
   - Install `git-crypt` on all computers where you need access to the repository:
     ```bash
     sudo apt-get install git-crypt  # On Ubuntu/Debian
     ```
   - Initialize `git-crypt` in your repository:
     ```bash
     git-crypt init
     ```
   - Define the files or folders to be encrypted in `.gitattributes`. For example, to encrypt `.obsidian`:
     ```bash
     .obsidian/* filter=git-crypt
     ```
   - Add **GPG keys** for collaborators (or just for yourself) so that only certain people can decrypt the files.

2. **BlackBox** (by StackExchange):
   - `BlackBox` works similarly to `git-crypt`, allowing you to encrypt files before committing them to the repository.
   - This tool is useful for teams but also works well for individuals who need to keep private files synced across machines.

   **Setup Process**:
   - Install `BlackBox` and configure it in your repository.
   - Encrypt specific files (e.g., `.obsidian/*`).
   - Use `blackbox_edit` to decrypt the files when you need to work with them, and they will remain encrypted for others.

---

### Option 2: Use a **Private Fork** or **Separate Private Repo for Sensitive Files**
Another approach is to create a **separate private repository** for the sensitive files (or fork the main repo into a private one), syncing between the two as necessary. This keeps the sensitive files **out of the public repo** altogether while allowing you to use them across machines.

#### Steps:
1. **Public Repository**: The main repository remains public, but it doesn't contain your sensitive files or folders (e.g., `.obsidian`).
2. **Private Repository**: You create a private repository (or private fork) that contains your sensitive files and is only accessible by you (or selected collaborators).
   - You can use a tool like [**Git Submodules**](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to include the private repo within the public repo without exposing its contents.

   **Example**:
   - Public repo (GitHub): Contains all non-sensitive project files.
   - Private repo (GitHub or another service): Contains `.obsidian` and other sensitive files.
   - On your machine, use submodules to bring both repositories together:
     ```bash
     git submodule add git@github.com:your-private-repo.git private-folder
     ```
     This way, you can work with both repos seamlessly, but others who clone the public repo won’t have access to the private one.

---

### Option 3: Manual Sync (Less Ideal)
You could keep the private files **out of the public repo** and **sync them manually** between your devices using other tools, such as **rsync**, **cloud storage**, or private file-sharing services. While this doesn't integrate the files into Git directly, it ensures your private files are still synced.

#### Example:
- Use a service like **Dropbox**, **Google Drive**, or a private **NAS** to sync the `.obsidian` folder between devices while excluding it from the Git repo.
- Sync only non-sensitive parts of the project in the public repo.

---

### Conclusion
If you need all files in the repo across multiple machines while keeping them hidden from others:

1. **Encryption (e.g., git-crypt)** is the most seamless solution. It allows you to store all files in the repo, but only you (and authorized users) can decrypt them.
2. **Using a private repo for sensitive files** (or submodules) is another way to keep certain files completely separate from the public repo while syncing them privately.
   
If you need more details on setting up any of these methods, feel free to ask!