---
title: "Alternate TWMs for Fedora and Wayland l"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Prompt Summary: You are asking whether Sway is the best tiling window manager for Wayland on Fedora.

Sway is indeed one of the most popular and well-regarded tiling window managers for Wayland, especially because it is designed to be a drop-in replacement for i3, which is an X11 tiling window manager. However, whether it's the "best" depends on your specific needs and preferences. Here’s a breakdown of Sway compared to some other Wayland-compatible tiling window managers:

1. Sway

Pros:

Seamless Transition from i3: If you have used i3, Sway will feel very familiar, as it uses almost identical configuration and keybindings.

Wayland-Native: Built from the ground up for Wayland, it is stable, reliable, and well-supported.

Extensible: Supports tools like swaybar, swaylock, and swayidle for a full desktop environment experience.

Good Performance: Efficient and lightweight, suitable for both low and high-end systems.


Cons:

Compatibility: Since it's Wayland-native, some X11-specific features may not work without XWayland.



2. River

Pros:

Dynamic Tiling: Unlike Sway (which is a manual tiler), River offers more dynamic tiling options, which may suit users who want windows to adjust their positions automatically.

Simplicity: Highly minimal and lightweight, with a focus on simplicity.

Customizability: River uses a client-server model, which can be controlled and scripted externally.


Cons:

Newer and Less Mature: May not have as many features or as stable as Sway.



3. Hyprland

Pros:

Extremely Customizable: Offers features like window animations, custom tiling layouts, and more fine-grained control than Sway.

Eye Candy for Tiling WM: Supports advanced graphical features like rounded corners, drop shadows, and blur, which are rare in tiling WMs.

Active Development: Quickly growing in popularity with an active development community.


Cons:

Can Be More Resource-Intensive: The visual features make it heavier than more minimal managers like Sway.

Setup Complexity: Requires more configuration than Sway for basic usage.



4. Wayfire + wf-shell (Plugin-Based)

Pros:

Highly Modular: Uses a plugin system, allowing you to enable only the features you need.

Can Be Used as a Tiler: Not a pure tiling WM, but can be configured for tiling behavior.

Good for Hybrid Use: Supports both tiling and floating layouts.


Cons:

Not a True Tiling WM: You’ll need to customize it more to achieve a fully tiling experience.



5. dwl (Dynamic Window Layout)

Pros:

Based on DWM: Similar philosophy to DWM, focusing on minimalism and simplicity.

Wayland-Compatible: Lightweight and efficient, designed for users who prefer a minimal setup.


Cons:

Requires Patching for Customization: Much like DWM, you will need to patch and rebuild for custom features.



Conclusion

Sway is likely the best choice if you:

Want a reliable, well-supported tiling window manager that feels like i3.

Prefer stability and ease of setup, with a good mix of features out-of-the-box.

Don’t need flashy visuals but want solid performance and customization options.


Consider other options if you:

Want more visual customization or dynamic tiling (Hyprland).

Are looking for a simpler, more minimal solution (River or dwl).

Prefer modularity and a hybrid tiling/floating experience (Wayfire).


Overall, Sway offers the most mature and comprehensive Wayland-native tiling experience on Fedora. It is straightforward to set up, highly configurable, and balances performance with usability. However, trying out different options might give you a better sense of what works best for your workflow. Let me know if you'd like more details on any of these!

