---
title: "Updated script for calculating a data manifest"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of Prompt:** You asked for a script that processes all CSV files in the directory where the script is run and generates a manifest for each CSV into a subfolder called `params` within the same directory.

---

Here’s the modified script that will generate the manifest for each CSV in the current folder, and save the output into a new folder called `params`:

```python
import pandas as pd
import os

def generate_manifest_for_all_csvs():
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Create a folder called 'params' within the current directory to store the manifests
    output_folder = os.path.join(current_dir, 'params')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all CSV files in the current directory
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
    
    # Loop through each CSV file and generate a manifest
    for csv_file in csv_files:
        # Load CSV file into a pandas DataFrame
        csv_path = os.path.join(current_dir, csv_file)
        df = pd.read_csv(csv_path)

        # Create a list to hold information about each column
        manifest = []

        for col in df.columns:
            col_info = {
                'Column Name': col,
                'Data Type': df[col].dtype,
                'Unique Values': df[col].nunique(),
                'Description/Notes': 'Add description here'  # Can be customized
            }
            manifest.append(col_info)

        # Convert the manifest list into a DataFrame
        manifest_df = pd.DataFrame(manifest)
        
        # Generate the output filename for the manifest
        output_file = os.path.join(output_folder, f"{os.path.splitext(csv_file)[0]}_manifest.csv")
        
        # Save the manifest DataFrame to a CSV file in the 'params' folder
        manifest_df.to_csv(output_file, index=False)
        print(f"Manifest for {csv_file} saved to {output_file}")

# Run the function
generate_manifest_for_all_csvs()
```

### **Explanation:**
- **Folder creation:** The script creates a folder named `params` in the directory where it runs, if the folder does not already exist.
- **Manifest generation:** It processes each CSV file in the current directory, generating a manifest with column names, data types, and unique value counts.
- **Output:** Each manifest is saved as a CSV file in the `params` folder, named as `original_filename_manifest.csv`.

When you run this script, it will generate a manifest for all CSV files in the current directory and store them in the `params` folder.