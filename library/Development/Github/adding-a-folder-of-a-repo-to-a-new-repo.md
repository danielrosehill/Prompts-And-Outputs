---
title: "Adding a folder of a repo to a new repo"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

is it possible to add a folder within one of my existing github repos as a submodule to this one? or if i just add the whole repo as a submodule within the cofnig folder will that mess things up: https://github.com/danielrosehill/Israeli-News-Links/tree/main/Links/11Oct24/RSS/by-groups

Yes, you can **add a folder** within an existing GitHub repository as a **submodule** within your Newsboat config folder. However, Git doesn’t allow you to add just a **subfolder** of a repository as a submodule. Instead, you can add the **entire repository** as a submodule and then use the specific folder you need from within it.

Here's a guide to help you add the **entire repo** as a submodule to your Newsboat configuration, and ensure that this setup won’t mess anything up:

### Step 1: Add the Repo as a Submodule in the Newsboat Directory

You can add the **Israeli-News-Links** repository (or any Git repository) as a submodule within your `~/.newsboat` directory.

1. **Navigate to your Newsboat config directory**:
   ```bash
   cd ~/.newsboat
   ```

2. **Add the repository as a submodule**:
   Since you need the `RSS/by-groups` folder, you will add the entire repository as a submodule and use that folder as needed.

   ```bash
   git submodule add https://github.com/danielrosehill/Israeli-News-Links.git Links
   ```

   This will add the **Israeli-News-Links** repository as a submodule in the `Links` directory inside your `~/.newsboat` directory.

3. **Initialize and pull the submodule**:
   ```bash
   git submodule init
   git submodule update
   ```

### Step 2: Reference the Desired Folder in Newsboat

Now that you have the submodule in place, you can reference any RSS feeds in the **`Links/11Oct24/RSS/by-groups`** directory within your `~/.newsboat` folder.

1. **Open your `urls` file** to add feeds from the submodule:
   ```bash
   nano ~/.newsboat/urls
   ```

2. **Add feeds from the submodule**:
   You can reference any feed URLs stored in the submodule's folder. Here’s an example of how you could add them:

   ```plaintext
   Links/11Oct24/RSS/by-groups/group1.rss
   Links/11Oct24/RSS/by-groups/group2.rss
   ```

   Make sure to format it according to your RSS feed file paths or contents in the submodule.

### Step 3: Commit and Push the Changes

1. **Add the submodule to Git**:
   After adding the submodule, commit the changes to your main Newsboat repository.

   ```bash
   git add .gitmodules Links/
   git commit -m "Added Israeli-News-Links as a submodule"
   ```

2. **Push the changes** to your GitHub repository:
   ```bash
   git push origin main
   ```

### Step 4: Keeping the Submodule Up-to-Date

Whenever the `Israeli-News-Links` repository is updated, you can **pull** the latest changes into your submodule by running the following commands:

1. **Pull the latest changes for the submodule**:
   ```bash
   cd ~/.newsboat/Links
   git pull origin main
   ```

2. **Update the submodule in your main repo**:
   ```bash
   cd ~/.newsboat
   git add Links
   git commit -m "Updated submodule to latest version"
   git push
   ```

### Step 5: Cloning the Repository with the Submodule

If someone clones your main repository and you want them to get the submodule as well, they will need to run:

```bash
git clone --recurse-submodules https://github.com/danielrosehill/Newsboat-Israel-Feeds.git
```

If they have already cloned the repository, they can initialize and update the submodule with:
```bash
git submodule init
git submodule update
```

### Key Points to Consider:

1. **Entire Repo as Submodule**: Git doesn’t support adding just a subfolder as a submodule. By adding the entire repository as a submodule, you can access any files or directories from the submodule.
   
2. **Separate Versioning**: The submodule tracks its own repository separately. Any updates you make to the **Israeli-News-Links** repo won’t automatically reflect in your Newsboat repository unless you manually update the submodule.

3. **Git Submodule Overhead**: Submodules can add a little complexity, especially for those unfamiliar with Git submodules. However, they provide a clean way to link separate repositories without copying content directly.

### Conclusion:

- You can **add the whole repo as a submodule** and use the required folder (`Links/11Oct24/RSS/by-groups`) in your **Newsboat** configuration.
- This won’t mess things up, but remember that the **entire submodule repo** is cloned, not just a folder.
- You can reference the feeds in that folder in your `urls` file, and everything will work smoothly.