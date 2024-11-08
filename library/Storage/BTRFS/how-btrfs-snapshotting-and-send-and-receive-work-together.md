---
title: "How BTRFS snapshotting and send and receive work together"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


When you want to store a Btrfs snapshot on another system, such as an external SSD, you can use **Btrfs send/receive**. Here’s how it works:

1. **Create a Snapshot on the Local System**:
   The snapshot remains on the same filesystem and only references existing data blocks without copying them.

2. **Transfer Snapshot to External SSD**:
   Use `btrfs send` to stream the snapshot to another location, and `btrfs receive` to write it on the external SSD. This process copies the actual data, creating a complete backup that can be used to restore the system. 

By doing this, you transfer all necessary data from the snapshot without duplicating files locally.