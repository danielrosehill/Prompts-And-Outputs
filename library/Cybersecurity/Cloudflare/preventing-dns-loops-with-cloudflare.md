---
title: "Preventing DNS loops with Cloudflare"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To **prevent DNS loops** when using **Cloudflare Zero Trust Access** (often called **Cloudflare Access**) to manage remote access to local services, and specifically when accessing those services over the LAN via their **Cloudflare endpoints**, you can configure several settings. The goal is to ensure that local DNS queries do not get inadvertently routed back through the **Cloudflare Tunnel**, creating a **DNS loop**. Here are some steps and configurations you can adjust to mitigate these issues:

### **Key Steps to Avoid DNS Loops with Cloudflare Access on LAN**

#### **1. Set Up Split-Horizon DNS**
**Split-Horizon DNS** (or **Split DNS**) is one of the most effective ways to prevent DNS loops. The idea is to have different DNS responses based on whether the request is coming from inside your network (LAN) or from outside (through Cloudflare).

- **Internal DNS Resolution**:
  - Set up a local DNS resolver (such as **Pi-hole**, **Unbound**, or your router’s DNS server) to respond with the **local IP address** for services such as **Home Assistant** (`192.168.1.3`).
  - For example, when accessing `ha.testhomewebsite.com` from the LAN, the local DNS server should return the internal IP (`192.168.1.3`), allowing traffic to stay on the local network.

- **External DNS Resolution via Cloudflare**:
  - For requests coming from outside the LAN, **Cloudflare DNS** (or another public DNS) can return the **Cloudflare Tunnel address**.
  - This setup helps avoid local DNS queries going through the Cloudflare Tunnel, preventing a DNS loop.

To achieve this, you'll need to:
- **Create Internal DNS Overrides**: On **Pi-hole** or your internal DNS server, add a DNS entry for `ha.testhomewebsite.com` pointing to `192.168.1.3`.
- **Use Conditional Forwarding**: Configure your DNS server to forward queries based on their origin to either the **internal DNS resolver** or **Cloudflare**.

#### **2. Use Local Bypass (Split Tunnel) Configuration**
By default, **Cloudflare Tunnel** sends all traffic through Cloudflare, including traffic from your **local LAN**. You can configure **Cloudflare WARP client** (or other Zero Trust configurations) to **bypass certain traffic** when it’s local to avoid looping back through the tunnel.

- **Create Split Tunnel Rules**:
  - Log in to the **Cloudflare Zero Trust Dashboard**.
  - Go to **Settings** > **Network** > **Split Tunnels**.
  - Add a rule to **exclude** your **local IP range** from being sent through the **Cloudflare Tunnel**.
  - For example, exclude the **192.168.1.0/24** subnet. This will allow devices on your LAN to communicate directly rather than sending those requests to **Cloudflare**, which prevents loops for internal traffic.

#### **3. Modify DNS Policies in Cloudflare Access**
**Cloudflare Access** allows you to configure **DNS policies** that can affect how DNS resolution happens for Zero Trust-connected devices. By creating smart DNS policies, you can direct requests appropriately:

- **Internal vs. External Resolution**:
  - **Go to**: **Cloudflare Zero Trust Dashboard** > **Gateway** > **DNS Policies**.
  - Create a **DNS policy** that directs DNS queries for internal domain names (e.g., `ha.testhomewebsite.com`) to an internal resolver (such as **Pi-hole**) when the request is coming from within your LAN.
  - If the request comes from outside the LAN, let **Cloudflare** handle it. This prevents internal requests from looping through Cloudflare when they could simply be handled locally.

#### **4. Local Hosts File for Devices Using Cloudflare**
If you only have a few devices that are being affected by the **DNS loop** issue, consider editing the **hosts file** on those devices to prevent them from relying on **Cloudflare Tunnel** for local services:

- **Edit Hosts File**:
  - On **Windows**, modify the hosts file at `C:\Windows\System32\drivers\etc\hosts`.
  - On **macOS/Linux**, modify the hosts file at `/etc/hosts`.
  - Add an entry for the internal hostname that points directly to the local IP address:
    ```plaintext
    192.168.1.3   ha.testhomewebsite.com
    ```
  - This will force the device to resolve `ha.testhomewebsite.com` to the **local IP address** (`192.168.1.3`), even if it's also configured to use **Cloudflare Tunnel**.

#### **5. Disable Loopback on Specific DNS Entries**
If certain domain names are causing DNS loops, **Cloudflare Zero Trust** settings can be adjusted to **exclude** those specific names from being resolved through **Cloudflare Tunnel**:

- **Cloudflare Dashboard**:
  - Go to the **DNS settings** for your **Cloudflare domain**.
  - Locate any problematic records that might be looping back to your internal network.
  - Either **remove** these records or configure **local DNS resolution** for these domains.

#### **6. Adjust Access Policies for Internal vs. External Users**
Cloudflare allows you to set up **Access Policies** that specify who can access what, and from where. If you’re accessing **Home Assistant** or other services both internally and externally, set different policies to handle internal versus external access:

- **External Access via Cloudflare Tunnel**:
  - Set the policy for **external users** so that access to `ha.testhomewebsite.com` happens via the **Cloudflare Tunnel**.

- **Internal Access Directly**:
  - Ensure that any **internal device** doesn’t try to resolve **local services** through the Cloudflare Tunnel by specifying exceptions or bypassing **Cloudflare Access** when connected to the local network.

#### **7. Set Up mDNS or Use Local Discovery Services**
If your devices are compatible, **mDNS** (Multicast DNS) can allow services like **Home Assistant** to be discoverable on the **local network** without needing a Cloudflare-based DNS lookup:

- **Use mDNS** to resolve **`homeassistant.local`** to the correct IP address (`192.168.1.3`) without involving the **Cloudflare Tunnel**.
- This is particularly useful if you're accessing **Home Assistant** only locally and want to avoid DNS complexities.

### **Summary**
To prevent **DNS loops** when accessing local services over the LAN through their **Cloudflare endpoints**:
1. **Implement Split-Horizon DNS**: Configure separate DNS resolution paths for internal and external domains.
2. **Set Up Split Tunnels**: Exclude your local IP range from Cloudflare’s split tunneling to allow local traffic to stay local.
3. **Modify Cloudflare Access DNS Policies**: Ensure internal domain names are resolved internally rather than going through Cloudflare.
4. **Edit Hosts File**: For critical devices, add local entries to the **hosts file** to resolve local IPs without relying on **Cloudflare Tunnel**.
5. **Disable Loopback on Specific Entries**: Remove or adjust records that might lead to recursive DNS queries.
6. **Set Up Appropriate Access Policies**: Create access policies that differentiate between **internal** and **external** users.
7. **Use mDNS**: Utilize **mDNS** to allow **Home Assistant** to be discoverable on the **local network** without DNS.

These strategies can help you eliminate DNS loops and ensure efficient, reliable access to your **Home Assistant** and other services over both LAN and WAN. Let me know if you need further guidance with any specific settings or steps!