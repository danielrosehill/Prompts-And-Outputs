---
title: "Automating extension updates in Home Assistant"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can automate updates for installed extensions (add-ons, integrations, or custom components) in **Home Assistant** using either built-in features or community-developed options. Here are a few methods to achieve automatic updates:

### 1. **HACS (Home Assistant Community Store) Automation**
   If you're using HACS for managing custom components, integrations, or frontend themes, you can create an automation to check for updates and install them automatically.

   - **Create an Automation**: Use Home Assistant's automation feature to periodically check for updates and notify you or apply the updates directly.
   
   Example Automation:
   ```yaml
   automation:
     - alias: "Update HACS components"
       trigger:
         - platform: time
           at: "03:00:00"  # Time to run the automation
       action:
         - service: hacs.upgrade
   ```

   This automation can be scheduled to run daily or at any preferred interval. It will update all available HACS extensions automatically.

   **Note**: To use the `hacs.upgrade` service, ensure you have the HACS extension properly installed and configured.

### 2. **Using Supervisor for Official Add-ons**
   If you are using official Home Assistant add-ons managed through the **Supervisor** (for Home Assistant OS or Supervised installations), you can configure updates via automation. Add-ons can be updated using the `hassio.addon_update` service in Home Assistant.

   Example Automation:
   ```yaml
   automation:
     - alias: "Auto-update Add-ons"
       trigger:
         - platform: time
           at: "04:00:00"  # Time to check for updates
       action:
         - service: hassio.addon_update
           data:
             addon: "core_ssh"  # Replace with the add-on you want to auto-update
   ```

   You can create a similar automation for each add-on you want to keep updated automatically. Alternatively, you could create a script to update all add-ons.

### 3. **Update Notifications with `hassio.addon_update`**
   Instead of fully automating updates, you can set up a notification system that alerts you when updates are available for specific add-ons or integrations, allowing you to manually approve updates.
   
   Example Automation for Notification:
   ```yaml
   automation:
     - alias: "Notify Addon Updates"
       trigger:
         - platform: state
           entity_id: sensor.hassio_updates  # Tracks available updates
           to: 'on'
       action:
         - service: notify.notify
           data:
             message: "Updates available for Home Assistant add-ons."
   ```

### 4. **Custom Scripts for Periodic Updates**
   You can create a custom script or use a tool like **Cron** to run at intervals and automatically apply updates to Home Assistant components. This approach is more advanced and requires some custom coding.

### Conclusion:
You can automate updates for Home Assistant extensions via HACS or the Supervisor using built-in services like `hacs.upgrade` and `hassio.addon_update`. You can also set up notification automations to be alerted when updates are available. These methods allow you to keep your system and components updated without manual intervention.