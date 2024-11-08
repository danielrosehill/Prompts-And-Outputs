---
title: "Programatically pulling apart notes in Obsidian"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great work

Now another question for you.

Let's say that I wanted to glob through a folder of these and simply extract a list of only the unique identifiers and output that into a file

Or I wanted to glob through that same folder and produce a CSV which had two columns ID and Title. Where ID was the ID part of the title and the title was the actual title given to the note

Could both these things be done with relative ease?

# Output

Yes, both of these tasks can be done relatively easily using Python's glob module and some string manipulation. Let's break down each task:

1. Extracting unique identifiers:

```python
import glob
import os

# Assuming the files are in a folder named 'notes'
file_pattern = 'notes/*.md'  # Adjust the pattern based on your file extension
files = glob.glob(file_pattern)

unique_ids = set()

for file in files:
    filename = os.path.basename(file)
    # Assuming the ID is always the first 5 characters (e.g., O2324)
    unique_id = filename[:5]
    unique_ids.add(unique_id)

# Write unique IDs to a file
with open('unique_ids.txt', 'w') as f:
    for id in sorted(unique_ids):
        f.write(id + '\n')

print(f"Extracted {len(unique_ids)} unique IDs")
```

2. Creating a CSV with ID and Title columns:

```python
import glob
import os
import csv

file_pattern = 'notes/*.md'
files = glob.glob(file_pattern)

with open('id_title.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Title'])  # Write header

    for file in files:
        filename = os.path.basename(file)
        # Assuming the ID is always the first 5 characters
        id = filename[:5]
        # Assuming the title starts after the ID and a space, and excludes the file extension
        title = filename[6:-3]  # Adjust -3 if your file extension is different
        writer.writerow([id, title])

print(f"Processed {len(files)} files")
```

These scripts assume:
1. Your files are in a folder named 'notes'.
2. The file names follow the pattern you described (e.g., "O2324 Some Title.md").
3. The ID is always the first 5 characters of the filename.
4. There's a space between the ID and the title in the filename.

You may need to adjust the string slicing (`filename[:5]`, `filename[6:-3]`) if your actual file naming convention is different.

Both scripts can be easily modified to handle different file patterns or naming conventions. They use the glob module to find files matching a pattern, which is efficient for directory traversal.

To use these scripts:
1. Save each script as a .py file (e.g., `extract_ids.py` and `create_csv.py`).
2. Place the script in the parent directory of your 'notes' folder.
3. Run the script using Python from the command line:
   ```
   python extract_ids.py
   ```
   or
   ```
   python create_csv.py
   ```

These scripts should process your files quickly and efficiently, even with a large number of files.
 