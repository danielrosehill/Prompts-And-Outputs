---
title: "Easy ways to install SSL cert on HAOS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


In the **Terminal & SSH add-on** for **Home Assistant OS**, the **`authorized_keys`** section is located in the **configuration settings** for the add-on. Here is how you can find and add your SSH public key:

### **Location of the `authorized_keys` Section**:
1. **Access the Terminal & SSH Add-on**:
   - Open **Home Assistant**.
   - Go to the **Supervisor** tab (or **Settings > Add-ons**, depending on your version).
   - Find the **Terminal & SSH** add-on in the list of installed add-ons and click on it.

2. **Navigate to the Configuration Tab**:
   - After opening the add-on, you should see different tabs, such as **Info**, **Configuration**, and **Logs**.
   - Click on the **Configuration** tab.

3. **Find the `authorized_keys` Section**:
   - In the **Configuration** tab, you will see a **YAML-like text box** where you can configure various settings for the add-on.
   - The default configuration will look something like this:
     ```yaml
     ssh:
       username: root
       password: ''
       authorized_keys: []
       sftp: false
       compatibility_mode: false
     ```
   - The **`authorized_keys`** line is where you need to add your SSH key. It is empty by default (`[]`), but you will need to modify it to include your SSH public key.

4. **Add Your SSH Key**:
   - Replace the empty list (`[]`) with your **SSH public key** in YAML format. It should look like:
     ```yaml
     ssh:
       username: root
       password: ''
       authorized_keys:
         - ssh-rsa xxxxxxxxxxxxxxxxxxxxxMruWE3RNIeAyP/xxxxxxxNv/xxxxxxxVpQz+DdS2VEaxWCm9/gjuIWJuXKzW4z6Kc7lcwgq/ZSCnDiBNQ6YRQKoUUO1W9Q5OlbAw6/yQgxvh57m0/xxxxxxx80hKSVCVuOm2J/tMyvf+xxxxxxxmqiPZsGztj7doJfkTbpRMzxL/xxxxxxxM1qvEOO36k= daniel@danielworkstation
       sftp: false
       compatibility_mode: false
     ```

5. **Save the Configuration**:
   - Once you've pasted your public key into the `authorized_keys` section, click **Save** to apply the changes.

6. **Start or Restart the Add-on**:
   - Go to the **Info** tab of the SSH add-on.
   - If the add-on is already running, click **Restart**. If it’s not running, click **Start**.

After adding your key and restarting the add-on, you should be able to SSH into your Home Assistant instance using the **private key** associated with the public key you added. 

### **Summary**:
- Navigate to **Supervisor** > **Terminal & SSH** add-on > **Configuration**.
- Add your SSH public key under the **`authorized_keys`** section.
- Save the configuration and start or restart the add-on.

Let me know if you need further guidance on any of these steps!