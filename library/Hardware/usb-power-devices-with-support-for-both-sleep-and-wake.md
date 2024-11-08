---
title: "USB power devices with support for both sleep and wake"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you find any compatible USB power management devices that explicitly support both putting the compute to sleep and waking it upt?

# Output

Unfortunately, there doesn't seem to be a widespread availability of USB power buttons that explicitly support both putting a computer to **sleep** and **waking it up** right out of the box. However, there are a few options that come close to what you're looking for, with some custom configuration required for full functionality.

### What is possible:
1. **Waking up from Suspend**: Most USB power buttons, such as the **Eleduino ATX USB Power Button** or **iFixit USB Power Button**, can wake your system from a suspend state as long as USB wake is enabled in the BIOS. This feature is supported by the BIOS and Fedora Linux without additional software once set up correctly【22†source】【23†source】.

2. **Putting the Computer to Sleep**: To use the same button for putting the system to sleep, you'll need to set up custom scripts on Fedora using tools like `evtest` or `udevadm`. You can bind the USB power button press to the `systemctl suspend` command, effectively allowing it to act as a "sleep" button【24†source】.

### Devices you could consider:
- **Eleduino ATX USB Power Button**: This is a USB button primarily used to turn on, restart, or wake up your computer. However, it can be extended with Linux configuration to act as a suspend button.
  
- **Sabrent External USB Power Switch**: Although it’s mainly a USB hub, you can use its power switches to control device power and wake-up features, again requiring software configuration for suspend functionality.

For both solutions, the wake-up function works well once the USB wake feature is enabled in your BIOS, while the sleep function can be configured using custom scripts to listen for a button press and trigger a suspend command.

If you're comfortable with basic Linux terminal commands and configurations, these options should provide what you're looking for. If you'd like help with specific commands or setting up the script, feel free to ask!