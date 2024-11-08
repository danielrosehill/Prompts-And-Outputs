---
title: "How to install Anaconda on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! Setting up **Anaconda** on **Fedora** is a straightforward process that involves downloading the installer and running a script. Below, I'll provide a complete step-by-step guide to help you install Anaconda on your Fedora system.

### **Step 1: Download the Anaconda Installer**
First, you need to download the **Anaconda installer** for Linux.

- You can download it from the [Anaconda official download page](https://www.anaconda.com/products/distribution), or you can directly download it using the command line.

To download directly using the command line:

1. Open your terminal and use `wget` to download the installer:

   ```sh
   wget https://repo.anaconda.com/archive/Anaconda3-latest-Linux-x86_64.sh
   ```

This command downloads the **latest version** of Anaconda for Linux.

### **Step 2: Verify the Installer (Optional)**
It's always a good idea to verify the integrity of the downloaded file by checking its SHA-256 checksum. This ensures that the download was successful and has not been corrupted.

1. **Generate the SHA-256 Checksum**:

   ```sh
   sha256sum Anaconda3-latest-Linux-x86_64.sh
   ```

2. Compare the output hash with the one listed on the [Anaconda distribution page](https://www.anaconda.com/products/distribution#download-section). If they match, your installer is verified.

### **Step 3: Run the Installer**
Next, you need to run the installer script to install Anaconda on your system.

1. **Make the Installer Executable**:

   ```sh
   chmod +x Anaconda3-latest-Linux-x86_64.sh
   ```

2. **Run the Installer**:

   ```sh
   ./Anaconda3-latest-Linux-x86_64.sh
   ```

3. **Follow the Prompts**:
   - You will be prompted to review the **license agreement**. Press **Enter** to scroll through and type `yes` to accept.
   - When prompted for the **installation location**, it's recommended to use the **default location** (`~/anaconda3`). This keeps your installation organized and ensures easier updates.
   
### **Step 4: Initialize Anaconda**
Once the installation completes, the installer will ask if you wish to initialize Anaconda. This step is crucial because it ensures that Anaconda is added to your system's PATH, making it easier to use.

- When asked to **initialize Anaconda3**, type `yes`.

This process modifies your shell’s initialization script (`.bashrc` or `.zshrc`) to include the Anaconda path so that the `conda` command is always available.

### **Step 5: Activate Changes**
To make sure the changes take effect, you need to either **restart your terminal** or run the following command:

```sh
source ~/.bashrc
```

Alternatively, you can run:

```sh
conda init
```

This ensures that Anaconda is properly initialized whenever you start a new terminal session.

### **Step 6: Verify Installation**
To verify that Anaconda is installed correctly, you can run:

```sh
conda --version
```

This command should return the current version of Conda, indicating that the installation was successful.

### **Step 7: Update Anaconda**
After installation, it's a good practice to update Anaconda to make sure you have the latest versions of packages and bug fixes:

```sh
conda update --all
```

This will update Conda and all packages that are installed.

### **Step 8: Test the Installation**
Now, let’s test the installation and create a simple **Conda environment**:

1. **Create a New Environment**:
   - For example, create an environment named `test_env` with Python 3.9:

   ```sh
   conda create --name test_env python=3.9
   ```

2. **Activate the Environment**:

   ```sh
   conda activate test_env
   ```

   You should see the terminal prompt change to indicate that you’re now in the `test_env` environment.

3. **Deactivate the Environment**:

   ```sh
   conda deactivate
   ```

### **Using Anaconda Navigator (Optional)**
Anaconda Navigator is a GUI that comes with Anaconda and allows you to manage environments and packages without needing to use the command line. To launch it:

```sh
anaconda-navigator
```

This will open a graphical interface where you can:
- **Create and manage environments**.
- **Install packages** without using the terminal.
- **Launch tools** like Jupyter Notebook, JupyterLab, Spyder, etc.

### **Setting Up Shortcut Commands (Optional)**
If you find the command to activate Conda too long, you can create an alias for it:

1. Open your `.bashrc` or `.zshrc` file in an editor:

   ```sh
   nano ~/.bashrc
   ```

2. Add an alias at the bottom:

   ```sh
   alias conda_activate='source ~/anaconda3/bin/activate'
   ```

3. Save and reload `.bashrc`:

   ```sh
   source ~/.bashrc
   ```

Now, you can use `conda_activate` to quickly activate your Anaconda environment.

### **Tips for Managing Anaconda on Fedora**:
- **Updating Anaconda Regularly**: You should update regularly to keep everything running smoothly.
  ```sh
  conda update conda
  conda update anaconda
  ```
- **Disk Space Management**: Anaconda takes up a significant amount of space (3-5 GB). To keep disk usage under control:
  - **Clean package cache**: You can clear Conda’s cache to free up space.
    ```sh
    conda clean --all
    ```

### **Uninstalling Anaconda (If Needed)**
If at some point you need to **uninstall Anaconda**, you can follow these steps:

1. **Remove the Installation Directory**:
   ```sh
   rm -rf ~/anaconda3
   ```

2. **Remove Conda Initialization from Shell**:
   Edit your `.bashrc` or `.zshrc` file and remove the lines added by Anaconda (usually referring to initialization).

3. **Reload the Shell**:
   ```sh
   source ~/.bashrc
   ```

### **Summary of Steps to Install Anaconda on Fedora**:
1. **Download the Installer**: Use `wget` or visit the Anaconda website.
2. **Run the Installer**: Run the `.sh` script to start the installation.
3. **Initialize Anaconda**: Ensure it’s added to your PATH by allowing initialization.
4. **Activate and Verify**: Source `.bashrc` or run `conda init` to activate Anaconda.
5. **Update and Test**: Update Anaconda and create a test environment to verify everything works.

With these steps, you should have **Anaconda** installed on your Fedora system, ready to manage environments and packages for data science and development work. Let me know if you need more details or run into any issues during setup!