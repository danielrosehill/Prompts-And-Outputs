---
title: "Verifying configuration changes in Home Assistant"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, if you're connecting to **Home Assistant** via **Cloudflare Tunnel** and routing through **Nginx Proxy Manager** (NPM), which is running on **192.168.1.20**, you'll need to configure **Home Assistant** to trust the incoming connection from Nginx Proxy Manager. Here’s what you need to configure:

### 1. **Add Nginx Proxy Manager as a Trusted Proxy**

Home Assistant must know that Nginx Proxy Manager is forwarding traffic on behalf of the client, so you need to configure **trusted proxies** in your `configuration.yaml`.

#### Steps:
1. **Edit the `configuration.yaml`** file in Home Assistant and add the following:

   ```yaml
   http:
     use_x_forwarded_for: true
     trusted_proxies:
       - 192.168.1.20  # Nginx Proxy Manager IP
   ```

   - **`use_x_forwarded_for: true`**: This allows Home Assistant to use the `X-Forwarded-For` header to get the actual IP address of the client.
   - **`trusted_proxies`**: This is where you specify the IP address of Nginx Proxy Manager, which is **192.168.1.20** in your setup.

2. **Restart Home Assistant** for the changes to take effect.

### 2. **Optional: CORS Configuration (if required)**

If you're facing any issues with accessing the frontend or resources not loading correctly, you may need to configure **CORS** (Cross-Origin Resource Sharing) in Home Assistant.

In the `configuration.yaml`, add the following under `http`:

```yaml
http:
  cors_allowed_origins:
    - https://your-domain.com  # The domain used for Home Assistant via NPM
```

This is needed if you are using a custom domain that is routed through Cloudflare Tunnel and Nginx Proxy Manager.

### 3. **SSL Configuration**

- If **Nginx Proxy Manager** is terminating SSL (e.g., using Let's Encrypt), you don’t need to enable SSL in Home Assistant. You can keep Home Assistant running with HTTP internally, and Nginx Proxy Manager will handle HTTPS externally.
- If you want to ensure that connections to Home Assistant are always encrypted, you can enforce SSL in NPM by checking the **Force SSL** option when configuring the proxy host.

### 4. **Firewall/Network Rules**

Ensure that Home Assistant is accessible from the Nginx Proxy Manager (NPM) server (i.e., from **192.168.1.20**). Verify that port **8123** is open and that the connection is allowed from NPM to Home Assistant's local IP.

### 5. **Test the Setup**

After configuring the above, try accessing Home Assistant via the domain you've configured in Cloudflare Tunnel and Nginx Proxy Manager (e.g., `https://homeassistant.yourdomain.com`).

### Summary of Steps:
1. Add **Nginx Proxy Manager (192.168.1.20)** as a **trusted proxy** in Home Assistant’s `configuration.yaml`.
2. Enable `use_x_forwarded_for` to handle the correct IP forwarding.
3. Optionally configure **CORS** if needed.
4. Ensure that NPM is handling **SSL termination** and that Home Assistant is running over HTTP internally.

These configurations will ensure that Home Assistant accepts the incoming connections from Nginx Proxy Manager through Cloudflare Tunnel.

Let me know if you need further help with the setup!