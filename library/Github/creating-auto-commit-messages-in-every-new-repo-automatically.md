---
title: "Creating auto commit messages in every new repo automatically"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



For the automatic commit message idea .. is there a way to include that by default in every new repo I create?

# Output

Yes, you can set up a default configuration for automatic commit messages by creating a **global Git template directory**. This way, every new Git repository you initialize will automatically include your desired Git hooks and configurations.

Here’s how you can set up the `prepare-commit-msg` hook globally for all new repositories:

### 1. **Set Up a Global Git Template Directory**

Git allows you to define a global template directory that will be used whenever you create a new repository. This directory can include hooks, config files, and more.

#### Steps:

1. **Create a template directory** where the global Git hooks will reside:
   ```bash
   mkdir -p ~/.git-templates/hooks
   ```

2. **Create the `prepare-commit-msg` hook** in this directory:
   ```bash
   nano ~/.git-templates/hooks/prepare-commit-msg
   ```

3. **Add the following script** to automate the commit message (e.g., a simple "Update" message):
   ```bash
   #!/bin/sh
   echo "Update" > $1
   ```

4. **Make the hook executable**:
   ```bash
   chmod +x ~/.git-templates/hooks/prepare-commit-msg
   ```

5. **Configure Git to use the template directory** globally:
   ```bash
   git config --global init.templateDir ~/.git-templates
   ```

### 2. **How This Works**

- Now, every time you initialize a new Git repository with `git init`, the `prepare-commit-msg` hook will be copied from the template directory into the `.git/hooks/` folder of the new repository.
- This hook will automatically add the predefined commit message ("Update") whenever you create a commit in that repository.

### 3. **Customizing the Commit Message**

You can modify the `prepare-commit-msg` hook to use more dynamic content if needed, such as adding a timestamp or file names:

```bash
#!/bin/sh
echo "Automated update on $(date)" > $1
```

This will generate commit messages like:

```
Automated update on Mon Oct 9 14:30:22 UTC 2024
```

### 4. **Applying to Existing Repositories**

For existing repositories, you would need to manually copy the `prepare-commit-msg` hook to their `.git/hooks/` directories. You can automate this with a script if you want to apply it to multiple existing repositories.

```bash
cp ~/.git-templates/hooks/prepare-commit-msg /path/to/your/repo/.git/hooks/
```

### Summary

By setting up a global Git template directory with a `prepare-commit-msg` hook, you can automate commit message generation for every new repository you create. This approach ensures that the hook is present in every new repo without needing to manually configure each one.