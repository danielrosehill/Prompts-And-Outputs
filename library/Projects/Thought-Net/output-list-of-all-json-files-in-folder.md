---
title: "Output list of all JSON files in folder"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You can easily list all `.json` files in a directory and output them into a `.txt` file in Python using the `os` or `pathlib` module. Here’s an example Python script that accomplishes this task:

### Python Script:

```python
import os

# Define the directory containing the JSON files
directory_path = '/path/to/your/directory'

# Define the output text file
output_file_path = '/path/to/your/output_file.txt'

# Get the list of all .json files in the directory
json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]

# Write the list of files to a .txt file
with open(output_file_path, 'w') as output_file:
    for json_file in json_files:
        output_file.write(json_file + '\n')

print(f"List of JSON files written to {output_file_path}")
```

### Explanation:
- **`os.listdir(directory_path)`**: Lists all files in the specified directory.
- **`f.endswith('.json')`**: Filters the list to include only files that end with `.json`.
- **Writing to a file**: The filtered list of JSON files is written to a `.txt` file, one per line.

### Output:
The `.txt` file will contain the names of all the `.json` files in the specified directory, with each file name on a new line.

### Example Output in `.txt`:
```
file1.json
file2.json
file3.json
```

You can run this script to generate the `.txt` file with the list of `.json` files from any directory. Just replace the `directory_path` and `output_file_path` with your actual folder paths.