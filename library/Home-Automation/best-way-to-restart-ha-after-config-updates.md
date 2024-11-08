---
title: "Best way to restart HA after config updates"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, there is a lighter way to apply changes without fully rebooting Home Assistant. Instead of using `ha core reboot`, which restarts the entire Home Assistant core, you can use `ha core restart`. This command restarts the core services without rebooting the entire system, making the process faster.

Here’s the command:

```bash
ha core restart
```

This will reload the configuration and apply changes without requiring a full system reboot. It’s the preferred option after updating the `configuration.yaml` file.