---
title: "Script for suggesting logical folders for outputs and then moving the files into them"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:**
You asked for a Python script that recursively scans markdown files in a specified directory (`OUTPUTS_PATH`). Based on the file names, it should suggest 10 folder categories to group the outputs into, ask the user to confirm the categorization, and then create the folders and move the files into them if the user agrees.

Here's the Python script:

```python
import os
import shutil
import collections
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Define the output path
OUTPUTS_PATH = "/home/daniel/Vaults/outputhub_vault/Output_Hub/Outputs"

def get_markdown_files(directory):
    """Recursively get all markdown files from a directory."""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def suggest_folders(markdown_files, num_folders=10):
    """Suggest folder names based on clustering of file names."""
    filenames = [os.path.basename(file) for file in markdown_files]
    
    # Extract keywords using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(filenames)
    
    # Use KMeans clustering to suggest folder categories
    kmeans = KMeans(n_clusters=num_folders, random_state=42)
    kmeans.fit(tfidf_matrix)
    
    # Create a dictionary of suggested folder names and file groups
    folder_suggestions = collections.defaultdict(list)
    for idx, label in enumerate(kmeans.labels_):
        folder_name = f"Group_{label + 1}"
        folder_suggestions[folder_name].append(markdown_files[idx])
    
    return folder_suggestions

def move_files_to_folders(folder_suggestions, base_path):
    """Move files to the suggested folders."""
    for folder_name, files in folder_suggestions.items():
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            shutil.move(file, os.path.join(folder_path, os.path.basename(file)))
        print(f"Moved {len(files)} files to {folder_name}")

def main():
    markdown_files = get_markdown_files(OUTPUTS_PATH)
    if not markdown_files:
        print("No markdown files found in the specified directory.")
        return
    
    folder_suggestions = suggest_folders(markdown_files)
    
    # Print out the suggested folders and file names
    print("Suggested categorization:")
    for folder_name, files in folder_suggestions.items():
        print(f"\n{folder_name}:")
        for file in files:
            print(f"  - {os.path.basename(file)}")
    
    # Ask the user for confirmation
    confirm = input("\nDo you want to proceed with this categorization? (yes/no): ").strip().lower()
    if confirm == "yes":
        move_files_to_folders(folder_suggestions, OUTPUTS_PATH)
        print("Files have been moved to the new folders.")
    else:
        print("No changes have been made.")

if __name__ == "__main__":
    main()
```

### Explanation:
1. **Functions**:
   - `get_markdown_files()`: Recursively collects all markdown files in the specified directory.
   - `suggest_folders()`: Uses TF-IDF vectorization and KMeans clustering to group similar files based on their names. Suggests 10 groups by default.
   - `move_files_to_folders()`: Moves the files to folders based on user-confirmed categorization.
   
2. **User Interaction**: The script suggests categories, lists files under each, and asks for confirmation before moving files.

3. **Dependencies**: Make sure to install required packages if not already installed:
   ```bash
   pip install scikit-learn
   ```

This script should provide a straightforward way to group your markdown outputs and organize them efficiently based on file name similarities.