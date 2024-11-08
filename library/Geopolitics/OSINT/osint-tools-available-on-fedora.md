---
title: "OSINT tools available on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use Fedora Linux. Any noteworthy OSINT tools available on this platform?

# Output

Fedora Linux is a great platform for OSINT due to its open-source nature and compatibility with many powerful tools. Here are some noteworthy OSINT tools that work well on Fedora Linux:

### 1. **Maltego**
   - **Function**: Maltego is a comprehensive tool for conducting network analysis and visualization of OSINT data. It helps identify relationships between entities such as people, domains, organizations, and IP addresses.
   - **Availability**: Available via **Flatpak** or by downloading directly from the Maltego website.
   - **Use Case**: Ideal for mapping social networks, cyber investigations, and tracking connections between individuals and organizations.
   - **Website**: [Maltego](https://www.maltego.com)

### 2. **theHarvester**
   - **Function**: A popular tool for gathering OSINT on domains, emails, IPs, and subdomains. It collects data from sources like search engines, PGP key servers, and social networks.
   - **Installation**: Can be installed via **Python pip** or from the Fedora repositories.
   - **Use Case**: Useful for reconnaissance when investigating domains or individuals' publicly available data.
   - **Command**: `sudo dnf install theharvester`

### 3. **Recon-ng**
   - **Function**: A web reconnaissance tool with a modular framework similar to Metasploit. It allows OSINT analysts to gather data about hosts, contacts, domains, and other entities.
   - **Installation**: Available via **Python pip**.
   - **Use Case**: Automates the collection of data from public sources like social media, WHOIS, and more.
   - **Command**: `sudo pip install recon-ng`

### 4. **SpiderFoot**
   - **Function**: SpiderFoot is an OSINT automation tool that performs extensive reconnaissance by scanning data from over 100 sources, including social media, DNS records, IP addresses, and more.
   - **Installation**: Install via **Python pip** or use Docker if you prefer a containerized environment.
   - **Use Case**: Ideal for large-scale investigations where multiple data points need to be correlated automatically.
   - **Website**: [SpiderFoot](https://www.spiderfoot.net)

### 5. **OSINT Framework (Browser-based)**
   - **Function**: A collection of links and tools curated for OSINT investigations, focusing on everything from people searches to domain and IP lookups.
   - **Use Case**: Helps analysts find the right tools for specific OSINT tasks and investigations.
   - **Website**: [OSINT Framework](https://osintframework.com)

### 6. **Sherlock**
   - **Function**: Sherlock is a tool that searches for usernames across multiple social media platforms to track an individual’s online presence.
   - **Installation**: Available via **GitHub** and can be installed with **Python pip**.
   - **Use Case**: Useful for discovering all the platforms where a particular username or alias is being used.
   - **Command**: `git clone https://github.com/sherlock-project/sherlock`

### 7. **ExifTool**
   - **Function**: A metadata extraction tool that analyzes metadata from images, documents, and other files. ExifTool is often used to retrieve GPS coordinates, camera settings, and timestamps from images.
   - **Installation**: Available in Fedora repositories.
   - **Use Case**: Great for analyzing media files to uncover hidden data like geolocation and time details.
   - **Command**: `sudo dnf install perl-Image-ExifTool`

### 8. **Shodan**
   - **Function**: A search engine that allows users to find information on devices connected to the internet. Shodan provides insights into the security of devices and services online.
   - **Installation**: Can be used via web interface or installed as a Python package.
   - **Use Case**: Ideal for tracking exposed devices like routers, servers, and IoT devices.
   - **Website**: [Shodan](https://www.shodan.io)

### 9. **Google Earth Pro**
   - **Function**: A satellite imagery and mapping tool, useful for geographical analysis and historical imagery.
   - **Installation**: Install via **Flatpak** or by downloading the Linux version from the website.
   - **Use Case**: Ideal for OSINT analysts working with geolocation or verifying locations of interest through satellite imagery.
   - **Website**: [Google Earth](https://www.google.com/earth/)

### 10. **WHOIS and DNS Tools**
   - **Function**: Basic network tools for querying WHOIS data and DNS information. These can be used to gather registration details for domains and network infrastructure.
   - **Tools**: `whois`, `dig`, and `nslookup` are typically pre-installed on Fedora or available via the Fedora repository.
   - **Use Case**: Useful for gathering domain ownership information and DNS configurations.
   - **Command**: `sudo dnf install bind-utils` (for `dig` and `nslookup`)

### 11. **Metagoofil**
   - **Function**: A tool for extracting metadata from public documents (PDF, Word, Excel, etc.) found through search engines. It can provide valuable information such as author names, software versions, and more.
   - **Installation**: Available via **GitHub**.
   - **Use Case**: Useful for finding potentially sensitive information embedded in public documents.
   - **Command**: `git clone https://github.com/laramies/metagoofil`

### 12. **FOCA (via Wine)**
   - **Function**: FOCA is a Windows-based tool that extracts metadata from documents to discover information like server details, software versions, and internal structure of organizations.
   - **Installation**: FOCA can be run on Fedora using **Wine**.
   - **Use Case**: Useful for deep metadata extraction from a wide variety of document types.
   - **Website**: [FOCA](https://github.com/ElevenPaths/FOCA)

---

These tools provide a range of capabilities from network reconnaissance to social media investigation and geolocation analysis, all of which are essential for OSINT investigations. Many of these tools are either available natively on Fedora Linux or can be installed through Python or GitHub, making them highly accessible for Fedora users. Let me know if you'd like help setting up or using any of these tools!