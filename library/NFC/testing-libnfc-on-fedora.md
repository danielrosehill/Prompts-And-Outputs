---
title: "Testing LibNFC on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To use **LibNFC** for reading an NFC tag and automatically opening a URL, follow these steps:

### Step 1: Install LibNFC
```bash
sudo dnf install libnfc libnfc-utils
```

### Step 2: Configure LibNFC
Ensure your `acr122_usb.conf` is properly set up in `/etc/nfc/libnfc.conf` to recognize your ACR1252 device:
```bash
device.connstring = "usb"
device.driver = "acr122_usb"
```

### Step 3: Use `nfc-poll` to Read Tags
Run:
```bash
nfc-poll
```
It will display data from the NFC tag, including the URL if it's an NDEF record.

### Step 4: Automate URL Opening (Optional)
Create a script to read the output and open URLs:
```bash
#!/bin/bash
url=$(nfc-poll | grep -oP '(?<=URI: ).*')
if [ ! -z "$url" ]; then
    google-chrome "$url"
fi
```
Make the script executable:
```bash
chmod +x read-nfc-url.sh
```
Now, running `./read-nfc-url.sh` should read the NFC tag and open the URL in Chrome.