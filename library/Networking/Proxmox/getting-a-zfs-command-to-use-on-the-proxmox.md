---
title: "Getting a ZFS command to use on the Proxmox"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Now that we've established that it's ZFS, could you give me a command which will show ideally all of these details: current disk usage, current disk remaining. ZFS status. Last scrub. List of all discs in the server.

# Output

To display all the requested details about your **ZFS** pool and the disks in your server, you can use the following **commands**. Each command provides specific information about the pool's status, disk usage, and hardware:

### 1. **ZFS Pool Status, Scrub Information, and Disk Usage**
This command will provide the **current status**, **scrub history**, and **disk usage** (used/available space) for the ZFS pool:

```bash
zpool list -v
```

- This will show:
  - **Size**: Total size of the ZFS pool.
  - **Alloc**: Allocated (used) space.
  - **Free**: Remaining free space.
  - **Health**: Health of the ZFS pool.

You can also use the following to get a more detailed status (including the last scrub and individual disk health):

```bash
zpool status
```

- **Scan** field will show the date and result of the last scrub.

### 2. **Detailed Disk Usage Information**
For detailed usage statistics of each dataset within the ZFS pool, including **used** and **available** space, run:

```bash
zfs list
```

- This will show how much space is used by each dataset and how much remains available.

### 3. **List All Disks on the Server**
To list **all disks** currently connected to the server (whether or not they are part of the ZFS pool), use:

```bash
lsblk
```

- This will list all block devices, including mounted and unmounted drives, and show their sizes, mount points, and partitions.

Alternatively, for more detailed information, including **UUIDs** and partitions:

```bash
fdisk -l
```

This command will show detailed partition and disk information for all drives on the server.

### Combined Workflow

If you want to combine the most relevant commands into one workflow to display current **ZFS status**, **disk usage**, and all **disks** on the server, here’s an ideal command sequence:

```bash
echo "ZFS Pool Status:" && zpool status && echo -e "\nZFS Pool Usage:" && zfs list && echo -e "\nDisks on Server:" && lsblk
```

- **`zpool status`**: Shows ZFS status, including last scrub.
- **`zfs list`**: Shows detailed usage statistics of the ZFS pool.
- **`lsblk`**: Lists all disks on the server.

This will provide all the relevant information in one go. Let me know if you need further customization!