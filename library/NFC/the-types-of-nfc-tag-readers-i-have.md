---
title: "The types of NFC tag readers I have"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I have the ACR122U and the ACR1252. Any tools for either?

# Output

**Summary of the prompt:** The user has the ACR122U and ACR1252 NFC readers and asked for tools that support either.

### Tools for ACR122U and ACR1252 NFC Readers

Both the **ACR122U** and **ACR1252** are popular USB NFC readers from ACS (Advanced Card Systems). Here are tools and libraries that can help you interact with them on Fedora:

### 1. **`acr122u-tool` for ACR122U**
   - **Description:** Specifically designed for the ACR122U, `acr122u-tool` allows you to interact with this reader for reading and writing NFC tags. It's a lightweight utility for various operations.
   - **Features:**
     - **Read/Write**: Perform basic read and write operations on supported tags.
     - **Change Settings**: Adjust settings specific to the ACR122U (e.g., beep, LED control).
   - **Installation:** You may need to build this from source if it's not in the default Fedora repositories. Check GitHub or similar sites for the source.
   - **Example Usage:**
     ```bash
     acr122u-tool -r   # Read from the NFC tag
     acr122u-tool -w "Hello World"   # Write "Hello World" to the NFC tag
     ```

### 2. **`libnfc` and `nfc-utils` for Both Readers**
   - **Description:** `libnfc` and its associated `nfc-utils` support a range of NFC readers, including both ACR122U and ACR1252. You can use the tools to perform various NFC operations, like reading UIDs, writing data, and more.
   - **Installation:**
     ```bash
     sudo dnf install nfc-utils
     ```
   - **Usage Examples:**
     - **`nfc-poll`**: To detect and read NFC tags.
       ```bash
       nfc-poll
       ```
     - **`nfc-mfclassic`**: For MIFARE Classic read/write.
       ```bash
       nfc-mfclassic r A dump.mfd
       ```
     - **Device Configuration:** You can specify the device when there are multiple readers:
       ```bash
       nfc-poll -d usb:072f/2200
       ```

### 3. **`pcsclite` and `pcsc-tools` for Both Readers**
   - **Description:** These tools can help you interact with USB smart card readers, including the ACR122U and ACR1252. `pcscd` is the daemon that manages smart card connections, and `pcsc_scan` provides a detailed readout of detected cards.
   - **Installation:**
     ```bash
     sudo dnf install pcsc-lite pcsc-tools
     ```
   - **Usage:**
     ```bash
     sudo pcsc_scan
     ```
   - **Note:** Ensure `pcscd` is running:
     ```bash
     sudo systemctl start pcscd
     sudo systemctl enable pcscd
     ```

### 4. **NFCpy for Custom Scripting (Both Readers)**
   - **Description:** **NFCpy** is a Python library that can communicate with various NFC readers, including both ACR122U and ACR1252. It allows you to write custom scripts for reading, writing, and even emulating NFC tags.
   - **Installation:**
     ```bash
     pip install nfcpy
     ```
   - **Example Script:**
     ```python
     import nfc

     def read_tag():
         clf = nfc.ContactlessFrontend('usb')
         tag = clf.connect(rdwr={'on-connect': lambda tag: False})
         print(f"Tag UID: {tag.identifier.hex()}")

     read_tag()
     ```

### 5. **ACS Drivers and SDKs for ACR122U and ACR1252**
   - **Description:** ACS provides drivers and SDKs specific to their readers, which can offer more features than generic tools like `libnfc`. This can be useful for advanced use cases or specific NFC operations that require direct access to the reader’s capabilities.
   - **ACS Driver Installation:**
     - Check the [ACS website](https://www.acs.com.hk) for Linux drivers and SDKs.
     - **Follow Instructions**: Download and follow the included README for setup. This often involves compiling driver libraries from source.

### 6. **Flashing and Firmware Tools for ACR1252**
   - **Description:** The ACR1252 supports more features than the ACR122U, and you can access some of them via firmware utilities. These tools can help with tasks like upgrading firmware, adjusting settings, and more.
   - **Accessing the ACS Firmware Utility:**
     - Obtain it from the ACS website.
     - Use their utility to flash the reader and enable specific features (e.g., Type 4 card support).
   - **Note:** Be cautious with firmware updates. Always ensure you have the correct version for your reader model.

### Summary
- **Dedicated Tools:** Use **`acr122u-tool`** for the ACR122U and **ACS SDK/Drivers** for more robust control over both devices.
- **General NFC Tools:** **`libnfc`/`nfc-utils`** and **`pcsc-tools`** are great for standard read/write tasks across many NFC readers, including the ACR models.
- **Custom Scripting:** **NFCpy** is flexible for creating tailored NFC applications, supporting both ACR122U and ACR1252 readers.
- **Firmware and Drivers:** **ACS drivers and firmware utilities** can help unlock more advanced features of your readers.

These tools and utilities should help you make the most of your ACR122U and ACR1252 NFC readers on Fedora. Let me know if you need more guidance on any specific setup!