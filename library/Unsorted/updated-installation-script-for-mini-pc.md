---
title: "Updated installation script for mini PC"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**How to Set Up a Central Gateway VM on Proxmox**

In this guide, we'll walk through the steps to set up a **VM on Proxmox** that utilizes most of the mini PC's resources to serve as a **central gateway** for managing remote access to your home network services. This will include setting up **NGINX** as a reverse proxy, configuring a **Cloudflare Tunnel**, adding **WireGuard VPN** for secure access, and creating a **landing page** using **Dashy** to provide easy access to local services. We'll use **Ubuntu Server 22.04 LTS** as the operating system for the VM.

### **Step 1: Create a New VM in Proxmox**
1. **Log in to the Proxmox Web Interface**:
   - Navigate to your Proxmox instance and select the node where you want to create the VM.
   - Click on **Create VM**.

2. **Configure the VM Settings**:
   - **General**: Provide a VM ID and name for the VM (e.g., "Central-Gateway-VM").
   - **OS**: Select the **Ubuntu Server 22.04 LTS ISO** that you've uploaded to Proxmox.
   - **System**: Set BIOS to "Default" and leave other settings as default.
   - **Sockets**: Set to **1**.

3. **Assign Resources**:
   - **CPU**: Allocate **3 out of 4 CPU cores** to the VM, leaving one core for Proxmox itself.
   - **Memory**: Allocate **12 GB** of RAM to the VM, keeping **4 GB** for Proxmox.
   - **Disk**: Assign **80-100 GB** of storage to the VM, depending on your needs and available space.

4. **Network Configuration**:
   - Use the existing bridge (`vmbr0`), which connects the VM directly to your LAN.
   - Assign a **static IP** during the Ubuntu installation to simplify routing and remote access later.

5. **Finish the VM Creation**:
   - Click **Finish** to create the VM, then start the VM to begin installing Ubuntu.

### **Step 2: Install and Configure Ubuntu Server**
1. **Install Ubuntu Server**:
   - Follow the installation prompts for **Ubuntu Server 22.04 LTS**.
   - Set up a **static IP address** for the VM (e.g., `192.168.1.100/24`).
   - Ensure **OpenSSH** is installed during setup for easy remote management.

2. **Update System Packages**:
   - After logging in via SSH or the Proxmox console, run:
     ```bash
     sudo apt update && sudo apt upgrade -y
     ```

### **Step 3: Set Up NGINX as a Reverse Proxy**
1. **Install NGINX**:
   ```bash
   sudo apt install nginx -y
   ```

2. **Configure NGINX**:
   - Create a configuration file for the reverse proxy:
     ```bash
     sudo nano /etc/nginx/sites-available/reverse-proxy.conf
     ```
   - Add the following configuration to set up reverse proxy routes for local services (e.g., Home Assistant and NAS):
     ```nginx
     server {
         listen 80;
         server_name testhomewebsite.com;

         location /ha {
             proxy_pass http://192.168.1.3:8123;  # Home Assistant VM
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }

         location /nas {
             proxy_pass http://192.168.1.50:5000;  # NAS
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```
   - Save and close the file (`Ctrl + O`, `Enter`, `Ctrl + X`).

3. **Enable and Restart NGINX**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### **Step 4: Set Up Cloudflare Tunnel**
1. **Install Cloudflared**:
   ```bash
   curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
   sudo mv cloudflared /usr/local/bin/
   sudo chmod +x /usr/local/bin/cloudflared
   ```

2. **Authenticate Cloudflare**:
   - Run the following to authenticate with Cloudflare:
     ```bash
     cloudflared tunnel login
     ```
   - Follow the URL provided to connect your Cloudflare account.

3. **Create and Configure the Tunnel**:
   - Create a new tunnel:
     ```bash
     cloudflared tunnel create testhomewebsite
     ```
   - Create the tunnel configuration file:
     ```bash
     sudo nano /etc/cloudflared/config.yml
     ```
   - Add the following configuration:
     ```yaml
     tunnel: testhomewebsite
     credentials-file: /root/.cloudflared/credentials.json

     ingress:
       - hostname: testhomewebsite.com
         service: http://localhost:80
       - service: http_status:404
     ```

4. **Run the Tunnel**:
   ```bash
   cloudflared tunnel run testhomewebsite &
   ```

### **Step 5: Set Up WireGuard for VPN Access**
1. **Install WireGuard**:
   ```bash
   sudo apt install wireguard -y
   ```

2. **Generate WireGuard Keys**:
   ```bash
   wg genkey | tee privatekey | wg pubkey > publickey
   ```

3. **Configure WireGuard**:
   - Create the configuration file:
     ```bash
     sudo nano /etc/wireguard/wg0.conf
     ```
   - Add the following configuration:
     ```ini
     [Interface]
     Address = 10.0.1.1/24
     PrivateKey = $(cat privatekey)
     ListenPort = 51820

     [Peer]
     PublicKey = <Client-Public-Key>
     AllowedIPs = 10.0.1.2/32
     ```

4. **Bring Up the WireGuard Interface**:
   ```bash
   sudo wg-quick up wg0
   ```

### **Step 6: Create a Landing Page Using Dashy**
1. **Install Docker**:
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sh get-docker.sh
   ```

2. **Deploy Dashy**:
   - Create a folder for Dashy and move into it:
     ```bash
     mkdir ~/dashy && cd ~/dashy
     ```
   - Create a Docker Compose file:
     ```yaml
     version: '3'
     services:
       dashy:
         image: lissy93/dashy
         container_name: dashy
         ports:
           - 8080:80
         volumes:
           - ./config.yml:/app/config.yaml
         restart: unless-stopped
     ```
   - Start Dashy using Docker Compose:
     ```bash
     sudo docker-compose up -d
     ```

3. **Add Dashy to NGINX**:
   - Update the NGINX reverse proxy configuration to include Dashy:
     ```nginx
     location /dashboard {
         proxy_pass http://localhost:8080;
         proxy_set_header Host $host;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         proxy_set_header X-Forwarded-Proto $scheme;
     }
     ```
   - Restart NGINX:
     ```bash
     sudo systemctl restart nginx
     ```

### **Summary**
With these steps, you have set up a **central gateway VM** on Proxmox that uses most of the mini PC's resources. The VM includes **NGINX** as a reverse proxy, a **Cloudflare Tunnel** for secure external access, **WireGuard VPN** for internal secure access, and **Dashy** as a landing page for easy navigation of all services. This setup will help you efficiently manage remote access to your home network while keeping it secure and organized.