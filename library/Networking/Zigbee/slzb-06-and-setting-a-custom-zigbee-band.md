---
title: "SLZB-06 and setting a custom Zigbee band"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The **SLZB-06** is a Zigbee coordinator (often used with Zigbee2MQTT or other similar setups), and yes, it **supports configuring a custom Zigbee channel** for device connectivity.

When using the SLZB-06 in **Zigbee2MQTT** or a similar Zigbee management tool, you can specify which Zigbee channel to use. Here's how you can configure it:

### 1. **Configuring the Zigbee Channel in Zigbee2MQTT**
If you’re using **Zigbee2MQTT** with the SLZB-06, follow these steps:

1. **Locate the Zigbee2MQTT Configuration File**:
   - The configuration file is usually located at `/opt/zigbee2mqtt/data/configuration.yaml` or another relevant directory, depending on your setup.
   
2. **Edit the Configuration File**:
   Open the file and locate the `advanced` section. Add or modify the `channel` field to set a custom channel.
   
   Example:
   ```yaml
   advanced:
     channel: 20  # Set the Zigbee channel here
   ```
   
   Make sure the channel is compatible with your network setup, as discussed earlier.

3. **Restart Zigbee2MQTT**:
   After making the change, restart Zigbee2MQTT for the new settings to take effect.

   ```bash
   sudo systemctl restart zigbee2mqtt
   ```

### 2. **Available Zigbee Channels**
The SLZB-06 should support channels **11 to 26**, with channels like **15**, **20**, or **25** often recommended to avoid interference from 2.4 GHz Wi-Fi.

- Channel 15: Less likely to overlap with Wi-Fi channels.
- Channel 20: Generally a good choice in mixed environments.
- Channel 25: High-end channel that avoids much of the Wi-Fi traffic.

### 3. **Check Current Channel**
You can check which Zigbee channel is currently in use through the Zigbee2MQTT logs or by running:
```bash
cat /opt/zigbee2mqtt/data/state.json | grep channel
```

This should display the active channel for your SLZB-06.

### Summary
The SLZB-06 supports configuring custom Zigbee channels, allowing you to minimize interference with Wi-Fi networks. By adjusting the channel in **Zigbee2MQTT’s configuration file**, you can set your Zigbee network to operate on an optimal band for your environment.

Let me know if you need further help with the configuration!