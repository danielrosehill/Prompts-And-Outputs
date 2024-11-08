---
title: "Script to try convert markdown files to JSON graph nodes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:**
You asked if the script can detect prompts within the markdown files and note them accordingly in the JSON output.

To enhance the script, I'll modify it to specifically look for sections within the markdown that resemble prompts and outputs. I'll assume a typical structure where the prompt might be clearly labeled or demarcated (e.g., a heading "Prompt" followed by the text). If the script finds these sections, it will include them separately in the JSON file.

### Updated Script:
```python
import os
import json
import re
from pathlib import Path

# Define paths
SOURCE_PATH = "/home/daniel/Git/LLM-and-AI/obsidian-reformatting/current_vault"
DESTINATION_PATH = "./graph_json"

def ensure_directory_exists(directory):
    """Ensure that the destination directory exists; create it if it does not."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_title_and_content(markdown_file):
    """Extract title and content from a markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Assuming the title is the first line in the markdown file (common practice)
    lines = content.splitlines()
    title = lines[0].strip() if lines else "Untitled"
    body = "\n".join(lines[1:]).strip()

    return title, body

def extract_prompt_and_output(content):
    """Extract the prompt and output sections from the markdown content."""
    # Simple regex patterns to detect sections labeled as "Prompt" and "Output"
    prompt_match = re.search(r'(?<=#\s*Prompt:)(.*?)(?=#|$)', content, re.DOTALL | re.IGNORECASE)
    output_match = re.search(r'(?<=#\s*Output:)(.*?)(?=#|$)', content, re.DOTALL | re.IGNORECASE)

    prompt = prompt_match.group(0).strip() if prompt_match else None
    output = output_match.group(0).strip() if output_match else None

    return prompt, output

def derive_topics_from_text(text):
    """Derive possible topics from the text using basic keyword extraction."""
    words = re.findall(r'\w+', text.lower())
    # Simple heuristic: most common words that are not too short
    common_words = [word for word in words if len(word) > 3]
    # Return unique topics as a basic representation of key subjects
    return list(set(common_words))[:5]  # Limit to 5 topics for simplicity

def convert_markdown_to_json(markdown_file, output_folder):
    """Convert a markdown file to a JSON node suitable for graph DB ingestion."""
    title, content = extract_title_and_content(markdown_file)
    prompt, output = extract_prompt_and_output(content)
    topics = derive_topics_from_text(content)

    # Generate JSON data
    json_data = {
        "id": Path(markdown_file).stem,
        "title": title,
        "content": content,
        "prompt": prompt,
        "output": output,
        "topics": topics,
        "related": [],  # Placeholder for manual or future automated relationships
        "source": "Markdown Repository",
        "path": str(markdown_file)
    }

    # Save to JSON file
    json_filename = os.path.join(output_folder, f"{Path(markdown_file).stem}.json")
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)
    print(f"Created JSON node: {json_filename}")

def process_markdown_repository(source_path, destination_path):
    """Process all markdown files in the source path and convert to JSON nodes."""
    ensure_directory_exists(destination_path)
    
    for root, _, files in os.walk(source_path):
        for file in files:
            if file.endswith(".md"):
                markdown_file = os.path.join(root, file)
                convert_markdown_to_json(markdown_file, destination_path)

def main():
    # Ensure the destination directory exists
    ensure_directory_exists(DESTINATION_PATH)
    
    # Convert markdown repository to JSON nodes
    process_markdown_repository(SOURCE_PATH, DESTINATION_PATH)
    print("Conversion to JSON nodes completed.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Detecting Prompts and Outputs**:
   - The `extract_prompt_and_output` function uses regular expressions to find sections labeled as "Prompt" and "Output" within the markdown file.
   - The script assumes these sections are marked using headers or keywords (e.g., `# Prompt:`). If you have a different format, the regex can be adjusted accordingly.

2. **JSON Structure**:
   - The JSON data now includes two new fields:
     - **`prompt`**: The detected prompt text.
     - **`output`**: The corresponding generated output.
   - This distinction makes it easier to map the relationships between prompts and their outputs, aiding in graph database integration.

3. **Running the Script**:
   Place the script in the desired location and run:
   ```bash
   python3 markdown_to_json_with_prompts.py
   ```

This script should help you convert your markdown files into a structured JSON format, clearly separating prompts and outputs for easier ingestion into a graph database. Let me know if more customization is needed!