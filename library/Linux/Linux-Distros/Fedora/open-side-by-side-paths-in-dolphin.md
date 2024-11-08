---
title: "Open side by side paths in Dolphin"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*

# Prompt

Could you write a script that will open these two folders in a side by side layout in dolphin

```
/home/dworkstation/gitrepos/blogs/danielgoespromptingblog/output-pipeline
/home/dworkstation/gitrepos/blogs/danielgoespromptingblog/blog/content
```

# Output

Here’s a simple script to open the two specified folders side-by-side in Dolphin file manager:

```bash
#!/bin/bash

# Define the folder paths
FOLDER1="/home/dworkstation/gitrepos/blogs/danielgoespromptingblog/output-pipeline"
FOLDER2="/home/dworkstation/gitrepos/blogs/danielgoespromptingblog/blog/content"

# Open Dolphin with a split view layout for the two folders
dolphin --split "$FOLDER1" "$FOLDER2"
```

### Instructions
1. Save this script as `open_dolphin_split.sh`.
2. Make it executable with:

   ```bash
   chmod +x open_dolphin_split.sh
   ```

3. Run the script:

   ```bash
   ./open_dolphin_split.sh
   ```

This script will open Dolphin in split view with each folder displayed on either side.