---
title: "Verifying that you can run CF tunnels with Nginx reverse proxy"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it's definitely possible—and quite common—to use **Cloudflare Tunnels** in combination with **Nginx Reverse Proxy Manager**. This setup allows you to route external traffic into your internal services securely and manage multiple services behind a single domain or subdomain without port conflicts.

### Why Use Cloudflare Tunnel with Nginx Reverse Proxy Manager?

1. **Cloudflare Tunnel**: Allows you to expose your local network services (hosted behind NAT or a firewall) to the internet without opening ports on your router. This makes it highly secure and avoids issues with port forwarding.
   
2. **Nginx Reverse Proxy Manager (NPM)**: Acts as a reverse proxy, handling all incoming traffic and forwarding it to the appropriate internal services. You can route traffic based on subdomains, paths, or even hostnames, while managing SSL certificates, headers, and much more.

Combining these two tools allows you to:
- Use **Cloudflare Tunnel** to securely expose services hosted on your internal network.
- Use **Nginx Reverse Proxy Manager** to handle multiple services behind a single IP or domain without port conflicts.

### How to Set It Up

Here’s a step-by-step guide for setting up **Cloudflare Tunnel** with **Nginx Reverse Proxy Manager** to manage your services.

### Step 1: **Set Up Cloudflare Tunnel**

1. **Create a Cloudflare Tunnel**:
   - If you haven't already, install the Cloudflare Tunnel agent on your server.
   - Create a tunnel using the `cloudflared` tool:

     ```bash
     cloudflared tunnel create <tunnel-name>
     ```

2. **Configure Tunnel with Cloudflare**:
   - After creating the tunnel, create a configuration file (usually located in `/etc/cloudflared/config.yml`) to define where the traffic should go.
   
   For example, the configuration might look like this:
   
   ```yaml
   tunnel: <tunnel-id>
   credentials-file: /root/.cloudflared/<tunnel-id>.json

   ingress:
     - hostname: app1.example.com
       service: http://localhost:80
     - hostname: app2.example.com
       service: http://localhost:80
     - service: http_status:404
   ```

   - The above configuration assumes you'll have **Nginx Reverse Proxy Manager** running locally on port 80, and **Cloudflare Tunnel** will direct the traffic to the local Nginx instance.

3. **Run the Tunnel**:
   To start the tunnel:

   ```bash
   cloudflared tunnel run <tunnel-name>
   ```

4. **Set Up DNS in Cloudflare**:
   - In your Cloudflare account, create DNS records (CNAME) for `app1.example.com`, `app2.example.com`, etc., and point them to the Cloudflare Tunnel.

### Step 2: **Install Nginx Reverse Proxy Manager (NPM)**

1. **Install Nginx Proxy Manager using Docker**:

   You can install Nginx Reverse Proxy Manager (NPM) using Docker and Portainer or with Docker Compose.

   **Docker Compose file** for Nginx Proxy Manager:
   
   ```yaml
   version: '3'
   services:
     npm:
       image: 'jc21/nginx-proxy-manager:latest'
       restart: always
       ports:
         - "80:80"      # HTTP
         - "443:443"    # HTTPS
         - "81:81"      # Nginx Proxy Manager Admin
       environment:
         - DB_SQLITE_FILE=/data/database.sqlite
       volumes:
         - ./data:/data
         - ./letsencrypt:/etc/letsencrypt
   ```

   - Save this as `docker-compose.yml`, then run the following commands to bring NPM up:
   
   ```bash
   docker-compose up -d
   ```

2. **Access the Nginx Proxy Manager**:

   - Access the Nginx Proxy Manager UI by navigating to:
     ```
     http://<your-server-ip>:81
     ```

   - The default login credentials are:
     - **Email**: `admin@example.com`
     - **Password**: `changeme`

   You’ll be prompted to change the password on first login.

### Step 3: **Configure Nginx Reverse Proxy for Services**

Now that Nginx Reverse Proxy Manager is running, you can configure reverse proxy hosts to direct traffic to your local services.

1. **Add a Proxy Host** in Nginx Proxy Manager:
   - Go to the **"Hosts"** section and click on **"Add Proxy Host"**.
   
   - For **app1.example.com**:
     - **Domain Names**: `app1.example.com`
     - **Scheme**: http
     - **Forward Hostname/IP**: The **Docker container name** or the IP address where the service is running (e.g., `app1`).
     - **Forward Port**: The internal service port (e.g., 8080).
     - **SSL**: Enable SSL via Let's Encrypt if you want secure access.

   - Repeat this process for `app2.example.com`, and other services as needed.

2. **Request SSL Certificates via Let's Encrypt** (Optional):
   If you're managing SSL with Nginx Proxy Manager, you can enable automatic SSL certificate generation via **Let's Encrypt**. When adding or editing a Proxy Host, you can request an SSL certificate by:
   
   - Selecting the **SSL** tab.
   - Checking the **"Force SSL"** box.
   - Enabling the option to **"Request a new SSL certificate"** and providing a valid email address for Let's Encrypt.

   This way, Nginx Proxy Manager will automatically handle SSL certificates for you.

### Step 4: **Verify and Test**

Once everything is set up:
1. You can visit `app1.example.com` or `app2.example.com` in a browser.
2. Cloudflare Tunnel will route traffic to your server.
3. Nginx Reverse Proxy Manager will handle the request and route it internally to the correct Docker container.

### Advantages of Using Both Together:
- **Cloudflare Tunnel** handles the secure connection to the outside world without the need to expose your server's ports.
- **Nginx Reverse Proxy Manager** manages the traffic on your local server and routes it to the correct services running inside Docker containers.
- You avoid port conflicts and can manage multiple services on the same IP using domain-based routing.

---

### Summary of Key Steps:
1. **Set up a Cloudflare Tunnel** to your server to securely expose services.
2. **Install Nginx Reverse Proxy Manager** using Docker or Docker Compose to manage local traffic.
3. **Configure proxy hosts in NPM** to route traffic from specific domains (like `app1.example.com`) to your internal services.
4. **Optionally manage SSL certificates** through Nginx Proxy Manager using Let's Encrypt.

By combining these tools, you can securely manage multiple services without worrying about port conflicts, all while taking advantage of Cloudflare’s secure tunneling and Nginx’s reverse proxy capabilities.

Let me know if you need further clarification or assistance setting this up!