---
title: "Reverting changes to udev"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there a way to undo whatever changes these commands did to my system:

sudo sh -c 'echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0fd9\", TAG+=\"uaccess\"" > /etc/udev/rules.d/70-streamdeck.rules' sudo udevadm trigger

# Output

Sure thing! To **undo the changes** made by these commands, you simply need to remove the file that was created and trigger **udevadm** again to update the rules applied to your system.

### What These Commands Did:
The command you ran created a **udev rule** for a **USB device** (specifically the Elgato Stream Deck). The udev rule matches any device with a **Vendor ID (`0fd9`)** and adds the `uaccess` tag, allowing users with active sessions to access the device.

To **undo** this, follow these steps:

### 1. Remove the Created Udev Rules File
The command you ran created the file `/etc/udev/rules.d/70-streamdeck.rules`. You can remove this file with:

```bash
sudo rm /etc/udev/rules.d/70-streamdeck.rules
```

### 2. Reload Udev Rules
After removing the udev rules file, you need to **reload udev rules** so the changes take effect. Run:

```bash
sudo udevadm control --reload
```

### 3. Apply the Changes
To make sure the changes are applied to all USB devices immediately, trigger udev again:

```bash
sudo udevadm trigger
```

### Summary of Steps to Undo:
1. **Remove the udev rule file**:
   ```bash
   sudo rm /etc/udev/rules.d/70-streamdeck.rules
   ```
2. **Reload udev rules**:
   ```bash
   sudo udevadm control --reload
   ```
3. **Apply the changes** (trigger):
   ```bash
   sudo udevadm trigger
   ```

### Optional Step: Verify Changes
If you'd like to verify that the udev rule has been removed and that no rules with the **Vendor ID `0fd9`** exist anymore, you can check the rules directory:

```bash
grep -r "0fd9" /etc/udev/rules.d/
```

If nothing is returned, it means the rules related to **Vendor ID `0fd9`** have been successfully removed.

Let me know if this helps or if you need further assistance!