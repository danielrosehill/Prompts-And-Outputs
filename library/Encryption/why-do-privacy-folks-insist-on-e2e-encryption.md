---
title: "Why do privacy folks insist on E2E encryption"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

In the world of knowledge management, some people advocate using end to end encryption. I'm using Obsidian and syncing my notes to B2. They are not encrypted although I'm connecting to B2 over HTTPS. I would consider this reasonably secure and I'm not worried about B2 "snooping" on my notes. What exactly is that that more privacy conscious users are worried about and how would they criticise my setup?

# Output

In the world of knowledge management, especially among privacy-conscious users, concerns around **end-to-end encryption (E2EE)** often center on protecting data not just in transit (over HTTPS) but also **at rest** and against unauthorized access by service providers or third parties. Here's an analysis of what more privacy-conscious users may be worried about in your current setup with Obsidian and B2, and how they might criticize it:

### 1. **Provider Access to Data (Data at Rest)**
   - **The Concern**: Even though your notes are being transferred to B2 securely over HTTPS (which ensures protection during transmission), the data at rest (stored in B2) is not encrypted in a way that prevents the provider (Backblaze) from accessing it. If your notes are stored in plaintext on B2, privacy-conscious users would worry that Backblaze, or any other entity with access to their infrastructure (e.g., employees or government agencies), could potentially view, copy, or misuse your notes.
   - **Criticism**: Privacy advocates might argue that the service provider (B2) could be compelled by law enforcement, subject to a data breach, or have rogue employees accessing the unencrypted data. Since there is no E2EE, Backblaze technically has the ability to read your notes if they choose to.

### 2. **Vulnerabilities Beyond HTTPS (Encryption in Transit)**
   - **The Concern**: While HTTPS provides encryption in transit (i.e., your data is encrypted as it moves between your device and the B2 servers), the protection stops once the data is stored on the server. Privacy-conscious users advocate for encryption that ensures even if data is intercepted on the server or if the storage provider is compromised, the data remains unreadable.
   - **Criticism**: They would say that relying solely on HTTPS for security is insufficient because it protects data only while it is in transit, not when it is stored.

### 3. **Potential Data Breaches**
   - **The Concern**: Data breaches are a constant concern for cloud service providers. If a breach were to occur at B2, attackers could potentially access unencrypted user data. Without E2EE, the responsibility for securing data at rest lies with the provider rather than the user.
   - **Criticism**: Privacy-conscious users would suggest that your current setup leaves your notes vulnerable to exposure if B2 were to suffer a breach, as the data is stored in a readable format on their servers.

### 4. **No Control Over Data Deletion**
   - **The Concern**: Another privacy issue with cloud storage without encryption is that once you upload your notes to a third-party server (like B2), you have limited control over what happens to them. Even if you delete your notes, copies could potentially exist on backup servers or in logs, and you would have no way of verifying that all traces of your data are truly gone.
   - **Criticism**: Privacy-conscious users would argue that without encryption, you have to trust the provider entirely with the handling of your data, including its deletion.

### 5. **Metadata Exposure**
   - **The Concern**: Even with HTTPS and a relatively secure cloud provider, unencrypted storage could expose metadata (such as file names, modification times, or file sizes) which may provide insights into the contents of your notes, even if the content itself isn't accessed.
   - **Criticism**: Privacy advocates would point out that if metadata is not encrypted, it can still give away sensitive information even if the provider doesn’t access the content of your notes.

### **Privacy-Conscious Criticism Summary**:
1. **No End-to-End Encryption (E2EE)**: Your data is stored unencrypted on B2, leaving it accessible to the service provider or anyone who gains unauthorized access to their infrastructure.
2. **Trust in Provider**: Your security depends on trusting Backblaze to handle your data responsibly, whereas E2EE would remove that need for trust since only you hold the encryption keys.
3. **Risk of Breaches**: Should B2 be hacked or subpoenaed, your unencrypted notes could be exposed to third parties, which wouldn’t happen if E2EE were in place.

### **How to Address These Concerns**:
- **End-to-End Encryption**: Implement a solution where your notes are encrypted locally before they are uploaded to B2. Tools like [Cryptomator](https://cryptomator.org/) or [rclone](https://rclone.org/) with encryption can be used to ensure that only encrypted versions of your files are stored on the cloud provider.
- **Use of E2EE Plugins**: Obsidian has a community plugin, [Obsidian E2EE](https://github.com/fvictorio/obsidian-e2ee), which can encrypt your notes locally before syncing them to the cloud, ensuring that even if the cloud storage is breached or accessed, the data remains protected.
- **Self-hosted Sync**: For full control, some users opt to self-host their sync services (e.g., using Nextcloud with E2EE enabled) to minimize reliance on third-party providers and ensure complete data control.

By implementing end-to-end encryption, you would maintain the same level of convenience in syncing notes across devices while addressing the privacy concerns raised by more security-conscious users.