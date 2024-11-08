---
title: "Installing the self signed cert in HOAS"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, the **`/config/ssl`** directory at the base level is indeed the correct place to store SSL certificates on **Home Assistant OS**. This is a well-known directory for SSL storage, making it easy for Home Assistant to find and use them. Let’s modify the steps to reflect this.

### **Steps to Install the Self-Signed SSL Certificate**

#### **1. Navigate to the SSL Directory**
- **SSH** into your Home Assistant instance.
- Navigate to the **`ssl`** directory:
  ```bash
  cd /config/ssl
  ```
  - This is where SSL certificates should be stored for Home Assistant.

#### **2. Generate the Self-Signed Certificate**
- Use **OpenSSL** to generate the certificate and key:
  ```bash
  openssl req -new -x509 -days 365 -nodes -out fullchain.pem -keyout privkey.pem
  ```
  - **`fullchain.pem`**: This is your self-signed public certificate.
  - **`privkey.pem`**: This is the associated private key.

  You will be prompted to provide some information, such as **Country**, **State**, **Organization**, etc. For **Common Name (CN)**, provide the **domain name or IP address** used to access Home Assistant (e.g., `ha.testhomewebsite.com` or `192.168.1.3`).

#### **3. Update the Home Assistant Configuration**
- Open **`configuration.yaml`** in your **SSH** session or use the **File Editor** add-on in Home Assistant.
- Add or update the following section to point to the generated certificate and key:

  ```yaml
  http:
    ssl_certificate: /config/ssl/fullchain.pem
    ssl_key: /config/ssl/privkey.pem
  ```
- **Save** the configuration file after making these changes.

#### **4. Restart Home Assistant**
- To apply the changes, **restart Home Assistant**:
  - You can do this by navigating to **Settings > System > Restart**, or using the **Developer Tools**.

#### **5. Access Home Assistant Using HTTPS**
- Once Home Assistant is restarted, you should be able to access it using **HTTPS**:
  - **URL**: `https://<home_assistant_ip>:8123`
- Your browser will likely display a **security warning** since this is a self-signed certificate. You can safely bypass this warning by clicking "Advanced" and then "Proceed to unsafe."

### **Summary**:
- **SSL Directory**: Store your SSL certificates in **`/config/ssl`**.
- **Generate Certificates** with **OpenSSL** and place them in the **`ssl`** directory.
- **Update `configuration.yaml`** to reference these certificates.
- **Restart Home Assistant** to apply changes and use **HTTPS** for secure access.

This will allow encrypted access to your Home Assistant server, securing communication for local and external access. Let me know if you need help with any further steps!