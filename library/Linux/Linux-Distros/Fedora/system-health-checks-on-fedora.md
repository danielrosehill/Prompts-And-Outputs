---
title: "System health checks on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Great. Is there a diagnostics tool that can do deep system inspection for my Fedora computer? A GUI to make sure that everything is running properly

# Output

Based on the search results and your query, there are a few GUI-based diagnostic tools available for Fedora that can perform deep system inspection:

1. Hardinfo2:
   - A comprehensive system information and benchmark tool
   - Provides detailed hardware and software information
   - Offers benchmarking capabilities
   - Installation: `sudo dnf install hardinfo2`
   - Usage: Run `hardinfo2` from the terminal or find it in your applications menu

2. GSmartControl:
   - Specifically for checking the health of hard drives and SSDs
   - Uses SMART technology to diagnose storage device issues
   - Provides detailed information about disk health, temperature, and potential problems
   - Installation: `sudo dnf install gsmartcontrol`

3. GNOME System Monitor:
   - Pre-installed on Fedora Workstation with GNOME
   - Offers real-time monitoring of system resources
   - Provides information on running processes, CPU usage, memory usage, and disk activity

4. Cockpit:
   - A web-based system administration and monitoring tool
   - Offers a comprehensive view of system health and performance
   - Can be accessed remotely through a web browser
   - Installation: `sudo dnf install cockpit`
   - Enable and start: 
     ```
     sudo systemctl enable --now cockpit.socket
     ```
   - Access: Open a web browser and go to https://localhost:9090

5. KInfoCenter (for KDE environments):
   - Provides detailed system information
   - Offers a clean interface with categorized panels
   - Installation (if not already present): `sudo dnf install kinfocenter`

These tools offer various levels of system inspection and diagnostics. Cockpit and Hardinfo2 are particularly comprehensive, providing deep insights into system health and performance. GSmartControl is excellent for focusing on storage device health, while GNOME System Monitor and KInfoCenter offer quick overviews of system status.

For the most comprehensive system check, you might want to use a combination of these tools. Start with Hardinfo2 or Cockpit for a broad overview, use GSmartControl to check your drives' health, and keep GNOME System Monitor or KInfoCenter open for real-time monitoring.
 