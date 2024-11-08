---
title: "Tools to validate filenames in repository"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there are several tools and approaches that can help you **lint** through your repository to identify non-compliant file names, such as files containing forbidden characters like apostrophes. These tools will allow you to check for improper file names according to specified rules and conventions.

### 1. **Custom Shell Script with `find` and Regular Expressions**
You can use a simple shell script to search your repository for file names that contain forbidden characters like apostrophes (`'`). Here's an example of a shell command that searches for file names containing an apostrophe:

```bash
find /path/to/your/repo -name "*'*"
```

This command will search recursively through the directory `/path/to/your/repo` and list any files that contain an apostrophe in the name. You can modify this to search for other invalid characters as well.

If you want to include additional characters or enforce naming conventions (e.g., no spaces, only lowercase, etc.), you can use a more complex regular expression. For example, to search for any files with spaces or uppercase letters:

```bash
find /path/to/your/repo -name "*[[:space:]]*" -o -name "*[A-Z]*"
```

### 2. **ESLint with `eslint-plugin-filenames`**
If your repository is primarily JavaScript (or TypeScript), you can use **ESLint** with the `eslint-plugin-filenames` plugin to enforce file naming conventions.

#### Installation:
```bash
npm install eslint eslint-plugin-filenames --save-dev
```

#### Configuration (`.eslintrc.json`):
Add the `filenames/match-regex` rule in your ESLint configuration to enforce a specific naming convention:
```json
{
  "plugins": ["filenames"],
  "rules": {
    "filenames/match-regex": [2, "^[a-z0-9-]+$", true]
  }
}
```

This rule ensures that all file names match the regular expression `^[a-z0-9-]+$`, which means only lowercase letters, numbers, and hyphens are allowed. You can modify the regex to fit your specific requirements (e.g., disallowing apostrophes or spaces).

### 3. **Prettier with `prettier-plugin-organize-files`**
While **Prettier** is usually focused on code formatting, you can use the `prettier-plugin-organize-files` to lint file and folder structures to ensure they follow specific naming conventions.

#### Installation:
```bash
npm install prettier prettier-plugin-organize-files --save-dev
```

#### Configuration (`prettier.config.js`):
You can configure it to enforce certain naming rules:
```js
module.exports = {
  plugins: [require('prettier-plugin-organize-files')],
  organizeFiles: {
    fileNamePattern: /^[a-z0-9-]+$/,
  },
};
```
This ensures that file names only contain lowercase letters, numbers, and hyphens, similar to the ESLint example.

### 4. **`check-files-naming` CLI Tool**
Another option is to use a dedicated tool like **check-files-naming**, a CLI tool that checks for file naming conventions based on regex patterns.

#### Installation:
```bash
npm install -g check-files-naming
```

#### Usage:
You can then run the following command to check file names in your repository:
```bash
check-files-naming "^[a-z0-9-]+$" /path/to/your/repo
```
This tool will recursively check all file names and validate them against the provided regular expression.

### 5. **Python Script Using `os` and `re` Libraries**
If you prefer Python, you can write a script to check for non-compliant file names in your repository.

#### Example Python Script:
```python
import os
import re

# Define the directory to check
directory = "/path/to/your/repo"

# Define a regex pattern for valid file names (e.g., no apostrophes, only lowercase and dashes)
pattern = re.compile(r"^[a-z0-9-]+$")

# Walk through the directory and check file names
for root, dirs, files in os.walk(directory):
    for file in files:
        if not pattern.match(file):
            print(f"Invalid file name: {os.path.join(root, file)}")
```

This script recursively checks all files in the given directory and prints any file names that do not match the regular expression.

### 6. **Git Hooks Using `husky` and `lint-staged`**
If you want to enforce file naming conventions during the commit process, you can use **git hooks** to automatically check file names. Tools like **Husky** and **lint-staged** can be configured to run a file-naming check before each commit.

#### Installation:
```bash
npm install husky lint-staged --save-dev
```

#### Configuration (`package.json`):
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "*": [
      "check-files-naming '^[a-z0-9-]+$'"
    ]
  }
}
```

This setup ensures that no files with invalid names can be committed to the repository.

---

### Summary:
To identify and lint non-compliant file names (e.g., files with apostrophes or spaces), you can choose from a variety of tools:
- **Shell scripts**: Simple and quick for specific cases using `find`.
- **ESLint**: For JavaScript projects, especially if you want to enforce file name conventions.
- **Prettier or `check-files-naming`**: CLI tools that can lint file structures.
- **Custom Python Script**: If you prefer a flexible approach.
- **Git Hooks**: To enforce naming conventions during commit processes with tools like **Husky** and **lint-staged**.

Each of these approaches allows you to automatically detect and enforce file naming rules in your repository. Let me know if you'd like more help setting one of these up!