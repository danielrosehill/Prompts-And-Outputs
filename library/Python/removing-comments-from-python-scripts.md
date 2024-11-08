---
title: "Removing comments from Python scripts"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there an easy way to remove lots of comments in a Python file.

For example, as in this codeblock:

![[Removing comments from Python scripts.png]]

# Output

To remove all comments from a Python file, you can use the `tokenize` module. Here's a script that reads a Python file, removes comments, and writes the cleaned code to a new file:

```python
import tokenize

def remove_comments(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            tokens = tokenize.generate_tokens(source_file.readline)
            for token_type, token_string, _, _, _ in tokens:
                if token_type != tokenize.COMMENT:
                    destination_file.write(token_string)

# Usage
remove_comments('your_script.py', 'cleaned_script.py')
```

### Explanation

- **`tokenize.generate_tokens()`**: This function generates tokens from the source file.
- **Filter**: The script writes only non-comment tokens to the destination file.
- **Output**: The cleaned code is saved in `cleaned_script.py`.

This approach uses Python's built-in libraries to handle tokenization, ensuring that comments are accurately removed without affecting the rest of the code.
 