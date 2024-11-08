---
title: Avoiding cross-network interference Zigbee and WiFi 2.4 Ghz
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

I have the following networks at home:

- A dedicated 5 Ghz Wifi network for devices that support it
- A dedicated 2.4 Ghz Wif network specifically provisioned for IoT devices that can only work on 2.4 Ghz.
- A Zigbee network for Zigbee MQTT

And I'm thinking about adding:

- A Zigbee ZHA device

Can you provide me some guidance on what I can do to avoid or minimise frequency conflicts?

# Output

To avoid or minimize frequency conflicts between your 2.4 GHz Wi-Fi network, Zigbee network, and the planned addition of Zigbee ZHA devices, you can take a few steps to optimize frequency usage.

### 1. **Understand the Frequency Overlaps**
Both **Wi-Fi 2.4 GHz** and **Zigbee** operate in the 2.4 GHz frequency band, which means they can interfere with each other if not carefully configured. Here's a quick breakdown:
- **Wi-Fi 2.4 GHz** uses channels 1 through 11 (in most regions), with each channel being about 22 MHz wide.
- **Zigbee** operates on channels 11 to 26 in the 2.4 GHz band, with each channel about 2 MHz wide.

### 2. **Choosing Non-Overlapping Channels**
To minimize conflicts, you can choose non-overlapping channels for your Wi-Fi and Zigbee networks. Here’s a basic guide to help:
- **Wi-Fi Channels**: Wi-Fi channels 1, 6, and 11 are non-overlapping and typically the best choices.
- **Zigbee Channels**: Channels 15, 20, and 25 are commonly recommended to avoid Wi-Fi interference.

You can use the following channel separation:
- **Wi-Fi Channel 1**: Avoid using Zigbee channels **11, 12, 13, 14, 15** (consider using **Zigbee 20 or 25**).
- **Wi-Fi Channel 6**: Avoid Zigbee channels **16, 17, 18, 19, 20** (consider **Zigbee 15 or 25**).
- **Wi-Fi Channel 11**: Avoid Zigbee channels **21, 22, 23, 24, 25** (consider **Zigbee 15 or 20**).

### 3. **Suggestions for Your Setup**
- **5 GHz Wi-Fi**: No conflict with Zigbee since it operates on a different band. You can use this network for high-speed, latency-sensitive devices.
  
- **2.4 GHz Wi-Fi**: Since this is dedicated to your IoT devices, choose a channel with minimal interference. For example:
  - Set your **Wi-Fi 2.4 GHz** on **channel 1**.
  - Set your **Zigbee MQTT** network on **channel 20**.
  - When adding your **Zigbee ZHA device**, make sure it uses a channel like **15 or 25**.

### 4. **Monitor for Interference**
Once the networks are set up, you should:
- **Check for interference**: Use tools like `Wi-Fi Analyzer` (available on Android or desktop) to check for Wi-Fi congestion and Zigbee-specific tools (like **Zigbee2MQTT** logs) to monitor Zigbee network stability.
- **Adjust if necessary**: If you experience interference, consider tweaking the channels based on real-world performance.

### 5. **Additional Tips**
- **Reduce Signal Strength**: If your Wi-Fi 2.4 GHz network has a high signal strength, it might bleed over and interfere with Zigbee. You can try reducing the signal strength on your router for 2.4 GHz, especially if it's only serving nearby IoT devices.
- **Antenna Positioning**: Separate your Wi-Fi router and Zigbee coordinator physically if possible. This can help reduce interference due to signal overlap.

### Summary of Recommended Settings:
- **Wi-Fi 5 GHz**: No conflict with Zigbee; use freely.
- **Wi-Fi 2.4 GHz**: Set to **channel 1**.
- **Zigbee MQTT**: Set to **channel 20**.
- **Zigbee ZHA**: Set to **channel 15** (or channel 25 as an alternative).

By carefully selecting your channels and reducing overlap, you should be able to avoid frequency conflicts and have a smooth-running network.

Let me know if you need further guidance!

