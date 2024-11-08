---
title: "How secure are Cloudflare Access tunnel endpoints against probing and DNS scanning?"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

So we're creating hostnames for the tunnel endpoints. Can these by found by anyone on the internet? Doesn't providing paths to your network resources like this pose a risk? Or is Cloudflare Access protection good enough

# Output

Creating **public hostnames** for your internal resources through **Cloudflare Tunnels** does carry some risks, but **Cloudflare Access** can be an effective layer of protection when configured correctly. Here’s a breakdown of the risks and how to mitigate them:

### **1. Can the Hostnames be Found by Anyone on the Internet?**
- **DNS Discoverability**: Public **DNS records** for subdomains like `ha.testhomewebsite.com` or `nas.testhomewebsite.com` could be **found by DNS scans** if they are not protected. Anyone with tools like **Shodan**, **Censys**, or other DNS scanners can potentially discover these endpoints.
- **Cloudflare Tunnels**: While the DNS records are public, the tunnel itself does not expose the internal network directly in the way a traditional port-forwarding setup would. The traffic is encrypted, and **Cloudflare acts as a proxy** to your internal devices. However, without additional security measures, anyone who knows the hostname can still attempt to access your services.

### **2. Does Providing Paths to Internal Network Resources Pose a Risk?**
- **Exposure of Services**: Providing paths to internal network services, even via **Cloudflare Tunnels**, means that someone who discovers the hostname can attempt to connect. This could expose these services to **brute-force attacks**, **credential stuffing**, or other methods, especially if there is no further protection in place.
- **Attack Surface**: If there are vulnerabilities in the services exposed (e.g., weak login systems, outdated software), these can be exploited if the attacker can reach the service.

### **3. Is Cloudflare Access Good Enough for Protection?**
**Cloudflare Access** provides a robust level of security when configured properly. Here’s why:

- **Authentication and Authorization**: **Cloudflare Access** acts as an additional layer that requires users to authenticate before accessing services. You can enforce **multi-factor authentication (MFA)**, **SSO** using Google, GitHub, or other identity providers. This is often enough to stop most unauthorized attempts.
- **Zero Trust Model**: **Cloudflare Access** operates under the **Zero Trust** principle, meaning **no one** is trusted by default. Users must authenticate and be authorized for each request, which greatly reduces the risk of unauthorized access.
- **TLS Encryption**: Traffic is encrypted between the user and Cloudflare, and again between Cloudflare and your origin server. This makes eavesdropping or sniffing significantly harder.

### **4. Best Practices to Mitigate Risk**
- **Use Cloudflare Access for All Tunnel Endpoints**: Ensure that each hostname is protected by **Cloudflare Access**. Without this, hostnames can be accessed if discovered.
- **Limit Service Exposure**: Only expose the services that absolutely need remote access. For example, avoid exposing services like **Proxmox** unless you need to manage it remotely.
- **MFA and SSO**: Require **multi-factor authentication** for all users accessing your services. This adds an extra layer of security beyond just knowing the hostname and having credentials.
- **Strong Passwords and Updates**: Ensure that all services you expose have **strong passwords** and are regularly **updated** to mitigate vulnerabilities.
- **Access Policies**: Use **access policies** to control who can access each service. For example, you can allow only certain users, IP ranges, or device trust levels.
  
### **Summary**
- **Yes**, creating public hostnames for your tunnel endpoints means they could be found by someone scanning DNS or using similar methods. However, the real risk lies in whether these endpoints are **accessible** or **vulnerable**.
- **Cloudflare Access** provides strong protection by enforcing **authentication and authorization**. If configured well, this greatly mitigates the risks associated with having public DNS records.
- **Best Practice**: Use **Cloudflare Access**, ensure **TLS encryption**, use **MFA**, and expose only the services you need to. This approach will help you benefit from remote access while minimizing the risks of exposing your internal resources. 

If you follow these practices, your setup will be quite secure, leveraging both **Cloudflare's tunneling** and **Zero Trust security** measures.