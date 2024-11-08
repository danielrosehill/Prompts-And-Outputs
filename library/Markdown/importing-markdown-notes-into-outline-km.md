---
title: "Importing markdown notes into Outline KM"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking for the best way to import a large collection of Markdown notes into Outline Knowledge Manager (KM).

### Importing Markdown Notes into Outline KM

Outline KM doesn't have a direct bulk import feature specifically for Markdown files, but there are several ways you can manage importing your collection effectively. Here are the best approaches to consider:

### 1. **Use Outline’s Document Import Feature**

Outline supports importing Markdown files individually via its web interface. While this method may not be ideal for a large collection, it can be useful for importing smaller groups of notes.

1. **Prepare Your Markdown Files**
   - Ensure your files are well-organized, and consider creating directories or folders that reflect how you want them structured in Outline.

2. **Import Files Manually**
   - Go to **Outline KM** and select a **collection** or **folder** where you want to import the notes.
   - Click **New**, then **Import**, and select a Markdown file.
   - Repeat this process for each file, or batch smaller groups of Markdown files if your collection is manageable.

### 2. **Automate Upload Using Outline’s API**

For importing a large number of Markdown notes, you can use Outline’s **API** to automate the process. This is the most efficient way to handle bulk uploads.

#### Step-by-Step to Automate with the API:

1. **Create an API Token**
   - Go to your **Outline settings** and generate an **API token**. This token will allow you to authenticate programmatically.

2. **Write a Script to Upload Files**
   - You can use a programming language like **Python** to interact with the Outline API.
   - Here’s an example of how to do this:
     - Make sure to replace `YOUR_API_TOKEN`, `COLLECTION_ID`, and `FOLDER_ID` with your actual data.

   ```python
   import os
   import requests

   # Replace with your Outline KM URL and API token
   API_URL = "https://your-outline-url.com/api/documents.create"
   API_TOKEN = "YOUR_API_TOKEN"
   COLLECTION_ID = "YOUR_COLLECTION_ID"

   headers = {
       "Authorization": f"Bearer {API_TOKEN}",
       "Content-Type": "application/json"
   }

   def upload_markdown(file_path, collection_id, parent_id=None):
       with open(file_path, 'r') as file:
           content = file.read()
           data = {
               "title": os.path.basename(file_path).replace('.md', ''),
               "text": content,
               "collectionId": collection_id
           }
           if parent_id:
               data["parentDocumentId"] = parent_id
           
           response = requests.post(API_URL, json=data, headers=headers)
           if response.status_code == 200:
               print(f"Uploaded {file_path}")
           else:
               print(f"Failed to upload {file_path}: {response.text}")

   # Path to your Markdown notes
   markdown_directory = "/path/to/your/markdown/files"

   for file_name in os.listdir(markdown_directory):
       if file_name.endswith(".md"):
           file_path = os.path.join(markdown_directory, file_name)
           upload_markdown(file_path, COLLECTION_ID)
   ```

3. **Organize Files by Collections or Folders**
   - If you have subfolders within your Markdown notes, consider updating the script to handle folder structures. You can modify the script to create a **parent document** (folder) for each subdirectory and then add each Markdown file as a **child document**.

### 3. **Use a File Syncing Tool with Export Options**

If you are comfortable managing files on your server, you can automate the upload process with file syncing tools that interact with Outline:

1. **Rclone (Advanced)**
   - **Rclone** is a tool that can sync files between cloud services, and while Outline isn’t natively supported, you can use Rclone to **push files to a web server**, which can then be picked up by an Outline process if configured to read from a specific directory.
   - This method requires more setup but can be useful if you frequently update your Markdown notes and want to maintain synchronization between Outline and your local files.

2. **Deploy a File-Watching Script**
   - Consider using **inotify** (Linux) or **fswatch** (macOS) to watch your local directory for changes, and when new Markdown files are added, have the script automatically push them to Outline via the API.

### 4. **Manual Import via Copy-Paste (Least Efficient)**

If your collection isn't too large, you can manually copy and paste the content of each Markdown file into Outline:

1. **Open Markdown Files Locally**
   - Open your Markdown files using any text editor.
2. **Create a New Document in Outline**
   - In Outline, create a new document and paste the content. Use Outline’s Markdown editor to make any necessary adjustments.

### Recommendations:
- **For Large Collections**: Use the **API method** to automate the upload process. It’s the most scalable and repeatable way to handle large numbers of files.
- **For Small Groups of Notes**: Consider manually importing or copying and pasting them through Outline’s interface.
- **For Ongoing Synchronization**: Consider setting up a **file-watching script** or advanced solutions like **Rclone** to sync files from your local machine.

### Summary
1. **Manual Import**: Use Outline’s web interface to import files one by one.
2. **API Automation**: Write a script to automate bulk uploads.
3. **Syncing Tools**: Set up sync solutions for ongoing updates.

Using the API is the most efficient and scalable approach if you have a large collection of Markdown notes to import into Outline KM.