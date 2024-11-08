---
title: "Why DDC might be unavailable on a display"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you think of some other reasons why DDC might not be working? Let's assume the cable is ok

# Output

If the cable is fine, here are some other potential reasons why **DDC/CI** might not be working:

1. **Monitor Setting Disabled**: DDC/CI may be disabled in the monitor’s OSD (on-screen display) settings. Ensure it’s turned on.
2. **Compatibility Issues**: Some monitor inputs (e.g., specific HDMI ports) may not support DDC/CI, even if other inputs like DisplayPort do.
3. **GPU Driver**: Outdated or incompatible GPU drivers can interfere with DDC/CI functionality.
4. **Wayland Restrictions**: Some versions of Wayland restrict DDC/CI communication, which works better under X11.
5. **Power-saving Mode**: Monitors in power-saving modes may disable DDC/CI.

These could impact DDC/CI functioning.