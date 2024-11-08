---
title: "Controlling smart TV from HA and Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You asked about integrating your **LibreELEC** TV with **Home Assistant**, remotely controlling it from your **Fedora** desktop, and probing its hardware.

### 1. **Home Assistant Integration**
You can integrate your **LibreELEC** (Kodi-based) TV with **Home Assistant** to control it, including kiosk mode for displays. Here's how:

- **Install Kodi Add-on in Home Assistant**: Home Assistant has a native integration for **Kodi** (which LibreELEC runs). You can add the integration by going to **Settings > Devices & Services** and searching for **Kodi**.
- **Enable Web Interface in LibreELEC**: On your TV, go to **Settings > Services** in Kodi, enable the **Web Server**, and note the IP address and port. You will need this information to link with Home Assistant.
- **Set up the integration**: Enter the IP (in your case 192.168.1.6) and port in Home Assistant, and you should now be able to control the TV remotely.
- **Kiosk Mode**: To turn it into a kiosk, you can use **Kodi's** native fullscreen settings and manage what is displayed using Home Assistant automations. For instance, you could rotate dashboards or use it for static displays (e.g., security camera feeds, news dashboards).

### 2. **Remote Control from Fedora Desktop**
You can control your **LibreELEC** smart TV directly from your Fedora desktop with the following methods:

- **SSH Access**: LibreELEC allows SSH access, which is enabled by default. You can use it for administrative control and some command-line Kodi operations. From Fedora, you can SSH into the device using:
  ```
  ssh root@192.168.1.6
  ```
  Default password is `libreelec` unless changed.

- **Kodi Remote Control Tools**:
  - You can install **Kodi Remote** or other tools like **Yatse** on Fedora for direct control.
  - Use **VNC** if you prefer GUI-based control (though VNC is not natively supported by LibreELEC and might need configuration).

### 3. **Probing the Hardware**
To probe the hardware on your **LibreELEC** TV, you can use **SSH** to get access to the system and run various Linux commands:

- **Check CPU, Memory, and Storage**:
  ```
  cat /proc/cpuinfo
  cat /proc/meminfo
  df -h
  ```
- **Check connected peripherals (HDMI, USB)**:
  ```
  dmesg | grep hdmi
  lsusb
  ```
- **Check network interfaces**:
  ```
  ifconfig
  ```
- **View full system information**:
  ```
  uname -a
  ```
  If you're comfortable, you could also install **lshw** (a hardware lister) or use other lightweight monitoring tools via SSH.

Let me know if you need help setting up these features or further probing hardware details!