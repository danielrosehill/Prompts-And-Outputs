---
title: "How to configure a redirection in NPM with Cloudflare"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
I have Nginx Proxy Manager installed now. I'm routing traffic that arrives via a Cloudflare Tunnel running to the ingress gateway (192.168.1.20) onto services that I want to host on the server this is running on (192.168.1.1). Let's say that I created an access point for Portainer at portainer.testhomewebsite.com. That's running on port 9000 on the server (so 192.168.1.1:9000). Could I set up a redirect in Nginx Proxy Manager so that I don't need to specify the port in Cloudflare?

# Output

Yes, you can set up **Nginx Proxy Manager** to handle traffic for **portainer.testhomewebsite.com** and route it to **port 9000** on your server, so you don't need to specify the port in Cloudflare.

Here’s how you can configure it:

### Step-by-Step Instructions:

1. **Log in to Nginx Proxy Manager**:
   - Access the **Nginx Proxy Manager** web interface using the management port (typically `http://<your-server-ip>:81`).

2. **Add a New Proxy Host**:
   - Navigate to **Hosts** > **Proxy Hosts** and click on **Add Proxy Host**.

3. **Configure the Proxy Host for Portainer**:
   - **Domain Names**: Enter the domain you want to use for Portainer, e.g., `portainer.testhomewebsite.com`.
   - **Scheme**: Select `http` since Portainer is running on HTTP by default on port 9000.
   - **Forward Hostname/IP**: Enter the internal IP address of your server, i.e., `192.168.1.1`.
   - **Forward Port**: Enter `9000` (Portainer’s port).
   - **Block Common Exploits**: Enable this option for security.
   - **Websockets Support**: Enable this if you expect Portainer to need it (optional but recommended).

4. **SSL Settings** (Optional but recommended):
   - Go to the **SSL** tab.
   - Check **Force SSL** to ensure all traffic is served over HTTPS.
   - Select **Request a new SSL certificate** and check **Force SSL** if you want to request a certificate from Let's Encrypt for your domain.
   - Enter a valid email address and agree to the Let's Encrypt terms.

5. **Save the Configuration**:
   - Click **Save** to create the proxy host.

### What Happens Now:
- All traffic arriving at **portainer.testhomewebsite.com** (without specifying port 9000) will be routed by Nginx Proxy Manager to your Portainer instance running on **192.168.1.1:9000**.
- If you enabled SSL, Nginx Proxy Manager will also handle the HTTPS certificate, so requests will be securely forwarded.

### Testing:
Once you’ve set this up, you can test it by going to:

```
http://portainer.testhomewebsite.com
```

Or, if you enabled SSL:

```
https://portainer.testhomewebsite.com
```

Nginx Proxy Manager will route the traffic to **192.168.1.1:9000** without you needing to explicitly specify the port in Cloudflare.

Let me know if you need more details!