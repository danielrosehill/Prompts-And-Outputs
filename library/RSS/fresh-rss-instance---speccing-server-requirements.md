---
title: "Fresh RSS instance - speccing server requirements"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
What are the minimum server recommendations for running a Fresh RSS instance?

# Output

For running a **FreshRSS** instance, the server requirements are relatively light, as it is designed to be resource-efficient. Here are the **minimum server recommendations**:

### Minimum Server Recommendations:
1. **CPU**:
   - **Single-core CPU** is sufficient, although a dual-core or better is recommended for a smoother experience when handling many feeds.

2. **RAM**:
   - **512 MB of RAM** is enough for small personal instances (up to 100 feeds), but more RAM (1-2 GB) is recommended for handling a larger number of feeds or multiple users.

3. **Storage**:
   - FreshRSS requires very little disk space for the software itself, but the total disk space depends on how many feeds and articles are stored.
   - **1 GB of storage** is sufficient for personal use, but this will vary depending on how long you retain articles and how frequently you fetch updates.

4. **Software Requirements**:
   - **PHP**: Minimum version 7.0 (FreshRSS recommends 7.4 or higher).
   - **Web Server**: Apache or Nginx. Both work fine, though Nginx is more lightweight.
   - **Database**: MySQL/MariaDB or SQLite.

5. **Operating System**:
   - FreshRSS can run on any **Linux distribution**, including Ubuntu, Debian, and Fedora. You can also run it on other OSes like FreeBSD or Docker.

6. **Network**:
   - FreshRSS can be run on a home server, VPS, or cloud server. Ensure you have enough bandwidth, especially if refreshing feeds frequently or hosting for multiple users.

### Example Configurations:
- For a small personal instance (100-200 feeds):
   - **1 vCPU, 512MB-1GB RAM, 10GB storage** would be more than enough.
- For more users or larger setups (1000+ feeds):
   - **1-2 vCPUs, 2GB RAM, 20GB storage** recommended to handle multiple updates efficiently.

### Performance Tuning:
- For better performance with larger databases, consider using **MariaDB** over SQLite, and tune the PHP memory limit as necessary depending on the number of feeds you manage.

### Conclusion:
For most personal and small-scale FreshRSS instances, a **small VPS** (e.g., with **1GB RAM** and **1 vCPU**) or even a home server setup will suffice. If you plan to scale up or support multiple users, **2GB of RAM** and a bit more storage will provide better performance.

