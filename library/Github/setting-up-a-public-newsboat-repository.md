---
title: "Setting up a public Newsboat repository"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you give me a guide on how to to sync my newsboat config with Github? I ended up not using the dotfiles system. I want to exclude cache.db I've already set up the remote repo here: https://github.com/danielrosehill/Newsboat-Israel-Feeds.git so I just want to hide cache and do an initial push (and maybe set up a basic config also

# Output

Here’s a step-by-step guide to **syncing your Newsboat configuration** with GitHub while **excluding the cache file (`cache.db`)**. You’ll push your configuration to the remote repository you've already set up: [https://github.com/danielrosehill/Newsboat-Israel-Feeds.git](https://github.com/danielrosehill/Newsboat-Israel-Feeds.git).

### Step 1: Set Up Your `.gitignore` to Exclude Cache Files
You want to ensure that **`cache.db`** (and any other unwanted files) are excluded from your Git repository.

1. **Navigate to your Newsboat directory**:
   ```bash
   cd ~/.newsboat
   ```

2. **Create a `.gitignore` file** (if you don’t already have one):
   ```bash
   nano .gitignore
   ```

3. **Add the following lines** to exclude `cache.db` and other temporary files that Newsboat generates:
   ```plaintext
   cache.db
   queue
   downloaded-enclosures
   ```

   - `cache.db`: Stores Newsboat's cache of articles, which you don't need to sync.
   - `queue`: Stores a list of URLs queued for download.
   - `downloaded-enclosures`: Stores downloaded podcast episodes or other enclosures.

4. **Save and exit** the file:
   - For **nano**, press `CTRL + O` to save and `CTRL + X` to exit.

### Step 2: Initialize the Git Repository (If Not Already Initialized)
Since you're working directly in your `.newsboat` directory, you can turn it into a Git repository.

1. **Initialize Git** in your `~/.newsboat` directory:
   ```bash
   git init
   ```

2. **Add the remote repository** (if not already added):
   ```bash
   git remote add origin https://github.com/danielrosehill/Newsboat-Israel-Feeds.git
   ```

### Step 3: Add the Files to Your Git Repo

1. **Check the status** to see which files are tracked and which are ignored:
   ```bash
   git status
   ```

2. **Stage your files** (make sure the cache and unwanted files are not listed due to the `.gitignore`):
   ```bash
   git add config urls .gitignore
   ```

3. **Commit the files**:
   ```bash
   git commit -m "Initial commit of Newsboat configuration and feeds"
   ```

### Step 4: Push the Configuration to GitHub

1. **Push your changes** to the remote repository:
   ```bash
   git push -u origin main
   ```

### Step 5: Set Up a Basic Configuration File (Optional)

If you haven’t customized your **`~/.newsboat/config`** file yet, here are some useful options you can add to improve your experience:

1. **Edit the `config` file**:
   ```bash
   nano ~/.newsboat/config
   ```

2. **Basic settings** for Newsboat:

   - **Set your default browser**:
     ```bash
     browser "firefox %u"
     ```
   - **Limit the number of articles per feed** to avoid clutter:
     ```bash
     max-items 100
     ```
   - **Reload feeds automatically** after a specified time (in minutes):
     ```bash
     reload-time 60
     ```
   - **Sort articles by date (newest first)**:
     ```bash
     article-sort-order date-desc
     ```

3. **Save and exit** the configuration file (`CTRL + O`, `CTRL + X`).

4. **Add and commit the new config changes**:
   ```bash
   git add config
   git commit -m "Added basic configuration to Newsboat"
   ```

5. **Push the changes** to your GitHub repository:
   ```bash
   git push
   ```

### Step 6: Verify Your Changes on GitHub
You can now visit your repository URL ([https://github.com/danielrosehill/Newsboat-Israel-Feeds.git](https://github.com/danielrosehill/Newsboat-Israel-Feeds.git)) to verify that your **`config`** and **`urls`** files are uploaded, and the **cache** is properly excluded.

### Summary:
1. **Create a `.gitignore`** to exclude `cache.db` and other temporary files.
2. **Initialize Git** in your `.newsboat` directory.
3. **Add your configuration files** (`urls`, `config`) and commit them.
4. **Push the changes** to your remote GitHub repository.
5. Optionally, **set up a basic `config`** file to enhance your Newsboat experience.

This will allow you to share your **Newsboat configuration** while ensuring that sensitive or unnecessary files are not exposed!