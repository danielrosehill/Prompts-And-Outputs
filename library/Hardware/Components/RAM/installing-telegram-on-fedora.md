---
title: "Installing Telegram on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The easiest way to install **Telegram** on **Fedora** is to use one of the following methods:

### **Method 1: Install via Flatpak (Recommended)**
Flatpak is a universal packaging system, and Telegram is officially available through it.

1. **Install Flatpak** (if it’s not already installed):
   ```bash
   sudo dnf install flatpak
   ```
   
2. **Add Flathub Repository** (if not already added):
   ```bash
   sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **Install Telegram via Flatpak**:
   ```bash
   flatpak install flathub org.telegram.desktop
   ```

4. **Run Telegram**:
   After installation, you can run Telegram via:
   ```bash
   flatpak run org.telegram.desktop
   ```
   
   Or search for **"Telegram"** in your application launcher.

**Pros**:
- Flatpak keeps **Telegram Desktop** up-to-date automatically.
- Flatpak works across multiple distributions, so you get the latest version.

### **Method 2: Install via RPM (Fedora Repository)**
Telegram is also available directly from Fedora’s official repository.

1. **Install Telegram Desktop using DNF**:
   ```bash
   sudo dnf install telegram-desktop
   ```

**Pros**:
- Quick installation using Fedora’s package manager.
- It will receive updates through the system updates.

**Cons**:
- Sometimes, the version available in Fedora repositories might not be the very latest.

### **Method 3: Install via Snap**
Another option is to use **Snap**, which is similar to Flatpak.

1. **Install Snap**:
   ```bash
   sudo dnf install snapd
   ```

2. **Enable Snap**:
   Create a symbolic link to enable classic snap support:
   ```bash
   sudo ln -s /var/lib/snapd/snap /snap
   ```

3. **Install Telegram via Snap**:
   ```bash
   sudo snap install telegram-desktop
   ```

**Pros**:
- Snap packages are easy to install and update.

**Cons**:
- Snap tends to use more system resources compared to native packages or Flatpak.

### **Method 4: Install via Binary (Manual Installation)**
You can also download Telegram directly from the official website and run it as a portable app.

1. **Download Telegram**:
   Visit [Telegram’s official download page](https://telegram.org/dl/desktop/linux) and download the **tar.xz** file for Linux.

2. **Extract the Archive**:
   ```bash
   tar -xvf tsetup*.tar.xz
   ```

3. **Run Telegram**:
   Navigate to the extracted folder and run the executable:
   ```bash
   cd Telegram
   ./Telegram
   ```

**Pros**:
- You get the latest version directly from Telegram.

**Cons**:
- Updates need to be done manually.
  
### **Recommended Approach**
The **Flatpak method** is generally the **easiest and most reliable** way to install Telegram on Fedora because it provides automatic updates and ensures you have the latest version directly from **Flathub**.

If you prefer not to use Flatpak, the **dnf method** is also quite straightforward and integrates well with the system package manager.