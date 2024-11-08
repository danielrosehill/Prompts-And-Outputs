---
title: "How to configure file mounting volumes for Outline"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You want the bind mounts for your Docker volumes to be visible directories (not preceded by a dot) and would like recommendations on where to create these directories on the host system.

### Recommended Location for Bind Mounts on the Host

To keep things organized and ensure that your data is easily accessible, it's best to create the directories in a central, clearly defined location. Here are recommended paths:

- **Recommended Directory on the Host**: `/srv/docker/outline`

This path (`/srv/docker/outline`) is a good practice because `/srv` is often used for data that needs to be shared or is managed by server services, and it helps keep all your Docker-related data in one place.

### Step-by-Step Configuration:

1. **Modify `docker-compose.yml` to Use Bind Mounts in `/srv/docker/outline`**

Here’s the updated `docker-compose.yml` configuration:

```yaml
services:
  outline:
    image: docker.getoutline.com/outlinewiki/outline:latest
    env_file: ./docker.env
    ports:
      - "3000:3000"
    volumes:
      - /srv/docker/outline/storage-data:/var/lib/outline/data
    depends_on:
      - postgres
      - redis
    environment:
      PGSSLMODE: disable

  redis:
    image: redis
    env_file: ./docker.env
    ports:
      - "6379:6379"
    volumes:
      - /srv/docker/outline/redis.conf:/redis.conf
    command: ["redis-server", "/redis.conf"]
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 30s
      retries: 3

  postgres:
    image: postgres
    env_file: ./docker.env
    ports:
      - "5432:5432"
    volumes:
      - /srv/docker/outline/database-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-d", "outline", "-U", "user"]
      interval: 30s
      timeout: 20s
      retries: 3
    environment:
      POSTGRES_USER: 'outline'
      POSTGRES_PASSWORD: 'p4fXErNVhMVrWoj3NPzW'  # Updated password
      POSTGRES_DB: 'outline'

  https-portal:
    image: steveltn/https-portal
    env_file: ./docker.env
    ports:
      - '80:80'
      - '443:443'
    links:
      - outline
    restart: always
    volumes:
      - /srv/docker/outline/https-portal-data:/var/lib/https-portal
    healthcheck:
      test: ["CMD", "service", "nginx", "status"]
      interval: 30s
      timeout: 20s
      retries: 3
    environment:
      DOMAINS: 'yourbusinesskb.com -> http://outline:3000'
      STAGE: 'production'
      WEBSOCKET: 'true'
      CLIENT_MAX_BODY_SIZE: '0'

volumes:
  https-portal-data:
  storage-data:
  database-data:
```

2. **Create the Required Directories on the Host System**

Run the following commands to create the necessary directories:

```bash
sudo mkdir -p /srv/docker/outline/storage-data
sudo mkdir -p /srv/docker/outline/database-data
sudo mkdir -p /srv/docker/outline/https-portal-data
sudo touch /srv/docker/outline/redis.conf
```

3. **Ensure Proper Permissions**

To allow Docker services to read and write to these directories, set the correct permissions:

```bash
# Allow full access to the directories (adjust permissions based on your security requirements)
sudo chmod 777 /srv/docker/outline/storage-data
sudo chmod 777 /srv/docker/outline/database-data
sudo chmod 777 /srv/docker/outline/https-portal-data
sudo chmod 644 /srv/docker/outline/redis.conf

# Set ownership to the appropriate user (e.g., root)
sudo chown -R root:root /srv/docker/outline
```

### Explanation of the Setup

1. **Location**: `/srv/docker/outline` is chosen for better organization, making it easier to locate Docker data if you need to manage, back up, or inspect it directly.
2. **Permissions**: Setting appropriate permissions ensures Docker can read/write, but you can adjust permissions based on your security requirements.
3. **Bind Mounts**: This setup ensures your data is explicitly managed on the filesystem, and you can see exactly where it is stored.

### Verify Everything is Working

1. **Run Docker Compose**:
   ```bash
   docker-compose up -d
   ```

2. **Check Mounted Directories**:
   - Ensure that data is being stored correctly in `/srv/docker/outline/storage-data`, `/srv/docker/outline/database-data`, and `/srv/docker/outline/https-portal-data`.
   - You can check the contents of these directories with:
     ```bash
     ls -la /srv/docker/outline/storage-data
     ls -la /srv/docker/outline/database-data
     ls -la /srv/docker/outline/https-portal-data
     ```

### Summary

1. **Recommended Mount Location**: `/srv/docker/outline` for better organization and visibility.
2. **Create Directories**:
   - `/srv/docker/outline/storage-data`
   - `/srv/docker/outline/database-data`
   - `/srv/docker/outline/https-portal-data`
   - `/srv/docker/outline/redis.conf`
3. **Set Permissions**: Ensure Docker services can read/write.
4. **Run and Verify**: Use Docker Compose to start services and verify data persistence.

By following these steps, you can ensure your Docker services use bind mounts with visible, easily accessible directories, leading to better data management and persistence.