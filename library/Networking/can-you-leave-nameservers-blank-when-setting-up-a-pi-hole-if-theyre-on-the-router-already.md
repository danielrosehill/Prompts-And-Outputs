---
title: "Can you leave nameservers blank when setting up a Pi Hole if they're on the router already"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


No, you **should not leave the upstream DNS server settings blank in Pi-hole**, even if your ISP router already has DNS settings configured. Here’s why:

### **Why Upstream DNS Servers in Pi-hole Must Be Set**
1. **How Pi-hole Works**:
   - **Pi-hole** is a **DNS server** for your LAN that blocks ads and other unwanted domains by filtering DNS queries. However, when Pi-hole doesn’t know the answer to a request (i.e., if the request isn’t cached or blocked), it needs to forward that query to an **upstream DNS server** to get the answer.
   - If you **do not configure an upstream DNS server** in Pi-hole, it won’t have any way to resolve queries that it doesn’t already know. This will lead to **failed DNS lookups**, meaning your devices won’t be able to resolve domain names properly.

2. **Pi-hole’s Role vs. ISP Router DNS**:
   - Your **ISP router’s DNS configuration** only applies to clients that directly use the router as their DNS resolver. 
   - Pi-hole acts as an independent **DNS resolver** for your network, so it needs to have its own list of upstream DNS servers to forward requests to. The router’s DNS settings don’t automatically cascade down to Pi-hole.

### **Configuring Upstream DNS in Pi-hole with ISP DNS**
If you want Pi-hole to still use the DNS servers specified in your ISP router, you can configure **Pi-hole** in such a way that it uses the **ISP’s DNS servers** as its upstream:

1. **Determine the DNS Servers Used by Your ISP Router**:
   - You can log in to your **router’s admin page** (usually accessible through `http://192.168.1.1` or similar) and look for the **DNS settings** under **Internet Settings** or **WAN Settings**.
   - Often, ISPs use their own **DNS servers** or assign well-known public DNS servers like **Google** or **Cloudflare**.

2. **Enter ISP DNS in Pi-hole Configuration**:
   - Go to the **Pi-hole Admin Interface** at `http://<pi-hole-ip>/admin`.
   - Navigate to **Settings** > **DNS**.
   - Under the **Upstream DNS Servers** section, you can enter the **IP addresses** of your **ISP’s DNS servers**.
   - Alternatively, you can select a public DNS server, such as **Google**, **Cloudflare**, or **Quad9**.

### **Should You Use the ISP DNS, or Pick Another Option?**
- **ISP DNS Servers**:
  - Using **ISP-provided DNS servers** might provide a small performance benefit, as they are typically geographically close.
  - However, some ISPs **track** DNS requests or even **filter** the domains that can be accessed. If privacy or censorship is a concern, you may want to avoid using ISP DNS.

- **Public DNS Providers**:
  - You can use public options like **Cloudflare (1.1.1.1)**, **Google DNS (8.8.8.8)**, or **Quad9 (9.9.9.9)** for better privacy and performance.
  - These DNS servers are often **faster** and offer **additional privacy protections** compared to ISP DNS.

### **Summary**
- **Do not leave upstream DNS settings blank** in Pi-hole; it needs an upstream DNS server to forward requests that are not already blocked or cached.
- You can configure Pi-hole to use **ISP DNS servers** by finding the DNS addresses used by your router and adding them to Pi-hole.
- Alternatively, you can use a **public DNS server** like Cloudflare, Google, or Quad9, which might offer better **performance, privacy**, and **security**.

If your goal is **privacy**, it's usually better to use a public DNS service known for protecting users' privacy, such as **Cloudflare** or **Quad9**, rather than relying on your ISP's DNS servers.