---
title: "Seeing if GPT can generate a Docker Compose from scratch"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# prompt
Can you generate a docker compose that will set up Grafana with Postgres as the backing database and anything else I might need for my application? I can configure variables in a .env or in the YAML
# Output
Here is the Docker Compose file for setting up **Grafana** with **PostgreSQL** as the backing database. You can define the environment variables in a `.env` file or directly in the YAML if preferred.

```yaml
version: "3.7"

services:
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    environment:
      - GF_SECURITY_ADMIN_USER=${GF_ADMIN_USER}
      - GF_SECURITY_ADMIN_PASSWORD=${GF_ADMIN_PASSWORD}
      - GF_DATABASE_TYPE=postgres
      - GF_DATABASE_HOST=postgres:5432
      - GF_DATABASE_NAME=${POSTGRES_DB}
      - GF_DATABASE_USER=${POSTGRES_USER}
      - GF_DATABASE_PASSWORD=${POSTGRES_PASSWORD}
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    depends_on:
      - postgres

  postgres:
    image: postgres:13
    container_name: postgres
    environment:
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  grafana_data:
  postgres_data:
```

### Example `.env` File:
Here’s an example of how to configure your environment variables in a `.env` file:

```
GF_ADMIN_USER=admin
GF_ADMIN_PASSWORD=admin_password
POSTGRES_DB=grafana
POSTGRES_USER=grafana_user
POSTGRES_PASSWORD=secure_password
```

### Instructions:
1. Save the `.env` file in the same directory as your `docker-compose.yml`.
2. Run `docker-compose up -d` to bring up the Grafana and PostgreSQL services.

This setup will launch Grafana on port **3000** and PostgreSQL on port **5432**.