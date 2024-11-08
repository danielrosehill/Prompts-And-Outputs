---
title: "auto sync vault and resource usage"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You are correct to be cautious, but the level of resource intensity for periodic auto-sync in Obsidian, especially when syncing to B2, depends on several factors:

Factors to Consider:

1. Vault Size and Frequency of Changes:

Since your vault is primarily text-based, syncing small markdown files typically isn’t resource-intensive. If you aren't frequently adding large attachments (e.g., images or PDFs), the impact should be minimal.



2. Sync Frequency:

The resource usage will depend on how often the sync happens. A very frequent sync (e.g., every minute) might use more CPU, battery, and bandwidth. However, syncing every 10–30 minutes might not be noticeable unless you're making significant changes.



3. B2 (Backblaze) Sync Overhead:

B2 is known for being efficient with incremental updates, meaning it usually only uploads the changes made since the last sync, which should keep resource usage low.



4. Battery and Network Usage:

The main impact would likely be on your device's battery and data usage, especially if you're on mobile data. If you're primarily on Wi-Fi and charging, the periodic auto-sync might not noticeably affect performance.




Conclusion:

Auto-syncing every 10-30 minutes is unlikely to cause significant resource drain for text-heavy vaults like yours. If you’re concerned, you can test enabling it for a few days with moderate frequency (e.g., 15 minutes) and monitor resource usage (battery, CPU, etc.) to see if it noticeably impacts performance.

If you're not seeing any issues, you may want to enable it for more convenience.

