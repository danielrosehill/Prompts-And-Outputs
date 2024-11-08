---
title: "Script to convert folder of markdown files to kebab case"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can use a simple shell script to convert all Markdown file names in a folder to kebab case. Here's how you can do it:

### Script: Convert to Kebab Case

1. **Create a Shell Script**:
   Save the following script as `convert-to-kebab.sh`:

   ```bash
   #!/bin/bash

   # Function to convert string to kebab case
   to_kebab_case() {
       echo "$1" | sed -E 's/([a-z])([A-Z])/\1-\2/g' | tr ' ' '-' | tr '_' '-' | tr '[:upper:]' '[:lower:]'
   }

   # Directory containing your Markdown files
   DIRECTORY="${1:-.}"

   # Process each .md file in the directory (and subdirectories)
   find "$DIRECTORY" -type f -name "*.md" | while read -r file; do
       # Get the directory and filename
       dir=$(dirname "$file")
       filename=$(basename "$file")
       
       # Convert the filename to kebab case
       kebab_case=$(to_kebab_case "$filename")
       
       # Rename the file only if the name has changed
       if [[ "$filename" != "$kebab_case" ]]; then
           mv "$file" "$dir/$kebab_case"
           echo "Renamed: $file -> $dir/$kebab_case"
       fi
   done
   ```

2. **Make the Script Executable**:
   Open a terminal and run:
   ```bash
   chmod +x convert-to-kebab.sh
   ```

3. **Run the Script**:
   You can run the script by specifying the directory containing your Markdown files. For example:
   ```bash
   ./convert-to-kebab.sh /path/to/markdown/files
   ```

   If you want to run it on the current directory, just use:
   ```bash
   ./convert-to-kebab.sh
   ```

### Explanation of the Script:
- The `to_kebab_case` function converts CamelCase, spaces, and underscores to kebab case.
- It uses `find` to locate all `.md` files, including those in subdirectories.
- Files are renamed only if their names change after conversion to avoid unnecessary operations.
- The script handles spaces, underscores, and uppercase letters effectively.

**Note**: It's a good idea to back up your files before running the script, just in case any renaming doesn’t go as expected.