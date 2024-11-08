---
title: "Proxmox web UI ports"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Prompt Summary:** You are asking which ports can be used to access the web UI for Proxmox.

---

The Proxmox web UI can be accessed on **port 8006** by default. You can reach it by navigating to:

```
https://<proxmox-server-ip>:8006
```

Make sure to use `https` as the Proxmox web interface requires a secure connection. If needed, you can customize the port by modifying the Proxmox configuration files:

### **Changing the Web UI Port (Optional)**
To change the default port:
1. **Edit the Proxmox web server configuration file:**
   ```bash
   nano /etc/pve/local/pveproxy.cfg
   ```
2. **Add or modify the `port` line:**
   ```bash
   port 8080
   ```
3. **Restart the Proxmox proxy service:**
   ```bash
   systemctl restart pveproxy
   ```

After making this change, the web UI will be accessible on `https://<proxmox-server-ip>:8080` (or whatever port you set).