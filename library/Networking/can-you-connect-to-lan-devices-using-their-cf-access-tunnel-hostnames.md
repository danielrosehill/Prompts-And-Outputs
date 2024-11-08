---
title: "Can you connect to LAN devices using their CF access tunnel hostnames"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is possible to connect to your LAN devices using the hostnames from your **Cloudflare Access tunnels**, but there are some steps you'll need to follow to ensure everything is set up correctly.

Here’s how to approach it:

### 1. **Cloudflare Tunnel Setup**
You already have a **Cloudflare tunnel** set up, but to access your LAN devices using hostnames, you need to ensure that each device on your LAN is reachable via a unique domain/subdomain. Here's the process:

- **Create Hostnames for Each LAN Device**: 
   In Cloudflare, you can assign each LAN device a unique **subdomain** or **hostname**. For example, if your primary domain is `testhomewebsite.com`, you can create subdomains like:
   - `homeassistant.testhomewebsite.com` for your Home Assistant instance.
   - `nas.testhomewebsite.com` for your NAS.
   - `desktop.testhomewebsite.com` for your general-purpose desktop.

- **Set Up Tunnel Routes**: 
   For each device you want to access via its hostname, configure a **Cloudflare Tunnel route** to map the subdomain to the local IP address of the device. For example, if your Home Assistant runs on `192.168.1.3`, you can set up a route like this:
   - `homeassistant.testhomewebsite.com` → `http://192.168.1.3:8123`

   To configure this:
   - In your Cloudflare dashboard, under **Access > Tunnels**, create a route for each device by specifying the hostname and the internal IP/port combination.

### 2. **DNS Configuration**
Once the Cloudflare tunnels are in place, you need to ensure that DNS is correctly set up:

- **Cloudflare DNS**: Make sure that your subdomains (e.g., `homeassistant.testhomewebsite.com`) are correctly mapped to Cloudflare's zero-trust service, which will proxy the traffic to your LAN device through the tunnel.
  
- **Custom Domains with Cloudflare**: If using custom domains or subdomains, ensure that Cloudflare DNS is properly configured to route the requests through the tunnel to your local network.

### 3. **Access Control via Cloudflare Access**
To ensure security, you can use **Cloudflare Access** policies to manage who can access your LAN devices via these hostnames:
- Set up **Zero Trust Access policies** in the **Cloudflare Access** dashboard to allow or deny access based on email, IP address, or other criteria.
- Ensure only authorized users can connect through the tunnels to the local devices.

### 4. **Accessing Devices Using Hostnames**
Once everything is set up:
- You can access your devices by entering the **hostname** in the browser or appropriate tool (e.g., `homeassistant.testhomewebsite.com`).
- The Cloudflare tunnel will forward the request to the local device using the tunnel’s established route.

### Considerations:
- **Persistent Connectivity**: Ensure that the **Cloudflare daemon** (`cloudflared`) is running on your local network or gateway device that manages the tunnel.
- **SSL Certificates**: If needed, Cloudflare can provide **SSL/TLS certificates** to secure the connection between the tunnel and the hostname, ensuring secure access.
  
### Example:
To access **Home Assistant** at `http://192.168.1.3:8123`, you could:
1. Set up a tunnel route in Cloudflare to point `homeassistant.testhomewebsite.com` to `192.168.1.3:8123`.
2. Visit `homeassistant.testhomewebsite.com` in your browser, and Cloudflare will route the traffic to your local Home Assistant instance.

### Conclusion:
You can definitely use the **hostnames of your Cloudflare tunnels** to access LAN devices. The key steps involve configuring each device’s tunnel, setting up the DNS routing, and securing access through Cloudflare Access policies.

Let me know if you need further clarification or help with setup!