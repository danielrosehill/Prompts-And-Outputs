---
title: "How to use OPML files with Newsboat"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



**OPML (Outline Processor Markup Language)** files are commonly used to bundle multiple RSS feeds, but **Newsboat** itself does not directly consume OPML files. However, you can import OPML files into Newsboat by extracting the RSS feed URLs from them.

Here’s a guide to working with **OPML files** in Newsboat:

### Step 1: Convert the OPML to a List of RSS Feeds
Since your submodule contains **OPML files**, you’ll need to extract the RSS feed URLs from the OPML files and place them in your `urls` file, which Newsboat uses for feed subscriptions.

#### a. **Manual Approach** (Extract RSS Feeds from OPML)
1. **Navigate to the directory** containing your OPML files (inside the submodule):
   ```bash
   cd ~/.newsboat/Links/11Oct24/RSS/by-groups
   ```

2. **Open the OPML file** in a text editor (e.g., `group1.opml`):
   ```bash
   nano group1.opml
   ```

3. **Extract the RSS feed URLs** manually from the OPML file. OPML files usually look something like this:
   ```xml
   <outline title="Example Feed" text="Example Feed" type="rss" xmlUrl="https://example.com/rss" />
   <outline title="Another Feed" text="Another Feed" type="rss" xmlUrl="https://anotherexample.com/rss" />
   ```

4. **Copy the `xmlUrl` values**, which contain the RSS feed URLs.

5. **Add these URLs** to your `~/.newsboat/urls` file:
   ```bash
   nano ~/.newsboat/urls
   ```

6. **Paste the extracted RSS feed URLs** into the `urls` file:
   ```txt
   https://example.com/rss group1
   https://anotherexample.com/rss group1
   ```

#### b. **Automated Approach** (Script to Extract RSS Feeds from OPML)
If you have a lot of OPML files and want to automate the extraction, you can use a small **Python script** to parse the OPML files and extract the URLs into the `urls` file.

1. **Create a Python script** (e.g., `opml_to_newsboat.py`) to extract the RSS URLs from the OPML files:

   ```bash
   nano ~/opml_to_newsboat.py
   ```

2. **Add this script**:
   ```python
   import xml.etree.ElementTree as ET

   # Path to your OPML file
   opml_file = "~/.newsboat/Links/11Oct24/RSS/by-groups/group1.opml"
   # Path to your Newsboat urls file
   newsboat_urls_file = "~/.newsboat/urls"

   def extract_rss_urls(opml_file, newsboat_urls_file):
       tree = ET.parse(opml_file)
       root = tree.getroot()

       with open(newsboat_urls_file, 'a') as urls_file:
           for outline in root.findall('.//outline'):
               xml_url = outline.get('xmlUrl')
               if xml_url:
                   urls_file.write(f"{xml_url} group1\n")

   # Run the function
   extract_rss_urls(opml_file, newsboat_urls_file)
   ```

3. **Run the script** to automatically extract RSS URLs from the OPML file and append them to your `urls` file:
   ```bash
   python3 ~/opml_to_newsboat.py
   ```

   This script parses the OPML file and adds all RSS URLs to the `urls` file with the tag `group1`.

### Step 2: Refresh Newsboat
Once you have added the RSS feed URLs (whether manually or via a script), refresh Newsboat to load the feeds.

1. **Open Newsboat**:
   ```bash
   newsboat
   ```

2. **Refresh feeds** by pressing `r` inside Newsboat. Your new RSS feeds should now appear in the feed list.

### Step 3: Set Up Git to Track and Sync Your Newsboat Configuration

1. **Commit the updated `urls` file** (containing the RSS feeds extracted from the OPML files):
   ```bash
   cd ~/.newsboat
   git add urls
   git commit -m "Added feeds from OPML to Newsboat"
   ```

2. **Push the changes** to your remote GitHub repository:
   ```bash
   git push
   ```

### Summary

- **Newsboat cannot use OPML files directly**, but you can extract the RSS feed URLs from them and add them to your `urls` file.
- You can extract the RSS feed URLs **manually** by opening the OPML file and copying the `xmlUrl` attributes or **automate** the process using a **Python script** to parse the OPML file.
- Once you have extracted the RSS URLs, add them to your `~/.newsboat/urls` file and categorize them using tags as needed.
- After updating the feeds, commit and push your changes to the GitHub repository.

This way, you can leverage your existing OPML files while still using Newsboat to monitor the feeds.