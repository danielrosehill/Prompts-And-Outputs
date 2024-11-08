---
title: "Trying to control the monitor that works with DDCUTIL"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt:** You are asking if there is a way to control only the functioning display using `ddcutil`.

### How to Control Only the Functioning Display:

Yes, you can target the functioning display specifically by identifying it through its **I2C bus** or **DRM connector**. Since your working monitor (Display 1) is connected via **I2C bus `/dev/i2c-3`** and **DRM connector `card1-DP-2`**, you can instruct `ddcutil` to control only this display by specifying the bus or connector.

### Two Methods to Target the Specific Display:

1. **Using the I2C Bus:**
   - You can directly specify the I2C bus (`/dev/i2c-3`) to control only Display 1:
     ```bash
     ddcutil --bus=3 setvcp 10 50  # Set brightness to 50% on /dev/i2c-3
     ```
   - This ensures that commands are sent only to the functioning display connected via that bus.

2. **Using the DRM Connector:**
   - You can also control the display by specifying the DRM connector:
     ```bash
     ddcutil --display card1-DP-2 setvcp 10 50  # Set brightness to 50% on card1-DP-2
     ```

### Confirm Display ID:
To confirm that you are targeting the correct display, you can use the following command to list all detected displays and their IDs:
```bash
ddcutil detect
```
This will show you which displays are connected to each bus or DRM connector, allowing you to confidently target the functioning one.

By specifying either the I2C bus or the DRM connector, you can control only the display that works without affecting the others.

#  