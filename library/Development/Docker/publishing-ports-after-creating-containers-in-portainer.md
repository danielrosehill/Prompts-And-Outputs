---
title: "Publishing ports after creating containers in Portainer"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Seems good but no ports are running. Can I add those in Portainer after I've created the containers?

# Outputs
Yes, you can **add ports** to your containers in **Portainer** after the containers have been created. However, **Docker** doesn't natively allow modifying port mappings on a running container. You have two options to address this:

### Option 1: Stop and Recreate the Containers with Ports

The recommended approach is to **stop and recreate** the containers with the required port mappings. Here’s how to do it in **Portainer**:

1. **Stop the Containers**:
   - In **Portainer**, go to your **FreshRSS** and **PostgreSQL** containers and stop them.
   
2. **Modify and Recreate with Port Mapping**:
   - Select **Duplicate/Edit** on each container in Portainer.
   - Under **Network**, you’ll see the **Published Ports** section.
   - Add the necessary port mappings:
     - For example, for FreshRSS, you can map port `80` on the host to port `80` on the container (or whatever port you need):
       ```
       Host: 8080, Container: 80
       ```
   - Click **Deploy the Container**. This will recreate the container with the new port mappings.

### Option 2: Modify the `docker-compose.yml` File and Redeploy

If you prefer using Docker Compose, you can add the port mappings to your `docker-compose.yml` file, then redeploy the services. Here’s how to add ports:

```yaml
services:
  freshrss:
    image: freshrss/freshrss:latest
    container_name: freshrss
    hostname: freshrss
    restart: unless-stopped
    logging:
      options:
        max-size: 10m
    ports:
      - "8080:80" # Add this line for port mapping
    volumes:
      - data:/var/www/FreshRSS/data
      - extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Europe/Paris
      CRON_MIN: '3,33'
      TRUSTED_PROXY: 172.16.0.1/12 192.168.0.1/16
```

After updating your Compose file:
1. Run `docker-compose down` to stop the containers.
2. Run `docker-compose up -d` to recreate them with the port mappings.

### Summary:
- **Portainer** allows you to modify ports by duplicating and redeploying containers.
- **Docker Compose** is more suitable for managing persistent changes like port mappings.
