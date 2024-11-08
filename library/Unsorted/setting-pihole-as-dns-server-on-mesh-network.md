---
title: "Setting PiHole as DNS server on mesh network"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can absolutely set **Pi-hole** as the **DNS server** on your **TP-Link Deco mesh network** if your **ISP router** does not allow you to set a custom DNS server. By configuring Pi-hole on the Deco system, all devices connected to the Deco mesh will use **Pi-hole** for **DNS resolution** and benefit from ad blocking and filtering. Here’s how to set it up:

### **Why Configure Pi-hole on the TP-Link Deco Mesh Instead of the ISP Router?**
- **Deco Mesh as Primary Network**: The Deco mesh likely handles all your devices' connections and acts as the main **gateway** for those devices. Configuring Pi-hole as the DNS server in the Deco system will ensure that all connected devices automatically use Pi-hole.
- **Override ISP Router Limitations**: If your **ISP router** doesn’t allow changing DNS settings, configuring the Deco mesh lets you work around this limitation effectively.

### **Steps to Set Pi-hole as DNS Server on TP-Link Deco**
1. **Open the TP-Link Deco App**:
   - The **Deco system** is controlled via the **TP-Link Deco mobile app** (available for Android and iOS).

2. **Access Network Settings**:
   - **Open the Deco app** and ensure that you are logged in to your Deco account.
   - **Select your network** to open the main screen for your mesh network.

3. **Navigate to Advanced Settings**:
   - Tap on the **“More”** tab at the bottom of the screen.
   - Go to **“Advanced”** settings.
   - Look for the **“IPv4”** section or **“DHCP Server”** settings. (This section might have different names depending on your Deco model and app version.)

4. **Configure DNS Settings**:
   - Scroll down until you find the **“DNS Server”** setting.
   - **Select Manual** instead of the automatic/default settings.
   - Set the **Primary DNS** to the **local IP address of your Pi-hole**. For example:
     - **Primary DNS**: **`192.168.1.30`** (or whatever IP your Pi-hole uses).
   - For the **Secondary DNS**, you can:
     - **Leave it blank** to force all DNS queries through Pi-hole.
     - **Use a public DNS server** (e.g., **`1.1.1.1`** or **`8.8.8.8`**) to provide a fallback if Pi-hole becomes unavailable.

5. **Save and Apply Settings**:
   - Save the settings, and your Deco system will apply these changes to all devices connected to the network.
   - The **Deco mesh system** will now tell all devices to use Pi-hole for DNS resolution.

6. **Restart Devices (Optional)**:
   - To ensure that all devices use the new DNS settings immediately, you may need to **restart** or **reconnect** each device on your network.
   - Devices should now automatically receive the **Pi-hole IP address** as their **DNS server** from the Deco system.

### **Considerations**
- **Avoiding Double NAT**: If your ISP router is still acting as a **router** and assigning IP addresses (instead of being in **bridge mode**), you might be running a **Double NAT** setup. This isn’t usually a big issue for Pi-hole but can add some network complexity. If possible, consider putting your ISP router into **bridge mode**, allowing Deco to handle all routing and DHCP.
- **Secondary DNS**: Be mindful that if you add a **Secondary DNS server** (like **Google or Cloudflare**), devices may bypass Pi-hole at times if they choose to use the secondary server. If you want to ensure **all DNS requests go through Pi-hole**, leave the **secondary DNS** blank.

### **Testing the Setup**
To ensure Pi-hole is working correctly as the DNS server:

1. **Pi-hole Admin Console** (`http://<pi-hole-ip>/admin`):
   - Go to the **“Query Log”** page in the Pi-hole Admin interface.
   - You should see **DNS requests** coming from the devices on your network. If you see requests from multiple IP addresses on your network, this indicates that devices are using Pi-hole as intended.

2. **Test Blocking**:
   - Open a web browser on any device connected to the Deco mesh and visit a site known to have ads.
   - If Pi-hole is working properly, ads should be **blocked**.

### **Advanced Setup (Optional) - DHCP via Pi-hole**
If you want to **force all devices** on your network to use **Pi-hole** without worrying about a **secondary DNS bypass**:
- **Disable DHCP on the Deco**: Disable the **DHCP server** on the Deco mesh system.
- **Enable DHCP on Pi-hole**: Enable the **DHCP server** in the Pi-hole settings (`Settings > DHCP`).
- This way, **Pi-hole** assigns IP addresses and informs all devices on the network to use **itself as the DNS server**, ensuring no DNS requests bypass Pi-hole.

### **Summary**
- You can **easily configure Pi-hole as the DNS server** in the **TP-Link Deco** mesh network settings to handle all DNS requests.
- Use the **Deco app** to set Pi-hole’s IP (`192.168.1.30`) as the **primary DNS**.
- Optionally set a **secondary DNS** for redundancy or leave it blank to force all traffic through Pi-hole.
- **Restart devices** to ensure they adopt the new settings.
- For **maximum control**, consider running DHCP through Pi-hole and disabling DHCP on the Deco mesh.

This setup should ensure that your entire network benefits from **ad-blocking**, **tracking prevention**, and **privacy enhancements** offered by Pi-hole while maintaining reliable DNS resolution. Let me know if you need any further assistance!