---
title: "Routing traffic onto Docker apps without exposing ports locally"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Given that your Nginx Proxy Manager (NPM) is running on one machine (machine 1, ingress gateway), and the Docker apps are on a separate server (machine 2), here’s how you could set up internal routing without exposing ports on machine 2.

### Solution: Use an SSH Tunnel or VPN Between Machines

Since NPM and your Docker apps are on different machines, and you don’t want to expose ports on machine 2, you have two main options to securely route traffic internally:

#### Option 1: Use an SSH Tunnel
1. **Set up an SSH Tunnel** from machine 1 (NPM server) to machine 2 (Docker server) that forwards traffic from a local port on machine 1 to the internal app on machine 2.
2. **Create the SSH Tunnel**:
   - Run this command on machine 1 (NPM):
     ```bash
     ssh -N -L localhost:<local-port>:localhost:<app-port> user@192.168.1.2
     ```
     - Replace `<local-port>` with an unused port on machine 1 (e.g., 8080).
     - Replace `<app-port>` with the internal port of the Docker app on machine 2 (e.g., 80 if your app listens on HTTP).
     - Replace `user@192.168.1.2` with your SSH username and the IP address of machine 2.
   - This command forwards requests from `localhost:8080` on machine 1 to the application’s internal port on machine 2.
3. **Configure NPM**:
   - In NPM, set up a new proxy host and point it to `http://localhost:<local-port>` (e.g., `http://localhost:8080`), which now directs traffic to the Docker app on machine 2 through the SSH tunnel.

#### Option 2: Use a VPN (e.g., WireGuard or Tailscale)
1. **Create a VPN** between machine 1 (NPM server) and machine 2 (Docker server), allowing secure internal communication without exposing ports publicly.
   - **Install and configure the VPN** (e.g., WireGuard or Tailscale) on both machines to establish a secure, encrypted network.
2. **Assign a VPN IP to Docker Apps on Machine 2**:
   - With the VPN active, assign a private IP within the VPN network (e.g., 10.1.1.2) to your Docker app container on machine 2.
3. **Configure NPM to Route to the VPN IP**:
   - In NPM on machine 1, set the proxy host to point to the VPN IP of your Docker app container on machine 2 (e.g., `http://10.1.1.2:80`).

### Summary of Both Options
- **SSH Tunnel**: Create an SSH tunnel from machine 1 to machine 2, forwarding traffic from a local port on machine 1 to the Docker app on machine 2. Use `localhost:<local-port>` in NPM to route traffic to the Docker app.
- **VPN**: Set up a VPN between machine 1 and machine 2, and assign a VPN IP to the Docker app. Use the VPN IP in NPM to route traffic securely to machine 2 without exposing ports.

Both methods enable internal routing between machines without opening ports on machine 2, allowing NPM to route traffic securely to your Docker applications.