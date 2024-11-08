---
title: "Tiling window managers for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use Fedora + KDE Plasma. I've used tiling window managers before, although I wouldn't want to go back to using one as my daily DE. What I would like to do, however, is have a program that runs as a kind of "tile" that I could dedicate one of my screens to and drag programs into it and then set them up in an array. If I could save the layout for later use it would be even more ideal. Can you think of any such program?

# Output

Based on your requirements and the context of using Fedora with KDE Plasma, there are a few options that might suit your needs:

1. KWin Scripts:
KDE Plasma's window manager, KWin, supports scripting that can enhance its tiling capabilities. While not a separate program, you can use KWin scripts to create custom tiling layouts on specific screens or areas[1].

2. Polonium:
This is a successor to the popular Bismuth plugin for KDE Plasma. Polonium allows you to turn parts of your Plasma desktop into a tiling window manager. You could potentially configure it to work on just one screen, giving you the tiling functionality you desire without changing your entire desktop environment[1].

3. Krohnkite:
Another KWin script that adds tiling window management to KDE. It can be configured to work on specific screens or activities, which might fit your use case[1].

4. Tiling Assistant:
This is a GNOME extension, but it's worth mentioning as it mimics the Windows 11 tiling behavior. While it's not native to KDE, it demonstrates the kind of functionality you're looking for. You might find a KDE equivalent or be able to adapt a similar concept[4].

5. Custom Solution:
Given your specific requirements, you might consider developing a custom KWin script or Plasma widget that allows you to define a "tile area" on one screen where you can drag windows and arrange them in a tiled layout. This would give you the most control over the functionality and allow you to implement features like saving layouts.

To save layouts for later use, you might need to combine one of these tiling solutions with a custom script or application that can remember window positions and sizes. KDE's window rules can also be helpful in automatically positioning windows in specific locations on startup.

Remember that while these solutions can provide tiling functionality within KDE Plasma, they may not offer the full power of a dedicated tiling window manager. However, they should allow you to create a tiling area on one screen without compromising your overall desktop environment experience.

 