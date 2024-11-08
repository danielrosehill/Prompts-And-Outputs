---
title: "How to make a GH submodule read only"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is possible to effectively make a **Git submodule read-only** so that you can **pull changes** but avoid accidentally committing and pushing changes to the submodule. There are several ways to ensure that the submodule behaves in a read-only manner.

### Methods to Make Submodule Read-Only:

#### 1. **Restrict Permissions on the Submodule Directory**
You can change the file permissions on the submodule directory to **read-only** for your user, preventing accidental edits.

##### Steps:
1. **Navigate to your submodule directory**:
   ```bash
   cd path/to/your-private-repo/your-submodule
   ```

2. **Set the directory to read-only**:
   ```bash
   chmod -R a-w .
   ```
   This will remove write permissions (`-w`) on the entire submodule directory, effectively making it read-only. You will need to reset the permissions (`chmod +w .`) if you ever need to change it in the future.

##### Pros:
- Prevents accidental edits.
  
##### Cons:
- If you do need to make edits temporarily, you will need to manually adjust the permissions.

---

#### 2. **Use a Read-Only Git URL for the Submodule**
If you want to ensure that you **cannot push changes** to the submodule, use a **read-only URL** (like a public HTTPS link instead of SSH) when setting up the submodule.

##### Steps:
1. **Remove the existing submodule** (if you’ve already added it):
   ```bash
   git submodule deinit your-submodule
   git rm your-submodule
   ```

2. **Re-add the submodule using a read-only URL** (for example, the HTTPS URL):
   ```bash
   git submodule add https://github.com/danielrosehill/Israeli-News-Links.git
   git submodule update --init --recursive
   ```

3. **Update the `.gitmodules` file** to point to the HTTPS URL:
   ```ini
   [submodule "your-submodule"]
       path = your-submodule
       url = https://github.com/danielrosehill/Israeli-News-Links.git
   ```

   This way, Git will not prompt you to push changes, as it’s using a **read-only HTTPS URL**.

##### Pros:
- Prevents pushing to the submodule repository entirely.

##### Cons:
- You will have to modify the URL back to SSH if you need write access in the future.

---

#### 3. **Ignore Changes in Submodule**
You can configure Git to **ignore local changes** in the submodule, ensuring that even if you accidentally modify files, Git will not consider them for commits or pushes.

##### Steps:
1. **Ignore changes in the submodule**:
   ```bash
   git config submodule.your-submodule.ignore all
   ```

   This setting will ensure that changes in the submodule directory are ignored by Git and won’t show up as modifications in `git status`.

2. **Alternatively**, you can set this option globally by modifying your `.gitmodules` file:

   ```ini
   [submodule "your-submodule"]
       path = your-submodule
       url = https://github.com/danielrosehill/Israeli-News-Links.git
       ignore = all
   ```

##### Pros:
- Allows you to make changes without Git tracking them.
  
##### Cons:
- Does not physically prevent changes, just hides them from Git.

---

### 4. **Use Git Hooks to Prevent Commits in Submodule**
You can set up a **pre-commit hook** in your repository to automatically abort any commit that includes changes to the submodule.

##### Steps:
1. Create a `pre-commit` hook script inside `.git/hooks/pre-commit`:
   ```bash
   #!/bin/sh
   if git diff --cached --name-only | grep -q '^your-submodule/'; then
     echo "Error: You have staged changes in the submodule. Commit aborted."
     exit 1
   fi
   ```

2. Make the hook executable:
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

##### Pros:
- Automates the process of preventing commits to the submodule.

##### Cons:
- Requires maintaining the hook in the repository.

---

### Summary:
- **Changing permissions** ensures that the files are truly read-only.
- **Using a read-only URL** (HTTPS instead of SSH) prevents accidental pushes.
- **Ignoring changes in submodules** allows you to edit but avoid tracking changes.
- **Git hooks** can be a useful safeguard to prevent commits to submodules.

For a simple approach, using a **read-only HTTPS URL** and/or **ignoring submodule changes** may be the most practical.