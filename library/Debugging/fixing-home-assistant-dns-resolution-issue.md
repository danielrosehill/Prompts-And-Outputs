---
title: "Fixing Home Assistant DNS resolution issue"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


If you can access your **Home Assistant** instance via a **Cloudflare Tunnel** from your desktop but not from other devices on your LAN, there are a few possible reasons related to network configuration, DNS resolution, and device-specific firewall settings. Let’s go through some of the most common causes and how you can troubleshoot and fix them.

### **1. Split DNS or DNS Resolution Issues**
The most likely reason for not being able to access the instance from devices on your **local network** is an issue with DNS resolution. This happens because devices on the LAN try to resolve the domain name of the tunnel differently from devices outside.

- **Check DNS Resolution**: When a request is made using the domain name that points to the Cloudflare Tunnel, devices on the LAN might not resolve it correctly, especially if your network's DNS server or router handles DNS differently.

#### **Solution: Local DNS Configuration (Split DNS)**
To resolve this issue, you can set up a **split DNS** configuration:
- **Router DNS Override**: Set up a custom DNS rule on your **router** to resolve the Home Assistant hostname (`ha.testhomewebsite.com`, for example) to the **local IP address** of the Home Assistant instance (e.g., `192.168.1.3`).
- **Local DNS Server**: If you have a local DNS server (e.g., **Pi-hole** or a **DNSMasq** setup), you can add a custom entry so that any queries from the LAN for `ha.testhomewebsite.com` are directed to the local IP.
  
This ensures that any request originating from within the LAN uses the direct internal IP instead of trying to route through the Cloudflare Tunnel, which could lead to connectivity issues.

### **2. NAT Loopback (Hairpin NAT) Issue**
Some **routers** do not support **NAT Loopback** (also known as **Hairpin NAT**). NAT Loopback allows devices inside your LAN to use the external domain name (`ha.testhomewebsite.com`) and get correctly routed to the internal IP address.

- **Check Router Compatibility**: Ensure that your router supports NAT Loopback. If it doesn't, you will either need to:
  - Replace the router with one that does.
  - Use the **split DNS** solution mentioned above.

### **3. Firewall Rules and Network Segmentation**
It's possible that a **firewall rule** or **network segmentation** is preventing devices on the LAN from reaching the Home Assistant instance.

- **Firewall Settings**: Make sure that the firewall on your Home Assistant device allows connections from all internal IP addresses in your LAN.
- **VLANs**: If your network is segmented using **VLANs**, make sure that there are **inter-VLAN routing rules** that allow devices in different VLANs to communicate. VLAN segmentation can sometimes isolate devices, making it hard for them to communicate directly.

### **4. Host File Override on Devices**
You can manually edit the **hosts file** on the other devices (not ideal for a large number of devices but works as a quick test) to force them to resolve the domain to the local IP address.

- **On Windows**:
  - Open **Notepad as Administrator**.
  - Edit the file located at: `C:\Windows\System32\drivers\etc\hosts`.
  - Add the following line:
    ```
    192.168.1.3 ha.testhomewebsite.com
    ```
- **On Linux/macOS**:
  - Open a terminal and edit the `/etc/hosts` file using a text editor like **nano**:
    ```bash
    sudo nano /etc/hosts
    ```
  - Add the line:
    ```
    192.168.1.3 ha.testhomewebsite.com
    ```
  
This makes sure that requests from the local device are directed straight to the local IP.

### **5. Cloudflare Tunnel Configuration**
Ensure that the **Cloudflare Tunnel** configuration is correct and doesn't restrict local traffic. Sometimes, settings in **Cloudflare Access** might restrict who or from where the resources can be accessed.

- **Check Cloudflare Access Policies**: If you have defined policies for who can access your site via **Cloudflare Zero Trust** or **Access**, ensure that the policies aren’t inadvertently blocking devices from within your LAN.
- **Local IP Bypass**: In some cases, it may be beneficial to configure local IP addresses to **bypass** Cloudflare entirely for certain services.

### **6. Browser Cache and SSL Certificates**
If the domain was used earlier without proper SSL or in a different configuration, devices on the LAN may have cached incorrect SSL certificates or data.

- **Clear Browser Cache**: Clear the browser cache and cookies related to the Home Assistant domain on the affected devices.
- **SSL Certificates**: If there are SSL-related issues, make sure your devices trust the **Cloudflare SSL certificate** being used for the tunnel.

### **Summary of Solutions**
1. **Split DNS**: Configure a split DNS on your router or DNS server to resolve `ha.testhomewebsite.com` to the **local IP** when accessed from within the LAN.
2. **NAT Loopback**: Ensure your router supports **NAT Loopback**, or implement a workaround using a local DNS rule.
3. **Firewall/VLANs**: Check the firewall settings on Home Assistant and ensure there’s no **network segmentation** preventing access.
4. **Hosts File Override**: Manually edit the **hosts** file on devices to force them to connect to the **local IP**.
5. **Cloudflare Tunnel Settings**: Verify that your Cloudflare Access settings are not restricting local device access.
6. **Clear Cache**: Clear the **browser cache** or reset any cached SSL data that may be causing issues.

Try these solutions and see if one resolves your connectivity issue. If you need more detailed guidance on any of these steps, feel free to ask!