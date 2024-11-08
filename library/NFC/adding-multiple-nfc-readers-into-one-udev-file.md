---
title: "Adding multiple NFC readers into one udev file"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it's perfectly fine to have multiple devices defined in the same **udev** rules file like this. Each line in the **`99-nfc.rules`** file specifies a separate rule for a different NFC reader based on its **Vendor ID** and **Product ID**.

### Explanation
- **Each line corresponds to a different device**, and the rules are processed independently.
- The udev system will apply the correct permissions and group settings to any device matching the specific **`idVendor`** and **`idProduct`** values.

### What You Have:
1. **First Device**:
   ```bash
   SUBSYSTEM=="usb", ATTRS{idVendor}=="072f", ATTRS{idProduct}=="223b", GROUP="input", MODE="0666"
   ```
   - This sets devices with Vendor ID **072f** and Product ID **223b** to have group **`input`** and mode **0666**.

2. **Second Device**:
   ```bash
   SUBSYSTEM=="usb", ATTRS{idVendor}=="072f", ATTRS{idProduct}=="2200", GROUP="input", MODE="0666"
   ```
   - This sets devices with Vendor ID **072f** and Product ID **2200** to also have group **`input`** and mode **0666**.

### Additional Notes:
- **Make sure the rules file is formatted correctly**. As long as each line has the correct syntax, there will be no issues.
- **Reload udev rules** to apply changes:
  ```bash
  sudo udevadm control --reload-rules
  sudo udevadm trigger
  ```
- If you run into any permission issues, you may need to **restart** or **unplug/replug** the devices after applying the new rules.

This setup should allow both NFC readers to work with the **`input`** group and provide appropriate permissions to users in that group. Let me know if everything works as expected!