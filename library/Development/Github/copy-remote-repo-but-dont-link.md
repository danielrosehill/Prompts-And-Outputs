---
title: "Copy remote repo but don't link"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


---
Prompt: "I would like to find a way to copy files from a remote repository that I own to use it as a skeleton for building out a new repo. What I don't want to do is link the current repo to the remote. I just need a way to pull in the files. Can you recommend how to do this?"
---
To copy files from a remote GitHub repository to use them as a skeleton for building out a new repo without linking the current repository to the remote, you can use the following methods:

### 1. **Using `git archive`**
   `git archive` allows you to export the contents of a remote repository (or specific directories/files within it) as a `.tar.gz` or `.zip` archive without cloning the entire repository.

   **Steps**:
   1. Create an archive of the repository or a specific folder.
   2. Extract the archive in your new repository.

   **Example:**
   ```bash
   curl -L https://github.com/username/repository/archive/refs/heads/main.tar.gz | tar -xz
   ```

   This command:
   - Downloads the archive of the `main` branch from the specified repository.
   - Extracts it into the current directory.

   If you want to extract only a specific directory, you can do something like this:
   ```bash
   curl -L https://github.com/username/repository/archive/refs/heads/main.tar.gz | tar -xz --strip-components=1 repository-main/path/to/directory
   ```

   Replace `username`, `repository`, and `main` with your GitHub username, repository name, and branch name, respectively. Adjust `path/to/directory` to target a specific folder within the repository.

### 2. **Using `wget` or `curl` for Specific Files**
   If you only need a few specific files, you can use `wget` or `curl` to download individual files.

   **Example with `wget`:**
   ```bash
   wget https://raw.githubusercontent.com/username/repository/main/path/to/file
   ```

   **Example with `curl`:**
   ```bash
   curl -O https://raw.githubusercontent.com/username/repository/main/path/to/file
   ```

   Replace `username`, `repository`, `main`, and `path/to/file` with the appropriate values for the file you want to download.

### 3. **Using `degit`**
   `degit` is a tool specifically designed for this purpose. It fetches the files from a repository without keeping the `.git` history or linking the new repository to the original one.

   **Installation**:
   ```bash
   npm install -g degit
   ```

   **Usage**:
   ```bash
   degit username/repository my-new-repo
   ```

   This command:
   - Downloads the contents of `username/repository` into the `my-new-repo` directory.
   - You can then initialize a new Git repository in `my-new-repo` without any link to the original repository.

### 4. **Using GitHub's `Download ZIP` Option**
   If you want a more manual approach:
   - Navigate to the repository on GitHub.
   - Click the "Code" button.
   - Select "Download ZIP".
   - Extract the downloaded ZIP file to your desired location.
   - Initialize a new Git repository in the extracted directory.

These methods allow you to copy files from your remote repository and use them as a starting point for a new repository without creating any link between the new and original repositories.