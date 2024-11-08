---
title: "How to use rclone over the CLI to push a backup archive to the cloud"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Can you teach me how to use rclone to manually push a backup archive to a bucket? Let's say that I have a tar.gz I want to backup on my desktop. I'd like to firstly review my buckets, then find the right one to use. Then, I'll want to upload the archive to that bucket and monitor the progress.

# Output

Here’s a step-by-step guide on how to use **rclone** to back up your `tar.gz` archive to a bucket, review your available buckets, and monitor the progress of the upload.

### 1. **Install rclone (if not already installed)**
If rclone is not yet installed, you can install it via your package manager. For example, on Fedora (which you are using):
```bash
sudo dnf install rclone
```

### 2. **Configure rclone for your cloud storage**
First, you need to configure rclone with your cloud storage provider (AWS S3, Google Cloud, Backblaze B2, etc.).

- Run the rclone config command to set up a new remote:
  ```bash
  rclone config
  ```
- Follow the prompts to create a new remote, providing the necessary credentials and information for your cloud storage provider. Each provider has specific steps, but rclone’s documentation provides detailed instructions for popular services like AWS, B2, Google Drive, and others.

### 3. **Review Your Buckets**
Once your cloud provider is configured, you can list all available buckets in your account with:
```bash
rclone lsd remote:/
```
Replace `remote` with the name of the remote you configured (e.g., `s3`, `b2`, `gdrive`, etc.). This will list the directories (buckets in the case of S3 or B2).

### 4. **Upload the tar.gz Archive**
After reviewing your buckets and choosing the correct one, you can upload the file to your selected bucket. Let’s say your archive is located on your desktop as `backup.tar.gz`, and you want to upload it to a bucket called `my-backups-bucket`.

Use the following command:
```bash
rclone copy ~/Desktop/backup.tar.gz remote:my-backups-bucket/ --progress
```
This command:
- Copies `backup.tar.gz` to the `my-backups-bucket` bucket.
- The `--progress` flag will show the upload progress in real-time.

### 5. **Monitor the Upload Progress**
The `--progress` flag will show the transfer rate, amount of data uploaded, and estimated completion time. If you want more detailed logs, you can add:
```bash
rclone copy ~/Desktop/backup.tar.gz remote:my-backups-bucket/ --progress -v
```
The `-v` flag adds verbosity, displaying more detailed information about the process.

### 6. **Verify the Upload**
Once the upload is complete, you can verify it by listing the contents of the bucket:
```bash
rclone ls remote:my-backups-bucket/
```
This will show the files in the bucket, including your newly uploaded `backup.tar.gz`.

### 7. **Optional: Sync Directories**
If you want to regularly back up directories instead of single files, you can use the `sync` command, which ensures that the destination matches the source:
```bash
rclone sync ~/Desktop/backup-directory/ remote:my-backups-bucket/ --progress
```
This is useful for keeping an entire directory in sync with your cloud bucket.

### Example Workflow Summary:
1. Configure rclone with `rclone config`.
2. Review your buckets using `rclone lsd remote:/`.
3. Upload the archive with `rclone copy ~/Desktop/backup.tar.gz remote:my-backups-bucket/ --progress`.
4. Verify the upload with `rclone ls remote:my-backups-bucket/`.

Let me know if you'd like more details on any specific step!