---
title: How to install a client cert on a Fedora computer
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To install the client certificate on your **Fedora Linux** computers, you'll need to add the certificate and private key to your system’s certificate store or use it with specific applications like browsers. Here's how to do it:

### Steps to Install a Client Certificate on Fedora Linux:

#### 1. **Ensure You Have the Client Certificate and Private Key**
   - You should have a **PEM** or **PKCS#12 (.p12)** file that contains both the client certificate and the private key.
   - If you have them in separate files (e.g., `client.crt` and `client.key`), you can combine them into a `.p12` file (preferred for importing).

   If you need to create a `.p12` file, you can use the following command:
   ```bash
   openssl pkcs12 -export -out client_cert.p12 -inkey client.key -in client.crt
   ```
   You will be prompted to enter a password to protect the `.p12` file, which will be needed when importing the certificate.

#### 2. **Install the Certificate for System-Wide Use (optional)**
   If you want the certificate to be available system-wide (for services and applications that use system certificates):

   1. Copy the `.pem` or `.p12` file to the system’s certificate store:
      ```bash
      sudo cp client_cert.pem /etc/pki/ca-trust/source/anchors/
      ```

   2. Update the system’s certificate store:
      ```bash
      sudo update-ca-trust
      ```

   This makes the certificate trusted system-wide, but it doesn’t directly apply it for client authentication (that needs to be configured in specific applications).

#### 3. **Install the Certificate for Use in Browsers**

   If you mainly want to use the client certificate for browsing (e.g., for accessing Cloudflare-protected resources via **Firefox** or **Chrome**), you’ll need to import the certificate into the browser's certificate manager.

   ##### **For Firefox**:
   1. Open **Firefox**.
   2. Go to the **Menu** (three lines in the top-right corner) and choose **Preferences** (or **Settings**).
   3. Scroll down to **Privacy & Security** and find the **Certificates** section.
   4. Click **View Certificates**.
   5. In the **Your Certificates** tab, click **Import**.
   6. Select your **.p12** file and click **Open**.
   7. Enter the password you set when exporting the `.p12` file, and Firefox will import the certificate.
   8. Once imported, Firefox will automatically present the certificate when required.

   ##### **For Chrome (or Chromium-based browsers)**:
   Chrome/Chromium on Linux uses the **GNOME Keyring** or **KDE Wallet** for managing certificates, so you will need to import the certificate into your keyring.

   1. Open **Chrome**.
   2. Go to **Settings** > **Privacy and Security** > **Security**.
   3. Scroll down and click on **Manage certificates**.
   4. In the certificate manager, click the **Your Certificates** tab and choose **Import**.
   5. Select your `.p12` file, enter the password when prompted, and import the certificate.

#### 4. **Configure Network Manager for Specific Applications (optional)**:
   If you’re using a **VPN** or connecting to services over the network that require a client certificate, you can configure the **Network Manager** to use the certificate for specific connections.

   1. Open **NetworkManager** from your system tray or by searching **Settings > Network**.
   2. Select the connection you want to configure (such as a VPN or Wi-Fi connection).
   3. In the settings for that connection, go to the **Security** or **Authentication** section.
   4. Select the **client certificate** you want to use from the file dialog (either `.pem` or `.p12` format).

#### 5. **Verify the Certificate Installation**:
   Once you have installed the certificate, try accessing a Cloudflare Access-protected resource. Your browser or application should automatically present the client certificate, and you should gain access without being prompted for login.

### Summary:
- Use a `.p12` file for easier management.
- For **system-wide use**, add the certificate to the system certificate store.
- For **browser-specific use**, import the certificate into Firefox or Chrome’s certificate manager.
- Optionally, configure **Network Manager** to use the certificate for specific connections (like VPNs).

Once installed, your Fedora device will present the certificate for authentication whenever you try to access Cloudflare Access-protected resources, bypassing further login challenges.