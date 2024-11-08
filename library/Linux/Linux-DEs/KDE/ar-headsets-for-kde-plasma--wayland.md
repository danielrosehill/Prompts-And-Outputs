---
title: "AR headsets for KDE Plasma + Wayland"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You asked whether there are any AR headsets that support working with KDE Plasma and Wayland (Fedora).

As of now, support for AR headsets on Linux, especially with KDE Plasma and Wayland, is relatively limited, and most AR devices are primarily targeted toward Windows or macOS environments. However, there are some potential options:

1. **OpenHMD**: This is an open-source project aimed at supporting a variety of VR/AR headsets on Linux. While it primarily supports VR, it's evolving to handle more AR devices. Headsets like the **Microsoft HoloLens** might eventually be supported through open-source drivers, though integration with KDE Plasma and Wayland might require additional customization and effort.

2. **Nreal Light**: Nreal provides AR glasses that run on Android and have Linux driver support through community efforts. However, the support is rudimentary and may not offer full integration with KDE Plasma and Wayland without some manual setup and development.

3. **Valve Index (Experimental)**: Although primarily a VR headset, there is some support through platforms like SteamVR on Linux. You can experiment with AR-like setups using KDE Plasma on X11, but Wayland support is still evolving in terms of compatibility with such hardware.

Right now, none of the mainstream AR devices officially support Wayland and KDE Plasma natively, and most efforts are either community-driven or in the experimental stage. For serious work with AR on Fedora, you might need to rely on developing or tweaking drivers and software.