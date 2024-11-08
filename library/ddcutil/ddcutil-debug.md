---
title: "ddcutil debug"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

This is the output that I get when I run ddcutil. What does it mean?

```Display 1  
  I2C bus:  /dev/i2c-3  
  DRM connector:           card1-DP-2  
  EDID synopsis:  
     Mfg id:               AOC - UNK  
     Model:                2275W  
     Product code:         8821  (0x2275)  
     Serial number:        B63HBQA002521  
     Binary serial number: 16843009 (0x01010101)  
     Manufacture year:     2017,  Week: 44  
  VCP version:         2.1  
  
Display 2  
  I2C bus:  /dev/i2c-4  
  DRM connector:           card1-HDMI-A-1  
  EDID synopsis:  
     Mfg id:               AOC - UNK  
     Model:                2275W  
     Product code:         8821  (0x2275)  
     Serial number:        B63GCQA006616  
     Binary serial number: 16843009 (0x01010101)  
     Manufacture year:     2016,  Week: 50  
  VCP version:         Detection failed  
  
Invalid display  
  I2C bus:  /dev/i2c-5  
  DRM connector:           card1-HDMI-A-2  
  EDID synopsis:  
     Mfg id:               AOC - UNK  
     Model:                2275W  
     Product code:         8821  (0x2275)  
     Serial number:        B63GCQA006621  
     Binary serial number: 16843009 (0x01010101)  
     Manufacture year:     2016,  Week: 50  
  DDC communication failed. (getvcp of feature x10 returned Error_Info[DDCRC_RETRIES in ddc_write_read_with_r  
etry, causes: DDCRC_DDC_DATA(2), DDCRC_READ_ALL_ZERO(5), DDCRC_DDC_DATA, DDCRC_READ_ALL_ZERO(2)])
```

# Output

Based on the information provided, it seems you're experiencing issues with controlling the brightness of your AOC monitors using ddcutil on Fedora Linux. Here's an analysis of the situation and some suggestions:

1. Monitor Detection:
   - ddcutil is detecting two of your AOC 2275W monitors (Display 1 and Display 2).
   - A third monitor is detected but marked as "Invalid display" due to DDC communication failure.

2. Connection Types:
   - Display 1 is connected via DisplayPort (card1-DP-2)
   - Display 2 is connected via HDMI (card1-HDMI-A-1)
   - The invalid display is also connected via HDMI (card1-HDMI-A-2)

3. Issues:
   - Display 2 has a VCP version detection failure
   - The invalid display has DDC communication failures

Suggestions:

1. Check Monitor Settings:
   - Ensure that DDC/CI is enabled in the on-screen display (OSD) menu of each monitor[2].

2. I2C Module:
   - Verify that the i2c-dev module is loaded:
     ```
     sudo modprobe i2c-dev
     ```

3. User Permissions:
   - Make sure your user has permission to access the I2C bus[2]. You can check this with:
     ```
     sudo ddcutil environment
     ```

4. Try Different Connections:
   - The DisplayPort connection (Display 1) seems to be working better. If possible, try connecting all monitors via DisplayPort.

5. NVIDIA Driver Settings:
   - Since you're using Fedora, you might be using the NVIDIA proprietary driver. If so, add these settings to your X configuration[3]:
     ```
     Option "RegistryDwords" "RMUseSwI2c=0x01;RMI2cSpeed=100"
     ```

6. Update or Downgrade Drivers:
   - Recent NVIDIA driver updates have caused issues with DDC/CI for some users[3]. Consider trying an older driver version (e.g., 525.116.04) if you're on a newer version.

7. Use Alternative Methods:
   - If ddcutil continues to fail, you can try using xrandr for software brightness control:
     ```
     xrandr --output DP-2 --brightness 0.7
     ```
     (Replace DP-2 with the actual output name from xrandr)

8. Check for Updates:
   - Ensure you're using the latest version of ddcutil, as newer versions might have fixes for your specific monitors.

9. Monitor-Specific Settings:
   - Some AOC monitors have a "DDC/CI" option in their OSD menu. Make sure it's enabled on all your monitors.

10. Disable Dynamic Contrast:
    - If your monitors have a Dynamic Contrast feature, try disabling it as it can interfere with brightness control.

If these steps don't resolve the issue, you might need to resort to using the physical buttons on your monitors for brightness control. The fact that one monitor is working suggests that the issue might be related to specific monitor settings or connection types rather than a system-wide problem.

 