---
title: "Why use NPM when you can specify hostnames in Cloudflare itself"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The approach of using **Nginx Proxy Manager (NPM)** with **Cloudflare Tunnel** has several advantages compared to just directly specifying hostnames in Cloudflare. Here’s a breakdown of why you might want to use NPM in combination with Cloudflare Tunnels, and how this setup can be beneficial for managing local services:

### 1. **Centralized Traffic Management (Reverse Proxy)**

With **Nginx Proxy Manager** acting as a reverse proxy, you centralize the management of all incoming traffic:

- **One central entry point**: Instead of having Cloudflare directly forward traffic to individual services, NPM becomes the single entry point. You can manage multiple services (e.g., `app1`, `app2`, `portainer`) on different ports, paths, or subdomains **all through one interface**.
- **Easier to manage complex setups**: With multiple services, you often need custom routes, header management, SSL termination, and more. NPM allows you to configure these things in one place without needing to modify each service or configure Cloudflare individually for each application.

### 2. **Avoid Port Conflicts on the Same Server**

By routing traffic through **NPM**, you can avoid port conflicts because NPM uses **host-based** or **path-based routing**. Here’s how it helps:

- **No need to expose multiple ports** on your server. For example, instead of exposing `192.168.1.1:9000` for Portainer, `192.168.1.1:8080` for another service, and so on, you can expose **only one port** (e.g., port 80 or 443) for NPM.
- **Portainer, Nextcloud, or other services** can run on any port internally (e.g., 9000, 8080) without needing to expose these ports to the public.

In contrast, if you manage each service via Cloudflare Tunnel directly, you would need to specify and manage multiple ports manually.

### 3. **SSL Termination and Automatic Certificate Management**

NPM allows for **easy SSL management**:

- **Automatic Let's Encrypt SSL**: NPM can automatically handle issuing, renewing, and managing SSL certificates for your domains.
- You don’t need to configure SSL certificates for each service separately in Cloudflare. With NPM, you can manage all certificates in one place, making it easier to set up and secure each service without complex manual setups.
  
Without NPM, you would need to manually manage SSL certificates for each service or rely on Cloudflare for SSL termination.

### 4. **Internal Docker Networking and Service Isolation**

If you are running services inside Docker containers, NPM allows you to leverage **internal Docker networking**:

- Services running in Docker containers (like Portainer, Home Assistant, etc.) can communicate over Docker’s internal network without exposing their ports to the external world. NPM can handle all the external traffic routing while services remain isolated internally.
- With Docker’s internal DNS, NPM can forward traffic to Docker containers by their service names, making it more flexible when dealing with Docker-based microservices.

Without NPM, each service would need to expose its own port (either to Docker or to Cloudflare Tunnel), which increases complexity and potential for port conflicts.

### 5. **Easier Management of Multiple Services**

NPM simplifies the process of managing multiple services on the same host:

- **User-friendly UI**: NPM has an easy-to-use web interface where you can add and configure new services, routes, and SSL certificates with just a few clicks.
- **Multiple domains/subdomains**: NPM allows you to manage many different domains or subdomains for different services on the same server. You can have `portainer.example.com`, `nextcloud.example.com`, `app.example.com`, all handled by NPM.

Without NPM, managing multiple services through Cloudflare alone might involve more complex configurations at the DNS level or within each service.

### 6. **Access Control and Security**

NPM provides built-in **access control features**:

- You can add **password protection** for specific services or paths.
- You can restrict access to certain services based on IP addresses or geographical regions.
- With **custom headers** and more fine-grained control over traffic, NPM gives you more flexibility to secure your services.

With Cloudflare alone, you would have to configure these features separately for each service or rely on Cloudflare Access (which adds another layer of complexity).

### 7. **Better Load Balancing and Failover Options**

If you have multiple instances of a service running, Nginx Proxy Manager (like Nginx itself) can handle **load balancing** and **failover** between multiple backends. This makes it easier to scale services or ensure high availability.

### 8. **Path-Based Routing and URL Rewriting**

NPM can perform advanced URL rewriting and **path-based routing**:

- You can forward traffic based on URL paths (e.g., `/app1`, `/app2`) rather than using multiple subdomains.
- This is useful if you want to have one domain (e.g., `example.com`) and route traffic based on different paths (`example.com/app1` -> app1 service, `example.com/app2` -> app2 service).

With Cloudflare Tunnel directly, this would be more difficult to manage, especially with multiple services on the same hostname.

---

### Summary of Advantages with NPM + Cloudflare:

1. **Centralized management** of all traffic and services through NPM.
2. **No port conflicts**; you only expose ports for NPM (typically 80/443).
3. **Automatic SSL certificate management** through NPM’s Let's Encrypt integration.
4. **Better security** with access controls, custom headers, and SSL termination.
5. **Path-based routing** or **domain-based routing** for multiple services on the same host.
6. **Internal service isolation** with Docker networks, making it easier to manage microservices.
7. **Simpler DNS management** in Cloudflare, as you only need to point domains to NPM and not individual services.

---

### When to Use Just Cloudflare Tunnels:
If you only have one or two services and don't want the overhead of managing NPM, you could use Cloudflare Tunnels directly, but for more than a few services, NPM becomes much easier to manage.

If you're planning on hosting several services on your server, using **Nginx Proxy Manager** alongside **Cloudflare Tunnel** simplifies the setup and provides greater flexibility, security, and ease of use.

Let me know if you need further clarification or help with the setup!