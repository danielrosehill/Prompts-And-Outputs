---
title: "Capturing Obsidian plugins into awesome list"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm creating a list of AI related Obsidian plugins. I'm trying to think of an efficiennt way to generate this list from the plugins page. It's going to be curated, but equally I don't want to have to manually enter the description and link for every single plugin. Any ideas for how to automate the process of capturing this from the web page and formatting it into markdown?

# Output

To efficiently generate a curated list of AI-related Obsidian plugins from the plugins page while automating the process of capturing descriptions and links, you could use a combination of web scraping and markdown formatting. Here's an approach you could consider:

1. Use a web scraping tool or browser extension to extract data from the Obsidian plugins page. Some options include:

   - Data Miner Chrome extension[8]
   - Web Scraper Chrome extension[7]
   - ParseHub[7]
   - Octoparse[7]

2. Configure the scraper to extract the following information for each plugin:
   - Plugin name
   - Description
   - Link to the plugin

3. Export the scraped data to a CSV or JSON format.

4. Use a script (Python, JavaScript, or even a no-code tool like Zapier) to process the exported data and convert it into markdown format. The script should:

   - Filter the plugins based on AI-related keywords
   - Format each plugin entry into markdown, including the name as a header, description as text, and link as a markdown link

5. Review and manually curate the generated markdown list, adding or removing entries as needed.

Here's a sample Python script that could help with step 4:

```python
import csv
import re

def is_ai_related(text):
    ai_keywords = ['ai', 'artificial intelligence', 'machine learning', 'nlp', 'natural language']
    return any(keyword in text.lower() for keyword in ai_keywords)

with open('obsidian_plugins.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    markdown_output = ""
    
    for row in reader:
        if is_ai_related(row['name']) or is_ai_related(row['description']):
            markdown_output += f"## {row['name']}\n\n"
            markdown_output += f"{row['description']}\n\n"
            markdown_output += f"[Learn more]({row['link']})\n\n"

with open('ai_obsidian_plugins.md', 'w') as mdfile:
    mdfile.write(markdown_output)
```

This approach combines automated data extraction with manual curation, allowing you to efficiently create your list while maintaining control over its content. The web scraping step saves time on data entry, while the filtering and markdown conversion automate the formatting process. You can then review and refine the generated markdown list to ensure it meets your specific needs[1][2][3][4].

 