---
title: "Modern E2E encrypted tools for privacy conscious users"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say that besides email I wanted to find an E2E encryption tool for: instant messaging (to replace WhatsApp), VoIP ( to replace skype), and web conferencing (to replace Zoom). What are the modern alternatives for those for privacy conscious users? I'm on Fedora + Andoid.

# Output

For privacy-conscious users seeking **end-to-end encryption (E2EE)** tools to replace popular services like WhatsApp (instant messaging), Skype (VoIP), and Zoom (web conferencing), there are excellent alternatives that prioritize privacy and security. Below are recommendations tailored to **Fedora + Android** users, with strong E2EE features:

### **1. Instant Messaging (Replacement for WhatsApp)**

#### **Signal**
- **Platform**: Android, iOS, Linux (Fedora-compatible), Windows, macOS
- **Encryption**: Signal uses its own **Signal Protocol**, which is widely regarded as one of the most secure encryption protocols for messaging.
- **Key Features**:
  - **End-to-end encryption** by default for all messages, calls, and media shared between Signal users.
  - Supports **group chats**, **voice notes**, and **media sharing**.
  - Self-destructing messages and **disappearing messages** for extra privacy.
  - **Open-source**: Signal’s code is open and regularly audited for security.
  - **Federated phone number-based identity**, but also allows for anonymous registration (via secondary phone numbers or services like Google Voice).
- **Why it’s a good replacement**: Signal is considered the **gold standard** for secure messaging. It’s easy to use, offers cross-platform support, and focuses heavily on privacy. The protocol it uses has been adopted by many other apps, and it’s a great alternative to WhatsApp, providing E2EE by default.
- **Drawbacks**: Requires a phone number for sign-up (though workarounds exist), and some users might prefer not to share their phone numbers.

#### **Session**
- **Platform**: Android, iOS, Linux, Windows, macOS
- **Encryption**: Built on **Signal Protocol** and **Onion Routing** (similar to Tor for extra anonymity).
- **Key Features**:
  - End-to-end encryption for **one-on-one** and **group messaging**.
  - Focus on **anonymity**: No phone number or email address is required to register.
  - Decentralized, running on a distributed network rather than central servers.
  - Supports **file sharing**, **voice messages**, and **decentralized storage**.
  - **Open-source**: All code is available for review.
- **Why it’s a good replacement**: **Session** is a more privacy-focused alternative to Signal, emphasizing anonymity and decentralized architecture. It’s ideal if you want to avoid sharing a phone number and want more control over your metadata.
- **Drawbacks**: Some features (like real-time responsiveness) may be slightly slower than centralized services due to onion routing.

### **2. VoIP (Replacement for Skype)**

#### **Jami (Ring)**
- **Platform**: Android, iOS, Linux (Fedora-compatible), Windows, macOS
- **Encryption**: Jami offers **end-to-end encryption** for all communications, including voice and video calls, messaging, and file transfers.
- **Key Features**:
  - **Decentralized and peer-to-peer (P2P)**: Jami doesn't rely on central servers, making it very secure and private.
  - **No account needed**: You don’t need to register with an email or phone number—your identity is tied to a locally generated cryptographic key.
  - Supports **voice, video calls**, and **instant messaging** with **E2EE**.
  - **Open-source**: Jami is open-source and fully auditable.
  - Works across multiple devices with the same identity.
- **Why it’s a good replacement**: Jami offers excellent privacy due to its decentralized nature and E2EE, making it a perfect Skype alternative. You can make secure VoIP calls and text-based communications without needing an account, giving you full control of your data.
- **Drawbacks**: Since Jami is decentralized, certain features (like file synchronization) can be slower compared to centralized services like Skype.

#### **Linphone**
- **Platform**: Android, iOS, Linux (Fedora-compatible), Windows, macOS
- **Encryption**: Linphone supports **SRTP** (Secure Real-time Transport Protocol) and **ZRTP** for secure voice and video calls, along with **TLS** encryption for signaling.
- **Key Features**:
  - Supports **SIP-based VoIP** (Session Initiation Protocol), allowing users to make encrypted voice and video calls.
  - **E2EE** support for voice calls using **ZRTP** (no need to exchange public keys manually).
  - Can be used with **SIP providers** for internet telephony, allowing more flexibility.
  - **Open-source**, which is great for auditing and transparency.
