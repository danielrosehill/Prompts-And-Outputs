---
title: "Where to store the private key on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


The **private key** should **not** be stored in the system-wide certificate store with the certificate (since it’s sensitive), but it must still be accessible to applications that require it for **mutual TLS (mTLS)** authentication. Typically, the private key is stored in a secure location on the filesystem, and you reference it directly from the application or service that needs it.

Here’s a detailed approach for handling the **private key** securely on Fedora:

### 1. **Securely Store the Private Key**

The **private key** should be stored in a secure, non-public directory with proper permissions. Here’s a standard approach:

1. **Create a Directory for Private Keys** (if one doesn’t already exist):
   You can store the private key in a dedicated directory for sensitive files, such as `/etc/ssl/private/`.

   ```bash
   sudo mkdir -p /etc/ssl/private
   ```

2. **Copy the Private Key to this Directory**:
   Copy the private key file (`client_key.key`) to this secure directory:

   ```bash
   sudo cp client_key.key /etc/ssl/private/
   ```

3. **Set Secure Permissions**:
   Ensure that only the root user (or a specific user if needed) has access to the private key:

   ```bash
   sudo chmod 600 /etc/ssl/private/client_key.key
   sudo chown root:root /etc/ssl/private/client_key.key
   ```

   This ensures that only **root** (or specific services, if configured) can access the private key.

### 2. **Configure Applications to Use the Private Key**

When applications (e.g., **NetworkManager**, **OpenVPN**, **Apache**, or **Nginx**) need the private key for mutual TLS, you point them directly to the location of the key file.

Here’s how to configure common applications to use the private key:

#### **For NetworkManager** (VPN or Wi-Fi):
1. Open **NetworkManager** and go to the connection that requires the certificate.
2. In the **Security** or **Authentication** section, where it asks for the **Private Key**, point to the path of the private key, such as `/etc/ssl/private/client_key.key`.
3. Make sure the **client certificate** points to the **PEM certificate** stored earlier (`/etc/pki/ca-trust/source/anchors/client_cert.crt`).

#### **For OpenVPN**:
If you’re using **OpenVPN**, you would configure the `.ovpn` file to reference the certificate and private key separately:

```bash
cert /etc/pki/ca-trust/source/anchors/client_cert.crt
key /etc/ssl/private/client_key.key
```

#### **For Apache or Nginx** (Web Servers):
In **Apache** or **Nginx**, you configure the SSL settings to reference both the **certificate** and **private key** paths.

- For **Apache** (`/etc/httpd/conf.d/ssl.conf` or another SSL config):
   ```bash
   SSLCertificateFile /etc/pki/ca-trust/source/anchors/client_cert.crt
   SSLCertificateKeyFile /etc/ssl/private/client_key.key
   ```

- For **Nginx** (`/etc/nginx/conf.d/ssl.conf` or similar):
   ```bash
   ssl_certificate /etc/pki/ca-trust/source/anchors/client_cert.crt;
   ssl_certificate_key /etc/ssl/private/client_key.key;
   ```

### 3. **System-Wide Usage of the Private Key (Not Recommended)**

**Important**: Storing the private key directly in system-wide paths is generally **not recommended** unless absolutely necessary because it’s a sensitive file. It’s best to keep the private key in a secure directory (like `/etc/ssl/private/`) and reference it explicitly only in the configurations that need it, rather than adding it to the certificate store. 

You should also **limit access** to the private key file to the user or service that actually needs it, like a web server, VPN service, or application.

### Summary:
1. **Private Key Storage**:
   - Store the private key in a secure directory like `/etc/ssl/private/`.
   - Set restrictive permissions (`600`) so only root or the relevant service can access it.

2. **Referencing the Private Key**:
   - Configure applications to point to the private key when needed (e.g., `/etc/ssl/private/client_key.key`).
   - Ensure that the application using the private key has the appropriate permissions to access it.

This approach keeps your **private key** secure while ensuring it’s accessible for the services and applications that need it for mutual TLS (mTLS) authentication. Let me know if you need help with configuring a specific service!