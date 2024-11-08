---
title: "Seeing the snapshots that BTRFS creates"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To find out where the Snapper snapshot went, you can list the snapshots using the following command:

```bash
sudo snapper -c SSD-Snapshots list
```

This will show a list of all snapshots managed under the `SSD-Snapshots` configuration. You can then find the actual location of these snapshots, which are typically stored in a `.snapshots` directory inside the subvolume being managed. 

### Checking Snapshot Location:
If you want to see the full path, navigate to:
```bash
cd /.snapshots
ls
```

This should show the directories where your snapshots are located.