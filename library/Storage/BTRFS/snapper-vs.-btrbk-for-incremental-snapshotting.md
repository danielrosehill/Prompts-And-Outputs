---
title: "Snapper vs. BTRBK for incremental snapshotting"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

You identified Snapper and BTRBK as two tools that could be used efficiently to create incremental snapshots of a BTRFS filesystem onto an external SSD also formatted as BTRFS. Can you help me decide which would be more suitable for this application (or suggest an alternate tool?)

# Output

Here’s a comparison between **Snapper** and **Btrbk** to help you decide which tool is more suitable for creating incremental snapshots of a Btrfs filesystem onto an external SSD:

| Feature                   | Snapper                                                   | Btrbk                                           |
| ------------------------- | --------------------------------------------------------- | ----------------------------------------------- |
| **Ease of Setup**         | Easier initial setup, integrates with OpenSUSE and Fedora | Requires configuration but flexible             |
| **Incremental Snapshots** | Supports incremental snapshots                            | Supports incremental backups via send/receive   |
| **Automation**            | Cron jobs for automation                                  | Built-in automation options                     |
| **Exclusions**            | Limited control over exclusions                           | Can exclude subvolumes, granular control        |
| **Use Case**              | Best for managing local snapshots                         | Ideal for efficient backups to external devices |

### Recommendation:
- **Use Snapper** if you want a straightforward setup for **local** snapshots.
- **Use Btrbk** if you need **more flexibility** with external backups, especially when configuring incremental transfers and exclusions.