---
title: "Configuring 5200 to print from fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To make sure you can print from your Fedora computer to the HP DeskJet 5200 series, you need to verify a few settings on both your printer and Fedora. Here’s a checklist and configuration guidance for ensuring everything works smoothly:

### 1. **Network Configuration on HP DeskJet 5200**
- **Connected to the Same Network**: Make sure your printer is connected to the same WiFi network as your Fedora computer. This is crucial if you are printing over IPP (Internet Printing Protocol).
- **IP Address**: Ensure your printer has a **static IP address** or a DHCP reservation from your router to prevent the IP from changing, which can disrupt printing.
  - On the printer control panel, go to **Settings > Network Settings** to confirm and set a **Static IP**.
- **Enable Wireless Printing**:
  - Make sure the **wireless feature** is enabled, especially if you are using WiFi to connect.
  - Look for an option like **Wireless Direct** or **WiFi Direct** if you need the printer to connect directly to devices without a router.

### 2. **Protocol Settings**
- **IPP (Internet Printing Protocol)**: Ensure that **IPP** is enabled on the printer. Most modern HP printers come with this enabled by default.
- **mDNS (Multicast DNS)**: Also called **Bonjour**, this service helps Fedora and other computers discover the printer on the network. Make sure **mDNS/Bonjour** is enabled in the network settings of the printer.

### 3. **Installing the Printer on Fedora**
To properly set up the printer on Fedora, you should use either a **driverless configuration** or **HPLIP**, the official HP Linux driver package. Here’s how to proceed:

#### **Option 1: Using HPLIP (Recommended for Better Control)**
HP Linux Imaging and Printing (HPLIP) is the official HP solution for Linux that provides full-feature support, including photo printing, checking ink levels, and managing printing preferences.

1. **Install HPLIP**:
   - You can install HPLIP directly from Fedora's repositories:
     ```bash
     sudo dnf install hplip hplip-gui
     ```
   - After installation, you can use the **HP Device Manager** (`hplip-gui`) to set up the printer.

2. **Add the Printer**:
   - Run the **HP Device Manager** GUI by executing:
     ```bash
     hp-setup
     ```
   - Follow the prompts to add the printer. HPLIP will search for available printers on the network and automatically configure the correct drivers.

3. **Printer Verification**:
   - Once installed, print a **test page** from the HP Device Manager to verify that the printer is correctly configured.

#### **Option 2: Adding a Driverless Printer (IPP)**
If you do not want to use HPLIP, you can add the printer using the built-in Fedora printer configuration utility with **IPP**:

1. **Open Printer Settings**:
   - Go to **Settings > Printers** in GNOME or open a terminal and type:
     ```bash
     system-config-printer
     ```

2. **Add Printer**:
   - Click **Add** and select the HP DeskJet 5200 series from the list.
   - **Select Connection**: Use **IPP** (`Internet Printing Protocol`) or **driverless (exact-cmd)`.
   - Make sure you choose the correct **network IP address** of the printer to ensure reliable communication.

3. **Test the Printer**:
   - Print a **test page** to verify that the printer works correctly.
   - Check the paper size is set to **A4** or another appropriate size for your needs.

### 4. **Firewall Configuration on Fedora**
If you have a firewall running on Fedora, make sure that it allows connections to your printer:

1. **Allow IPP**:
   - Ensure that **IPP (port 631)** is open in your firewall. You can add a rule using `firewalld`:
     ```bash
     sudo firewall-cmd --permanent --add-service=ipp
     sudo firewall-cmd --reload
     ```
   This ensures that print jobs over IPP can be sent without being blocked.

### 5. **Printer Services and Options**
- **Printer Sharing**: If your Fedora computer and printer are on the same network, printer sharing must be enabled on the printer. In the printer settings, look for **Sharing Settings** and enable the option to **Allow Printing from Other Devices**.
- **Print Quality and Paper Size**: Set the default **print quality** to suit your needs (e.g., photo or draft). Also, ensure the **paper size** is set to A4 if that’s the paper type you’re using.

### 6. **Optional: Update Printer Firmware**
Occasionally, outdated firmware can cause connectivity or functionality issues. Visit the **HP Support website** to check for firmware updates for the HP DeskJet 5200 and update it if needed. This can help improve compatibility and reliability when connecting with various devices, including Fedora.

### Summary:
1. **Printer Configuration**:
   - Connect to the same network.
   - Set a static IP address.
   - Enable **IPP** and **mDNS**.

2. **Fedora Setup**:
   - Install **HPLIP** (recommended) or set up using **IPP driverless**.
   - Add the printer via **Settings > Printers** or use **HP Device Manager**.

3. **Firewall**: Ensure IPP (port 631) is allowed through Fedora’s firewall.

4. **Test**: Print a test page to ensure everything works.

Using **HPLIP** is the best approach if you need better control over printer features. However, **driverless IPP** can also work well for straightforward printing tasks. Let me know if you have any questions or if you need further assistance!