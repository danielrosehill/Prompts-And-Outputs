---
title: "Rsync syntax to create a backup folder in PWD"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You can achieve this by combining the **`mkdir -p`** command with **`rsync`** in a single line. The `mkdir -p` command ensures that the target backup directory is created if it doesn't already exist.

Here’s the combined command:

```bash
mkdir -p homeboxdata_backup && rsync -av --info=progress2 homeboxdata/ homeboxdata_backup/

```

### Explanation:
- **`mkdir -p homeboxdata_backup`**: This creates the `homeboxdata_backup` directory if it doesn't already exist. The `-p` option ensures no error is thrown if the directory already exists.
- **`&&`**: Ensures that `rsync` will only run if the `mkdir` command is successful.
- **`rsync -av --progress homeboxdata/ homeboxdata_backup/`**: This performs the backup as discussed previously, copying the contents of `homeboxdata` into `homeboxdata_backup`.

This way, you ensure that the destination directory is created if it doesn't already exist before starting the backup process.

Let me know if you need more help!