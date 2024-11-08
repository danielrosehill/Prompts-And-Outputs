---
title: "Keeping track of package installations on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

On a modern fedora computer, packages can be installed in many ways: from DNF, flatpak, Brew, appimage ... and probably more. Is there any way to keep track of *all* the packages that you have installed so that you might know how to prune the system if it were required?

# Output

Yes, on a modern Fedora system, it can be challenging to keep track of packages installed through different methods like DNF, Flatpak, Homebrew (Linuxbrew), AppImages, and others. However, there are ways to track packages from these various sources and help with system pruning if needed. Here’s a guide to keeping track of all the packages installed from different package managers.

### **Tracking Packages from Various Sources**

#### **1. DNF (Fedora's Default Package Manager)**
DNF packages are installed from Fedora's official repositories and managed via DNF. To list all installed DNF packages:
```bash
dnf list installed
```

To generate a list of DNF-installed packages and save it to a file:
```bash
dnf list installed > ~/dnf_installed_packages.txt
```

#### **2. Flatpak**
Flatpak is a common method for installing applications in Fedora. To list all installed Flatpak applications:
```bash
flatpak list
```

To save this list to a file:
```bash
flatpak list > ~/flatpak_installed_packages.txt
```

#### **3. Homebrew (Linuxbrew)**
If you have installed packages through Homebrew (or Linuxbrew), you can list all installed packages with:
```bash
brew list
```

To save the list of installed Homebrew packages to a file:
```bash
brew list > ~/brew_installed_packages.txt
```

#### **4. AppImage**
AppImage applications are usually standalone, and they don’t have a centralized package manager like DNF or Flatpak. To keep track of AppImages, you can manually store them in a dedicated directory (e.g., `~/AppImages`). Then, you can list all files in that directory:
```bash
ls ~/AppImages > ~/appimage_installed.txt
```

Alternatively, if you downloaded AppImages into various directories, you could search the filesystem:
```bash
find / -type f -name "*.AppImage" > ~/appimage_installed_packages.txt
```

#### **5. Snap (if used)**
Snap packages can also be used to install software. To list all installed Snap packages:
```bash
snap list
```

To save the Snap package list to a file:
```bash
snap list > ~/snap_installed_packages.txt
```

#### **6. Python Packages (pip)**
If you have installed Python packages via pip, you can list them with:
```bash
pip list
```

To save the list of installed pip packages:
```bash
pip list > ~/pip_installed_packages.txt
```

#### **7. Node.js Packages (npm)**
If you use Node.js and npm, you can list globally installed npm packages:
```bash
npm list -g --depth=0
```

To save this to a file:
```bash
npm list -g --depth=0 > ~/npm_installed_packages.txt
```

### **Combine the Lists into a Single File**
To simplify tracking, you can combine all the lists into one file. For example:
```bash
cat ~/dnf_installed_packages.txt ~/flatpak_installed_packages.txt ~/brew_installed_packages.txt ~/appimage_installed_packages.txt ~/snap_installed_packages.txt ~/pip_installed_packages.txt ~/npm_installed_packages.txt > ~/all_installed_packages.txt
```

### **Automating the Process with a Script**
You can create a script to regularly track all packages across these package managers:

```bash
#!/bin/bash

# Create a folder for the lists
mkdir -p ~/package_lists

# Track DNF packages
dnf list installed > ~/package_lists/dnf_installed_packages.txt

# Track Flatpak packages
flatpak list > ~/package_lists/flatpak_installed_packages.txt

# Track Homebrew packages
brew list > ~/package_lists/brew_installed_packages.txt

# Track AppImages (from ~/AppImages folder)
ls ~/AppImages > ~/package_lists/appimage_installed_packages.txt

# Track Snap packages
snap list > ~/package_lists/snap_installed_packages.txt

# Track pip packages
pip list > ~/package_lists/pip_installed_packages.txt

# Track npm packages
npm list -g --depth=0 > ~/package_lists/npm_installed_packages.txt

# Combine everything into a single file
cat ~/package_lists/*.txt > ~/package_lists/all_installed_packages.txt

echo "All package lists saved to ~/package_lists/"
```

Make the script executable:
```bash
chmod +x track_installed_packages.sh
```

You can run this script periodically to keep track of all installed packages across different package managers.

### **Pruning Unwanted Packages**
Once you have a consolidated list of packages, you can begin pruning by removing unnecessary packages. Here’s how:

- **DNF**: Remove packages with:
  ```bash
  sudo dnf remove <package_name>
  ```

- **Flatpak**: Remove Flatpak apps with:
  ```bash
  flatpak uninstall <package_name>
  ```

- **Homebrew**: Uninstall Homebrew packages with:
  ```bash
  brew uninstall <package_name>
  ```

- **Snap**: Remove Snap packages with:
  ```bash
  sudo snap remove <package_name>
  ```

- **AppImages**: Simply delete the AppImage file to remove the application.

This method ensures you can keep track of everything installed on your system and maintain control over which packages to keep or remove when pruning is needed.