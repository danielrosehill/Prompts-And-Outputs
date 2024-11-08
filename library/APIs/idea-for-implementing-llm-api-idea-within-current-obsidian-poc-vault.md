---
title: "Idea for implementing LLM API idea within current Obsidian POC vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have attached a file which provides contextual information about a system that I am currently working on. I would like to add some additional functionality to it.

Specifically I would like to be able to automatically send prompts to an LLM API directly through the system. 

I am thinking of some ways I could achieve this. 

One idea I had was to create subfolders in my Prompts folder. Perhaps there could be a subfolder called Run and a subfolder called Drafts. Once prompts move from the drafts folder into the run they would automatically be sent to the LLM API and the output would be collected and saved into the outputs folder. 

However, I don't think that this is the best approach. 

Please remember that I am using Obsidian and it's a vault on my local filesystem. So whatever system you can think of will have to work with this. But the key functionality I'm looking for is that the prompt will be sent automatically and collected and saved in the outputs folder with a corresponding file name and (ideally) an automatic link to the prompt from which it was generated.

# Output

Based on the context provided and your requirements, I can suggest an approach that leverages Obsidian's capabilities and integrates with an LLM API. Here's a proposed solution:

## Automated Prompt Execution System

### Prompt Execution Trigger

Instead of using subfolders, we can utilize Obsidian's YAML frontmatter to control prompt execution. This approach is more flexible and doesn't require moving files between folders.

1. Add a YAML frontmatter to each prompt file with an "execute" flag:

```yaml
---
execute: true
model: gpt-3.5-turbo
---
```

2. When this flag is set to true, it will trigger the prompt to be sent to the LLM API.

### Implementation

To implement this system, we can use the Obsidian Local REST API plugin[3]. This plugin provides a secure HTTPS interface that allows interaction with your notes programmatically. Here's how we can set it up:

1. Install the Obsidian Local REST API plugin.
2. Set up authentication and secure the API endpoint.
3. Create a script (e.g., in Python) that does the following:
   - Polls the Obsidian vault for prompts with `execute: true` in their frontmatter.
   - Sends these prompts to the chosen LLM API.
   - Saves the output in the Outputs folder.
   - Updates the original prompt file with a link to the output and sets `execute: false`.

### Workflow

1. Create a new prompt in the Prompts folder.
2. When ready to execute, set `execute: true` in the frontmatter.
3. The external script, running at regular intervals, will:
   - Detect the prompt to be executed.
   - Send it to the LLM API.
   - Save the response in the Outputs folder.
   - Update the original prompt file with a link to the output.

### Code Example

Here's a basic Python script to illustrate this approach:

```python
import requests
import json
import os
from datetime import datetime

OBSIDIAN_API_URL = "https://localhost:27124"  # Adjust as needed
API_KEY = "your_obsidian_api_key"
LLM_API_KEY = "your_llm_api_key"

def get_prompts_to_execute():
    response = requests.get(f"{OBSIDIAN_API_URL}/vault", headers={"Authorization": API_KEY})
    files = response.json()
    return [f for f in files if f.get("frontmatter", {}).get("execute") == True]

def execute_prompt(prompt_file):
    # Read prompt content
    response = requests.get(f"{OBSIDIAN_API_URL}/vault/{prompt_file['path']}", headers={"Authorization": API_KEY})
    content = response.json()["content"]
    
    # Send to LLM API (example using OpenAI)
    llm_response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {LLM_API_KEY}"},
        json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": content}]}
    )
    
    # Save output
    output_content = llm_response.json()["choices"][0]["message"]["content"]
    output_filename = f"Output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    requests.post(
        f"{OBSIDIAN_API_URL}/vault/Outputs/{output_filename}",
        headers={"Authorization": API_KEY},
        json={"content": output_content}
    )
    
    # Update original prompt file
    updated_content = f"{content}\n\n[[{output_filename}]]"
    requests.put(
        f"{OBSIDIAN_API_URL}/vault/{prompt_file['path']}",
        headers={"Authorization": API_KEY},
        json={"content": updated_content, "frontmatter": {"execute": False}}
    )

def main():
    prompts = get_prompts_to_execute()
    for prompt in prompts:
        execute_prompt(prompt)

if __name__ == "__main__":
    main()
```

This script would need to be run regularly (e.g., via a cron job) to check for and execute prompts.

## Additional Considerations

- **Error Handling**: Implement robust error handling to manage API failures or rate limiting.
- **Logging**: Add logging to track execution history and troubleshoot issues.
- **Queue System**: For heavy uscage, consider implementing a queue system to manage multiple prompts.
- **User Interface**: You could create a custom Obsidian plugin to provide a user interface for this functionality, making it easier to manage and monitor prompt execution[2].

By leveraging Obsidian's existing functionality and extending it with a custom script, this approach provides a flexible and scalable solution for automatically executing prompts and managing their outputs within your Obsidian vault.
 




## Extracted Prompts
[[Prompts/Idea for implementing LLM API idea within current Obsidian POC vault.md#Prompt 1|Prompt 1]]
