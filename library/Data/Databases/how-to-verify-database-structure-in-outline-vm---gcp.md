---
title: "How to verify database structure in Outline VM - GCP"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary:** You are asking for a document that describes how to check if the tables are working in the Outline VM, starting from connecting to the Google VM and then using PostgreSQL commands inside a Docker container.

---

# Checking Tables in PostgreSQL on Outline VM

This document provides step-by-step instructions to check the tables in the PostgreSQL database running on the Outline VM, including connecting to the VM, accessing the Docker container, and verifying the database tables.

### 1. Connect to the Google VM via Google Cloud Authentication

1. Open a terminal on your local machine.
2. Use the following command to connect to the Google VM:
   ```bash
   gcloud compute ssh <vm-instance-name> --zone <zone>
   ```
   - Replace `<vm-instance-name>` with the name of your Outline VM.
   - Replace `<zone>` with the zone where your VM is hosted (e.g., `us-central1-a`).

### 2. Access the PostgreSQL Docker Container

1. Once connected to the VM, enter the PostgreSQL container by running:
   ```bash
   docker exec -it docker_postgres_1 /bin/bash
   ```
   - `docker_postgres_1` is the name of the PostgreSQL container. Adjust this name if your container has a different identifier.

### 3. Enter the PostgreSQL Database

1. Inside the PostgreSQL container, use the following command to access the database:
   ```bash
   psql -h localhost -p 5432 -U outline -d outline
   ```
   - **`-h localhost`**: Connects to the database on the local host.
   - **`-p 5432`**: Specifies the default PostgreSQL port.
   - **`-U outline`**: Connects as the `outline` user.
   - **`-d outline`**: Connects to the `outline` database.

2. You should now see the `psql` prompt, indicating you have connected to the database successfully.

### 4. Verify the Database Tables

1. At the `psql` prompt, run the following command to list all tables:
   ```sql
   \dt
   ```
   - This command displays a list of all tables in the current database.
   - Verify that the expected tables are present and accessible.

2. If you want more detailed information about a specific table (e.g., `users`), you can use:
   ```sql
   \d users
   ```

### Example Commands Flow:

1. **Connect to VM**:
   ```bash
   gcloud compute ssh outline-vm --zone us-central1-a
   ```

2. **Access PostgreSQL Container**:
   ```bash
   docker exec -it docker_postgres_1 /bin/bash
   ```

3. **Enter Database**:
   ```bash
   psql -h localhost -p 5432 -U outline -d outline
   ```

4. **List Tables**:
   ```sql
   \dt
   ```

### Notes:
- Make sure the PostgreSQL container (`docker_postgres_1`) is running. You can check this with:
  ```bash
  docker ps
  ```
- If you encounter any permission or authentication issues, ensure the credentials (`-U outline`) and database names (`-d outline`) are correct and match your configuration.

This procedure allows you to confirm that the tables in the Outline database are working and accessible, ensuring smooth operation and troubleshooting as needed.

--- 

This guide should help you connect to the Outline VM, access the PostgreSQL container, and verify that the database tables are functioning correctly.