---
title: "Including export in bashrc"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, if you want to make the environment variables **permanent** by adding them to your `.bashrc` file (or `.zshrc` if you're using Zsh), you should include the **`export`** keyword when defining them.

Here’s how you can do it:

1. Open your `.bashrc` file in a text editor:
   ```bash
   nano ~/.bashrc
   ```

2. Add the following lines at the end of the file:
   ```bash
   export OPENAI_CONFIG_HOME="/custom/config/path"
   export OPENAI_DATA_HOME="/custom/data/path"
   ```

3. Save and close the file (in nano, you can press `Ctrl + X`, then `Y` to confirm, and `Enter` to save).

4. Apply the changes by sourcing the `.bashrc` file:
   ```bash
   source ~/.bashrc
   ```

Now, the environment variables `OPENAI_CONFIG_HOME` and `OPENAI_DATA_HOME` will be set permanently every time you open a new terminal session, and you won’t have to set them manually.

# What does the 'export' achieve when the variables are saved in bashrc?

When you add `export` commands to your `.bashrc` file, here’s what happens:

### 1. **Setting Environment Variables**:
   - The `export` command in **Bash** makes the specified environment variables available to the shell session and all **child processes** initiated from that shell. 
   - This means that when you use `export` in `.bashrc`, any script, program, or command run in the terminal will have access to these environment variables.

### 2. **Making Variables Available to Subprocesses**:
   - Without `export`, a variable would only be available in the current shell (local to that session) and wouldn’t be passed on to child processes.
   - When you `export` a variable, it is passed along to child processes (such as other programs, scripts, or commands) spawned from the shell, allowing them to access and use the variable.

### 3. **Making Variables Persistent**:
   - **.bashrc** is a configuration file that is executed every time a new **interactive Bash shell** is opened. By adding the `export` command to this file, the variables will be set automatically whenever you open a terminal or start a new Bash session.
   - This makes the variables **persistent** across terminal sessions.

### **Example**:
If you add the following to `.bashrc`:
```bash
export OPENAI_CONFIG_HOME="/custom/config/path"
export OPENAI_DATA_HOME="/custom/data/path"
```
- Every time you start a new terminal, those two environment variables (`OPENAI_CONFIG_HOME` and `OPENAI_DATA_HOME`) will be set and exported to the environment.
- Any program or command run from that terminal session will have access to these variables.

### **Summary of Key Points**:
- **`export` in `.bashrc`** makes environment variables available to **child processes** and ensures they are **set automatically** every time you start a new terminal session.
- This allows programs, scripts, and commands that run in the terminal to access those variables without needing to redefine them in each session.

This is particularly useful when you want to ensure certain configuration paths or settings are consistently available in your shell environment.