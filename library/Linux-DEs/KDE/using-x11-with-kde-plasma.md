---
title: "Using X11 with KDE Plasma"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I like KDE Plasma. Is there a way to use it with X11?

# Output

Yes, you can use KDE Plasma with X11 instead of Wayland. Here's how to switch your session to X11 while keeping KDE Plasma:

### Steps to Use KDE Plasma with X11:

1. **Log Out of Your Current Session**:
   - First, log out of your current Wayland session.

2. **Select X11 from the Login Screen**:
   - On the **login screen** (SDDM by default in Fedora with KDE Plasma), before entering your password:
     - Look for a **session type selector** (often at the bottom of the screen or in a dropdown).
     - Select **"Plasma (X11)"** or **"KDE Plasma (X11)"**. This option will switch your session to X11.
   
3. **Log In**:
   - Enter your password and log in as usual.
   - Your KDE Plasma desktop will now be running on X11 instead of Wayland.

### Make X11 the Default (Optional):
If you prefer to always use X11 for KDE Plasma:
   - Fedora will typically remember your session choice, so the next time you log in, it will default to X11.
   - If it doesn’t, you can change the default session by editing your display manager's configuration (SDDM), but manually choosing X11 during login should usually be enough.

This approach should allow you to use DDC/CI tools like `ddcutil` more reliably, as they tend to work better under X11.