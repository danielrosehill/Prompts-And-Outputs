---
title: "Draft blog post about my context library"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Title:** Building a Context Library to Supercharge Your LLM Outputs

**Introduction:**
When working with large language models (LLMs) like GPT, context is everything. Providing the right context can be the difference between getting a generic response and an answer that’s tailor-made for your needs. Tokenization limits and the need for repeat interactions can make it challenging to provide sufficient context every time. In this blog, I'll share a workflow I’ve developed—a context library—that enhances my ability to use LLMs effectively by storing and reusing contextual information.

**1. The Importance of Context in LLM Outputs**
To get useful responses from an LLM, the input prompts need to be both clear and context-rich. LLMs work better when they have relevant background information, and their quality of output is highly dependent on how much context they receive. Unfortunately, due to tokenization limits, it’s often impossible to feed in all the background details in every prompt. This results in shallow, less effective outputs.

To combat this, I've created a system that enables me to store relevant context and reuse it whenever needed, without constantly having to repeat myself.

**2. Introducing the Context Library**
The key to my workflow is what I call a "context library." This library lives inside my Obsidian vault—a markdown-first note-taking tool that allows me to keep my prompts, responses, and context snippets all in one place. The core idea of the context library is to create discrete pieces of information, or "context snippets," that can be reused across different prompts.

**3. What are Context Snippets?**
Context snippets are individual documents that contain specific details about me, my work, or any area I frequently interact with using an LLM. For example:

- **Professional Responsibilities:** This snippet includes information about my job, the projects I’m working on, and my primary goals.
- **Personal Context:** Another snippet contains details like where I live and my areas of interest.
- **Computer Hardware Specifications:** I even keep a snippet for my computer specs, which is helpful when I'm trying to evaluate upgrades or compatibility for new hardware. Here is my actual hardware context snippet:

```
### **System Specification**

#### **Computer Type**: Desktop, Custom Build

| **Component**    | **Specification**                                  |
| ---------------- | -------------------------------------------------- |
| **CPU**          | Intel Core i7-12700F 2.1GHz 25MB 1700 Tray         |
| **Motherboard**  | Pro B760M-A WiFi 1700 DDR5 MSI B760 Chip           |
| **RAM**          | Kingston 32GB DDR5 4800MHz (Model: KVR48U40BS8-16) |
| **GPU**          | AMD Radeon RX 7700 XT Pulse Gaming 12GB Sapphire   |
| **Power Supply** | Gold 80+ MDD Focus GX-850 850W Seasonic            |
| **Case**         | Pure Base 500 Be Quiet                             |
| **CPU Cooler**   | Pure Rock 2 Be Quiet                               |
| **OS**           | Fedora Workstation 40                              |

---

### **CPU Information**

- **Architecture**: x86_64
  - **CPU op-mode(s)**: 32-bit, 64-bit
  - **Address sizes**: 39 bits physical, 48 bits virtual
  - **CPU(s)**: 20 (0-19 online)
  - **Vendor**: GenuineIntel
  - **Model Name**: 12th Gen Intel Core i7-12700F
  - **Core(s) per Socket**: 12
  - **Thread(s) per Core**: 2

---

### **GPU Information**

- **Product**: Navi 32 [Radeon RX 7700 XT / 7800 XT]
- **Vendor**: Advanced Micro Devices, Inc. [AMD/ATI]

---

### **Memory (RAM)**

| **Slot**         | **Size** | **Type** | **Speed**  | **Manufacturer** |
| ---------------- | -------- | -------- | ---------- | ---------------- |
| Controller0-DIMMA2 | 16 GB   | DDR5     | 4800 MT/s  | Kingston         |
| Controller1-DIMMB2 | 16 GB   | DDR5     | 4800 MT/s  | Kingston         |

**Total RAM**: 32GB DDR5 4800 MHz

---

### **Storage Configuration (BTRFS + RAID1)**

- **Filesystem Label**: fedora
- **Total Size**: 2.73TiB
- **Total Used**: 226.66GiB
- **RAID1 Configuration**: Data and Metadata mirrored across drives.

| **Device** | **Path**       | **Total Size** | **Used**  |
| ---------- | -------------- | -------------- | --------- |
| NVME       | /dev/nvme0n1p1 | 931.51GiB      | 81.04GiB  |
| SSD1       | /dev/sda3      | 929.93GiB      | 79.00GiB  |
| SSD2       | /dev/sdb1      | 931.51GiB      | 81.03GiB  |

- **Data (RAID1)**: 245.00GiB
- **Metadata (RAID1)**: 7.00GiB
- **Unallocated Space**: 2.23TiB

---

### **Peripherals**

- **Monitors**: AOC 2275W x 3
- **Mouse**: Logitech MX Vertical

---
```

``````
By housing these snippets in a dedicated "context" folder in Obsidian, I have easy access to information that I can copy and paste into prompts to quickly bring an LLM up to speed.

**4. Workflow Example: Using Context Snippets for Efficiency**
Here’s how I use my context library in action:

Let’s say I want to prompt GPT to help me find a new graphics card for my computer. Instead of manually typing in all my computer specs each time, I can just include my "Computer Hardware" snippet as part of my prompt. This not only saves time but also ensures consistency, as the LLM always has accurate information.

For example, I might prompt:

```
I’m looking to upgrade my graphics card. Here are my current computer specs:

{{Insert Computer Hardware Context Snippet}}

Please suggest compatible graphics cards that would be an upgrade.
```

**5. Building Context Repositories: A Scalable Approach**
As I used this system more, I realized that having separate snippets is great, but for more advanced tasks, I needed an aggregated context. This led to creating “context repositories”—self-standing documents that combine multiple snippets for a specific purpose. For instance, I could create a “Work Project Repository” that combines my professional responsibilities with the details of the current project I’m working on.

This approach makes my prompts even more efficient because I can load entire repositories instead of picking individual snippets each time. This idea is particularly useful for business users who need to scale their use of LLMs without constantly providing context from scratch.

**6. Combining Context Snippets Dynamically**
Another area I’m exploring is how to dynamically concatenate multiple snippets to form a larger, aggregated context document. While this is more of an advanced use case, and potentially something that would benefit from a Retrieval-Augmented Generation (RAG) approach, it’s still possible to achieve a similar effect manually. This means pulling together context snippets dynamically depending on the specific prompt or project requirement.

**7. The Benefits of Using a Context Library**
- **Efficiency:** With a library of reusable snippets, I don’t need to repeat myself. I can generate better outputs with less effort.
- **Consistency:** Ensuring the LLM always receives the same context makes the responses more reliable.
- **Scalability:** Using aggregated context repositories allows me to tackle larger, more complex problems without starting from scratch every time.

**Conclusion:**
Creating a context library has been the single most effective improvement I’ve made in my interactions with LLMs. By building reusable context snippets, I can significantly boost the quality and consistency of outputs while saving time. Whether you’re using LLMs for business, software development, or personal projects, I highly recommend trying this approach. It’s a straightforward way to make the most of what AI can offer.

