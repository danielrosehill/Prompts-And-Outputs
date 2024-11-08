---
title: "Which name do you need to connect to a Docker container"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking which name to use for connecting to containers when you see two names displayed by `docker ps`: the container name (e.g., `docker_postgres_1`) and the image name (e.g., `postgres`).

### Which Name to Use for Connections

1. **Use the Container Name (`docker_postgres_1`)**
   - When connecting to or interacting with a running Docker container (e.g., using `docker exec`, `docker logs`, or `docker stop`), you should use the **container name**, which in your case would be `docker_postgres_1` for the PostgreSQL container.
   - Example:
     ```bash
     docker exec -it docker_postgres_1 psql -U <username> -d <database>
     ```

2. **Image Name (`postgres`) Identifies the Source**
   - The **image name** (`postgres`) represents the Docker image from which the container was created. It is mainly used when pulling images (`docker pull`), creating new containers (`docker run`), or viewing what image a running container is based on.
   - Example:
     ```bash
     docker pull postgres
     docker run --name new_postgres_container -d postgres
     ```

### Summary of Use Cases:
- **For direct interaction with running containers:** Use the **container name** (e.g., `docker_postgres_1`).
- **For managing or pulling images:** Use the **image name** (e.g., `postgres`). 

Make sure to replace placeholders (like `<username>` and `<database>`) with the actual PostgreSQL username and database you want to connect to.