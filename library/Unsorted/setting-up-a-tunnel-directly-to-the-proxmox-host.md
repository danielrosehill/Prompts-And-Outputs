---
title: "Setting up a tunnel directly to the Proxmox host"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I've always heard that it's highly discouraged to set up tunnels to Proxmox hosts. Is that definitely the case? If not, what you wrote makes sense to me. 

# Output

You're correct that exposing **Proxmox** hosts directly to the internet is generally discouraged. This is primarily due to security concerns, since a Proxmox host, as a hypervisor, often has elevated control over the VMs and containers that run on it, making it an attractive target for attackers. Here are some considerations about setting up tunnels to a **Proxmox** host:

### **1. Why Tunneling Directly to Proxmox is Discouraged**
- **Security Risks**: Proxmox hosts provide direct access to the management layer of your hypervisor, which could control all the VMs. If exposed to the internet, Proxmox could be a target for attacks, including brute force, exploit attempts, and other unauthorized access risks.
- **Web Interface Vulnerabilities**: Exposing the **Proxmox web interface** might open up potential vulnerabilities. Like all web interfaces, it is subject to the risk of unknown zero-day vulnerabilities, and exposing it could put your entire infrastructure at risk.

The general recommendation is to **never expose** Proxmox directly to the internet, even through a tunnel. Instead, use indirect methods of access to minimize risk, such as:

- **VPN Access**: Set up a **VPN** server on your network (using **WireGuard** or **OpenVPN**) and connect to your local network through the VPN before accessing Proxmox. This ensures that the Proxmox host remains only accessible from the internal network, reducing exposure.
- **Jump Host**: Use a **jump host (bastion host)** that acts as a secure intermediary. You would first connect to this host via SSH, and from there, access the Proxmox UI.

### **2. Tunnel Setup Considerations**
While using a **Cloudflare Tunnel** offers a secure way to create remote access without exposing ports, there are still concerns because:
- **Web-Based Attacks**: Even with authentication through Cloudflare Access, once access to the tunnel is obtained, the Proxmox UI is still open to attacks like CSRF or other web vulnerabilities.
- **Complexity of Hardening**: Hardening Proxmox for public exposure requires additional measures like WAF (Web Application Firewall), strong authentication, and strict access control.

### **3. Recommended Setup for Proxmox Access**
If you decide to use a **Cloudflare Tunnel**, the best practice is to mitigate risks by incorporating the following:
1. **Reverse Proxy**: Use a **reverse proxy** (such as **NGINX** or **Caddy**) in front of Proxmox, with additional layers of authentication (such as HTTP Basic Auth or OAuth). This adds another barrier between the tunnel and the Proxmox interface.
2. **Firewall Rules**: Implement firewall rules that only allow certain IP ranges (e.g., Cloudflare IPs) to connect to the Proxmox port (`8006`).
3. **Authentication Layers**:
   - Use **Cloudflare Access** to implement **Zero Trust security**. Cloudflare Access can enforce identity-based authentication, ensuring only trusted users can access the Proxmox host.
4. **Two-Factor Authentication (2FA)**: Enable **2FA** on your Proxmox host for an added layer of security.

### **Alternative Access Methods**
If exposing Proxmox via a tunnel makes you uneasy, consider these more conservative alternatives:

1. **VPN (Preferred Method)**:
   - Set up a VPN server on your mini PC or another device (using **WireGuard**, **OpenVPN**, or similar).
   - Use the VPN to connect to your local network securely, then access the Proxmox host at its local IP address (`192.168.1.10:8006`).
   - This approach significantly reduces the risk of exposure, since the Proxmox host remains on a private network and can only be accessed once connected to the VPN.

2. **SSH Port Forwarding via Jump Host**:
   - Create a **jump host** VM on the Proxmox hypervisor or on the mini PC.
   - Use SSH to connect to the jump host, then forward a local port to the Proxmox interface.
   - Example SSH command:
     ```bash
     ssh -L 8006:192.168.1.10:8006 user@jump_host_ip
     ```
   - After connecting, visit `https://localhost:8006` on your local browser to access Proxmox.

3. **Self-Hosted VPN + Reverse Proxy**:
   - Set up a **VPN server** on your mini PC.
   - Install **NGINX** as a reverse proxy on the mini PC to add additional security measures.
   - Only expose the VPN server externally, and once connected, access all your local services.

### **Conclusion**
Directly exposing your **Proxmox host** through a tunnel, even a **Cloudflare Tunnel**, can be risky. However, if you decide to proceed, adding multiple layers of security—such as using a **reverse proxy**, **firewall rules**, and **multi-factor authentication**—can help mitigate those risks.

**Preferred Approach**: Given the elevated control Proxmox has over your entire network, the **VPN + Reverse Proxy** method is the safest. This allows you to maintain a centralized access point (the mini PC) while keeping Proxmox safely behind a private network layer, accessible only via the VPN. 

If you're comfortable with the extra security steps, what I previously outlined would make sense, but leaning towards setting up a **VPN** first and using a jump host for Proxmox access is generally more recommended to keep your environment safe. Let me know if you need more specific configuration instructions or further help refining this setup!