- **Why it’s a good replacement**: Linphone provides a **SIP-based** alternative for encrypted VoIP communication. It’s a solid, flexible replacement for Skype, especially for users who want to control their VoIP infrastructure while still maintaining strong encryption.
- **Drawbacks**: More technical setup required if you're unfamiliar with SIP protocols. You’ll need to select a SIP provider or run your own SIP server for VoIP calls.

### **3. Web Conferencing (Replacement for Zoom)**

#### **Jitsi Meet**
- **Platform**: Android, iOS, Web-based (works on Fedora)
- **Encryption**: Jitsi Meet offers **end-to-end encryption** for video calls, though the feature is in development and limited to 1:1 calls (with encryption for group calls on the way).
- **Key Features**:
  - **No account required**: You can host or join meetings without needing to sign up.
  - Offers **encrypted video conferencing** with support for screen sharing, recording, and text chat.
  - Supports **browser-based conferencing**, so no installation is necessary (though mobile apps are available).
  - **Federated or self-hosted**: You can run your own Jitsi Meet server if you want full control over your conferencing data.
  - **Open-source** and highly customizable.
- **Why it’s a good replacement**: Jitsi Meet is an excellent Zoom replacement for privacy-conscious users. You can host encrypted meetings without the need for an account, and it can be **self-hosted** for maximum privacy and control.
- **Drawbacks**: End-to-end encryption is still limited to **one-on-one calls** for now. Group call encryption is in progress, but currently, Jitsi uses **DTLS-SRTP** for encryption (still secure, but not full E2EE).

#### **Element (Matrix) + Jitsi Integration**
- **Platform**: Android, iOS, Linux (Fedora-compatible), Web-based
- **Encryption**: **Element** is built on the **Matrix** protocol and offers **E2EE** for text, voice, and video communications. For larger video conferencing, it can be integrated with **Jitsi** for secure group calls.
- **Key Features**:
  - Matrix-based, decentralized messaging with **end-to-end encryption**.
  - Supports **group chats**, **voice and video calls**, and **file sharing** with full E2EE.
  - Integration with **Jitsi Meet** allows you to host or participate in web conferences with encryption, without needing an external Zoom-like platform.
  - **Open-source** and decentralized, with the option to self-host.
- **Why it’s a good replacement**: **Element + Jitsi** provides a full **privacy-first web conferencing** solution, with E2EE for messaging and secure conferencing for groups. It’s ideal for those who want both chat and web conferencing in one platform, along with the flexibility of hosting their own servers.
- **Drawbacks**: The Jitsi video integration is encrypted, but may not reach full E2EE yet in group calls. Self-hosting adds a layer of complexity if you go that route.

### **Summary of Alternatives for Privacy-Conscious Users**

| Service             | Category                 | Platform (Fedora + Android)  | E2EE Protocol         | Open-Source | Key Features                                |
| ------------------- | ------------------------ | ---------------------------- | --------------------- | ----------- | ------------------------------------------- |
| **Signal**          | Messaging                | Android, Linux, iOS, Windows | Signal Protocol       | Yes         | Secure messaging and calls with E2EE        |
| **Session**         | Messaging                | Android, Linux, iOS, Windows | Signal Protocol       | Yes         | Decentralized, no phone number required     |
| **Jami**            | VoIP, Messaging          | Android, Linux, iOS, Windows | P2P + E2EE            | Yes         | Fully decentralized VoIP and chat           |
| **Linphone**        | VoIP                     | Android, Linux, iOS, Windows | ZRTP + SRTP           | Yes         | SIP-based VoIP with secure communication    |
| **Jitsi Meet**      | Web Conferencing         | Web, Android, iOS, Linux     | DTLS-SRTP (1:1 E2EE)  | Yes         | No account required, federated/self-hosted  |
| **Element + Jitsi** | Messaging + Conferencing | Android, Linux, iOS, Windows | Matrix + Jitsi (E2EE) | Yes         | Secure group messaging with Jitsi for video |

### Conclusion

For each of your needs—messaging, VoIP, and web conferencing—there are secure, open-source alternatives that prioritize **privacy and encryption**:

- **Signal** and **Session** are strong candidates for replacing WhatsApp with fully encrypted messaging.
- For VoIP, **Jami** offers a decentralized, encrypted solution, while **Linphone** provides a **SIP-based** encrypted option.
- For web conferencing, **Jitsi Meet** or **Element