---
title: "Aggregating URL arrays"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here's a Python script that will concatenate every JSON file in the folder (excluding itself) into a single `all-rss.json` file. It assumes that each JSON file in the folder is formatted as an array of RSS feeds and the resulting file will contain all the feeds from each JSON file.

### Python Script: `concatenate_json.py`

```python
import os
import json

def concatenate_json_files(output_file):
    all_rss = []

    # Get the current script's name so it can be ignored
    current_script = os.path.basename(__file__)

    # Loop through all the files in the current directory
    for filename in os.listdir('.'):
        if filename.endswith('.json') and filename != output_file and filename != current_script:
            try:
                # Open and load the JSON file
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    # If the loaded data is a list, extend the all_rss list
                    if isinstance(data, list):
                        all_rss.extend(data)
                    elif isinstance(data, dict):
                        # If it's a dictionary, check for a list under "Jewish World - agencies" key
                        if "Jewish World - agencies" in data and isinstance(data["Jewish World - agencies"], list):
                            all_rss.extend(data["Jewish World - agencies"])

            except (json.JSONDecodeError, IOError) as e:
                print(f"Error processing {filename}: {e}")

    # Write the concatenated result to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_rss, f, indent=4)

if __name__ == "__main__":
    output_filename = 'all-rss.json'
    concatenate_json_files(output_filename)
```

### How it works:
1. **Read all JSON files**: The script reads every `.json` file in the current directory, ignoring itself and the output file (`all-rss.json`).
2. **Concatenate arrays**: It expects each JSON file to either be a list or contain a list under a key like `"Jewish World - agencies"`. It concatenates all these lists into one master list.
3. **Write to `all-rss.json`**: The resulting list is written to `all-rss.json`, which is overwritten every time the script runs.

### How to use:
1. Save the script as `concatenate_json.py` in the folder containing the JSON files.
2. Run the script using Python:
   ```bash
   python3 concatenate_json.py
   ```
3. The `all-rss.json` file will be created or updated with the concatenated JSON data.

This script will continue to work efficiently even when run repeatedly, as it ignores itself and doesn't enter a loop.