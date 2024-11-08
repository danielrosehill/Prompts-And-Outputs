---
title: "Does Cloudflare Tunnel make HTTPS Portal redundant"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking if the `https-portal` Docker container is redundant if you are already using Cloudflare Tunnel to handle traffic to your Outline KM setup.

### Is `https-portal` Redundant with Cloudflare Tunnel?

Yes, **if you are already using Cloudflare Tunnel**, then the `https-portal` Docker container likely becomes redundant. Here’s why:

### Why `https-portal` Is Redundant with Cloudflare Tunnel

1. **Cloudflare Handles SSL Termination**
   - When using **Cloudflare Tunnel**, Cloudflare already manages **SSL/TLS termination**. This means Cloudflare will handle the HTTPS traffic and securely route it to your internal services over an encrypted connection.
   - Therefore, you don’t need `https-portal` to handle HTTPS because Cloudflare is already doing this for you. 

2. **Cloudflare Tunnel Manages Traffic Routing**
   - Cloudflare Tunnel can be configured to **directly route traffic** to specific internal services (like your Outline KM Docker container) based on the domain you’ve set up. This can replace the reverse proxy function of `https-portal`.
   - For example, if you have configured Cloudflare Tunnel to forward `https://your-domain.com` directly to `http://localhost:3000`, then Cloudflare Tunnel already does the job of `https-portal`.

3. **Automatic SSL Management by Cloudflare**
   - Cloudflare automatically handles SSL certificate issuance, renewal, and security settings. You don’t need another layer to manage SSL certificates, which `https-portal` was designed to handle.

### Steps to Remove `https-portal` if Redundant

If you confirm that `https-portal` is not adding any extra value to your setup, you can safely remove it:

1. **Ensure Cloudflare Tunnel Is Properly Configured**
   - Verify that your Cloudflare Tunnel routes are correctly set up. Ensure that traffic to your domain (`https://your-domain.com`) is being forwarded to the correct internal service (e.g., `http://localhost:3000`).
   - You can check this by navigating to **Cloudflare Dashboard > Access > Tunnels** and confirming the **ingress rules**.

2. **Test Access Without `https-portal` Running**
   - Stop the `https-portal` container temporarily to ensure that Outline KM is still accessible:
     ```bash
     docker stop <https-portal-container-id>
     ```
   - Check that you can still access Outline via the Cloudflare Tunnel (e.g., via `https://your-domain.com`). If everything is working as expected, then `https-portal` is not needed.

3. **Remove `https-portal` from Docker Compose**
   - Update your `docker-compose.yml` to remove the `https-portal` service:
     ```yaml
     # https-portal:
     #   image: steveltn/https-portal
     #   env_file: ./docker.env
     #   ports:
     #     - '80:80'
     #     - '443:443'
     #   links:
     #     - outline
     #   restart: always
     #   volumes:
     #     - /srv/docker/outline/https-portal-data:/var/lib/https-portal
     #   healthcheck:
     #     test: ["CMD", "service", "nginx", "status"]
     #     interval: 30s
     #     timeout: 20s
     #     retries: 3
     #   environment:
     #     DOMAINS: 'yourbusinesskb.com -> http://outline:3000'
     #     STAGE: 'production'
     #     WEBSOCKET: 'true'
     #     CLIENT_MAX_BODY_SIZE: '0'
     ```

4. **Restart Docker Services**
   - Apply the changes by restarting your Docker services:
     ```bash
     docker-compose down
     docker-compose up -d
     ```

5. **Verify Secure Access via Cloudflare**
   - After making these changes, verify that you can still access Outline KM securely through Cloudflare. Your Cloudflare Tunnel should handle SSL and routing without any problems.

### Benefits of Removing Redundant Components

1. **Simpler Configuration**
   - Removing `https-portal` simplifies your setup, making it easier to maintain and troubleshoot.
2. **Lower Resource Usage**
   - One less Docker container running means lower memory and CPU usage on your VM.
3. **Avoid Conflicts**
   - Simplifies the networking stack, reducing the chances of port conflicts and other networking issues.

### Summary:
- **Redundant Functionality**: `https-portal` is redundant if you are already using Cloudflare Tunnel for SSL termination and traffic routing.
- **Steps to Remove**: Test without `https-portal`, update `docker-compose.yml`, and verify that Cloudflare Tunnel continues to handle secure connections.
- **Benefits**: Simpler setup, reduced resource usage, and fewer configuration conflicts.

Given that Cloudflare Tunnel can handle HTTPS and routing, there’s no need to keep `https-portal` running. Just ensure your Cloudflare configuration is solid before fully removing it.