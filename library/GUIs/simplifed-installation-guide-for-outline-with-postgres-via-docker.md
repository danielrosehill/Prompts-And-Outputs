---
title: "Simplifed installation guide for Outline with Postgres via Docker"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here is a simplified installation guide for setting up Outline with PostgreSQL, based on the documentation provided. This guide focuses on essential steps, making it easier to follow.

---

## **Outline + PostgreSQL Installation Guide**

### **1. Prerequisites**
- Ensure Docker and Docker Compose are installed on your server.
  - [Install Docker](https://docs.docker.com/get-docker/)
  - [Install Docker Compose](https://docs.docker.com/compose/install/)

### **2. Configuration**
1. **Environment File**:
   - Create a `docker.env` file based on [this sample file](https://github.com/outline/outline/blob/main/.env.sample).
   - Fill out the required environment variables and add at least one authentication provider to start Outline.

2. **Docker Compose File**:
   - Create a `docker-compose.yml` file in your setup directory.
   - Use the following configuration for a full setup with Outline, PostgreSQL, Redis, and HTTPS support.

   ```yaml
   services:
     outline:
       image: docker.getoutline.com/outlinewiki/outline:latest
       env_file: ./docker.env
       ports:
         - "3000:3000"
       volumes:
         - storage-data:/var/lib/outline/data
       depends_on:
         - postgres
         - redis

     postgres:
       image: postgres:16
       env_file: ./docker.env
       ports:
         - "5432:5432"
       volumes:
         - database-data:/var/lib/postgresql/data
       environment:
         POSTGRES_USER: 'user'
         POSTGRES_PASSWORD: 'pass'
         POSTGRES_DB: 'outline'

     redis:
       image: redis
       ports:
         - "6379:6379"

     https-portal:
       image: steveltn/https-portal
       ports:
         - "80:80"
         - "443:443"
       environment:
         DOMAINS: 'docs.mycompany.com -> http://outline:3000'
         STAGE: 'production'
         WEBSOCKET: 'true'
       volumes:
         - https-portal-data:/var/lib/https-portal

   volumes:
     storage-data:
     database-data:
     https-portal-data:
   ```

### **3. Database Setup**
Run these commands to initialize the PostgreSQL database for Outline:

```bash
docker compose run --rm outline yarn db:create --env=production-ssl-disabled
docker compose run --rm outline yarn db:migrate --env=production-ssl-disabled
```

### **4. Start Outline**
In the same directory as your `docker-compose.yml`, start the Outline service:

```bash
docker compose up -d
```

Check for any errors in the output to ensure that Outline, PostgreSQL, and Redis are connected and running.

### **5. Access Outline**
- Access Outline at `http://localhost:3000` or use your domain (e.g., `https://docs.mycompany.com`) if configured with HTTPS.

### **6. Updating Outline**
To update Outline, follow these steps:
1. **Backup the database**: Refer to the [backup documentation](https://docs.getoutline.com/s/hosting/doc/backups-KZtPOADCHG).
2. **Update the Outline image**:
   ```bash
   docker pull docker.getoutline.com/outlinewiki/outline:latest
   ```
3. **Restart the service**:
   ```bash
   docker compose up -d
   ```

---

This guide provides a streamlined setup for a self-hosted Outline installation with PostgreSQL, Redis, and optional HTTPS. Follow the linked documentation for advanced settings, like backup and authentication integrations.