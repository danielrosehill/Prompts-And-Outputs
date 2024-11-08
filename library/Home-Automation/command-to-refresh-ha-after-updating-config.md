---
title: "Command to refresh HA after updating config"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To refresh your Home Assistant server after modifying the `configuration.yaml` file, follow these steps:

1. **Check the configuration** (optional but recommended):
   Run this command to ensure the syntax and structure of your configuration file are correct:
   ```bash
   ha core check
   ```
   This will validate your configuration and alert you to any errors.

2. **Restart Home Assistant**:
   After validation, restart Home Assistant to apply the changes:
   ```bash
   ha core restart
   ```

If you're not using Home Assistant OS or `ha` commands and instead have Home Assistant running in Docker or as a service, you can use one of the following methods:

- **Docker**:
   ```bash
   docker restart homeassistant
   ```

- **Systemd service** (if Home Assistant is running as a service):
   ```bash
   sudo systemctl restart home-assistant.service
   ```

After restarting, your updated configuration should take effect.