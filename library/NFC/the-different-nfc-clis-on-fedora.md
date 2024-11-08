---
title: "The different NFC CLIs on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:** The user asked for an explanation of the different NFC CLIs available on Fedora and whether `libnfc` is different from `nfc-utils`.

### Overview of NFC Tools on Fedora

On Fedora, there are several command-line tools and libraries for working with NFC devices. Each has its own focus and functionality. Here's a breakdown:

### 1. **`libnfc`**
- **Description:** `libnfc` is a low-level library that provides the core functionality to communicate with NFC devices. It is a foundational component that other tools and applications build upon. 
- **Functionality:** It allows direct interaction with NFC hardware and provides the necessary APIs for reading from and writing to NFC tags.
- **Usage:** Typically used by developers and integrated into other software. Directly, it provides utilities for basic operations like polling for tags, reading, and writing data, especially for MIFARE Classic tags.

### 2. **`nfc-utils`**
- **Relationship to `libnfc`:** `nfc-utils` is a set of command-line tools that are built **on top of `libnfc`**. It uses `libnfc` as the underlying library to communicate with NFC devices but provides easier-to-use CLI commands for common tasks.
- **Tools Included in `nfc-utils`:**
  - **`nfc-poll`:** Scans and detects NFC tags, displaying basic information.
  - **`nfc-list`:** Lists available NFC devices connected to the system.
  - **`nfc-mfclassic`:** Reads from and writes to MIFARE Classic cards, using specific read and write commands.
  - **`nfc-emulate-forum-tag4`:** Used for testing and development, allowing emulation of Type 4 tags.
- **Installation:**
  ```bash
  sudo dnf install nfc-utils
  ```
- **Use Cases:** Handy for users who need straightforward command-line utilities to interact with NFC tags without writing custom scripts. 

### 3. **`pcsc-tools`**
- **Description:** While not specifically designed for NFC, `pcsc-tools` can be used with NFC readers that support the PC/SC (Personal Computer/Smart Card) standard. This tool provides a way to interact with smart cards and certain NFC tags.
- **Key Tool:**
  - **`pcsc_scan`:** Scans for smart cards (and some NFC tags), showing detailed information when a card or tag is detected.
- **Installation:**
  ```bash
  sudo dnf install pcsc-tools
  ```
- **Use Cases:** Useful for diagnostics, especially if you're unsure whether the NFC reader is being detected correctly or if you are dealing with smart cards alongside NFC tags.

### 4. **`nfcpy` (Python Library)**
- **Description:** While not a traditional CLI, `nfcpy` is a Python library that provides higher-level tools for developing NFC applications. It allows for custom scripts to be written to read from, write to, and interact with NFC tags.
- **Installation:**
  ```bash
  pip install nfcpy
  ```
- **Use Cases:** Best for users who want to create more complex NFC solutions. It’s also useful for those who need to perform custom actions beyond what `nfc-utils` provides.

### Summary of Differences
- **`libnfc` vs. `nfc-utils`:**
  - **`libnfc`** is a core library, offering low-level functions to communicate directly with NFC hardware. It requires more programming knowledge to use effectively.
  - **`nfc-utils`** provides a set of user-friendly CLI tools that utilize `libnfc` underneath, making it easier for non-developers to perform NFC tasks without writing code.
- **`pcsc-tools`:** Primarily for smart cards but can also recognize some NFC tags, useful for diagnostics.
- **`nfcpy`:** A Python-based solution that allows for extensive customization, suitable for more complex NFC interactions.

Each tool serves a slightly different purpose, so the best choice depends on what you need: basic reading/writing (`nfc-utils`), diagnostics (`pcsc-tools`), custom solutions (`nfcpy`), or direct hardware interaction (`libnfc`).