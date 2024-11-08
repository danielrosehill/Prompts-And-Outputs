---
title: "Reading NFC tags in Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To automatically read an NFC tag with a URL and open it in Chrome on Fedora, you can use a combination of tools and scripts:

### Approach:
1. **Use `nfcpy` (Python Library)**:
   - Install `nfcpy`:
     ```bash
     sudo pip install nfcpy
     ```
   - Create a Python script to read the NFC tag and extract the URL:
     ```python
     import nfc
     import webbrowser

     def on_connect(tag):
         url = tag.ndef.message[0].uri
         webbrowser.open(url)

     clf = nfc.ContactlessFrontend('usb')
     clf.connect(rdwr={'on-connect': on_connect})
     ```

2. **Configure Chrome as the Default Browser**:
   - Ensure Chrome is set as the default browser, so the `webbrowser.open()` call will launch it automatically.

### Additional Tools:
- **AutoKey**: Can be used to automate this script, running it on NFC tag detection.
- **LibNFC**: Alternatively, use command-line utilities to read the URL and a simple shell script to launch Chrome.

These steps can streamline the process of reading URLs from NFC tags and automatically opening them in Chrome.