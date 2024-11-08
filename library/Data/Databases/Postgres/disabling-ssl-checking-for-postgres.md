---
title: "Disabling SSL checking for Postgres"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To disable SSL for PostgreSQL in your setup, you need to add the `PGSSLMODE=disable` environment variable. Since the environment variables for PostgreSQL are already defined in the `docker-compose.yml` file, you can add `PGSSLMODE` in the `environment` section of the **Outline** service, not in the PostgreSQL service.

Here’s an example of how to add the `PGSSLMODE` variable to your Outline service in your `docker-compose.yml`:

### Example (Adding to Outline Service)
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
    environment:
      PGSSLMODE: disable  # Add this line to disable SSL for PostgreSQL
```

### Where to Add in Your `docker-compose.yml`

You would add this `PGSSLMODE` variable under the `environment` section for the **Outline** service. If you have a separate environment file (e.g., `.env` or `docker.env`), you can also add this variable there.

### Steps:
1. Add `PGSSLMODE: disable` under the `environment` block for the **Outline** service (not PostgreSQL).
2. Save the changes to your `docker-compose.yml` file.
3. Restart the services:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

This should prevent the SSL connection error and allow Outline to connect to the PostgreSQL database without requiring SSL.