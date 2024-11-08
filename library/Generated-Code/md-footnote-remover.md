---
title: "Glob through markdown files, remove footnote references"
---

## Output And Script

To remove footnote-style references like `[1][2]` from a directory of markdown files, you can use Python's `glob` module to iterate through the files and `re` (regular expressions) to find and remove those references. Here's a script that does this:

```python
import glob
import re

# Define the directory containing markdown files
directory = "path/to/your/markdown/files"

# Define the regex pattern to match footnote references like [1][2]
pattern = r'\[\d+\](?:\[\d+\])*'

# Iterate through all markdown files in the directory
for filepath in glob.glob(f"{directory}/*.md"):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove footnote references using regex
    new_content = re.sub(pattern, '', content)

    # Write the updated content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Processed {filepath}")
```

### Explanation:

1. **`glob.glob(f"{directory}/*.md")`**: This finds all markdown files (`*.md`) in the specified directory.
2. **`pattern = r'$$\d+$$(?:$$\d+$$)*'`**: This regular expression matches any sequence like `[1]`, `[1][2]`, etc.
   - `$$\d+$$`: Matches a number inside square brackets.
   - `(?:$$\d+$$)*`: Matches any additional number in brackets that may follow.
3. **`re.sub(pattern, '', content)`**: This removes all matched footnote references from the markdown content.
4. **File I/O**: The script reads each file, processes it, and writes the cleaned content back.

### How to Run:

- Replace `"path/to/your/markdown/files"` with the actual path to your markdown files.
- Run the script in your Python environment.

This will remove all footnote-style references from each markdown file in the specified directory.

&#x20;
