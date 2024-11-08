---
title: "Can you have LXCs that run Docker"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is **possible** to run **Docker inside LXC containers**, but it requires some additional configuration since LXC containers share the host kernel and Docker has its own process isolation mechanisms. With **Proxmox**, you can configure an **LXC container** to run Docker, but you'll need to adjust some container settings for it to work smoothly.

Here’s a guide on how to set up **Docker inside an LXC container on Proxmox**:

### Steps to Deploy LXCs that Run Docker

#### 1. **Create the LXC Container on Proxmox**
1. In the Proxmox web interface, go to **Create CT** (Create Container) to create a new LXC container.
   - Select a **Debian** or **Ubuntu** template (these work well with Docker).
   - Assign **resources** (CPU, memory, disk space) based on your needs.

#### 2. **Configure the LXC Container for Docker**
To run Docker inside the LXC container, you’ll need to enable a few specific features in the container configuration to allow the necessary privileges for Docker.

1. **Stop the container** if it’s running:
   ```bash
   lxc-stop -n container_name
   ```

2. **Edit the LXC configuration file**:
   - The LXC container configuration file is located at `/etc/pve/lxc/<container_id>.conf`.
   - Add the following lines to allow Docker to run inside the container:

     ```bash
     lxc.apparmor.profile: unconfined
     lxc.cap.drop:
     lxc.cgroup.devices.allow: a
     lxc.mount.auto: proc:rw sys:rw
     features: keyctl=1,nesting=1
     ```

   This configuration:
   - **Disables AppArmor** for the container, which can otherwise interfere with Docker’s operation.
   - **Enables nesting** (`features: keyctl=1,nesting=1`), which allows Docker to run inside the LXC container.
   - Allows Docker access to certain kernel features like cgroups and devices.

3. **Start the container** again:
   ```bash
   lxc-start -n container_name
   ```

#### 3. **Install Docker Inside the LXC Container**
Once the container is configured to run Docker, you can install Docker inside it like you would on any other Linux server.

1. **Enter the container**:
   ```bash
   lxc exec container_name -- /bin/bash
   ```

2. **Install Docker**:
   - First, update the package list:
     ```bash
     sudo apt update
     ```

   - Install Docker dependencies:
     ```bash
     sudo apt install apt-transport-https ca-certificates curl software-properties-common
     ```

   - Add Docker’s GPG key and repository:
     ```bash
     curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
     ```

   - Install Docker:
     ```bash
     sudo apt update
     sudo apt install docker-ce
     ```

3. **Verify Docker Installation**:
   - Once Docker is installed, check if it’s running properly inside the LXC container:
     ```bash
     sudo systemctl status docker
     ```
   - You can also run a test container:
     ```bash
     sudo docker run hello-world
     ```

   If Docker runs successfully, your LXC container is now capable of running Docker containers within it.

#### 4. **Optional: Persistent Storage for Docker Containers**
To persist data for Docker containers, you can mount a directory or volume from the host or attach storage volumes to your LXC container to use for Docker volumes.

1. **Add storage to the LXC container**:
   - In the Proxmox UI, you can add a mount point or additional disk storage that can be used by Docker within the container.

2. **Use the storage for Docker volumes**:
   - Inside the LXC container, you can configure Docker to use the additional storage for its volumes and persistent data.

#### 5. **Expose Docker Services via Cloudflare Tunnel**
Once Docker is running inside the LXC, you can run your applications as Docker containers and expose them to the outside world using your **Cloudflare Tunnel** setup. This will work just as it would for any other service hosted on your Proxmox server.

### Considerations and Caveats:
- **Nested containers**: While running Docker inside LXC is possible, remember that you are essentially nesting containers, which adds some complexity. Most use cases will work fine, but if you run into edge cases (especially related to networking or advanced Docker features), you may need to adjust LXC settings or consider running Docker directly on the host or in a VM.
- **Security**: Running Docker inside an LXC container with privileges (e.g., `lxc.apparmor.profile: unconfined`) might reduce the security isolation of the container, so make sure you understand the risks of relaxing certain security features.
- **Performance**: Running Docker inside an LXC container should perform well, but if you experience performance issues, running Docker directly on Proxmox or within a dedicated VM could offer better isolation and resource allocation.

### Conclusion:
Yes, it is **possible** and straightforward to deploy **LXCs that run Docker** on Proxmox by adjusting the container configuration. This gives you the flexibility of **lightweight containers (LXC)** combined with **Docker’s application portability**. This setup works well for hosting multiple services with Docker inside an LXC on Proxmox, and it’s a good option for efficient resource usage.

Let me know if you need further details or help with configuring your setup!