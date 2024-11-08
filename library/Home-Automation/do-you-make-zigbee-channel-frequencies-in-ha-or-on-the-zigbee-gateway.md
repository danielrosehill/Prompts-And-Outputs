---
title: "Do you make Zigbee channel frequencies in HA or on the Zigbee gateway"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Do I make these changes in Home Assistant or on the SLZB?
I'm using Zigbee2MQTT

# Output

Since you are using **Zigbee2MQTT** with your SLZB-06, you will make the changes **within Home Assistant**, specifically in the **Zigbee2MQTT** configuration file.

Here’s how you can adjust the Zigbee channel:

### Steps to Change the Zigbee Channel in Home Assistant (Zigbee2MQTT):
1. **Access the Zigbee2MQTT Add-on**:
   - In Home Assistant, go to **Settings > Add-ons > Zigbee2MQTT**.

2. **Open the Configuration File**:
   - In the Zigbee2MQTT add-on, navigate to the **Configuration** tab. This will show you the `configuration.yaml` file that Zigbee2MQTT uses.

3. **Set the Zigbee Channel**:
   - Find the `advanced` section in the configuration file (or create it if it doesn’t exist). Add or modify the `channel` setting to your desired channel (e.g., 15, 20, or 25).

   Example configuration:
   ```yaml
   advanced:
     channel: 20  # Set the desired Zigbee channel
   ```

4. **Save the Configuration**:
   - After editing, save the file.

5. **Restart Zigbee2MQTT**:
   - Once the configuration is saved, restart Zigbee2MQTT by going to the **Info** tab in the Zigbee2MQTT add-on and clicking the **restart** button.

After restarting, Zigbee2MQTT will start using the new Zigbee channel, and your devices will automatically reconnect.

### Summary:
- All changes are made **in Home Assistant** under the **Zigbee2MQTT add-on's configuration** file.
- The SLZB-06 itself doesn't need direct configuration.

Let me know if you need further assistance!