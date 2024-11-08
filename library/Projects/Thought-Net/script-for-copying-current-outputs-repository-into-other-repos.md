---
title: "Script for copying current outputs repository into other repos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:**
You requested a script that will copy the contents of a specified folder (`/home/daniel/Vaults/outputhub_vault/Output_Hub/Outputs`) into a local folder named `current_vault`. If `current_vault` does not exist, the script should create it. Additionally, the script should support incremental copying, making it suitable for repeated runs.

Here's the Python script using `rsync`-like functionality for incremental copying:

### Python Script:
```python
import os
import shutil
from pathlib import Path

# Define source and destination directories
SOURCE_PATH = "/home/daniel/Vaults/outputhub_vault/Output_Hub/Outputs"
DESTINATION_PATH = "./current_vault"

def ensure_directory_exists(directory):
    """Ensure that the destination directory exists; create it if it does not."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def incremental_copy(src, dest):
    """Recursively copy files from src to dest with incremental updates."""
    for root, dirs, files in os.walk(src):
        # Determine the relative path from the source root
        relative_path = os.path.relpath(root, src)
        dest_dir = os.path.join(dest, relative_path)

        # Ensure the destination directory exists
        ensure_directory_exists(dest_dir)

        # Copy each file if it doesn't exist or is newer in the source
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)

            # Only copy if the file is newer or doesn't exist in destination
            if not os.path.exists(dest_file) or os.path.getmtime(src_file) > os.path.getmtime(dest_file):
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} -> {dest_file}")

def main():
    # Ensure destination directory exists
    ensure_directory_exists(DESTINATION_PATH)
    
    # Perform incremental copy
    incremental_copy(SOURCE_PATH, DESTINATION_PATH)
    print("Incremental copy completed.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Incremental Copy Logic**:
   - The script uses `os.walk()` to recursively navigate through the source directory.
   - For each file, it checks if the file exists in the destination. If it doesn't exist or if the source file is newer, it copies the file over, thus performing an incremental update.

2. **Creating the Destination Directory**:
   - The function `ensure_directory_exists()` checks if `current_vault` exists and creates it if not.

3. **File Metadata Preservation**:
   - `shutil.copy2()` is used to ensure that file metadata (like timestamps) is preserved during the copy.

4. **Execution**:
   - The script can be run repeatedly without re-copying unchanged files, making it efficient for ongoing synchronization.

### Running the Script:
To run the script, place it in the directory where you want `current_vault` to be created and simply execute:
```bash
python3 incremental_copy.py
```

This script should effectively manage the task of incremental copying, ensuring that only new or updated files are copied each time it runs. Let me know if any tweaks are needed!