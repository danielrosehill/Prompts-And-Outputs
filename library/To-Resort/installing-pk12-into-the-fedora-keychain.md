---
title: "Installing PK12 into the Fedora keychain"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To import a **PKCS#12 (.p12)** certificate into the **system-wide credential store** on Fedora, follow these steps. This will make the certificate available for all applications and services that rely on the system-wide credential store, such as **NetworkManager**, **VPNs**, or other mTLS-based services.

### Step-by-Step Guide to Import PKCS#12 into System-Wide Credential Store:

#### 1. **Convert PKCS#12 to PEM Format**

Fedora’s system-wide credential store typically works with **PEM** files rather than **PKCS#12** files. Therefore, you first need to extract the **certificate** and **private key** from the `.p12` file and save them in **PEM** format.

Run the following command to extract the certificate and private key from your `.p12` file:

```bash
openssl pkcs12 -in client_cert.p12 -out client_cert.pem -nodes
```

- `client_cert.p12`: This is your input PKCS#12 file.
- `client_cert.pem`: This will be your output PEM file that contains both the certificate and private key.
- The `-nodes` flag tells OpenSSL not to encrypt the private key in the output PEM file.

After running the command, you’ll be prompted for the **password** that you set when creating the `.p12` file.

#### 2. **Split the PEM File (Optional, but Recommended)**

The output `client_cert.pem` will contain both the **certificate** and the **private key**. For better organization, you can split these into two separate files:

- **Certificate**: The part between `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----`.
- **Private Key**: The part between `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----`.

You can extract these into separate files:
- **Certificate**: Save this to a file named `client_cert.crt`.
- **Private Key**: Save this to a file named `client_key.key`.

If you prefer to leave them combined, the following steps will still work.

#### 3. **Copy the Certificate to the System Trust Store**

To make the certificate available system-wide, you need to copy the **certificate** (and, optionally, the key) to Fedora’s trusted certificate store.

Run the following command to copy the certificate file to the correct location:

```bash
sudo cp client_cert.crt /etc/pki/ca-trust/source/anchors/
```

This places the certificate into the system’s trusted certificate store. If you kept the private key separate, it should be stored securely and does **not** need to be copied into the system store (it will be referenced separately by applications that need it).

#### 4. **Update the System Trust Store**

After copying the certificate, you need to update the system’s certificate trust store. This ensures that the newly added certificate is recognized by the system:

```bash
sudo update-ca-trust
```

This command rebuilds the certificate trust list used by Fedora and other applications to trust certificates system-wide.

#### 5. **Using the Certificate in Applications**

Once the certificate is in the system trust store, it can be used by applications such as **NetworkManager** or any service that relies on system-wide certificates.

For example, if you're using **NetworkManager** for a VPN or Wi-Fi connection that requires mTLS:
1. Open **NetworkManager** and edit the VPN or network connection.
2. In the **Security** or **Authentication** section, point to the correct certificate from the store (usually under `/etc/pki/ca-trust/source/anchors/`).
3. Select the private key file (`client_key.key`) if it is stored separately.

### Summary of Commands:
1. **Convert PKCS#12 to PEM**:
   ```bash
   openssl pkcs12 -in client_cert.p12 -out client_cert.pem -nodes
   ```

2. **Copy the Certificate to the System Store**:
   ```bash
   sudo cp client_cert.crt /etc/pki/ca-trust/source/anchors/
   ```

3. **Update the System Trust Store**:
   ```bash
   sudo update-ca-trust
   ```

Now, your client certificate is available system-wide on Fedora, and applications that use the system trust store can access it for authentication.

Let me know if you need help with any part of this process!