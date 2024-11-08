---
title: "Converting GPT configurations into LLM general agent configs in a batch"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I have a folder full of markdown files with custom GPT configurations. They're all written like the example. I would like to "convert" all the config texts into optimised configurations for custom LLM agents that don't specify that they are custom GPTs specifically. Could you provide me with a method and script to write them? If this is something GPT3.5 could do cost effectively please suggest that

Example:
The purpose of this GPT should be to generate a completely randomised itinerary for the user that should give them things to do from when they get up to when it's time to go to bed. The GPT should ask the user where in the world he is located. Next the GPT should lay out an elaborate itinerary with the hope that it will provide entertainment and unusual experiences. The itinerary should include times and google map links and opportunities to have a beer every couple of hours.


# Output
To help you optimize the configuration texts for custom LLM agents by removing GPT-specific language, I can walk you through a method and provide a Python script that can both parse the markdown files and refactor the text. Additionally, I'll provide an option for using **GPT-3.5** to further rewrite the content to be more polished and neutral for any LLM.

### Approach:

1. **Parse the Markdown Files**: We'll loop through all the `.md` files in your folder, locate the "Config Text" section, and extract it.
2. **Rewrite the Config Text**:
   - Either use a **manual replacement** to remove references to GPT and make the text more general (e.g., replacing "GPT" with "LLM").
   - Or, send the extracted config text to **GPT-3.5** via OpenAI's API for a more thorough rewriting.
3. **Update the Files**: After converting the config text, the script will overwrite the original files with the new, optimized configurations.

### Example Rewriting of the Text:
For instance, your example config:
> The purpose of this GPT should be to generate a completely randomised itinerary for the user that should give them things to do from when they get up to when it's time to go to bed. The GPT should ask the user where in the world he is located. Next the GPT should lay out an elaborate itinerary with the hope that it will provide entertainment and unusual experiences. The itinerary should include times and google map links and opportunities to have a beer every couple of hours.

Would be rewritten to:
> The purpose of this agent is to generate a completely randomised itinerary for the user, giving them activities from morning until bedtime. The agent should ask the user for their location and then create an elaborate itinerary, providing entertainment and unique experiences. The itinerary should include time slots, map links, and opportunities to have a beer every couple of hours.

### Python Script for Parsing and Rewriting:

```python
import os
from glob import glob
import openai  # For GPT-3.5 integration

# Initialize your OpenAI API key
openai.api_key = 'your-openai-api-key'

# Path to the directory where the markdown files are located
directory_path = './Agents'

# Function to call GPT-3.5 for rewriting the config text
def optimize_with_gpt3(text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Rewrite this configuration text to be generic for any LLM. Remove any references to GPT:\n\n{text}",
        max_tokens=500,
        temperature=0.7
    )
    return response['choices'][0]['text'].strip()

# Function to manually replace GPT references with more general terms
def manual_replace(text):
    return text.replace('GPT', 'agent').replace('he is', 'they are')

# Function to process each markdown file
def process_markdown_files(directory, use_gpt=False):
    # Recursively find all markdown files
    md_files = glob(os.path.join(directory, '**', '*.md'), recursive=True)
    
    for md_file in md_files:
        with open(md_file, 'r+', encoding='utf-8') as file:
            content = file.read()
            
            # Find the Config Text section
            config_start = content.find("## Config Text")
            if config_start == -1:
                continue  # Skip files without a config section
            
            # Extract the config text
            config_text = content[config_start:]
            
            # Rewrite the config text
            if use_gpt:
                optimized_text = optimize_with_gpt3(config_text)
            else:
                optimized_text = manual_replace(config_text)
            
            # Update the file with the new content
            new_content = content[:config_start] + optimized_text
            file.seek(0)
            file.write(new_content)
            file.truncate()

# Call the function and choose whether to use GPT-3.5 or not
process_markdown_files(directory_path, use_gpt=True)

print("Processing complete!")
```

### How the Script Works:
1. **Searches for Markdown Files**: The script recursively finds all `.md` files under your `/Agents` directory.
2. **Extracts the "Config Text"**: The script looks for the `## Config Text` heading and grabs everything after it.
3. **Rewrites the Text**:
   - **Option 1**: If you choose `use_gpt=True`, it sends the text to GPT-3.5 to rephrase it in a more neutral way.
   - **Option 2**: If `use_gpt=False`, it manually replaces "GPT" with "agent" or "LLM" using string replacement.
4. **Updates the Files**: After processing, the script rewrites each file with the updated config text.

### Running the Script:

1. **Install Required Dependencies**:
   If you plan to use GPT-3.5, install the OpenAI Python client:
   ```bash
   pip install openai
   ```

2. **Add Your OpenAI API Key**:
   Replace `'your-openai-api-key'` in the script with your actual OpenAI API key.

3. **Run the Script**:
   ```bash
   python script_name.py
   ```

### Cost Efficiency with GPT-3.5:
- **Token usage**: The script sends small pieces of text (the config section) to GPT-3.5. These sections likely won’t use too many tokens, making the cost relatively low. Monitor the token usage on your OpenAI account to stay within budget.
- **Batch processing**: If you have many markdown files, consider processing them in batches to better manage costs and API limits.

### Manual Approach (Cost-Free):
If you prefer not to use GPT-3.5, the **manual replacement method** can quickly refactor most config texts. You can also further customize the manual replacement logic to handle different phrasings based on your specific needs.

---

Let me know if you need further adjustments or if you'd like more optimization options for the rewritten texts!