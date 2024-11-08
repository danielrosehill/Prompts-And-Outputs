---
title: "Is there such a thing as read only submodules in Github"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can use a GitHub repository as a submodule in **read-only mode** by adjusting your workflow and Git configuration. Here’s how you can achieve this:

### 1. **Add the Submodule as Usual**:
   First, add the desired repository as a submodule to your private repository. By default, this will allow you to pull updates but will also let you push changes if you have write access.

   ```bash
   git submodule add https://github.com/user/repository path/to/submodule
   ```

### 2. **Make the Submodule Read-Only**:
   To ensure that any changes you make in the submodule are not pushed back to the original repository, follow these steps:

#### Option 1: Change the Git Remote URL to `read-only`
   After adding the submodule, change its Git remote URL to a **read-only URL**, such as the HTTPS or GitHub `git://` protocol (which is read-only), preventing you from pushing changes.

   ```bash
   cd path/to/submodule
   git remote set-url origin https://github.com/user/repository.git
   ```

   Alternatively, if you want a non-pushable protocol:
   ```bash
   git remote set-url origin git://github.com/user/repository.git
   ```

   Now, when you work inside the submodule, you will be able to pull changes, but if you try to push, it will fail because the `git://` protocol is read-only.

#### Option 2: Block Push Access Locally
   Another way to prevent accidental pushes to the submodule is to configure Git to disallow pushing changes by setting a `remote.pushurl` to an invalid address.

   ```bash
   git remote set-url --push origin no_push
   ```

   This effectively blocks pushes by setting the push URL to a dummy address, ensuring that any changes made in the submodule won’t be pushed upstream.

### 3. **Periodic Updates**:
   To pull in updates from the original repository periodically, use:

   ```bash
   git submodule update --remote --merge
   ```

   This command will fetch and merge the latest changes from the submodule’s remote repository without attempting to push any changes.

### 4. **Copy Data to Your Private Repo**:
   You can periodically pull updates from the submodule and copy the necessary data into your main repository as needed. This ensures that you keep the submodule read-only but still benefit from its updates.

### Conclusion:
By modifying the remote URL or setting a dummy push URL, you can effectively treat a Git submodule as **read-only**. This allows you to periodically pull updates without the risk of accidentally pushing changes back to the original repository.