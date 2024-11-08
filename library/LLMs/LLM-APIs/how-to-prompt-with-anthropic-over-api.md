---
title: "How to prompt with Anthropic over API"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Please teach me how to use one of the Anthropic models for generating a python script. I'd like to use the API to do this programatically (I already have a key). My prompt is long so I'm going to save it as a text file. Please factor all of these things into the example.

# Output
Certainly! I'll provide you with a Python script that demonstrates how to use one of Anthropic's models (specifically Claude) via their API to generate a Python script based on a prompt stored in a text file. This example will cover:

1. Reading the prompt from a text file
2. Making an API call to Anthropic's Claude model
3. Handling the response and extracting the generated Python script

Here's the step-by-step guide with code:

1. First, make sure you have the `anthropic` library installed:

```bash
pip install anthropic
```

2. Create a Python script (e.g., `generate_script.py`) with the following content:

```python
import os
import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

# Set up the Anthropic client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Read the prompt from a text file
def read_prompt_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Generate Python script using Claude
def generate_python_script(prompt):
    response = client.completions.create(
        model="claude-2",  # You can change this to other available models
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} Please generate a Python script based on the following prompt:\n\n{prompt}\n\n{AI_PROMPT}",
    )
    return response.completion

# Main execution
if __name__ == "__main__":
    prompt_file_path = "prompt.txt"  # Change this to your prompt file path
    output_file_path = "generated_script.py"

    # Read the prompt
    prompt = read_prompt_from_file(prompt_file_path)

    # Generate the Python script
    generated_script = generate_python_script(prompt)

    # Save the generated script to a file
    with open(output_file_path, 'w') as file:
        file.write(generated_script)

    print(f"Generated Python script has been saved to {output_file_path}")
```

3. Create a text file (e.g., `prompt.txt`) in the same directory as your Python script, and put your long prompt in this file.

4. Set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

5. Run the Python script:

```bash
python generate_script.py
```

This script does the following:

1. It reads the prompt from the specified text file (`prompt.txt` by default).
2. It uses the Anthropic API to send the prompt to the Claude model and generate a Python script.
3. It saves the generated script to a new file (`generated_script.py` by default).

You can customize the script by:

- Changing the `model` parameter in the `generate_python_script` function to use a different Anthropic model.
- Adjusting the `max_tokens_to_sample` to control the length of the generated script.
- Modifying the file paths for input prompt and output script as needed.

Remember to handle API errors and rate limits appropriately in a production environment. Also, always review and test the generated script before using it, as AI-generated code may contain errors or unexpected behavior.

 




## Extracted Prompts
[[Prompts/How to prompt with Anthropic over API.md#Prompt 1|Prompt 1]]
