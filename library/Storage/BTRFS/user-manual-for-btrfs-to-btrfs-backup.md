---
title: "User manual for BTRFS to BTRFS backup"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt summary:** You have mounted your SSD at `/run/media/daniel/Workstation` and want to create a full system Btrfs snapshot (from `/`) and store it in a folder called `daniel-workstation` on the SSD. The folder hasn't been created yet.

### Here’s how you can proceed to create the full system Btrfs snapshot:

1. **Ensure the SSD is Mounted Correctly:**

   Confirm that the SSD is mounted at the correct location:
   ```bash
   df -h | grep Workstation
   ```

   You should see `/dev/sdc1` mounted at `/run/media/daniel/Workstation`.

2. **Create the Folder `daniel-workstation` on the SSD:**

   Since the folder `daniel-workstation` doesn’t exist, you need to create it:
   ```bash
   mkdir /run/media/daniel/Workstation/daniel-workstation
   ```

3. **Check for Existing Subvolumes:**

   Before taking the snapshot, check the current Btrfs subvolumes on your system:
   ```bash
   sudo btrfs subvolume list /
   ```

   You should see something like:
   ```
   ID 256 gen 12345 top level 5 path @
   ID 257 gen 12345 top level 5 path @home
   ```

   The `@` represents the root subvolume, and `@home` represents your home directory (if you have separate subvolumes).

4. **Take a Full System Snapshot of the Root Subvolume (`/`):**

   Use the `btrfs snapshot` command to take a snapshot of the root filesystem (`/`) and store it in the `daniel-workstation` folder on your SSD.

   If your root filesystem is using a subvolume like `@`, the command would be:
   ```bash
   sudo btrfs subvolume snapshot / /run/media/daniel/Workstation/daniel-workstation/root_snapshot_$(date +%F)
   ```

   This will create a snapshot of your root filesystem and place it inside the folder `daniel-workstation` on your external SSD.

5. **Optionally Snapshot the Home Directory (if it’s a Separate Subvolume):**

   If you have a separate subvolume for your home directory, you can snapshot that as well:
   ```bash
   sudo btrfs subvolume snapshot /home /run/media/daniel/Workstation/daniel-workstation/home_snapshot_$(date +%F)
   ```

6. **Verify the Snapshots:**

   List the contents of the `daniel-workstation` folder to verify that the snapshots were created successfully:
   ```bash
   ls /run/media/daniel/Workstation/daniel-workstation
   ```

   You should see something like:
   ```
   root_snapshot_YYYY-MM-DD
   home_snapshot_YYYY-MM-DD
   ```

### Summary of Commands:

1. **Mount SSD** (already mounted in your case):
   ```bash
   df -h | grep Workstation
   ```

2. **Create the `daniel-workstation` folder:**
   ```bash
   mkdir /run/media/daniel/Workstation/daniel-workstation
   ```

3. **Take a snapshot of the root filesystem (`/`):**
   ```bash
   sudo btrfs subvolume snapshot / /run/media/daniel/Workstation/daniel-workstation/root_snapshot_$(date +%F)
   ```

4. **Optionally snapshot the home directory:**
   ```bash
   sudo btrfs subvolume snapshot /home /run/media/daniel/Workstation/daniel-workstation/home_snapshot_$(date +%F)
   ```

5. **Verify the snapshots:**
   ```bash
   ls /run/media/daniel/Workstation/daniel-workstation
   ```

With this process, you'll have a full system snapshot stored in the `daniel-workstation` folder on your SSD, and this snapshot will be ready for restoration if needed in the future.