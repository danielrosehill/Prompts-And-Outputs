---
title: "Making sure it's safe to explore Sway"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm worried that if I install sway it will take over my whole DE but the nesting idea is interesting. Installing the package won't automatically change me over to it .. or running it nested?

# Output
You're right to be cautious, but **installing Sway** will not automatically take over your desktop environment (DE), and running Sway in a nested session will not affect your KDE Plasma environment either. Here's how it works in detail:

### What Happens When You Install Sway:

1. **Installing the Sway package**: Installing Sway via `dnf` will simply place the Sway binaries and associated files on your system. It won't change your default desktop environment or modify any system settings.

   To install Sway, you can run:
   ```bash
   sudo dnf install sway
   ```

   After installing Sway, **nothing will change** about your current KDE Plasma session. It will not automatically switch you to Sway on reboot or log out. 

2. **Running Sway Nested**: When you run Sway in nested mode, it operates **as a window** within your current KDE Plasma session. This means you can experiment with Sway and its tiling features without leaving KDE Plasma or affecting the rest of your desktop.

   To run Sway nested, use:
   ```bash
   sway --nested
   ```

   This will open a Sway session inside a single window on your KDE Plasma desktop. You can tile applications, test its features, and use it alongside your regular KDE workflow without any risk to your current setup.

### Key Points:
- **Installing Sway** won’t automatically switch your default session to Sway.
- **Running Sway** via the `sway --nested` command opens it inside a window on your KDE Plasma desktop.
- You can continue using KDE Plasma as your primary DE and switch back to it anytime after closing the nested Sway session.
- If you ever want to try a full Sway session, you can simply log out of KDE and choose "Sway" as a session in your login manager, but this is purely optional.

### Benefits of Sway in Nested Mode:
- You can test and configure Sway's tiling features without leaving KDE Plasma.
- It provides a sandboxed environment for tiling, useful for organizing specific apps or workflows.
- You can close the nested Sway window anytime and go back to KDE Plasma without rebooting or logging out.

### How to Uninstall Sway (if needed):
If you ever want to remove Sway from your system, you can uninstall it with:
```bash
sudo dnf remove sway
```

Would you like to proceed with this, or would you prefer more details on nesting Sway with some specific applications?
