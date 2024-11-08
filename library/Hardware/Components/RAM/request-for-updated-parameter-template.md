---
title: "Request for updated parameter template"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Let's revise the script, although some things can remain the same. The script will run through all the csv files in the pwd (ie, the script runs in the same folder as the data files). Its purpose is to generate a data manifest in markdown format. Each manifest should have the title filename_manifest.md where filename is the name of the CSV. The manifest should list all the columns in the CSV. It should then list all the unique parameters within each column in a format like this # Column Parameters With each parameter on a separate line

# Output

**Summary of Prompt:** You requested a revised script to process all CSV files in the current working directory and generate a data manifest in markdown format. The markdown file for each CSV should list all columns and their unique parameters.

---

Here is the revised Python script that generates a markdown manifest for each CSV in the current working directory:

```python
import pandas as pd
import os

def generate_markdown_manifest_for_all_csvs():
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Create a folder called 'params' within the current directory to store the markdown manifests
    output_folder = os.path.join(current_dir, 'params')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get a list of all CSV files in the current directory
    csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return

    # Loop through each CSV file and generate a manifest in markdown format
    for csv_file in csv_files:
        try:
            # Load CSV file into a pandas DataFrame
            csv_path = os.path.join(current_dir, csv_file)
            df = pd.read_csv(csv_path)

            # Prepare the manifest content
            markdown_content = f"# Manifest for {csv_file}\n\n"
            markdown_content += f"## Column Overview\n\n"

            for col in df.columns:
                unique_values = df[col].dropna().unique()
                markdown_content += f"### {col}\n\n"
                markdown_content += "Parameters:\n\n"
                for val in unique_values:
                    markdown_content += f"- {val}\n"
                markdown_content += "\n"

            # Generate the output filename for the markdown manifest
            output_file = os.path.join(output_folder, f"{os.path.splitext(csv_file)[0]}_manifest.md")
            
            # Write the markdown content to the file
            with open(output_file, 'w') as f:
                f.write(markdown_content)

            print(f"Manifest for {csv_file} saved to {output_file}")

        except Exception as e:
            print(f"Error processing {csv_file}: {e}")

# Run the function
generate_markdown_manifest_for_all_csvs()
```

### **Explanation of the Script:**
1. **Folder Setup:**
   - The script checks if a folder named `params` exists in the current working directory. If not, it creates one to store the markdown manifests.
   
2. **Processing CSV Files:**
   - It loops through all CSV files in the directory.
   - For each file, it reads the CSV using `pandas` and processes the columns.
   
3. **Markdown File Structure:**
   - For each CSV, a markdown file is created with the format `filename_manifest.md`.
   - Each column is listed as a header, followed by its unique parameters (values) in a bullet-point list.

4. **Output:**
   - Each manifest is saved in the `params` folder.
   - Markdown content is structured as:
     ```markdown
     # Manifest for filename.csv

     ## Column Overview

     ### Column Name
     Parameters:
     - value1
     - value2
     - value3
     ```

---

This script should now correctly create markdown files for each CSV in the directory, listing the unique values per column. The files will be stored in the `params` subfolder with appropriate naming conventions.