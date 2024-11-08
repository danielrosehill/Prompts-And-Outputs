---
title: "looking at feasibility of one million note vault"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Scaling your Obsidian vault to one million notes without significant slowdown or hardware constraints depends on several factors, such as the types of notes, the structure of your vault, and your device's hardware. Here’s a breakdown of what to consider:

1. Obsidian's Performance with Large Vaults

Text-Based Notes: Markdown files (which Obsidian uses) are extremely lightweight. Even with one million notes, the storage size might still be manageable, depending on the content. If each note remains text-based without large attachments, the performance impact on storage space would be minimal.

Indexing and Search: Obsidian maintains an index of all your notes to enable features like search, backlinks, and graph views. With one million notes, indexing and search operations might start to slow down, especially for complex queries, but this depends heavily on how efficiently Obsidian continues to optimize its internal systems over time.

Graph View: The graphical visualization of relationships between notes could become slow or resource-intensive as the number of notes increases. Disabling the graph view for a vault of that size might improve performance.


2. Hardware Considerations

Storage: Even with a million text-based notes, if each note averages 10 KB (a generous estimate), you would be looking at roughly 10 GB of storage. This should not be a problem on modern smartphones or computers with decent storage capacity.

RAM and CPU: Managing a vault with one million notes may require more RAM and CPU power, particularly when loading the vault, performing search operations, or running plugins. However, unless you have many large attachments or complex operations running in Obsidian, this should remain manageable on modern hardware.

Android Devices: On mobile, especially Android devices, you may encounter some constraints if the app tries to load too many notes into memory or process complex queries, but as long as you are using lightweight notes, the app should remain functional.


3. File System Constraints

File Access: File systems can handle millions of files, but performance might degrade slightly when managing that many files in a single directory. To mitigate this, ensure your notes are well-organized into subfolders.

Backup and Syncing: Syncing one million notes, especially with services like Backblaze B2, could introduce delays due to the sheer number of files. Incremental syncing (only syncing changed files) should help reduce this overhead.


Conclusion:

Yes, it's possible to scale to one million notes without causing significant slowdown, especially if you maintain the vault as primarily text-based markdown files. The most likely points of slowdown will be in search, graph view, and syncing large numbers of files. By optimizing folder structure, limiting complex queries, and using sufficient hardware (plenty of RAM and a strong CPU), you should be able to maintain performance as your vault grows.

