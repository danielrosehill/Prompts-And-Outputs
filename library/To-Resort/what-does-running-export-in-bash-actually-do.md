---
title: "What does running export in Bash actually do"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When you run the following commands in a terminal:

```bash
export OPENAI_CONFIG_HOME="/custom/config/path"
export OPENAI_DATA_HOME="/custom/data/path"
```

### Here’s what happens:

1. **Environment Variables**:
   - These commands set two **environment variables**: `OPENAI_CONFIG_HOME` and `OPENAI_DATA_HOME`.
   - An environment variable is a key-value pair stored in the environment of the shell session, which programs and processes can reference during execution.

2. **Purpose**:
   - These specific environment variables (`OPENAI_CONFIG_HOME` and `OPENAI_DATA_HOME`) likely tell the OpenAI-related CLI or application where to look for its **configuration files** and **data files**.
   - By default, many applications have predefined locations for configuration and data files (often in your home directory, such as `~/.config` for Linux). When you set these environment variables, you're overriding the default paths and directing the application to use custom directories for its configuration and data.

   - **OPENAI_CONFIG_HOME**: Specifies the directory where OpenAI-related configuration files will be stored or read from.
   - **OPENAI_DATA_HOME**: Specifies the directory where OpenAI will store or retrieve data files (such as caches, temporary files, or other data).

3. **Impact**:
   - After setting these environment variables, any OpenAI-related command-line tools or applications that are aware of these environment variables will use the paths you’ve specified rather than the default ones.
   - These variables are only set for the **current terminal session** unless added to a profile script (like `.bashrc`, `.zshrc`, etc.), in which case they will persist across terminal sessions.

4. **Temporary**:
   - The `export` command makes the environment variables available only within the current terminal session. If you open a new terminal, these variables will not be set unless added to a shell profile file.

### Example Use Case:
If you're using an OpenAI CLI tool that relies on certain configuration files, you can use these variables to specify a custom location for storing those files. For instance, this might be useful if you have different configurations for different projects and want to switch between them easily.

### How to Make This Permanent:
- To ensure these variables are always set when you open a new terminal session, you can add the `export` commands to your shell configuration file:
  ```bash
  echo 'export OPENAI_CONFIG_HOME="/custom/config/path"' >> ~/.bashrc
  echo 'export OPENAI_DATA_HOME="/custom/data/path"' >> ~/.bashrc
  ```
  Then, reload the configuration:
  ```bash
  source ~/.bashrc
  ```

Let me know if you need further clarification!