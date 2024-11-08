---
title: "Setting a custom DNS server for a network on an Android"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To **manually set the DNS server** on an **Android device** such that it only uses your **Pi-hole** when connected to your **home network**, you have a couple of options: configuring it specifically for your home Wi-Fi connection or using an app to handle it automatically. Here’s a detailed explanation of how to do each:

### **Option 1: Configure DNS for Home Wi-Fi Network Manually**
This method involves manually specifying the DNS server in your **Wi-Fi settings**. The DNS server settings will only apply when connected to that particular network, meaning you can use **Pi-hole** at home and other DNS servers elsewhere.

#### **Step-by-Step Guide**:
1. **Open Settings**:
   - Go to **Settings** on your **Android device**.

2. **Network & Internet**:
   - Tap on **“Network & Internet”** (or it might be called **“Connections”** or **“Wi-Fi & Network”** depending on your device).

3. **Select Your Home Wi-Fi Network**:
   - Tap on **Wi-Fi**, then find and **long-press** or **tap the gear icon** next to your **home Wi-Fi network** (the one you use at home).
   - Select **“Modify network”** or **“Advanced settings”**.

4. **Change IP Settings to Static**:
   - Scroll down to find **IP settings**.
   - By default, it is set to **“DHCP”**. Change this to **“Static”**. This will allow you to manually configure the network settings.

5. **Enter IP Configuration**:
   - **IP Address**: You’ll need to manually enter an **IP address** for your device that is within the range of your network (e.g., **`192.168.1.150`**).
   - **Gateway**: Set this to the **IP address of your router** (e.g., **`192.168.1.1`**).
   - **DNS 1**: Set **DNS 1** to the **IP address of your Pi-hole** (e.g., **`192.168.1.30`**).
   - **DNS 2**: Set **DNS 2** to another DNS server as a fallback (e.g., **`8.8.8.8`** for **Google DNS** or leave it blank if you want everything to go through Pi-hole).

6. **Save Changes**:
   - Tap **“Save”**. Your **Android device** will now use **Pi-hole** as the DNS server whenever it is connected to this specific Wi-Fi network.

#### **Important Notes**:
- The **Static IP** needs to be within the range of available IP addresses on your network, and it shouldn’t conflict with another device’s IP.
- This method ensures that **only your home network** will use Pi-hole, while other networks will use their default DNS settings.

### **Option 2: Use a DNS Management App (Like Intra or DNSChanger)**
There are also apps that allow you to **manage DNS** on a more **granular basis** or switch DNS settings based on the network. This can simplify configuration and remove the need for manual static IP configuration.

#### **DNS Management Apps**:
- **Intra** (by Jigsaw, part of Google):
  - **Intra** is an app that allows you to set custom DNS servers and **automatically applies** the configuration whenever you connect to a network.
  - You can manually enter your **Pi-hole IP address** to be used as the DNS server when connected to your home Wi-Fi.

- **DNSChanger**:
  - This app allows you to **switch DNS servers** easily.
  - It can be configured to **change the DNS automatically** based on which Wi-Fi network you are connected to.

#### **How to Use These Apps**:
1. **Download the App**:
   - Go to **Google Play Store** and install **Intra** or **DNSChanger**.
  
2. **Set Up Pi-hole DNS**:
   - Open the app and add a new custom DNS configuration using the **Pi-hole IP address** (e.g., **`192.168.1.30`**).
   - Set it to activate **only when connected** to your home Wi-Fi.

3. **Control DNS on a Network Basis**:
   - These apps allow you to set DNS server settings and easily switch them off or on, depending on which network you are using.

### **Option 3: Automate DNS Switching (Using Tasker)**
If you want a more automated solution, you can use **Tasker**, a powerful automation tool, to **automatically switch DNS** based on the Wi-Fi network you’re connected to.

#### **Using Tasker**:
1. **Download Tasker**:
   - Install **Tasker** from the **Google Play Store**.

2. **Create a Task to Change DNS**:
   - Set up a **profile** to detect when you’re connected to your **home Wi-Fi** network.
   - Create a **task** that changes the **DNS settings** or runs a DNS management app (such as **Intra**) when you connect.

3. **Switch DNS Settings Automatically**:
   - Tasker will activate the custom DNS setup whenever you connect to your home network.

### **Summary**
- **Option 1: Manually Configure DNS for Your Home Wi-Fi**:
  - Change the **IP settings** to **static** for your **home Wi-Fi** and set the **Pi-hole IP** as **DNS 1**. This works well if you prefer a manual approach and don’t mind configuring each device.
  
- **Option 2: Use DNS Management Apps (Intra or DNSChanger)**:
  - **Intra** or **DNSChanger** can manage the DNS settings more flexibly, without needing to manually set static IPs. These apps can be configured to apply **Pi-hole** settings only when on the home network.

- **Option 3: Use Tasker for Automation**:
  - Use **Tasker** to automatically enable specific DNS configurations or activate a DNS management app when you connect to your home Wi-Fi.

#### **Recommendation**
If you prefer the simplest solution that **does not require technical networking skills**, I recommend using **Intra** or **DNSChanger**, as they can make switching DNS servers much more convenient. If you want more automation, **Tasker** can be very helpful to fully automate the DNS switch based on your location.

By setting up Pi-hole as the DNS server for your Android device while at home, you can benefit from the ad and tracking blocking it provides, while still enjoying normal DNS resolution on other networks. Let me know if you need more help with any of these steps!