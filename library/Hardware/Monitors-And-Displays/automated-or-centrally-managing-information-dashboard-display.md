---
title: "Automated or centrally managing information dashboard display"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I have an Android tablet on my network which I purchased to run displays in kiosk mode.
Is there any way to centrally manage an on/off display schedule? I don't want to have to do this on the device itself as it's quite low powered
Free tools only

# Output

For centrally managing the **on/off display schedule** of your **low-powered Android tablet** in kiosk mode using only **free tools**, here are some solutions that can help you achieve this without manually configuring the device:

### **1. Fully Kiosk Browser (Free Version) + Remote Access**
**Fully Kiosk Browser** is an excellent app for managing Android devices in kiosk mode, and it offers a free version that supports many useful features, including remote management capabilities.

- **How It Works**:
  - Install the **Fully Kiosk Browser** on your tablet.
  - Enable the **Remote Admin feature** (requires setting up the local network interface, which is available in the free version).
  - Once configured, you can access the tablet remotely through any browser by visiting the tablet's IP address and controlling settings such as **display on/off**.

- **Remote Admin Access**:
  - Allows you to send commands to **turn the screen on/off**, manage brightness, and schedule screen wake/sleep.
  - This solution is easy to set up and doesn’t require any high processing power from the device.

**Steps**:
1. Install **Fully Kiosk Browser** on the tablet.
2. Enable **Remote Admin** (Settings > Remote Administration).
3. Access the Remote Admin UI from another device on your network to manage display schedules.

### **2. Home Assistant with Fully Kiosk Integration**
If you have **Home Assistant** running on your home server, you can use it to centrally control the tablet's display through **Fully Kiosk** integration.

- **Fully Kiosk + Home Assistant Integration**:
  - Use **Home Assistant** to send commands to the **Fully Kiosk Browser** installed on your tablet.
  - Set up automation rules in Home Assistant to **turn the display on/off** at specific times.
  
- **How to Set Up**:
  1. Install **Fully Kiosk Browser** on the tablet and configure the REST API.
  2. Integrate **Home Assistant** with **Fully Kiosk Browser** using the tablet's IP address and API key.
  3. Create an automation in **Home Assistant** that sends commands to the tablet at specific times.

This approach allows for **full automation** of the display schedule and central control, with no need to manage settings directly on the tablet.

### **3. Automate Using Termux and Crontab**
Another free solution is to use **Termux** and **crontab** for scheduled actions.

- **Termux** is a terminal emulator for Android that provides a Linux environment.
- You can use **ADB commands** within Termux to control the tablet’s power and display state, combined with **crontab** for scheduling.

**Steps**:
1. Install **Termux** on the tablet.
2. Install **crontab** in Termux to create schedules.
3. Use **ADB commands** to control the display (e.g., turn the display off at a scheduled time).

Example of an ADB command in Termux:
```bash
termux-schedule -c "adb shell input keyevent 26"
```
You can use this setup to toggle the screen on/off on a schedule.

### **4. Automate Using MQTT Broker and Tasker (Free Tools)**
If you’re familiar with **MQTT** and **Tasker**, you can set up an MQTT broker on your home server and use Tasker on the Android tablet.

- **Tasker** can listen for commands from the **MQTT broker**, and you can use it to turn the display on or off.
- This way, you control the schedule by publishing MQTT messages from a central system (like your home server).

**Steps**:
1. Set up an **MQTT broker** (e.g., **Mosquitto**, which is free) on your home server.
2. Install **Tasker** and the **MQTT Tasker Plugin** on your tablet.
3. Configure Tasker to listen for specific commands and act accordingly (e.g., turn off the screen).

### **5. Automate Display Control via Remote ADB Over Network (Free but Involves Some Manual Setup)**
You can use **ADB over the network** to control your tablet remotely, allowing you to turn the screen on/off.

- **Set Up ADB Over WiFi**:
  - Enable **developer options** and allow **ADB over network** on the tablet.
  - From your computer, use **ADB commands** to control the tablet's display.

Command Example:
```bash
adb connect <tablet_ip>
adb shell input keyevent 26  # This command toggles the screen (on/off)
```
- **Automate with Cron**:
  - You could create a **cron job** on a Linux computer or server to run these commands at specific times, effectively managing the display schedule remotely.

### **Summary**:
- **Fully Kiosk Browser + Remote Admin**: Easiest and most reliable for your use case. It allows remote access via browser and lets you schedule display control.
- **Home Assistant Integration**: If you already have Home Assistant, this allows powerful automation for managing the display.
- **Termux with Crontab**: Offers a free command-line approach, but involves a bit more setup.
- **MQTT with Tasker**: Flexible but requires MQTT setup and Tasker configuration.
- **Remote ADB Commands**: Provides direct control but requires some manual configuration.

The **Fully Kiosk Browser** with **Remote Admin** would probably be the simplest and most effective approach to achieve centralized control over the display schedule without overloading your low-powered tablet.