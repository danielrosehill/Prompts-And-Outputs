---
title: "Checking if libnfc can view device"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To check if **libnfc** can detect your USB NFC reader on Fedora, use the following command:

### Step 1: Run `nfc-list`
```bash
nfc-list
```
This will scan for connected NFC devices and display information if your reader is detected.

### Step 2: Check Output
- If the device is listed, it means `libnfc` recognizes the reader.
- If nothing appears, it could indicate an issue with configuration or permissions.

### Step 3: Confirm Device with `dmesg`
```bash
dmesg | grep -i usb
```
Look for entries related to **ACR1252** to ensure it's connected and recognized by the system. 

These steps will confirm whether `libnfc` can see your USB NFC reader.