---
title: "Python script for mapping out folder structure in remote B2 bucket"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

can you write a python script which would connect to a b2 bucket and provide a report on the file structure? All it would need to do is map out the file structure to 3 levels of recursion and print that to a txt document

# Output

It looks like there was an incomplete script in the previous message. I'll complete it and ensure it can connect to a Backblaze B2 bucket and generate a report of the file structure up to 3 levels. Here’s the updated script:

```python
import b2sdk.v2 as b2
import os

# Replace these credentials with your actual B2 credentials
B2_APPLICATION_KEY_ID = 'your_application_key_id'
B2_APPLICATION_KEY = 'your_application_key'
BUCKET_NAME = 'your_bucket_name'
OUTPUT_FILE = 'b2_file_structure_report.txt'

# Connect to B2 bucket
def connect_to_b2(application_key_id, application_key):
    info = b2.InMemoryAccountInfo()
    b2_api = b2.B2Api(info)
    b2_api.authorize_account("production", application_key_id, application_key)
    return b2_api

# Get file structure of the bucket
def get_file_structure(bucket, folder_prefix='', level=1, max_levels=3):
    if level > max_levels:
        return []

    file_structure = []
    for file_version, folder_name in bucket.ls(folder_prefix):
        # Only list latest versions of files
        if file_version.action == 'upload':
            file_structure.append((folder_prefix, file_version.file_name))

            # If this is a folder, recursively list files in it
            if folder_name.endswith('/'):
                sub_files = get_file_structure(bucket, folder_prefix=folder_name, level=level + 1, max_levels=max_levels)
                file_structure.extend(sub_files)

    return file_structure

# Write the file structure to a txt file
def write_file_structure_to_txt(file_structure, output_file):
    with open(output_file, 'w') as f:
        for folder_prefix, file_name in file_structure:
            indent = '    ' * (folder_prefix.count('/') - 1)
            f.write(f"{indent}{file_name}\n")

# Main function to connect, retrieve file structure, and write to a file
def main():
    b2_api = connect_to_b2(B2_APPLICATION_KEY_ID, B2_APPLICATION_KEY)
    bucket = b2_api.get_bucket_by_name(BUCKET_NAME)

    file_structure = get_file_structure(bucket)
    write_file_structure_to_txt(file_structure, OUTPUT_FILE)

    print(f"File structure has been written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
```

### Key Elements of the Script:
1. **B2 Credentials**: Replace `your_application_key_id`, `your_application_key`, and `your_bucket_name` with your actual Backblaze B2 credentials.
2. **Connection to B2**: The script connects to the B2 cloud storage using `b2sdk.v2`.
3. **Recursion**: The function `get_file_structure` recursively lists files up to 3 levels deep.
4. **Output File**: The final structure is saved to `b2_file_structure_report.txt`.

### Requirements:
- You need to install the B2 SDK for Python. You can do this by running:
  ```sh
  pip install b2sdk
  ```

This script will generate a simple report of the file structure, making it easy for you to navigate through the B2 bucket's organization up to 3 levels deep. Let me know if you need further modifications!