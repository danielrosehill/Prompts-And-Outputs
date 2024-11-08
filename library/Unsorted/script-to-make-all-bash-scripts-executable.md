---
title: "Script to make all Bash scripts executable"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you create another shortcut for me please? I'm creating a scripts folder that's synced through github. It's a bit cumbersome that every time I save a new bash script that I have to go into the terminal to make it executable. Could you write me a script that I can put in the base of the main repo which would recurse into every subdirectory and if it finds any bash scripts to make them executable?

# Output

Here’s a Bash script you can place in the base of your repository to automatically make all Bash scripts (`.sh` files) executable in every subdirectory:

```bash
#!/bin/bash
# Script to recursively make all .sh files executable in the current directory and subdirectories

# Find all .sh files and make them executable
find . -type f -name "*.sh" -exec chmod +x {} \;

# Optionally print the files that were made executable
echo "The following .sh files have been made executable:"
find . -type f -name "*.sh" -exec ls -l {} \;
```

### Instructions:
1. Save the script as `make_scripts_executable.sh` in the base of your repository.
2. Make this script executable (just once):
   ```bash
   chmod +x make_scripts_executable.sh
   ```
3. Now, every time you want to make sure all `.sh` files in your repository are executable, run the script:
   ```bash
   ./make_scripts_executable.sh
   ```

This will recursively find all `.sh` files and apply `chmod +x` to them, ensuring that they are executable.

Let me know if you need any adjustments to this!