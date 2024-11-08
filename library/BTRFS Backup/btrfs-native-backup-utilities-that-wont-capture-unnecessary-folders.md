---
title: "BTRFS native backup utilities that won't capture unnecessary folders"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

Are there any BTRFS snapshot utilities that can work with an external BTRFS SSD to create incremental snapshots of the host OS and which might even be able to intelligently avoid including unnecessary folders in the full system backups?

# Output

Yes, there are a few Btrfs snapshot utilities that can work with external Btrfs SSDs and offer incremental snapshot capabilities:

### 1. **Snapper**
- **Description**: Snapper is a powerful tool designed for Btrfs and LVM. It can automatically create incremental snapshots, which is ideal for backup purposes. 
- **Features**: Supports cleaning up old snapshots, configuration of exclusions via scripts, and automation.

### 2. **Btrbk**
- **Description**: Specifically designed for Btrfs, btrbk can efficiently create incremental snapshots and manage backups across local and external devices.
- **Features**: It allows for exclusion configurations, is highly customizable, and can handle multi-device setups.

### 3. **Timeshift (Limited Btrfs Features)**
- **Description**: Primarily for system restoration, Timeshift can utilize Btrfs snapshots. Though it's not specifically tailored for full external backup use, it offers snapshot capabilities.
- **Features**: Simple, intuitive, and can exclude directories based on configurations.

These tools can help automate and efficiently manage snapshots, with some degree of control over which folders to exclude. For external backups, **btrbk** is often the most robust and flexible solution.