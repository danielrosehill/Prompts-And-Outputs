---
title: "Knowledge management tools with support for NoSQL interlinked data stores"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


---
Prompt: Are there any note taking or knowledge management apps which store data in a NoSQL database which allows users to define custom taxonomies and fields as metadata and allows saved text files to be interlinked on that basis? If so please list both self hostable and SaaS tools that meet these requirements. For SaaS tools, please state how the user can backup the data.
---
Yes, there are several note-taking or knowledge management apps that store data in a NoSQL database, allow users to define custom taxonomies and fields as metadata, and support interlinking of saved text files based on that metadata. Below is a list of both self-hostable and SaaS tools that meet these requirements, along with information on how users can back up their data in the case of SaaS tools.

### **Self-Hostable Tools**

1. **Joplin (with Joplin Server)**
   - **Database**: Uses SQLite or a NoSQL-like synchronization backend when used with Joplin Server.
   - **Custom Taxonomies and Fields**: You can define custom tags and metadata fields through plugins.
   - **Interlinking**: Supports linking between notes using markdown links and tags.
   - **Backup**: As a self-hosted tool, you can back up the entire Joplin database by exporting notes as JEX files or syncing them to a directory structure.

2. **TiddlyWiki (with TiddlyServer or TiddlyWeb)**
   - **Database**: Uses JSON-like data structures within a single HTML file, or can be hosted on a NoSQL backend using TiddlyServer or TiddlyWeb.
   - **Custom Taxonomies and Fields**: Highly customizable with user-defined fields, tags, and taxonomies.
   - **Interlinking**: Natively supports linking between “tiddlers” (notes) with customizable metadata.
   - **Backup**: Backup is straightforward as you can copy the single HTML file or backup the hosted data.

3. **Trilium Notes**
   - **Database**: Uses a NoSQL database (MongoDB).
   - **Custom Taxonomies and Fields**: Allows custom attributes and metadata for each note.
   - **Interlinking**: Supports bi-directional linking between notes based on tags, metadata, or content.
   - **Backup**: Offers built-in export functionality for backup, or you can back up the MongoDB database directly.

4. **Dendron (VSCode Extension)**
   - **Database**: Utilizes a local file system but can be backed by a NoSQL-like structure when integrated with tools like CouchDB.
   - **Custom Taxonomies and Fields**: Allows for hierarchical tagging and custom metadata fields within markdown files.
   - **Interlinking**: Supports linking between notes using a hierarchical structure and custom metadata.
   - **Backup**: Backup can be managed using Git or another version control system.

### **SaaS Tools**

1. **Notion**
   - **Database**: Operates on a proprietary NoSQL database backend.
   - **Custom Taxonomies and Fields**: Allows users to define custom properties and metadata for database entries (e.g., notes).
   - **Interlinking**: Supports interlinking between notes and pages based on metadata or direct links.
   - **Backup**: Users can back up data by exporting content as Markdown, CSV, or HTML files. Additionally, there are API integrations and third-party tools (e.g., Notion Backup) for automated backups.

2. **Coda**
   - **Database**: Uses a NoSQL-like structure internally.
   - **Custom Taxonomies and Fields**: Allows users to define custom fields, taxonomies, and metadata within documents.
   - **Interlinking**: Supports linking between sections and rows based on metadata or direct references.
   - **Backup**: Data can be backed up by exporting documents to formats like CSV, PDF, or through the Coda API. Regular exports can be automated via third-party tools or scripts.

3. **Airtable**
   - **Database**: Operates on a NoSQL-like database backend.
   - **Custom Taxonomies and Fields**: Supports extensive customization of fields, metadata, and tags.
   - **Interlinking**: Allows linking records between tables, creating a web of interconnected data.
   - **Backup**: Data can be exported to CSV or Excel files. Airtable also offers an API that can be used for automated backups.

4. **Roam Research**
   - **Database**: Uses a graph-based NoSQL database.
   - **Custom Taxonomies and Fields**: Allows tagging and custom metadata within pages and notes.
   - **Interlinking**: Supports bi-directional linking between notes based on tags and references.
   - **Backup**: Data can be backed up by exporting all notes in Markdown format. Additionally, Roam offers an API for more advanced backup solutions.

5. **Tana**
   - **Database**: Uses a proprietary NoSQL-like backend.
   - **Custom Taxonomies and Fields**: Supports custom fields and metadata with a flexible tagging system.
   - **Interlinking**: Natively supports linking between notes and data points based on metadata.
   - **Backup**: Users can export their data in various formats (Markdown, JSON) for backup. Tana also provides an API for automated backup solutions.

### **Backup Considerations for SaaS Tools**
For SaaS tools, it’s important to establish a regular backup routine to ensure data integrity. You can use the built-in export functions or leverage APIs to automate the process. Additionally, third-party tools and scripts can be used to schedule and automate backups to local storage or cloud services like Google Drive, Dropbox, or a personal server.