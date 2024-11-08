---
title: How to generate a PDF concatenating a list of X markdown outputs
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

As you know, I have a large repository of markdown files in my Obsidian vault. Tomorrow, I would like to find a way to export the last 100 of them by creation date and export them all into one long PDF Ideally there should be page breaks between new files ... by which I mean each new file should be on a new page Is there a way to do this programatically and if so could you write me the script to make this work?

# Output

Based on the provided search results and your requirements, I can help you create a script to export the last 100 markdown files from your Obsidian vault into a single PDF with page breaks between files. We'll use Python with the `pypandoc` library to convert markdown to PDF. Here's a script that should accomplish this task:

```python
import os
from datetime import datetime
import pypandoc

# Set the path to your Obsidian vault
vault_path = '/path/to/your/obsidian/vault'  # Replace with your actual vault path

# List all markdown files in the vault
def get_markdown_files(vault_path):
    md_files = []
    for root, dirs, files in os.walk(vault_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

# Get markdown files sorted by creation date
def get_recent_markdown_files(vault_path, limit=100):
    md_files = get_markdown_files(vault_path)
    md_files_with_time = [(file, os.path.getctime(file)) for file in md_files]
    sorted_md_files = sorted(md_files_with_time, key=lambda x: x[1], reverse=True)[:limit]
    return [file[0] for file in sorted_md_files]

# Combine markdown files into a single string with page breaks
def combine_markdown_files(files):
    combined_content = ""
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            combined_content += content + "\n\n<div style='page-break-after: always;'></div>\n\n"
    return combined_content

# Main execution
if __name__ == "__main__":
    # Fetch the last 100 markdown files by creation date
    last_100_md_files = get_recent_markdown_files(vault_path)
    
    # Combine the content of these files
    combined_markdown = combine_markdown_files(last_100_md_files)
    
    # Set the output PDF file name
    output_file = f"obsidian_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    # Convert the combined markdown to PDF
    pypandoc.convert_text(combined_markdown, 'pdf', format='md', outputfile=output_file,
                          extra_args=['--pdf-engine=xelatex', '-V', 'geometry:margin=1in'])
    
    print(f"PDF created successfully: {output_file}")
```

To use this script:

1. Install the required library:
   ```
   pip install pypandoc
   ```

2. Make sure you have a LaTeX distribution installed on your system (e.g., MiKTeX for Windows or MacTeX for macOS).

3. Replace the `vault_path` variable with the actual path to your Obsidian vault.

4. Run the script.

This script does the following:

1. It finds all markdown files in your Obsidian vault.
2. It sorts these files by creation date and selects the 100 most recent ones.
3. It combines the content of these files into a single markdown string, adding page breaks between each file.
4. It uses `pypandoc` to convert the combined markdown to a PDF.
5. The output PDF will be named with the current date and time (e.g., `obsidian_export_20241002_143000.pdf`).

The script uses XeLaTeX as the PDF engine, which provides better support for various fonts and Unicode characters. The margins are set to 1 inch, but you can adjust this by modifying the `geometry:margin=1in` argument.

Remember to test this script on a small subset of files first to ensure it works correctly with your specific Obsidian setup and file content.