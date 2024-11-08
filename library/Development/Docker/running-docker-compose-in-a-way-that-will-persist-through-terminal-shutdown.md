---
title: "Running docker compose in a way that will persist through terminal shutdown"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To run your **Docker Compose** in a way that allows you to close the terminal while keeping the containers running, you should start the containers in **detached mode**. This can be done by adding the `-d` flag when running the `docker-compose up` command.

### Command:
```bash
docker-compose up -d
```

### What This Does:
- **Detached mode** (`-d`) runs the containers in the background, allowing you to close the terminal without stopping the containers.
- Once you run this command, Docker Compose will start the services as specified in your `docker-compose.yml` file and exit the terminal, leaving the services running in the background.

### Steps:
1. **Navigate to the directory** containing your `docker-compose.yml` file.
2. Run the following command:
   ```bash
   docker-compose up -d
   ```
3. After the services start, the terminal will return to the prompt, and you can safely close the terminal without affecting the running services.

### Verifying the Containers:
You can check if your containers are running by using the following command:
```bash
docker ps
```

This will show the list of active Docker containers and their status.