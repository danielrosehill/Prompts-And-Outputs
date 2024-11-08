---
title: "Integrating new display tablet in Home Assistant"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


How do I integrate the tablet into HA?

# Output


To integrate your **Android tablet** running **Fully Kiosk Browser** into **Home Assistant (HA)**, follow these steps. This integration will allow you to manage the tablet remotely from Home Assistant, including controlling the display, managing media, or even using it as a notification device.

### **Step 1: Set Up Fully Kiosk Browser on the Tablet**
1. **Install Fully Kiosk Browser**:
   - Download **Fully Kiosk Browser** from the **Google Play Store** and install it on your tablet.

2. **Enable Remote Administration**:
   - Open **Fully Kiosk Browser** and go to **Settings**.
   - Navigate to **Remote Administration (PLUS)** and enable it. Note down the **IP address** of the tablet as well as the **port number** (default is `2323`).
   - Set an **Admin Password** for secure access.

3. **Enable Remote Debugging and Device Info Access**:
   - Under **Settings > Device Management**, enable **Remote Debugging** and **Access Device Info**.

### **Step 2: Configure Home Assistant**
1. **Add Fully Kiosk Integration to Home Assistant**:
   - In your **Home Assistant** dashboard, navigate to **Configuration** > **Devices & Services**.
   - Click on **+ Add Integration** and search for "**Fully Kiosk Browser**".
   - If there is no official integration available directly in Home Assistant, you can add the integration manually via **configuration.yaml**.

2. **Use HACS for Integration (Optional but Recommended)**:
   - **HACS (Home Assistant Community Store)** allows you to install community integrations easily.
   - Install **HACS** in Home Assistant if you haven't already.
   - In **HACS**, search for "**Fully Kiosk Browser Integration**" and install it.
   - This integration will let you control the tablet via Home Assistant, such as turning the screen on/off, sending notifications, and more.

### **Step 3: Configure the Integration in `configuration.yaml`**
1. **Edit `configuration.yaml`**:
   - Add the following configuration to your `configuration.yaml` file:

   ```yaml
   fully_kiosk:
     - host: 192.168.1.XXX  # Replace with the IP address of your tablet
       port: 2323           # Default port used by Fully Kiosk
       password: YOUR_ADMIN_PASSWORD  # Admin password set in Fully Kiosk
       name: 'Tablet Display'         # Optional, name of the device
   ```

2. **Restart Home Assistant**:
   - After editing the configuration file, restart **Home Assistant** to apply the changes.

### **Step 4: Test the Integration**
- Once Home Assistant has restarted, go to your **Devices** section, and you should see the newly added **tablet device** under **Fully Kiosk**.
- You can now use Home Assistant to:
  - **Turn the display on/off**.
  - **Control brightness**.
  - **Display web pages or images**.
  - **Send text-to-speech messages** to the tablet.

### **Step 5: Create Automations in Home Assistant**
1. **Turn Display On/Off**:
   - Use Home Assistant's **Automation Editor** to create an automation.
   - For example, set the display to turn **off** every night at 11 PM and **on** every morning at 7 AM.

   ```yaml
   alias: Turn Tablet Display Off at Night
   trigger:
     platform: time
     at: '23:00:00'
   action:
     service: fully_kiosk.screen_off
     data:
       entity_id: fully_kiosk.tablet_display
   ```

2. **Custom Notifications**:
   - Use the **notification service** in Fully Kiosk to display messages or trigger alerts on the tablet from Home Assistant.**n**

### **Step 6: Use Fully Kiosk Services in Home Assistant**
- With the integration complete, you will be able to use several services in Home Assistant for **Fully Kiosk**:
  - **`fully_kiosk.load_url`**: Load a specific URL on the tablet.
  - **`fully_kiosk.screen_on` / `fully_kiosk.screen_off`**: Control the screen power state.
  - **`fully_kiosk.start_application`**: Start a specific application.

### **Summary**
- **Install Fully Kiosk Browser** on the tablet.
- **Enable Remote Administration** on Fully Kiosk.
- Use **HACS** to install the **Fully Kiosk Browser Integration** or manually configure it in **`configuration.yaml`**.
- Restart **Home Assistant** and configure automations to control the display centrally.

This setup will allow you to manage the **tablet's display schedule** without interacting directly with the low-powered device, leveraging the full power of Home Assistant to automate and control it effectively.