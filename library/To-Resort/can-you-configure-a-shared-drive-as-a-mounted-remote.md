---
title: "Can you configure a shared drive as a mounted remote"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is it possible to configure a Google shared drive as a remote in rclone or any other CLI that works with Fedora? And to do so in a way that doesn't require syncing the whole drive but more mounts it as a remote volume?

# Output

Yes, it is absolutely possible to configure a **Google Shared Drive** as a remote in **rclone** on Fedora (or any other Linux distribution) without syncing the entire drive, effectively mounting it as a remote volume. This method allows you to browse and work with files directly on the drive without downloading everything locally.

### Steps to Configure a Google Shared Drive as a Remote in rclone:

#### Step 1: Install rclone
If you haven't installed **rclone** yet, you can install it on Fedora using the following command:

```bash
sudo dnf install rclone
```

#### Step 2: Configure rclone for Google Drive
1. **Run the rclone configuration**:

   ```bash
   rclone config
   ```

2. **Add a new remote**:
   - Type `n` to create a new remote.
   - Name the remote (e.g., `mysharedrive`).

3. **Choose the cloud storage**:
   - Select **Drive** by typing the corresponding number (usually `13` for Google Drive).

4. **Configure Google Drive authentication**:
   - When prompted for the **Client ID** and **Client Secret**, leave them blank for the default or input your own if you have a Google API project set up.
   
5. **Scope of Access**:
   - Choose the access scope for rclone. To access both shared and personal drives, choose the following option:
     ```
     1 / Full access all files, including Application Data Folder.
     ```
     (Choose the appropriate number based on your version.)

6. **Shared Drive Support**:
   - When prompted with the question **"Configure this as a team drive?"**, type `y` to indicate that you want to configure the remote for a Shared Drive (Team Drive).

7. **Obtain the authentication token**:
   - Follow the on-screen instructions to log in to your Google account and authorize rclone.

8. **Complete the setup**:
   - If successful, rclone will confirm the connection and offer a few final options. Choose the defaults or fine-tune as needed, then type `q` to quit the configuration.

#### Step 3: Mount the Google Shared Drive
Now that the remote is configured, you can mount it as a remote volume using **rclone mount**. This step ensures that files are accessed directly from the cloud, without syncing the entire drive.

1. **Create a mount point** (if it doesn’t already exist):

   ```bash
   mkdir ~/sharedrive
   ```

2. **Mount the Google Shared Drive**:

   ```bash
   rclone mount mysharedrive: ~/sharedrive --vfs-cache-mode minimal
   ```

   - `mysharedrive` is the name of the remote you configured in rclone.
   - `~/sharedrive` is the local mount point.
   - `--vfs-cache-mode minimal` allows for minimal caching of files locally, so that you can access them as needed without downloading everything.

3. **Access the files**:
   - Now, files will be accessible under the mount point `~/sharedrive` as if they are part of the local file system. You can open, edit, and manage files directly on Google Drive without syncing them locally.

#### Step 4: Unmount the Google Drive
When you're done, unmount the drive using:

```bash
fusermount -u ~/sharedrive
```

### Optional: Automating the Mounting Process
You can create a systemd service to automatically mount the drive at boot or on demand:

1. **Create a systemd service file**:

   ```bash
   sudo nano /etc/systemd/system/rclone-sharedrive.service
   ```

2. **Add the following content**:

   ```ini
   [Unit]
   Description=Mount Google Shared Drive using rclone
   After=network-online.target

   [Service]
   Type=simple
   ExecStart=/usr/bin/rclone mount mysharedrive: /home/yourusername/sharedrive --vfs-cache-mode minimal
   ExecStop=/bin/fusermount -u /home/yourusername/sharedrive
   Restart=always
   User=yourusername

   [Install]
   WantedBy=multi-user.target
   ```

   - Replace `yourusername` with your actual username.
   - Replace `/home/yourusername/sharedrive` with the correct path for the mount point.

3. **Enable and start the service**:

   ```bash
   sudo systemctl enable rclone-sharedrive.service
   sudo systemctl start rclone-sharedrive.service
   ```

This will automatically mount the shared Google Drive upon boot and keep it running as a background service.

### Conclusion:
Using **rclone**, you can easily mount a Google Shared Drive as a remote volume without syncing the entire drive. This method is highly efficient, especially if you work with large shared drives and want direct access to files from the cloud.