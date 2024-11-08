---
title: "Why Google DNS causes problems resovling hostnames"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


If your router's DNS settings are configured to use Google's public DNS servers (`8.8.4.4` and `8.8.8.8`), that means all DNS requests from devices on your LAN are being routed externally to Google. This is likely causing issues when your devices on the LAN try to access your **Home Assistant** instance via the **Cloudflare Tunnel** since these DNS servers will resolve your domain to the external IP associated with the Cloudflare Tunnel, which might not work properly for devices inside your network.

To resolve the issue, you need to set up a **local DNS resolution** so that devices on your LAN can access Home Assistant using its **local IP** instead of going through the Cloudflare Tunnel when accessed from within the LAN. Here are some methods you can use:

### **Option 1: Set Up Local DNS on Your Router**
If your router supports **custom DNS entries** or **DNS override** features, you can set up a custom DNS rule for your Home Assistant domain (`ha.testhomewebsite.com`) to resolve to its local IP (`192.168.1.3`).

1. **Access Your Router's Settings**:
   - Open a web browser and enter your router’s IP address (usually something like `192.168.1.1` or `192.168.0.1`).
   - Log in to the router's admin panel.

2. **Navigate to DNS Settings**:
   - Look for the **DNS** settings or **LAN** settings where you can define custom entries.
   - Some routers have an option like **Static DNS** or **Local DNS Mapping**.

3. **Add a Custom DNS Entry**:
   - Add an entry for the domain you use for Home Assistant, e.g., `ha.testhomewebsite.com`.
   - Set the value to the **local IP address** of your Home Assistant instance (e.g., `192.168.1.3`).

4. **Save and Apply Changes**:
   - Save the changes and reboot the router if required.
   - This ensures that when devices on the LAN request `ha.testhomewebsite.com`, they will be directed to `192.168.1.3` instead of routing through Cloudflare.

### **Option 2: Use Pi-hole or a Local DNS Server**
If your router does not allow custom DNS entries, you could use **Pi-hole** or another **local DNS server** (like **DNSMasq**) to handle local DNS resolution.

1. **Set Up Pi-hole**:
   - Pi-hole is a network-wide ad blocker that also works as a **local DNS server**.
   - You can install Pi-hole on a **Raspberry Pi** or any Linux system.
   - During setup, you can add a custom DNS entry for `ha.testhomewebsite.com` to point to `192.168.1.3`.

2. **Set Your Router to Use Pi-hole**:
   - Configure your router to use the Pi-hole IP as the **primary DNS** server. This ensures that all devices on the LAN use Pi-hole for DNS, and Pi-hole will resolve `ha.testhomewebsite.com` to the local IP.

3. **Add Custom DNS Entry in Pi-hole**:
   - Open Pi-hole's web interface.
   - Go to **Local DNS** > **DNS Records**.
   - Add `ha.testhomewebsite.com` with the IP `192.168.1.3`.

### **Option 3: Edit the Hosts File on Each Device**
If you only have a few devices that need to access Home Assistant and don’t want to set up a DNS server, you can manually edit the **hosts file** on each device. This method is quick but not scalable if there are many devices.

#### **Windows:**
1. **Open Notepad as Administrator**:
   - Search for **Notepad**, right-click, and select **Run as administrator**.

2. **Open the Hosts File**:
   - In Notepad, open the hosts file located at:
     ```
     C:\Windows\System32\drivers\etc\hosts
     ```
3. **Add an Entry for Home Assistant**:
   - Add the following line at the end of the file:
     ```
     192.168.1.3 ha.testhomewebsite.com
     ```
4. **Save the File**.

#### **Linux/macOS:**
1. **Open Terminal** and edit the hosts file:
   ```bash
   sudo nano /etc/hosts
   ```
2. **Add the Entry**:
   ```bash
   192.168.1.3 ha.testhomewebsite.com
   ```
3. **Save** by pressing `CTRL+O`, then **Exit** with `CTRL+X`.

### **Option 4: Update Router DNS to Point to Internal DNS Server**
Another solution is to change the DNS setting in your router from Google's (`8.8.8.8` and `8.8.4.4`) to a local DNS server that you control (such as **Pi-hole** or **a DNS server on your network** that supports split DNS).

- Set the primary DNS server on your router to the IP of your **local DNS server**.
- If the local DNS server doesn’t know how to resolve a domain, it can forward the request to Google’s DNS or any other external DNS server.

### **Why This Problem Occurs (Technical Background)**
- **Cloudflare Tunnels** expose your service to the internet securely, which works great for external access. However, internally, when a DNS request is made to the external hostname (e.g., `ha.testhomewebsite.com`), it is sent through the tunnel, which might not be optimized or even available for local network access.
- Setting up **split DNS** allows local devices to resolve internal services directly to local IP addresses rather than through the internet, which avoids unnecessary latency, potential DNS issues, and connectivity restrictions.

### **Summary**
- **Update DNS** on your **router** or use a **local DNS server** like **Pi-hole** to point `ha.testhomewebsite.com` to the local IP address (`192.168.1.3`) for internal devices.
- **Edit Hosts File** on devices to force local resolution (quick but not scalable).
- Consider setting up **split DNS** to ensure local requests to the domain resolve to the local IP, while external requests use the Cloudflare Tunnel.

Choose the solution that works best for your setup, and let me know if you need more detailed steps on any particular method!