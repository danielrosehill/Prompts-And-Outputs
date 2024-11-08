---
title: "What are average performance impacts of modern encryption algorithms"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

What's the average system performance degradation using encryption. For instance if I were to use encryption for just my Obsidian vault how much slower would it be than if it weren't encrypted with AES256? And are there any algorithms that can be used for E2E encryption that don't have any noticeable slowdown at all on modern hardware?

# Output

Encryption inevitably introduces some degree of performance degradation because of the computational overhead required to encrypt and decrypt data. However, modern encryption algorithms like **AES-256** are highly optimized, especially with hardware acceleration, so the impact on system performance can be quite small—often unnoticeable for many use cases, including encrypting an Obsidian vault. Let's break this down:

### **Performance Impact of AES-256 Encryption**

1. **AES-256 with Hardware Acceleration**:
   - **Minimal Overhead**: On modern hardware, especially CPUs that support **AES-NI (AES New Instructions)**, the performance impact of using **AES-256** encryption is very small. AES-NI is an extension to the instruction set of Intel and AMD processors that accelerates AES encryption, significantly reducing the time it takes to perform cryptographic operations.
   - **Real-world impact**: For tasks like encrypting an Obsidian vault, which involves reading and writing files to disk, the overhead of AES-256 encryption is likely to be **negligible** (often in the range of 1-3% performance degradation). The actual slowdown would depend on how frequently data is being written to and read from the encrypted vault, but for most use cases, you wouldn't notice a significant difference in day-to-day usage.

2. **AES-256 Without Hardware Acceleration**:
   - **Higher CPU Load**: On systems without hardware acceleration, AES-256 encryption can place a higher load on the CPU, leading to more noticeable performance degradation. However, even then, the impact is usually manageable for tasks like file encryption (e.g., reading and writing notes).
   - **Performance impact**: On older or low-power devices without AES-NI support, the overhead could range from **5-20%**, depending on how often encryption operations are performed (e.g., every time a file is accessed or saved). For encrypting small files like text documents in Obsidian, the effect would still likely be minimal unless you're working with large datasets or frequent sync operations.

### **Real-World Example for Obsidian Vault Encryption**

In the context of **Obsidian**:
- **Encrypted Vault**: If you were to encrypt your entire Obsidian vault using AES-256 (either by encrypting the filesystem where the vault is stored or by using a file-based encryption tool like **VeraCrypt** or **gocryptfs**), you’d experience very little performance degradation when opening, editing, and saving notes. This is because text files are relatively small and modern hardware can handle AES-256 encryption quickly.
- **Impact on Syncing**: If you use **end-to-end encryption (E2EE)** for syncing your notes to a cloud service, encryption would primarily impact the time it takes to **encrypt the file before uploading** and **decrypt it upon downloading**. Even in this case, the impact would likely be small.

#### Example Performance Impact:
- **Disk encryption benchmarks** on systems with AES-NI support typically show a **1-5% slowdown** for read/write operations on SSDs when using AES-256 full-disk encryption.
- For small files like text documents (as in Obsidian), the encryption overhead might add only a **few milliseconds** to read and write times, which is often imperceptible to the user.

### **Are There Encryption Algorithms with No Noticeable Slowdown?**

In practice, **no encryption algorithm** can operate without **some** performance overhead, but certain algorithms are more lightweight than others and are designed to minimize performance impact, especially when running on modern hardware.

1. **ChaCha20 (for E2E encryption)**:
   - **Fast in software**: **ChaCha20**, often used in combination with **Poly1305** for message authentication (as seen in the **WireGuard VPN** and **TLS**), is an alternative to AES that is designed to be faster in **software implementations**. While AES benefits from hardware acceleration (via AES-NI), ChaCha20 performs better in environments where hardware acceleration isn’t available.
   - **Comparable performance**: On modern CPUs, the performance of **ChaCha20** is comparable to AES-256 with hardware acceleration. In fact, **ChaCha20** can outperform AES in certain situations (e.g., mobile devices or embedded systems) because it doesn’t rely on specialized hardware instructions.
   - **Use case**: ChaCha20 is often used in E2E encryption for secure messaging (e.g., in **Signal** and **WhatsApp**) because it offers high performance without significant slowdown in typical use cases.

2. **XChaCha20**:
   - An extension of ChaCha20 that offers additional features, such as longer nonce sizes, making it suitable for E2E encryption with little to no noticeable performance impact on modern hardware. **XChaCha20** is becoming more popular in secure messaging and file encryption applications due to its strong security and efficiency.

### **Encryption in the Cloud: E2E Encryption for Syncing**

If you're using E2E encryption for syncing Obsidian files (or any files) to the cloud, the encryption process typically happens **before** data is uploaded and **after** it’s downloaded. The performance overhead here is also minimal because:
- **Files are relatively small**: Encrypting a text file (which is usually kilobytes in size) with AES-256 or ChaCha20 takes a fraction of a second.
- **Efficient Algorithms**: Both AES-256 and ChaCha20 are optimized for fast encryption/decryption, even for frequent file uploads and downloads.

### **Factors Affecting Encryption Performance**

1. **Hardware Acceleration**: As mentioned, **AES-NI** support in CPUs drastically reduces the performance impact of AES encryption. If your system has hardware acceleration (most modern CPUs do), you'll notice little slowdown when using AES-256.
   
2. **I/O Bound Operations**: If your system is bottlenecked by slow disk speeds (e.g., using an HDD instead of an SSD), encryption may add some additional latency, but on systems with fast SSDs, this is usually negligible.

3. **File Size**: Encryption performance can be more noticeable when dealing with large files (like media or large datasets). However, for small files (e.g., notes in an Obsidian vault), encryption overhead is barely perceptible.

### **Conclusion: Is the Performance Impact Noticeable?**
- For most **consumer-grade use cases** (like encrypting an Obsidian vault or using E2E encryption for syncing files), **AES-256** will introduce **minimal, if any, noticeable performance degradation** on modern hardware.
- If your system supports **AES-NI**, encryption with AES-256 will be very fast, and any slowdown will be difficult to notice in everyday usage.
- **ChaCha20** or **XChaCha20** are excellent alternatives to AES-256 for scenarios where **software-based encryption** is needed and where performance on mobile devices or systems without hardware acceleration is critical.

In short, encryption algorithms like **AES-256** and **ChaCha20** are highly optimized, and their performance impact is so low on modern hardware that it should not be a concern, especially for encrypting small files like those in an Obsidian vault.