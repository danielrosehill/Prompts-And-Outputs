---
title: "Adding automatic restart to Docker containers for Outline"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking whether Docker containers will automatically recreate if the machine is restarted.

### Automatic Restart Behavior for Docker Containers

By default, Docker containers **do not** automatically restart after a host machine reboot unless explicitly configured to do so. However, Docker provides ways to ensure that containers automatically restart under various conditions, including system reboots.

### Configuring Automatic Restart with `restart` Policy

To ensure that your Docker containers automatically start after a machine reboot, you can use the `restart` policy in your `docker-compose.yml` or when running `docker run`. Here’s how it works:

1. **`restart` Policies Explained**
   - **`no`** (default): Containers will not restart automatically.
   - **`always`**: Containers will always restart, regardless of the exit status. This also ensures that containers restart when the Docker daemon starts (e.g., after a system reboot).
   - **`on-failure`**: Containers will only restart if they exit with a non-zero error code.
   - **`unless-stopped`**: Containers will restart automatically unless they are explicitly stopped by the user. They will not restart if the user stops them manually but will restart on system reboot.

2. **How to Set the `restart` Policy in `docker-compose.yml`**

Here’s how you can modify your `docker-compose.yml` to make sure your containers automatically restart after a reboot:

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
    restart: always
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
    restart: always

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
    restart: always

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
```

### Explanation:
- **`restart: always`**: Adding this line to each service ensures that containers restart automatically after the Docker daemon starts up, such as after a system reboot.

### How to Apply These Changes

1. **Stop and Recreate Containers with Updated Configuration**
   - Use the following commands to stop and recreate your containers with the new `restart` policy:
     ```bash
     docker-compose down
     docker-compose up -d
     ```

2. **Verify Restart Policy**
   - To verify that the restart policy is set correctly, you can inspect a running container:
     ```bash
     docker inspect --format='{{.HostConfig.RestartPolicy.Name}}' <container-id>
     ```
   - Replace `<container-id>` with the ID or name of your container. It should show `always` if correctly configured.

### What Happens After a Reboot?

1. **When the Host Machine Restarts:**
   - The Docker daemon starts up.
   - Any containers with a restart policy of `always` or `unless-stopped` will automatically restart.
2. **When Docker Itself Restarts:**
   - The same behavior applies. Containers will restart based on their configured restart policy.

### Summary:
To ensure Docker containers restart automatically after a system reboot:
1. **Add `restart: always`** to each service in your `docker-compose.yml`.
2. **Recreate containers** with `docker-compose up -d` to apply changes.
3. **Verify restart policies** using `docker inspect`.

This setup guarantees that your services, including Outline, Redis, and PostgreSQL, will come back online after a server restart without manual intervention.