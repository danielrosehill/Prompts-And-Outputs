---
title: "Block level backup while Fedora is running"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Thanks for your help. As you know I'm running Fedora Linux. We've established that it would be a good idea to take a block level backup before moving over to RAID1. I have an NAS on my LAN. Can you suggest any tools that might allow me to take a block level backup while the OS is running? While Clonezilla is great, it's a bit of a pain to use!

# Output

Based on the information provided and your specific requirements for a block-level backup of your Fedora Linux system while it's running, here are some potential solutions:

1. Rsync with fsarchiver:
   While not strictly a block-level backup, this combination can create a full system backup that's restorable:

   ```bash
   sudo rsync -avAXHS --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} / /path/to/backup/
   sudo fsarchiver savefs /path/to/backup/system.fsa /dev/sdXY
   ```

   This would create a full copy of your system and then create an image of the filesystem structure.

2. LVM Snapshots:
   If your system is using LVM, you can create a snapshot and then use dd to create a block-level backup:

   ```bash
   sudo lvcreate -L10G -s -n backup /dev/vg0/root
   sudo dd if=/dev/vg0/backup | ssh user@nas-ip 'dd of=/path/to/backup.img'
   ```

3. Borg Backup:
   While not block-level, Borg is efficient and can create full system backups:

   ```bash
   sudo borg create --progress --compression lz4 user@nas-ip:/path/to/repo::backup-{now} / --exclude '/dev' --exclude '/proc' --exclude '/sys' --exclude '/tmp' --exclude '/run' --exclude '/mnt' --exclude '/media' --exclude '/lost+found'
   ```

4. Duplicity:
   Another tool that can create full system backups:

   ```bash
   sudo duplicity --exclude /proc --exclude /sys --exclude /tmp --exclude /run --exclude /mnt --exclude /media --exclude /lost+found / scp://user@nas-ip//path/to/backup
   ```

5. Timeshift:
   While primarily designed for system restore points, Timeshift can create BTRFS snapshots that can be used as backups[1].

For a true block-level backup while the system is running, you might need to use a combination of tools or consider using a live system for the backup process. The methods above provide alternatives that can create comprehensive system backups while the system is running, even if they're not strictly block-level.

Remember, whichever method you choose, it's crucial to test the restore process to ensure the backup is usable before proceeding with your RAID 1 migration.

 