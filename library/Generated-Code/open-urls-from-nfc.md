---
title: "Auto-open URLs from scanned NFC tags - OpenSUSE"
---

You want to create a system on **OpenSUSE** that triggers a script when your **ACR1252 NFC reader** is connected. The script should detect when an NFC tag is read, and if the tag contains a URL, it should automatically open the URL in **Google Chrome**. Here's a detailed guide on how you can achieve this:

## Steps

### 1. Set up udev rules to trigger a script when the NFC reader is connected

You can use **udev** to detect when your NFC reader is connected and run a script. Follow these steps:

- First, identify your NFC reader by running:
  ```bash
  udevadm info --attribute-walk --name=/dev/bus/usb/XXX/YYY
  ```
  Replace `/dev/bus/usb/XXX/YYY` with the correct path for your device.
- Create a new udev rule file:
  ```bash
  sudo nano /etc/udev/rules.d/99-nfc-reader.rules
  ```
- Add the following content to match your device (replace the `idVendor` and `idProduct` with values specific to your ACR1252 reader):
  ```bash
  SUBSYSTEM=="usb", ATTR{idVendor}=="XXXX", ATTR{idProduct}=="YYYY", ACTION=="add", RUN+="/path/to/nfc_script.sh"
  ```
- Reload udev rules:
  ```bash
  sudo udevadm control --reload-rules
  sudo udevadm trigger
  ```

This will ensure that whenever your NFC reader is connected, the script `/path/to/nfc_script.sh` will run.

### 2. Script to read NFC tags and detect URLs

You can use **nfcpy**, a Python library, to interact with the NFC tags and extract their content. Install it using:

```bash
pip install nfcpy
```

Here’s an example Python script (`nfc_script.sh`) that reads NFC tags and checks if they contain a URL:

```python
#!/usr/bin/env python3

import nfc
import ndef
import subprocess

def on_connect(tag):
    for record in tag.ndef.records:
        if isinstance(record, ndef.UriRecord):
            url = record.uri
            # Open URL in Google Chrome
            subprocess.run(['google-chrome', url])
            print(f"Opened URL: {url}")
    return True

def main():
    with nfc.ContactlessFrontend('usb') as clf:
        clf.connect(rdwr={'on-connect': on_connect})

if __name__ == '__main__':
    main()
```

### 3. Make the script executable

Ensure that the script is executable by running:

```bash
chmod +x /path/to/nfc_script.sh
```

### 4. Open URLs in Google Chrome

The Python script uses `subprocess.run()` to open URLs in Google Chrome. You can test opening a URL from the command line like this:

```bash
google-chrome https://example.com
```

This command will open the specified URL in Chrome\[5].

### 5. Testing

- After connecting your ACR1252 NFC reader, the udev rule should trigger the `nfc_script.sh` script.
- When an NFC tag containing a URL is scanned, Chrome should automatically open with the URL.

### Additional Tools

If you need more control over NFC communication or debugging, you could also explore tools like **libnfc**\[3] or other utilities like `nfc-list` or `nfc-scan-device`\[6].

By following these steps, you should be able to automate opening URLs from NFC tags with your ACR1252 reader on OpenSUSE.

&#x20;
