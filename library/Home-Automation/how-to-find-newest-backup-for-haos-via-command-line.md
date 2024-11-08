---
title: "How to find newest backup for HAOS via command line"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Summary of the prompt: Daniel is looking to find the freshest backup for Home Assistant via the command line.

---

To find the most recent (freshest) backup available for Home Assistant via the command line, you can follow these steps:

1. **List All Backups:**

   Use the following command to get a list of all available backups:
   ```bash
   ha backups list
   ```
   This will provide a summary of all backups, including their slugs, names, creation dates, and sizes. You can use this information to identify the most recent backup.

2. **Sort Backups by Date (Optional):**

   To get a more structured list and quickly identify the freshest backup, you can use `jq` to parse the output. Assuming `jq` is installed on your system:
   ```bash
   ha backups list --raw-json | jq '.data.backups | sort_by(.date) | reverse | .[0]'
   ```
   This command will sort the backups by date, in descending order, and show you the most recent one.

3. **Identify the Freshest Backup Slug:**

   Once you have the output, look for the `slug` key to identify the backup you want to use. You can then proceed to restore that backup with:
   ```bash
   ha backups restore <slug>
   ```

If you don’t have `jq` installed, you can still look at the dates manually in the output from `ha backups list` to identify the most recent one. The backup entries will contain a `date` field that you can use for reference.

Let me know if you need help with anything else regarding restoring or managing backups!

# When was this backup taken and how to restore to it

```
{  
 "slug": "7b5fbaea",  
 "name": "DailyBackup: Wednesday, October 16, 2024",  
 "date": "2024-10-15T23:30:00.270237+00:00",  
 "type": "partial",  
 "size": 60.07,  
 "location": null,  
 "protected": false,  
 "compressed": true,  
 "content": {  
   "homeassistant": true,  
   "addons": [],  
   "folders": []  
 }  
}
```

The backup you've listed has the following details:

- **Name**: DailyBackup: Wednesday, October 16, 2024
- **Slug**: 7b5fbaea
- **Date**: `2024-10-15T23:30:00.270237+00:00`

The date field (`2024-10-15T23:30:00.270237+00:00`) indicates the backup was taken at 23:30 UTC on October 15, 2024. To convert this to your local time, adjust based on your time zone. For example, if you're in Jerusalem (UTC+3), the local time would be:

- **Local Time**: October 16, 2024, at 02:30 AM (UTC+3)

### Restoring This Backup

To restore the backup using the CLI, follow these steps:

1. **Restore the Backup:**
   Since the backup type is partial, you can restore it as follows:
   ```bash
   ha backups restore 7b5fbaea
   ```
   This command will restore the specific backup using the provided slug (`7b5fbaea`).

2. **Restart Home Assistant:**
   Once the restore is complete, you may need to restart Home Assistant to apply the changes:
   ```bash
   ha core restart
   ```

The backup appears to contain the Home Assistant core configuration (`homeassistant: true`) but no add-ons or folders (`addons: []`, `folders: []`). This means that it will restore just the main configuration without any add-on data or folder content. Make sure this is what you want to do before proceeding.

Let me know if you need further assistance or clarification!