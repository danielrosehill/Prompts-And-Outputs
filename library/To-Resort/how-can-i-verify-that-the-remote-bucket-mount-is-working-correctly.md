---
title: "How can I verify that the remote bucket mount is working correctly"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To verify that your rclone mount is working and syncing with the remote B2 bucket, you can follow these steps:

### 1. **Create a Test File in the Mounted Directory**
You can create a small test file (e.g., `testfile.txt`) in your mounted directory to verify that it syncs to the remote bucket. Run the following command in your terminal:
```bash
echo "Test file for syncing" > /home/daniel/Clouds/BackupsFE/testfile.txt
```

### 2. **Verify the File Sync with rclone**
Once the file is created, you can verify that it has successfully synced up to the remote B2 bucket using the following steps:

#### **List the Bucket Contents via rclone**
You can use rclone to list the contents of the remote bucket, which should now include the `testfile.txt`:
```bash
rclone ls yourbusinessb2:drbackupsfe
```
If the mount is working correctly, you should see the `testfile.txt` listed in the output.

#### **Compare the Mounted Directory and Remote Bucket**
You can use rclone’s `check` command to compare the contents of your mounted directory and the remote bucket to verify that everything is synced correctly:
```bash
rclone check /home/daniel/Clouds/BackupsFE yourbusinessb2:drbackupsfe
```
This will check for differences between the local mount and the remote bucket, ensuring that they are identical.

### 3. **Verify Through the Web Interface**
As a final step, you can log in to the Backblaze B2 web interface and navigate to the `drbackupsfe` bucket. Check if `testfile.txt` has been uploaded to the bucket, confirming that the sync was successful.

This should verify that your rclone mount is working as expected and that files are syncing properly between your local system and the remote bucket. Let me know if you'd like any additional help!