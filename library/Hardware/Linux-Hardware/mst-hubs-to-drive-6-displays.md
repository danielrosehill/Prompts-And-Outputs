---
title: "MST hubs to drive 6 displays"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here is my GPU:
AMD Radeon RX 7700 XT PULSE GAMING 12GB

My OS is Fedora Workstation 40

Please suggest some MST hubs that I could use in order to increase the amount of displays I could drive 

I current have 3 displays connected to my computer and I would like to increase that to 6

# Output

Based on your AMD Radeon RX 7700 XT PULSE GAMING 12GB GPU and Fedora Workstation 40 OS, here are some MST hub recommendations to increase your display count from 3 to 6:

## **SIIG DisplayPort 1.4 to DisplayPort MST Hub**

https://www.amazon.com/SIIG-Port-DisplayPort-1-4-MST/dp/B08ZRVQ1WT

(Can be shipped!)

This hub is a good option for your setup:

- Model: CE-DP0R11-S1
- Features:
  - 4 DisplayPort outputs
  - Supports up to 4K@30Hz on all ports
  - Compatible with DisplayPort 1.4 GPUs (which your RX 7700 XT supports)
  - Works with Linux systems
- Price: Approximately $88.88[1]

This hub would allow you to add 3 more displays to your current setup, bringing your total to 6.

## Configuration for 6 Displays

To achieve 6 displays with this hub:

1. Keep your 3 currently connected displays as they are.
2. Connect the SIIG MST hub to one of your GPU's free DisplayPort outputs.
3. Connect 3 additional monitors to the MST hub.

## Important Considerations

1. **Linux Compatibility**: The SIIG hub is compatible with Linux systems, including Fedora Workstation 40.

2. **Power Requirements**: The hub requires USB bus power from a USB 3.0 port. Your Fedora system should have USB 3.0 ports available[1].

3. **Bandwidth Limitations**: When using MST hubs, the total bandwidth is shared among the connected displays. Your RX 7700 XT supports DisplayPort 1.4, which provides ample bandwidth, but you may need to adjust resolutions or refresh rates for optimal performance across all 6 displays.

4. **GPU Support**: Your AMD Radeon RX 7700 XT supports MST technology, which is crucial for this setup to work.

5. **Fedora Configuration**: You may need to configure your display settings in Fedora to recognize and properly arrange the additional monitors. This can typically be done through the system settings or using command-line tools like xrandr.

By using this MST hub with your existing setup, you should be able to achieve your goal of driving 6 displays from your AMD Radeon RX 7700 XT on Fedora Workstation 40. Remember to ensure your GPU drivers are up to date for the best compatibility and performance.

# Input
 Please recommend some additional options. I might wish to connect the additional screens via HDMI if that were possible (from the hub)
# Output

Based on your request for additional options, including the possibility of connecting screens via HDMI from the hub, here are some recommendations that could work with your AMD Radeon RX 7700 XT and Fedora Linux setup:

## StarTech.com Triple Monitor DisplayPort MST Hub

This hub offers a mix of DisplayPort and HDMI outputs:

- Features:
  - 1x DisplayPort and 2x HDMI outputs
  - Supports up to 4K@30Hz on each port
  - Compatible with DisplayPort 1.2 and higher
  - Linux compatible
- Price: Approximately $130-$150

This hub would allow you to add 3 more displays, with the flexibility of using HDMI for two of them.

## Club3D MST Hub DisplayPort 1.2 to HDMI 2.0 Dual Monitor

For a purely HDMI solution:

- Features:
  - 2x HDMI 2.0 outputs
  - Supports up to 4K@60Hz on each port
  - Compatible with DisplayPort 1.2 and higher
  - Works with Linux systems
- Price: Around $80-$100

You could use two of these hubs to add 4 HDMI displays to your setup.

## Configuration for 6 Displays

To achieve 6 displays with HDMI options:

1. Keep your 3 currently connected displays.
2. Use one of your GPU's free DisplayPort outputs to connect the StarTech.com Triple Monitor MST Hub.
3. This would add 2 HDMI and 1 DisplayPort connection, bringing your total to 6 displays.

Alternatively:
1. Keep your 3 current displays.
2. Use two of your GPU's free outputs to connect two Club3D Dual Monitor HDMI hubs.
3. This would add 4 HDMI connections, bringing your total to 7 displays.

## Important Considerations

1. **Linux Compatibility**: Both recommended hubs should work with Fedora Linux, but always check the latest user reviews for any potential issues.

2. **Bandwidth Limitations**: When using MST hubs, especially with mixed outputs (DP and HDMI), be aware of potential bandwidth limitations. You might need to adjust resolutions or refresh rates for optimal performance.

3. **HDMI Version**: The HDMI outputs on these hubs support different versions (1.4 or 2.0). Ensure they meet your resolution and refresh rate needs.

4. **Power Requirements**: These hubs typically require USB power. Ensure you have available USB 3.0 ports on your system.

5. **Fedora Configuration**: You may need to use xrandr or other display configuration tools in Fedora to properly set up and arrange the additional monitors.

These options provide flexibility in terms of connection types and should work well with your AMD Radeon RX 7700 XT on Fedora Linux. Remember to check for the latest firmware updates for your GPU and keep your system up to date for the best compatibility and performance.

 