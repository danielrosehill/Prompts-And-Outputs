---
title: "Setting up Pi Hole on Proxmox host"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is absolutely possible to set up **Pi-hole** on a **Proxmox host** as a **Virtual Machine (VM)**, and it is a great way to gain more control over DNS without having to modify the settings on your ISP router. Below, I'll walk you through the necessary steps, including how to size the VM, set up Pi-hole, and configure it to work in conjunction with your ISP router.

### **1. Setting Up Pi-hole as a VM on Proxmox**

#### **Step 1: Create a VM in Proxmox**
1. **Log in to Proxmox**.
2. **Create a New Virtual Machine**:
   - Go to **Datacenter** > **Node** (where you want the VM) > **Create VM**.
   - Give the VM a name like `Pi-hole`.
   - Assign an **Operating System**. A minimal Linux distribution like **Debian** or **Ubuntu Server** is recommended.

#### **Step 2: Configure VM Resources**
- **CPU**: Pi-hole does not need much CPU power. Assign **1 vCPU** (or 2 if you prefer some overhead).
- **RAM**: Allocate **512 MB to 1 GB** of RAM. Pi-hole is very lightweight, so **512 MB** should suffice.
- **Storage**: Use **10-20 GB** of storage for the VM disk. This is more than enough for Pi-hole and allows space for logs.
- **Network**: Ensure the VM has access to your **LAN network**, ideally via a **bridged network interface**.

#### **Step 3: Install the Operating System**
- Install **Debian** or **Ubuntu Server** as the OS.
- During installation, make sure the **network** is configured properly so that the Pi-hole VM can access your LAN and internet.

#### **Step 4: Install Pi-hole**
Once the OS is installed:
1. **Update System Packages**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```
2. **Install Pi-hole**:
   Run the one-line install command:
   ```bash
   curl -sSL https://install.pi-hole.net | bash
   ```
3. **Configure Pi-hole**:
   - During setup, select the **network interface** that the VM is using.
   - Set a **static IP** for the Pi-hole VM. You can do this during installation, or manually configure it afterward. The IP must be in the same range as your LAN (e.g., `192.168.1.x`).

### **2. Configuring Pi-hole to Work with Your ISP Router**

After installing Pi-hole, you need to make sure it is configured correctly to handle DNS queries for devices on your LAN.

#### **Step 1: Set the Pi-hole as Your Primary DNS Server**
There are a couple of ways to make Pi-hole work alongside your ISP router.

##### **Option 1: Manually Change DNS on Each Device**
Since you can't modify the DNS settings on the ISP router, you can change the DNS settings on each device to point to Pi-hole:
1. **Go to Network Settings** on each device.
2. Manually set the **DNS Server** to the IP address of your **Pi-hole VM** (e.g., `192.168.1.x`).
3. This way, all DNS requests from these devices will be routed through Pi-hole.

##### **Option 2: Use Pi-hole as an Upstream DNS Server**
1. **Leave the Router DNS as is** (Google DNS: `8.8.8.8`, `8.8.4.4`).
2. **On Pi-hole**, set the **Upstream DNS servers** to your preferred public DNS, such as **Google (8.8.8.8)**, **Cloudflare (1.1.1.1)**, or even the default provided by your ISP.
   - This ensures Pi-hole will act as an intermediary to filter requests before forwarding them upstream.
3. Any device whose DNS is set to **Pi-hole** will then filter traffic through Pi-hole before reaching external DNS servers.

#### **Step 2: Add Custom DNS Entries for Split DNS**
To make sure **Home Assistant** (`ha.testhomewebsite.com`) resolves correctly to its **local IP** for devices on your LAN:
1. **Go to Pi-hole’s Web Interface**:
   - Open a browser and go to `http://<Pi-hole IP address>/admin`.
2. **Add a Custom DNS Record**:
   - Navigate to **Local DNS** > **DNS Records**.
   - Add an entry for `ha.testhomewebsite.com` with the IP address of your Home Assistant (`192.168.1.3`).
   - This will ensure that devices using Pi-hole for DNS will resolve `ha.testhomewebsite.com` directly to its local IP, bypassing the Cloudflare Tunnel for LAN access.

#### **Step 3: Update DHCP Configuration (Optional)**
If your **ISP router** allows you to modify DHCP settings, you could set Pi-hole as the DNS server provided by the DHCP lease. This means that any device connecting to the network will automatically receive the Pi-hole’s IP address as their DNS server, without needing to manually update each device.
- **DHCP Settings on ISP Router**: Set the **DNS server** in the DHCP settings to the IP of Pi-hole (`192.168.1.x`).
- Not all ISP routers allow DHCP DNS settings changes, but if yours does, it simplifies the network configuration greatly.

### **3. Verify the Configuration**
Once you have Pi-hole set up and devices are using it:

1. **Check Devices’ DNS Settings**:
   - Make sure devices on the LAN have the **Pi-hole IP** as their DNS server.
   - On **Windows**, you can use:
     ```cmd
     ipconfig /all
     ```
     Look for **DNS Servers** to confirm it is set to Pi-hole.

2. **Test Home Assistant Access**:
   - From a device on the LAN, open a browser and try to connect to `http://ha.testhomewebsite.com`.
   - It should now resolve to the local IP address (`192.168.1.3`), allowing you to access Home Assistant directly.

3. **Check Pi-hole Dashboard**:
   - You can verify that DNS requests are passing through Pi-hole by visiting its **web dashboard** (`http://<Pi-hole IP>/admin`).
   - The dashboard will show logs of DNS queries, including requests for `ha.testhomewebsite.com`.

### **4. Hardware Requirements for the Pi-hole VM**
Pi-hole is lightweight, so the hardware requirements for your **Proxmox VM** are minimal:
- **CPU**: 1 or 2 cores (vCPU).
- **RAM**: 512 MB to 1 GB (depending on expected traffic).
- **Storage**: 10-20 GB (more than enough for Pi-hole and logs).
- **Network Interface**: Ensure the VM has access to the **LAN** via a bridged adapter.

### **Summary**
1. **Create a VM** on Proxmox with **1 vCPU**, **512 MB to 1 GB RAM**, and **10-20 GB storage**.
2. **Install Pi-hole** on a minimal Linux distro like **Debian** or **Ubuntu Server**.
3. **Configure Pi-hole** to have a **static IP** on your LAN.
4. **Set devices' DNS** to the Pi-hole IP to make use of Pi-hole filtering.
5. **Add a DNS record** in Pi-hole for `ha.testhomewebsite.com` to point to its **local IP** (`192.168.1.3`) for local access.

This setup will allow devices on your LAN to bypass the Cloudflare Tunnel when accessing Home Assistant, ensuring smooth local connectivity. Let me know if you need any more detailed guidance for any of these steps!