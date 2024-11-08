---
title: "Google Workspace - Ensuring Email Deliverability"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



### 1. **Enable SPF (Sender Policy Framework)**
   - You already have DMARC, so setting up **SPF** is a good complement. SPF helps prevent spoofing by specifying which mail servers are authorized to send emails on behalf of your domain.
   - **Add a TXT Record**:
     - **Type**: TXT
     - **Name**: `@`
     - **Content**: `v=spf1 include:_spf.google.com ~all`
   - This record allows Google servers to send emails and marks other servers as suspect.

### 2. **Enable DKIM (DomainKeys Identified Mail)**
   - Make sure your **DKIM** record is active (you mentioned adding the TXT record already).
   - DKIM ensures that the content of emails cannot be altered in transit, thus preventing email tampering.

### 3. **Set Up Security Keys or 2-Step Verification**
   - Enable **2-Step Verification (2SV)** for additional account security.
   - Use **security keys** (like a **YubiKey**) for the strongest protection. These keys use physical authentication to ensure only authorized users can access the account.
   - **Google Workspace Admin Console**: Go to **Security > 2-Step Verification** and **enforce** its use for all your accounts.

### 4. **Review Access and App Passwords**
   - **Audit Access to Your Account**:
     - Go to your Google Account's **"Security"** section to check **third-party apps** that have access. Remove any unnecessary or outdated access.
   - **Use App Passwords**: For apps that don’t support 2-Step Verification, use **App Passwords** to secure access instead of your main account password.

### 5. **Implement Advanced Phishing Protection**
   - As an admin, you can enforce **Advanced Protection Program** settings.
   - In the **Admin Console**, go to **Security > Google Workspace > Gmail > Safety** and enable features like **link scanning**, **attachment scanning**, and **external email warnings** to protect against phishing attacks.

### 6. **Review Gmail Settings for Security Improvements**
   - **Restrict IMAP/POP Access**: If you don’t need IMAP or POP, disable them in **Settings > Forwarding and POP/IMAP** to prevent potential exploits through these protocols.
   - **Check Filters and Forwarding Rules**: Make sure there are no **unauthorized filters or forwarding rules** set up in your account, as attackers sometimes set these to exfiltrate emails.

### 7. **Create Email Spoofing Prevention Rules (Optional)**
   - **Spoofing Prevention**: Configure **internal sender authentication** in the Google Admin Console.
   - In the Admin Console, go to **Apps > Google Workspace > Gmail > Safety > Spoofing and authentication** and ensure settings are enabled to prevent internal and external spoofing attacks.

### 8. **Monitor Your Domain’s Security with Security Dashboard**
   - Use Google Workspace’s **Security Dashboard** to monitor **suspicious activity**, including failed logins, account status, and unusual locations.

### 9. **Quarantine Suspicious Emails**
   - Set up **quarantine policies** for suspicious emails in **Admin Console > Apps > Google Workspace > Gmail > Compliance**.
   - Create filters that automatically **quarantine** emails failing **SPF, DKIM**, or **DMARC**.

### 10. **Enable Email Encryption**
   - Make sure that **TLS** (Transport Layer Security) is enabled for incoming and outgoing messages.
   - This ensures encryption in transit between mail servers.

### 11. **Educate Your Team on Phishing and Email Security Best Practices**
   - Provide training on how to identify **phishing emails**, avoid suspicious links, and recognize **spoofing attempts**.
   - Google Workspace offers **security tips** that can be distributed to users to ensure they’re aware of email risks.

### Summary
- **Enable SPF** and **DKIM** to complement DMARC.
- **Use 2-Step Verification** and **security keys** to secure access.
- **Audit third-party apps** and use **App Passwords** when needed.
- **Enable advanced phishing protection** and **TLS encryption**.
- **Review Gmail security settings** for additional hardening.

These steps combined will significantly improve the security of your email and protect your domain from being misused or compromised. Let me know if you need more specific guidance on any of these steps!