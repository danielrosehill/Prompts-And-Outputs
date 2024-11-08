---
title: "DNS probing tools that would work on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Got it! Since you're on **Fedora**, I'll provide specific commands for installing the tools compatible with your system:

### **1. Sublist3r**
**Sublist3r** is available through **pip**, which should work smoothly on Fedora.

**Installation**:
```bash
sudo dnf install python3-pip -y
pip3 install sublist3r
```

**Usage**:
```bash
sublist3r -d testhomewebsite.com
```

### **2. Amass**
**Amass** is a well-known DNS enumeration tool. You can use **snap** or download it directly from its GitHub page.

**Installation** using **Snap**:
```bash
# First, install snapd if you haven't already
sudo dnf install snapd -y
sudo ln -s /var/lib/snapd/snap /snap

# Then install Amass
sudo snap install amass
```
Or, you can download it from [Amass GitHub Releases](https://github.com/OWASP/Amass/releases) and extract it manually to use.

**Usage**:
```bash
amass enum -d testhomewebsite.com
```

### **3. dnsrecon**
**dnsrecon** is available via **pip**, and you can install it directly on Fedora.

**Installation**:
```bash
pip3 install dnsrecon
```

**Usage**:
```bash
dnsrecon -d testhomewebsite.com
```

### **4. Fierce**
**Fierce** can be installed on Fedora via **pip** as well.

**Installation**:
```bash
pip3 install fierce
```

**Usage**:
```bash
fierce --domain testhomewebsite.com
```

### **5. Dig (Manual DNS Queries)**
**`dig`** is part of the **bind-utils** package, which is available on Fedora.

**Installation**:
```bash
sudo dnf install bind-utils -y
```

**Usage**:
```bash
# To get A records
dig A testhomewebsite.com

# To get MX records
dig MX testhomewebsite.com

# To get TXT records
dig TXT testhomewebsite.com

# To get NS records
dig NS testhomewebsite.com
```

These tools should all work well on your **Fedora** system to help you enumerate DNS entries for **testhomewebsite.com** and analyze the DNS records to see what's publicly visible. Let me know if you need any further assistance with these tools!