---
title: "Unique LAN IPs for Docker containers running on Proxmox host"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is possible to configure Docker containers to get unique LAN IPs on an Ubuntu server running as a VM in Proxmox. You can achieve this by using **macvlan** networking or a **bridge network** configuration. Here’s how to do both:

### Option 1: Using macvlan Networking

**Macvlan** allows you to assign a unique IP address from your LAN directly to each Docker container, effectively treating each container as a separate device on your network.

#### Steps to Set Up macvlan:

1. **Create a macvlan Network**:
   - First, determine the name of the network interface on your Proxmox VM that connects to the LAN (usually something like `eth0` or `ens18`).
   - Run the following command to create a macvlan network in Docker:
     ```bash
     docker network create -d macvlan \
     --subnet=192.168.1.0/24 \  # Replace with your LAN subnet
     --gateway=192.168.1.1 \    # Replace with your LAN gateway
     -o parent=eth0 my_macvlan
     ```
   - Replace `eth0` with your actual interface name and adjust the subnet and gateway as necessary.

2. **Run Containers with the macvlan Network**:
   - When running your containers, you can specify the macvlan network and assign a static IP:
     ```bash
     docker run -d --name my_container \
     --network my_macvlan \
     --ip=192.168.1.100 \  # Replace with a unique IP for this container
     your_image_name
     ```

3. **Check Connectivity**:
   - Verify that your containers are reachable via their assigned IPs from other devices on the LAN.

### Option 2: Using a Bridge Network with DHCP

If you prefer not to use macvlan, you can also set up a bridge network where you configure a DHCP server to assign IPs to Docker containers.

#### Steps to Set Up a Bridge Network:

1. **Create a Custom Bridge Network**:
   - Create a bridge network in Docker:
     ```bash
     docker network create --driver bridge my_bridge
     ```

2. **Run Containers**:
   - Start your containers using the created bridge network:
     ```bash
     docker run -d --name my_container \
     --network my_bridge \
     your_image_name
     ```

3. **Configure DHCP**:
   - If you have a DHCP server on your LAN (like your router), configure it to assign specific IP addresses based on MAC addresses of the containers.
   - You can find the MAC addresses of the containers by inspecting them:
     ```bash
     docker inspect my_container | grep MacAddress
     ```

### Considerations

- **Network Conflicts**: Ensure that the IPs assigned to containers don’t conflict with existing devices on your network.
- **Performance**: macvlan is generally preferred for performance and simplicity in a LAN environment.
- **Container Restart**: Remember that if a container is restarted without a static IP defined, it may lose its assigned IP unless managed by a DHCP server.

### Conclusion

Both methods allow you to assign unique LAN IPs to your Docker containers. If you want direct access and simplicity, **macvlan** is often the best choice. However, using a bridge network with a DHCP server can also work, especially in more complex setups where you have additional network requirements.