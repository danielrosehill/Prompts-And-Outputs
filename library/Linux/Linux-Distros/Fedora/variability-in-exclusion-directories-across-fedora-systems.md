---
title: "Variability in exclusion directories across Fedora systems"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The list of directories to exclude might vary depending on individual system setups and configurations. Here are some factors that can cause variability:

1. **Custom Mount Points**: Users may have additional external drives or network shares mounted under `/mnt` or `/media`. Excluding these will depend on what needs to be backed up.
2. **Custom Services**: Some Fedora systems might have additional directories for custom services under `/srv` or `/opt`, which may or may not need exclusion.
3. **Package Managers**: Systems using Snap or Flatpak might have `/snap` or `/var/lib/flatpak` directories, which may be treated differently based on backup needs.

Overall, while some directories like `/proc`, `/sys`, and `/tmp` are typically safe to exclude universally, individual setups will dictate adjustments.