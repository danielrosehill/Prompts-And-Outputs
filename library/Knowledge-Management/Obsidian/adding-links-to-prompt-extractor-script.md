---
title: "Programatically add bidirectional links to prompt extraction script in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)


*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I created a Python script which automatically extracts prompts from the prompt and output documents that I capture into my Obsidian vault. The next step would be to automatically create bidirectional links between the original file and the copied prompt. Could this be done programatically?

# Output

Yes, you can programmatically create bidirectional links between the original file and the copied prompt in your Obsidian vault. Here's how you could extend your existing Python script to accomplish this:

## Extending the Script

To create bidirectional links, you'll need to modify both the original file and the extracted prompt file. Here's an approach to implement this functionality:

1. After extracting the prompts, add a link back to the original file in each extracted prompt file.
2. Add links to the extracted prompt files in the original file.

Here's a modified version of your script that includes these changes:

```python
import os
import re
import sys

def extract_prompts_and_create_links(vault_base_path):
    input_dir = os.path.join(vault_base_path, "Outputs")
    output_dir = os.path.join(vault_base_path, "Prompts", "Autocapture")

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            with open(input_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

            prompts = re.findall(r'(?:^|\n)(#+\s*Prompt\s*\d*\s*\n[\s\S]*?)(?=\n#+|$)', content, re.MULTILINE)

            if prompts:
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    for i, prompt in enumerate(prompts, 1):
                        outfile.write(prompt.strip() + '\n\n')
                        # Add link back to original file
                        outfile.write(f"[[{filename}|Original File]]\n\n")

                print(f"Extracted prompts from {filename}")

                # Add links to extracted prompts in the original file
                with open(input_path, 'a', encoding='utf-8') as infile:
                    infile.write("\n\n## Extracted Prompts\n")
                    for i in range(1, len(prompts) + 1):
                        infile.write(f"[[{filename}#Prompt {i}|Prompt {i}]]\n")

            else:
                print(f"No prompts found in {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_prompts_and_create_links.py <vault_base_path>")
        sys.exit(1)

    vault_base_path = sys.argv[1]
    extract_prompts_and_create_links(vault_base_path)
```

## How It Works

1. The script extracts prompts as before.
2. For each extracted prompt, it adds a link back to the original file using the Obsidian link syntax: `[[{filename}|Original File]]`.
3. In the original file, it appends a new section at the end with links to each extracted prompt, using the syntax: `[[{filename}#Prompt {i}|Prompt {i}]]`.

## Considerations

- This script modifies both the original files and creates new files, so make sure to back up your data before running it.
- The script assumes that the prompts in the original file are numbered sequentially. If this is not the case, you may need to adjust the linking logic.
- You might want to add error handling and logging to make the script more robust.

## Further Improvements

To make the script even more powerful, you could consider:

1. Adding a command-line option to specify whether to create bidirectional links or not.
2. Implementing a way to update existing links rather than always appending new ones.
3. Adding functionality to remove broken links if prompts are deleted.

Remember to test the script thoroughly on a small subset of your vault before running it on your entire collection to ensure it behaves as expected




## Extracted Prompts
[[Prompts/Adding links to prompt extractor script.md#Prompt 1|Prompt 1]]

