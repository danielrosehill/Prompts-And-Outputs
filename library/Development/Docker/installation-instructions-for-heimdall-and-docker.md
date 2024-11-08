---
title: "Installation instructions for Heimdall and Docker"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You are requesting instructions for setting up Heimdall using Docker Compose instead of running Docker commands manually.

---

Here's how to set up Heimdall using Docker Compose:

### **Step 1: Prerequisites**
Ensure you have **Docker** and **Docker Compose** installed on your system. If not, you can follow the official installation guides:
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

### **Step 2: Create a Directory for Heimdall**
First, create a directory where you will store the Docker Compose file and configuration:
```bash
mkdir ~/heimdall && cd ~/heimdall
```

### **Step 3: Create a Docker Compose File**
Inside the `~/heimdall` directory, create a `docker-compose.yml` file:
```bash
nano docker-compose.yml
```

Add the following content to the file:
```yaml
version: "3.8"

services:
  heimdall:
    image: ghcr.io/linuxserver/heimdall
    container_name: heimdall
    ports:
      - 8080:80
    volumes:
      - heimdall_data:/config
    restart: unless-stopped

volumes:
  heimdall_data:
```

#### **Explanation:**
- **`image:`** Specifies the Docker image to use.
- **`container_name:`** Names the container "heimdall."
- **`ports:`** Maps port 80 (inside the container) to port 8080 on your host. Change the host port if needed.
- **`volumes:`** Uses a Docker volume (`heimdall_data`) to persist data.
- **`restart:`** Ensures the container restarts automatically unless you stop it manually.

### **Step 4: Deploy Heimdall Using Docker Compose**
Run the following command to start Heimdall:
```bash
docker-compose up -d
```

### **Step 5: Access Heimdall**
Open a web browser and navigate to:
```
http://<your-server-ip>:8080
```
Replace `<your-server-ip>` with the IP address of the server where you installed Heimdall.

### **Step 6: Configure Heimdall**
1. **Add Services:**
   - Click "Add an Application" and fill in details like Name, URL, and Icon.
   - Heimdall can automatically fetch icons, or you can manually upload them.
2. **Customize Layout:**
   - Use the drag-and-drop feature to arrange services as needed.
3. **Enhanced Apps:**
   - For certain services (like Plex or Sonarr), you can enable enhanced app features to get status updates. Configure these by adding relevant API keys.

### **Step 7: Managing Heimdall**
To stop or start Heimdall, use:
```bash
docker-compose stop
docker-compose start
```
To view logs, use:
```bash
docker-compose logs -f
```
To restart Heimdall, use:
```bash
docker-compose restart
```

### **Step 8: Updating Heimdall**
To update Heimdall to the latest version, run:
```bash
docker-compose pull
docker-compose up -d
```
This will pull the latest image and recreate the container without losing your data.

### **Step 9: Backup and Restore (Optional)**
If you want to back up Heimdall’s configuration, you can create a backup of the Docker volume:
```bash
docker run --rm -v heimdall_data:/data -v $(pwd):/backup busybox tar czf /backup/heimdall_backup.tar.gz /data
```
This will create a `heimdall_backup.tar.gz` file in your current directory. To restore, run:
```bash
docker run --rm -v heimdall_data:/data -v $(pwd):/backup busybox tar xzf /backup/heimdall_backup.tar.gz -C /
```

### **Recap**
You should now have Heimdall set up on your server using Docker Compose, allowing easy access and organization of all your local services. You can manage everything through the web UI, add or rearrange service tiles, and keep it updated effortlessly.