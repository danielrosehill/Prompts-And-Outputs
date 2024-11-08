---
title: "Extract prompts using a script - Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's revisit the idea of using a python script to automatically extract the prompts I've renamed the prompts folder Prompts and the outputs folder Outputs In the outputs I format like this # Prompt prompttext # Output outputtext So prompttext in this example should be copied into the Prompts folder and given a file name that corresponds to the one of the output Can you write a script that tries to do this?

# Output

Here's a Python script that will automate the extraction of the `Prompt` section from your notes in the `Outputs` folder and save it as a new file in the `Prompts` folder. The script will use the filename of the output file as the basis for the prompt filename.

### Python Script

```python
import os
import re

# Paths to your Obsidian folders
output_folder = '/path/to/your/obsidian/vault/Outputs'
prompts_folder = '/path/to/your/obsidian/vault/Prompts'

# Create the prompts folder if it doesn't exist
os.makedirs(prompts_folder, exist_ok=True)

# Iterate through all markdown files in the Outputs folder
for root, dirs, files in os.walk(output_folder):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
                
                # Regex to extract the Prompt section
                match = re.search(r'# Prompt\n(.+?)\n# Output', content, re.DOTALL)
                if match:
                    prompt_text = match.group(1).strip()
                    
                    # Create a new filename for the prompt based on the output file name
                    prompt_file_name = f"{file.replace('.md', '')}_prompt.md"
                    prompt_file_path = os.path.join(prompts_folder, prompt_file_name)
                    
                    # Write the prompt text to a new markdown file in the Prompts folder
                    with open(prompt_file_path, 'w') as prompt_file:
                        prompt_file.write(f'# {file.replace(".md", "")} Prompt\n\n{prompt_text}')
                    
                    print(f"Extracted and saved prompt to {prompt_file_path}")
                else:
                    print(f"No prompt found in {file_path}")

print("All prompts have been processed.")
```

### How the Script Works:
1. **Folder Paths**: Replace `'/path/to/your/obsidian/vault/Outputs'` and `'/path/to/your/obsidian/vault/Prompts'` with the actual paths to your Obsidian folders.

2. **Regex Pattern**: The script uses a regular expression to find the text between `# Prompt` and `# Output`. It then extracts this `prompttext`.

3. **File Naming**: The script names the new prompt file based on the original output file name, appending `_prompt.md` to the name.

4. **File Creation**: It creates a new markdown file in the `Prompts` folder containing the extracted prompt text.

5. **Error Handling**: If the script doesn’t find a `# Prompt` section, it will print a message and skip that file.

### How to Run:
1. Save the script as `extract_prompts.py`.
2. Make sure you have Python installed.
3. Run the script from your terminal:
   ```bash
   python extract_prompts.py
   ```

This script will go through all the markdown files in your `Outputs` folder, extract the prompts, and save them into the `Prompts` folder with corresponding filenames. This should streamline your process and help keep your prompts organized efficiently in Obsidian.## Extracted Prompts
[[Prompts/Autocapture/Extract prompts using a script - Obsidian.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Extract prompts using a script - Obsidian.md#Prompt 1|Prompt 1]]
