---
title: "Optimising noise levels for current hardware"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To ensure **quiet operation** at the software level, you can apply several strategies that optimize how your hardware runs, reduce unnecessary load, and control fan speeds. Here are some modifications and tools you can use:

### 1. **Fan Speed Control with Software**
   - **Fan curve adjustment**: You can adjust your fan speeds based on temperature using software. This lets you reduce the fan speed during light workloads to keep the system quieter.
     - **For GPU**:
       - Use **AMD Radeon Software** to set a custom fan curve for your GPU. This allows you to specify fan speeds at different temperature levels, reducing unnecessary noise when the GPU is under minimal load.
       - Steps: Open **Radeon Software** > Go to **Performance** > **Tuning** > Enable **Custom Fan Curve**.
     - **For CPU and Case Fans**:
       - **Fan control software** such as **Fancontrol** (a Linux utility) or **SpeedFan** (for Windows) can be used to adjust the speed of your case and CPU fans.
       - On Fedora Linux, you can use the **lm-sensors** package along with **fancontrol**:
         ```bash
         sudo dnf install lm_sensors fancontrol
         sudo sensors-detect
         ```
       - You can create a custom configuration to keep fans at lower speeds when your system is under light load.

### 2. **Enable Power-Saving Modes**
   - **For CPU**: You can reduce CPU performance slightly by enabling power-saving modes, which helps reduce heat and therefore reduces the need for aggressive fan operation.
     - On Linux, use **TLP** or **cpupower** to manage power-saving features.
     - Install TLP:
       ```bash
       sudo dnf install tlp
       sudo systemctl enable tlp
       sudo systemctl start tlp
       ```
     - **TLP** automatically manages CPU power states, reducing the heat and fan noise when the system is idle.
   - **For GPU**: Enable **Power Efficiency** in **AMD Radeon Software**. This ensures that the GPU runs at lower clock speeds when not needed, reducing heat and noise.

### 3. **Limit Maximum Performance of the GPU**
   - You can cap your GPU’s maximum performance (underclocking it slightly) to reduce heat generation. This is particularly useful if you don’t need the full performance of your **Radeon RX 7700 XT** all the time.
   - In **Radeon Software**: Go to **Performance** > **Tuning** and reduce the **Power Limit** or set a lower maximum clock speed for your GPU.

### 4. **Use Silent/Power-Saving Profiles for Less-Intensive Tasks**
   - Many motherboard manufacturers, including MSI, have **BIOS settings** or software profiles that focus on quiet operation by reducing fan speeds and system performance when full power is unnecessary. Check your **BIOS settings** for an option to enable a silent profile.
     - For **MSI motherboards**, enter the BIOS by pressing **DEL** on startup, navigate to the **Hardware Monitor**, and adjust the fan curves or enable quiet fan mode.

### 5. **Undervolt Your CPU and GPU**
   - **Undervolting** is the process of reducing the voltage supplied to your CPU or GPU while maintaining stable operation. This reduces heat output and, as a result, reduces fan noise.
     - For **CPU**: On Fedora, use **cpupower** to adjust your CPU frequencies and voltage.
     - For **GPU**: In **Radeon Software**, you can undervolt the GPU by going to **Performance** > **Tuning** > Enable **Manual Tuning** and reducing the core voltage.

### 6. **Limit Background Processes**
   - Reducing the number of unnecessary background processes can lower the load on your CPU and GPU, reducing heat output and fan noise.
   - On **Fedora**, use **htop** to identify and kill unnecessary background processes:
     ```bash
     sudo dnf install htop
     htop
     ```
   - Disable any background services that are not essential to keep CPU usage minimal.

### 7. **Manage GPU Workload** 
   - You can limit or tune GPU workloads by adjusting the settings for specific applications or using frame rate limiters in games and other GPU-heavy applications. Lowering frame rates can reduce the load on your GPU, which will lower its temperature and the fan noise.

By combining these software-level tweaks, you can significantly reduce the noise your workstation produces, especially under low to moderate workloads. Let me know if you'd like further guidance on any specific software!