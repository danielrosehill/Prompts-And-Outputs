---
title: "Is it okay to have two Proxmox hosts on the LAN"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I'm now running two Proxmox hosts on my local network. Is this a problem? Any way to keep them separate? Could I back up on the VMs on the smaller host onto the bigger one.. or use them together in any other way?

# Output

Running **two Proxmox hosts on your local network** is not inherently a problem, but there are some considerations for keeping them distinct and possibly using them together to improve flexibility and resilience. Below are suggestions on how to **keep them separate**, **backup VMs**, and **utilize them together** effectively:

### Keeping the Proxmox Hosts Separate
To avoid conflicts or confusion, there are a few practical steps you can take:

1. **Assign Unique Hostnames**:
   - Make sure that each Proxmox host has a unique hostname.
   - You can assign names like `proxmox-big` and `proxmox-small` to easily differentiate them.

2. **Unique IP Addresses**:
   - Ensure that each Proxmox host is assigned a **unique static IP** on your network, which will make accessing them more straightforward. For example:
     - `proxmox-big`: `192.168.1.11`
     - `proxmox-small`: `192.168.1.12`

3. **Separate Management Access**:
   - Use a **server homepage/dashboard** like **Dashy** or **HomelabOS** to provide easy links to the management interfaces of each Proxmox host. This way, you can easily navigate between the two from a single interface.

### Using the Proxmox Hosts Together
There are several ways to use the Proxmox hosts together to maximize their value, from **VM backups** to **shared workloads**:

#### 1. Backup VMs on One Host to the Other
Backing up VMs from the smaller host to the larger host is a good strategy to ensure redundancy and prevent data loss. Here's how you can do it:

- **Proxmox Backup Server (PBS)**:
  - Install **Proxmox Backup Server** on the **larger host** to create a centralized backup point.
  - On the smaller host, configure the backup to store snapshots on the larger host.
  - This can be done directly through the Proxmox web interface:
    1. Set up a **storage location** on the larger host.
    2. Configure the **smaller Proxmox** node to use this storage as a target for backups.

- **NFS/SMB Storage**:
  - Set up **NFS** or **SMB** storage on the larger host.
  - Share this storage across the network and mount it on the smaller Proxmox host as backup storage.
  - This allows you to use **shared storage** as the backup target for VMs running on the smaller host.

#### 2. Create a Proxmox Cluster
Another option is to create a **Proxmox Cluster**, which allows both hosts to work together:

- **Proxmox Cluster**:
  - You can combine both Proxmox nodes into a single cluster, allowing you to manage both hosts from a single web interface.
  - **Benefits**:
    - Centralized management of both hosts.
    - Ability to **migrate VMs** between nodes seamlessly.
    - Shared resources and centralized backup management.
  - **Considerations**:
    - Clustering requires a stable network, as the nodes will constantly communicate with each other.
    - If both nodes are running on the same local network, clustering them can provide better management and flexibility for VM operations.

- **HA (High Availability)**:
  - If both hosts are in a cluster, you can also enable **high availability** (HA) for VMs, which means that if one host fails, the VMs can automatically migrate to the other host.
  - **Note**: HA requires shared storage and quorum to function effectively, and you should have a minimum of three nodes or an external quorum device to avoid split-brain scenarios.

#### 3. Shared Storage for Migrating VMs
- **Shared Storage Setup**:
  - Configure **shared storage** accessible by both hosts. This could be done using **NFS** or a **SAN**. Shared storage is important for **live migration** of VMs without downtime.
- **Use Cases**:
  - If you need to perform maintenance on one of the hosts, you can **migrate VMs** to the other host to keep services running.
  - Shared storage will also enable you to balance the workloads more easily between the two Proxmox servers.

### Recommended Strategy
1. **Backup Using Proxmox Backup Server**:
   - Use the **larger Proxmox host** as a central backup server for the VMs running on the smaller host.
   - This ensures that data from the smaller node is safely stored and can be restored quickly if necessary.

2. **Create a Cluster for Unified Management**:
   - If managing two separate nodes becomes cumbersome, consider **clustering** them for a more seamless experience.
   - This also opens up the ability to **migrate workloads** and makes management much easier, as you only need to log in to one interface.

3. **Utilize Shared Storage**:
   - To enhance migration capabilities, consider configuring **shared storage** accessible to both Proxmox hosts.
   - This helps in balancing the load between nodes and facilitates live migrations.

### Summary
- **Keep Hosts Separate**: Use unique hostnames and IPs, and a central dashboard to keep access simple.
- **Backup VMs**: Use **Proxmox Backup Server** or shared NFS storage to back up VMs from the smaller host to the larger one.
- **Cluster for Efficiency**: Consider clustering both Proxmox hosts for unified management, easier migrations, and potential high availability.
- **Shared Storage**: Set up shared storage for migrations and better load balancing between the hosts.

This approach will help you leverage both Proxmox hosts effectively and ensure redundancy, reliability, and efficient management. Let me know if you need more guidance on any of these steps!