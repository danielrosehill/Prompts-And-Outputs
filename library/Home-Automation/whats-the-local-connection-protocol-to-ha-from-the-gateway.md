---
title: "What's the local connection protocol to HA from the Gateway"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


For connecting to **Home Assistant** from the **gateway**, here is the local connection information you would use:

### **Local Connection Details for Home Assistant**:

- **Protocol**: **HTTP** or **HTTPS** (depending on your setup)
- **IP Address**: **`192.168.1.3`** (the IP address for Home Assistant OS VM)
- **Port**: **8123** (Home Assistant's default port)

### **Local URL to Access Home Assistant from the Gateway**:
- **HTTP**: `http://192.168.1.3:8123`
- **HTTPS**: `https://192.168.1.3:8123` (if you have SSL configured)

### **Explanation**:
- The **gateway VM** (at **`192.168.1.20`**) will connect to the **Home Assistant** instance using the **local IP** (**`192.168.1.3`**) on **port 8123**, which is the default port for Home Assistant's web interface.
- The **protocol** can be **HTTP** if you haven't set up SSL certificates. If you've configured **SSL** (using something like **Let's Encrypt**), you'll be able to connect over **HTTPS** for a secure connection. 

If you use the **Cloudflare Tunnel**, you can route requests for **`ha.testhomewebsite.com`** to this internal URL (`http://192.168.1.3:8123`), allowing external access through Cloudflare's edge.