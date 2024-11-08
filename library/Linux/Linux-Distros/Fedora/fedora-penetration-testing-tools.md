---
title: "Fedora penetration testing tools"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To summarize: you're asking about penetration testing tools that are available for **Fedora Linux**.

Fedora is well-suited for penetration testing, and there are numerous tools you can install to perform comprehensive security assessments on your system or website. Here's a list of commonly used tools that are compatible with Fedora:

### 1. **OWASP ZAP (Zed Attack Proxy)**
   - **Description**: An open-source tool for finding security vulnerabilities in web applications. It's one of the most widely used tools for web app security testing.
   - **Features**: Active and passive scanning, spidering, and fuzzing.
   - **Installation**:
     ```bash
     sudo dnf install zaproxy
     ```

### 2. **Nikto**
   - **Description**: A web server scanner that tests for over 6,700 vulnerabilities, including outdated software, misconfigurations, and dangerous files.
   - **Installation**:
     ```bash
     sudo dnf install nikto
     ```

### 3. **Nmap**
   - **Description**: One of the most popular network mapping and port scanning tools, used to discover devices, open ports, and services on a network.
   - **Installation**:
     ```bash
     sudo dnf install nmap
     ```

   - **Companion Tool**: **Zenmap** (Nmap's GUI frontend) for easier use.
     ```bash
     sudo dnf install zenmap
     ```

### 4. **Metasploit Framework**
   - **Description**: A comprehensive penetration testing framework that allows you to exploit vulnerabilities in systems. It has numerous payloads and exploit modules.
   - **Installation**:
     - Download the installer from the official site: [Metasploit](https://www.metasploit.com/download).
     - Install dependencies:
       ```bash
       sudo dnf install libpcap-devel openssl-devel postgresql-server ruby
       ```

### 5. **Aircrack-ng**
   - **Description**: A suite of tools for auditing wireless networks. It can be used to capture and crack WEP and WPA-PSK keys and monitor Wi-Fi traffic.
   - **Installation**:
     ```bash
     sudo dnf install aircrack-ng
     ```

### 6. **John the Ripper**
   - **Description**: A powerful password-cracking tool that supports a wide range of password types. It’s commonly used for brute-force attacks.
   - **Installation**:
     ```bash
     sudo dnf install john
     ```

### 7. **Hydra**
   - **Description**: A fast and flexible password-cracking tool designed for testing login forms, SSH, FTP, databases, and more via brute-force attacks.
   - **Installation**:
     ```bash
     sudo dnf install hydra
     ```

### 8. **Sqlmap**
   - **Description**: A popular tool for automating the process of detecting and exploiting SQL injection vulnerabilities in web applications.
   - **Installation**:
     ```bash
     sudo dnf install sqlmap
     ```

### 9. **Burp Suite Community Edition**
   - **Description**: An integrated platform for performing security testing of web applications. The community edition includes manual tools for testing vulnerabilities like XSS, CSRF, and SQL injection.
   - **Installation**:
     Download from [PortSwigger's Burp Suite](https://portswigger.net/burp/communitydownload) and follow the installation instructions.

### 10. **The Harvester**
   - **Description**: A tool for gathering open-source intelligence (OSINT), including email addresses, subdomains, and public information about a domain.
   - **Installation**:
     ```bash
     sudo dnf install theharvester
     ```

### 11. **Gobuster**
   - **Description**: A tool used to brute-force URIs, subdomains, and directories on a web server. It’s useful for discovering hidden files and directories.
   - **Installation**:
     ```bash
     sudo dnf install gobuster
     ```

### 12. **Wireshark**
   - **Description**: A network protocol analyzer that allows you to capture and analyze network traffic. It is highly useful for identifying vulnerabilities in network communications.
   - **Installation**:
     ```bash
     sudo dnf install wireshark
     ```

### 13. **OpenVAS**
   - **Description**: An open-source vulnerability scanner that can detect a wide range of security vulnerabilities in servers, network devices, and web applications.
   - **Installation**:
     Install it via the Greenbone Vulnerability Management (GVM) packages:
     ```bash
     sudo dnf install openvas
     ```

### 14. **Lynis**
   - **Description**: A security auditing tool designed for Unix-based systems, including Linux. It performs a security scan of the system to detect vulnerabilities and misconfigurations.
   - **Installation**:
     ```bash
     sudo dnf install lynis
     ```

### 15. **Hashcat**
   - **Description**: A robust password-cracking tool that supports multiple algorithms and parallel execution. It’s one of the fastest password recovery tools available.
   - **Installation**:
     ```bash
     sudo dnf install hashcat
     ```

### 16. **Fierce**
   - **Description**: A DNS reconnaissance tool designed to locate non-contiguous IP space and hostnames against a domain.
   - **Installation**:
     ```bash
     sudo dnf install fierce
     ```

### 17. **Wapiti**
   - **Description**: A web vulnerability scanner that can audit the security of web applications by searching for SQL injection, XSS, and other vulnerabilities.
   - **Installation**:
     ```bash
     sudo dnf install wapiti
     ```

### 18. **SET (Social Engineering Toolkit)**
   - **Description**: A toolkit for conducting social engineering attacks, useful for phishing campaigns, credential harvesting, and penetration testing scenarios.
   - **Installation**:
     Install SET by cloning the repository from GitHub:
     ```bash
     git clone https://github.com/trustedsec/social-engineer-toolkit.git
     cd social-engineer-toolkit
     sudo python setup.py install
     ```

### 19. **Dirb**
   - **Description**: A web content scanner designed to discover hidden files and directories on web servers by brute-forcing URL paths.
   - **Installation**:
     ```bash
     sudo dnf install dirb
     ```

### 20. **Dnsenum**
   - **Description**: A DNS enumeration tool that helps in discovering subdomains, domain information, and DNS records.
   - **Installation**:
     ```bash
     sudo dnf install dnsenum
     ```

---

### General Tips for Fedora Penetration Testing:

- **Use DNF Package Manager**: Fedora uses `dnf` as its package manager, making it easy to install and update pen testing tools from official repositories or third-party repositories.
  
- **Create a Test Environment**: Always test in a safe environment such as a **virtual machine** or on a **staging server** to prevent accidental damage to your production systems.

- **Set Up Virtual Machines (VMs)**: If you're testing exploits, consider using a VM to simulate vulnerable systems. Tools like **VirtualBox** or **KVM** can be used to create these environments.

### Conclusion:
Fedora Linux offers a wide range of penetration testing tools that can help you assess the security of your systems, websites, and networks. From vulnerability scanners (like OWASP ZAP, Nikto) to more advanced frameworks (like Metasploit and Burp Suite), you have plenty of options to conduct comprehensive security assessments on Fedora.

Let me know if you'd like help setting up or using any specific tools!