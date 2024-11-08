---
title: "The reboot options in the HAOS CLI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! When using the Home Assistant CLI (`ha` command), there are generally two different reboot options available. Each serves a different purpose, depending on what you want to restart:

### 1. **Core Restart**
   ```bash
   ha core restart
   ```

   - **Purpose**: This command restarts the **Home Assistant core** service itself.
   - **Scope**: It only restarts the Home Assistant application that manages automations, integrations, and other features. This is useful if you've made changes to the `configuration.yaml` or any other settings related directly to Home Assistant’s core that require a reload.
   - **Impact**: The rest of the system remains unaffected. The host OS, supervisor, and add-ons keep running normally while only the core application is restarted.

   Use this option when you make changes to the Home Assistant configuration or when something within Home Assistant is not working as expected (e.g., automations not firing) and you want to restart the core application without affecting anything else.

### 2. **Host Reboot**
   ```bash
   ha host reboot
   ```

   - **Purpose**: This command reboots the **entire Home Assistant host** machine.
   - **Scope**: It restarts everything, including the underlying operating system, supervisor, Home Assistant core, and all add-ons running on the host.
   - **Impact**: This is similar to rebooting a computer—everything will go down and come back up. It’s a more comprehensive reset, which can be helpful if there are issues with the OS itself or with multiple services that need to be restarted.
   
   Use this option if you suspect a deeper problem with the hardware, operating system, or need to clear persistent network or performance issues. It can also be useful if you have issues with add-ons that don’t get resolved by restarting the core.

### Summary of Differences
- **Core Restart (`ha core restart`)**: Restarts only Home Assistant’s core application.
- **Host Reboot (`ha host reboot`)**: Restarts the entire host, including the operating system, supervisor, Home Assistant core, and all add-ons.

In general, if you just want to apply a configuration change or refresh Home Assistant functionality, the **core restart** is sufficient. If you're facing systemic issues, then a **host reboot** is more appropriate.

Let me know if you need more detailed information on these or anything else related to Home Assistant!