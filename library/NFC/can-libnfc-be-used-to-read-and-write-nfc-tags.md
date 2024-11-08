---
title: "Can libnfc be used to read and write NFC tags"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of the prompt:** The user asked if `libnfc` can be used to both read and write NFC tags.

Yes, **`libnfc`** can be used for both reading and writing NFC tags. It is a versatile library that provides tools and APIs to interact with various NFC devices, including reading and writing operations on supported tags.

### Tools for Reading and Writing with `libnfc`

#### 1. **Reading NFC Tags**
- **`nfc-poll`:** This command is used to scan and detect NFC tags, displaying basic information about them.
  ```bash
  nfc-poll
  ```
  - This will show details like the tag’s UID, manufacturer, and other basic attributes. However, it doesn’t read the actual content stored on the tag.

- **`nfc-mfclassic r`:** Specifically for MIFARE Classic cards, you can read data blocks.
  ```bash
  nfc-mfclassic r A dump.mfd
  ```
  - **`r`**: Stands for read.
  - **`A`**: Uses authentication key A (you can switch to `B` for key B).
  - **`dump.mfd`**: Specifies the output file where the tag data will be saved.

#### 2. **Writing NFC Tags**
- **`nfc-mfclassic w`:** This tool allows you to write data back to MIFARE Classic cards.
  ```bash
  nfc-mfclassic w A mydata.mfd
  ```
  - **`w`**: Stands for write.
  - **`A`**: Uses authentication key A.
  - **`mydata.mfd`**: The input file containing the data you want to write to the tag.

- **`nfc-emulate-forum-tag4`:** This tool can emulate and write data for Type 4 tags, although it’s primarily for development and testing.
  ```bash
  nfc-emulate-forum-tag4 -r mytag.ndef
  ```
  - **`-r`**: Reads the data from the specified NDEF file and prepares to emulate it.

### Compatibility Notes
- **Tag Types:** `libnfc` is mainly effective with MIFARE Classic and similar ISO14443-A cards. For more advanced cards like MIFARE DESFire or other types (NTAG, ISO14443-B, ISO15693), you might need additional tools or libraries.
- **Access Control:** Writing to some NFC tags may require specific keys (like those on MIFARE Classic cards). Ensure you have the correct keys if access is restricted.

### Writing and Custom Scripts Using `libnfc` APIs
If the command-line tools don’t suit your needs, you can also create custom scripts using the **`libnfc`** library’s APIs. This provides more control over reading and writing processes, enabling features like:
- **Custom data structures**
- **Conditional data writing**
- **Advanced tag interactions**

### Conclusion
`libnfc` is a solid choice for both reading and writing NFC tags, particularly MIFARE Classic cards. If you're working with other tag types or need more advanced functionality, consider using additional libraries or custom development using the `libnfc` API.