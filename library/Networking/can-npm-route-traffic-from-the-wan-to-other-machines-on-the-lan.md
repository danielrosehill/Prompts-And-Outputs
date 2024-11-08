---
title: "Can NPM route traffic from the WAN to other machines on the LAN"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, **Nginx Reverse Proxy (including Nginx Proxy Manager)** can direct traffic to services running on other **local IPs** within your network. This is a common use case when you have services spread across different machines, containers, or IPs within a LAN, and you want to route external traffic to them via a centralized reverse proxy like Nginx.

### How It Works:

- Nginx acts as the reverse proxy and listens for incoming requests.
- Based on the request's **domain name** or **path**, Nginx routes traffic to the appropriate backend service, which can be running on a **different machine** (with a different local IP) in your network.

### Example Scenario:
You have:
- **Nginx Proxy Manager** running on **192.168.1.1**.
- A service running on **192.168.1.5:8080** (for example, a web app).
- Another service running on **192.168.1.10:9090** (for example, a database or another app).

You want to route traffic to these services without exposing them directly to the internet.

### Steps to Set It Up:

1. **Ensure Connectivity**:
   - Make sure that the Nginx server (on **192.168.1.1**) can access the services running on the other local IPs (e.g., **192.168.1.5** and **192.168.1.10**) within your LAN.
   - Check if firewalls or network rules allow connections between the Nginx server and other devices.

2. **Configure a Proxy Host in Nginx Proxy Manager**:

   Here’s how to do it using **Nginx Proxy Manager**:

   - Log into Nginx Proxy Manager (typically via `http://<your-nginx-server-ip>:81`).
   - Go to **Hosts** > **Proxy Hosts**.
   - Click on **Add Proxy Host**.

3. **Configure Proxy Host for Each Service**:

   For each service, you'll set up a proxy host configuration.

   #### For the service on **192.168.1.5:8080**:
   - **Domain Name**: For example, `app1.yourdomain.com`.
   - **Scheme**: HTTP (if the service on 192.168.1.5 is running HTTP).
   - **Forward Hostname/IP**: Enter `192.168.1.5` (the local IP of the service).
   - **Forward Port**: Enter `8080` (the port the service is running on).
   - Enable **Websockets Support** if needed (for services that rely on WebSocket communication).
   - Go to the **SSL** tab and configure SSL if required (e.g., request a new SSL certificate for the domain via Let's Encrypt).

   #### For the service on **192.168.1.10:9090**:
   - Follow the same steps as above, but change the domain name, hostname, and port accordingly.
   - **Domain Name**: For example, `app2.yourdomain.com`.
   - **Forward Hostname/IP**: `192.168.1.10`.
   - **Forward Port**: `9090`.

4. **Enable SSL (Optional but Recommended)**:
   - In each proxy host configuration, go to the **SSL** tab.
   - Enable **Force SSL** and **Request a new SSL certificate** if you want to serve traffic securely via HTTPS.
   - Nginx Proxy Manager will handle SSL certificates via Let's Encrypt.

5. **Save the Proxy Host Configuration**:
   - Once the configurations are saved, Nginx Proxy Manager will route traffic for `app1.yourdomain.com` to **192.168.1.5:8080**, and traffic for `app2.yourdomain.com` to **192.168.1.10:9090**.

### Testing:
- You can test by navigating to `http://app1.yourdomain.com` or `https://app1.yourdomain.com`, and it should route traffic to the service on **192.168.1.5:8080**.
- Similarly, test for `app2.yourdomain.com`.

### Example Use Cases:
- You may have a **web app** running on one local IP and a **database** or **API service** running on another.
- All traffic can go through Nginx, allowing you to handle SSL termination, logging, and access controls centrally.

### Alternative: Manual Nginx Configuration (without NPM):
If you're not using **Nginx Proxy Manager** and prefer to manually configure Nginx, you can directly edit the Nginx configuration file (usually `/etc/nginx/nginx.conf` or a separate file in `/etc/nginx/sites-available/`).

Here's an example of a manual Nginx configuration to proxy to another local IP:

```nginx
server {
    listen 80;
    server_name app1.yourdomain.com;

    location / {
        proxy_pass http://192.168.1.5:8080;  # Forward to local IP
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

server {
    listen 80;
    server_name app2.yourdomain.com;

    location / {
        proxy_pass http://192.168.1.10:9090;  # Forward to another local IP
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

After adding this configuration, reload Nginx:

```bash
sudo systemctl reload nginx
```

### Summary:

- **Nginx Proxy Manager** (or Nginx itself) can absolutely proxy traffic to services running on other local IP addresses in your network.
- This setup allows you to centralize traffic management, handle SSL, and provide secure access to multiple services running across different machines or containers in your LAN.
- You can route traffic based on **domain names** or **paths** while keeping all services behind the same Nginx reverse proxy.
  
This is particularly useful in scenarios where services are distributed across multiple devices in your network.

Let me know if you need further help or clarification!