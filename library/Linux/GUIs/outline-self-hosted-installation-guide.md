---
title: "Outline self-hosted installation guide"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Download: 25-Oct-24

Docker is the recommended way to run Outline – updated Docker images based on Alpine Linux are available on a monthly release cadence and are tested by the maintaining team.
#  Configuration

Using [this sample file](https://github.com/outline/outline/blob/main/.env.sample) as a reference create a `docker.env` file to contain the environment variables for your installation.

Be sure to include **all** of the values in the `Required` section and at least one [authentication provider](https://docs.getoutline.com/s/hosting/doc/authentication-7ViKRmRY5o) from the `Optional` section to have the application successfully start.

# Docker Compose

It is recommended to use Docker Compose to manage the various docker containers, if your Postgres, Redis, and storage are running in the cloud then you may skip this step and run the single Outline docker container directly.

  

1. Install [Docker Compose](https://docs.docker.com/compose/install/)
    
2. Create a `docker-compose.yml` file, an example configuration with all dependencies dockerized and environment variables kept in `docker.env` is as follows. If you are installing the enterprise edition the image name should be replaced with `outlinewiki/outline-enterprise`.  
      
    **Note:** It is recommended to pin the version of all images rather than relying on the latest tag so that you can remain in control of upgrades, e.g. `image: outlinewiki/outline:0.72.0` , `image: postgres:16`
    

  

```
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

  redis:
    image: redis
    env_file: ./docker.env
    ports:
      - "6379:6379"
    volumes:
      - ./redis.conf:/redis.conf
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
      - database-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-d", "outline", "-U", "user"]
      interval: 30s
      timeout: 20s
      retries: 3
    environment:
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: 'pass'
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
      - https-portal-data:/var/lib/https-portal
    healthcheck:
      test: ["CMD", "service", "nginx", "status"]
      interval: 30s
      timeout: 20s
      retries: 3
    environment:
      DOMAINS: 'docs.mycompany.com -> http://outline:3000'
      STAGE: 'production'
      WEBSOCKET: 'true'
      CLIENT_MAX_BODY_SIZE: '0'

volumes:
  https-portal-data:
  storage-data:
  database-data:
```

  

# Database

Create the database with the following command:

```
docker compose run --rm outline yarn db:create --env=production-ssl-disabled
```

  

Migrate the new database to add needed tables, indexes, etc:

```
docker compose run --rm outline yarn db:migrate --env=production-ssl-disabled
```

  

If you setup your Redis or Postgres outside the docker container you could use additional flag `--net="host"` for docker. In this case you will be able to use `localhost` as host in your `docker.env` file for Redis and Postgres.

# Running Docker Compose

Make sure you are in the same directory as `docker-compose.yml` and start Outline:

```
docker compose up -d
```

  

Check the output carefully for errors such as connecting to your database or redis instance. To make your installation accessible to the outside world look at the [SSL configuration](https://docs.getoutline.com/s/hosting/doc/ssl-pzk7WO8d1n) documentation.

# How To Update Outline

To update Outline, follow these steps:

1. [Backup the database](https://docs.getoutline.com/s/hosting/doc/backups-KZtPOADCHG)
    
2. Update to the latest image
    
    1. Use `docker pull docker.getoutline.com/outlinewiki/outline:latest` to download the image or
        
    2. If you are using docker-compose with a fixed version number then you will need to update the `docker-compose.yml` file to point to the latest version.
        
3. Run the container
    

## #Migrations

Note that as of v0.69.0 database migrations are ran automatically when changing image.

Migrations are ran automatically when the container starts up. If you want to prevent this behavior and run migrations manually pass the `--no-migrate` flag.


