---
title: "Searching for easier solution for prompt triggering in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

While that seems like a great solution, it's a little complicated. I'm looking for something that I can setup quickly and easily and developing a custom plugin will be quite some work. Do you have any alternative ideas? The workflow is that I start with a prompt and then send it for execution by pressing a button. Once that happens, the prompt will be sent via the LLM API. It will "return" to the Outputs folder where it will have the same name as the prompt. And finally a bidirectional link will be created between the prompt and the output to easily relate them.

# Output

I understand your desire for a simpler, quicker solution that doesn't involve developing a custom plugin. Given your specific workflow requirements, here's an alternative approach that leverages existing Obsidian plugins and features:

## Simplified Workflow Using Existing Plugins

1. **Template for Prompts**:
   Create a template for your prompts with a button using the "Buttons" plugin. This template will include a button to trigger the execution.

   ```markdown
   ---
   tags: prompt
   ---
   
   # Prompt: {{title}}
   
   [Your prompt text here]
   
   ```button
   name Execute Prompt
   type command
   action Shell commands: Execute Prompt
   color green
   ```
   
   ## Output
   [This section will be automatically populated with a link to the output]
   ```

2. **Shell Commands Plugin**:
   Install and configure the "Shell commands" plugin. This plugin allows you to execute shell commands from within Obsidian.

3. **Script for API Interaction**:
   Create a simple script (e.g., in Python) that handles the API call to the LLM and saves the output. Place this script in your Obsidian vault or in a convenient location on your system.

   ```python
   import sys
   import requests
   import os
   from datetime import datetime

   # Your LLM API details
   API_URL = "https://api.openai.com/v1/chat/completions"
   API_KEY = "your_api_key_here"

   def send_to_llm(prompt_path):
       with open(prompt_path, 'r') as file:
           prompt_content = file.read()
       
       response = requests.post(
           API_URL,
           headers={"Authorization": f"Bearer {API_KEY}"},
           json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt_content}]}
       )
       
       output_content = response.json()["choices"][0]["message"]["content"]
       prompt_name = os.path.basename(prompt_path).replace('.md', '')
       output_path = os.path.join(os.path.dirname(prompt_path), '..', 'Outputs', f"{prompt_name}_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
       
       with open(output_path, 'w') as file:
           file.write(f"# Output for {prompt_name}\n\n{output_content}")
       
       return output_path

   if __name__ == "__main__":
       prompt_path = sys.argv[1]
       output_path = send_to_llm(prompt_path)
       print(output_path)
   ```

4. **Shell Command Configuration**:
   In the Shell Commands plugin settings, create a new command:
   - Name: "Execute Prompt"
   - Command: `python /path/to/your/script.py "{{file_path}}"`
   - Output: Capture output

5. **Templater Plugin**:
   Install the Templater plugin to help with creating bidirectional links.

6. **Output Template**:
   Create a template for the output files:

   ```markdown
   ---
   tags: output
   prompt: "[[{{promptTitle}}]]"
   ---

   # Output for {{promptTitle}}

   {{outputContent}}
   ```

## Workflow

1. Create a new prompt using your prompt template.
2. Write your prompt in the designated area.
3. Click the "Execute Prompt" button.
4. The Shell Commands plugin will run your Python script, which will:
   - Send the prompt to the LLM API
   - Save the output in the Outputs folder
   - Return the path of the new output file
5. Use Templater to insert a link to the new output file in the prompt file.

This approach requires minimal setup and leverages existing plugins. It provides a straightforward way to create prompts, execute them, and link the outputs back to the prompts.

To further simplify this, you could create a QuickAdd macro that combines these steps, allowing you to create a prompt and execute it with a single command.

This solution offers a balance between simplicity and functionality, allowing you to quickly set up and start using your LLM workflow in Obsidian without the need for custom plugin development.

 




## Extracted Prompts
[[Prompts/Searching for easier solution for prompt triggering in Obsidian.md#Prompt 1|Prompt 1]]
