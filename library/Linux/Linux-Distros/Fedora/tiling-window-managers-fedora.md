---
title: "Tiling window managers Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Are there any tiling window managers that can be used on Fedora and in conjunction with kde plasma or in addition to it?

# Output

Yes, there are several tiling window managers that can be used with Fedora and integrated with KDE Plasma. Here are some options:

1. KWin Tiling Script: 
KDE Plasma's default window manager, KWin, has built-in tiling capabilities that can be enabled through scripts. While not as full-featured as dedicated tiling managers, it provides basic tiling functionality within the KDE environment[1].

2. Polonium:
This is a successor to the popular Bismuth plugin. Polonium allows you to turn your Plasma desktop into a tiling window manager. It's specifically designed for KDE Plasma and works well with Wayland[5].

3. i3:
i3 is one of the most popular standalone tiling window managers. While it's typically used on its own, it can be integrated with KDE Plasma. Fedora even offers an i3 Spin, making installation straightforward[6].

4. bspwm:
Another lightweight tiling window manager that can be used alongside KDE Plasma. It's known for its flexibility and can be configured to work with Plasma's components[1][2].

5. Qtile:
Qtile is a tiling window manager written in Python. It can be installed on Fedora and potentially integrated with KDE Plasma, though it may require more configuration[3][4].

6. awesome:
Originally a fork of dwm, awesome is another tiling window manager that can potentially be used with KDE Plasma. It's highly customizable using Lua scripts[4].

To use these tiling window managers with KDE Plasma, you'll generally need to replace KWin with your chosen tiling manager. This process usually involves creating a custom Plasma session that uses the tiling manager instead of KWin. 

Keep in mind that integrating a different window manager with KDE Plasma may require some configuration and troubleshooting to ensure all Plasma components work correctly with the new window manager. The level of integration and potential issues can vary depending on the specific tiling manager you choose.

 