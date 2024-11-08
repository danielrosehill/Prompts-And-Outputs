---
title: "Tiling window managers for Fedora ranked by popularity"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you give me a list of tiling window managers for Fedora Linux organised by the popularity, from most to least popular. For each please provide some notes about the estimated user base and popularity of the project

# Output

Here is a list of some of the most popular **tiling window managers** (TWMs) for **Fedora Linux**, organized by popularity, along with notes about their estimated user base and general popularity:

### 1. **i3**
   - **Popularity**: Widely regarded as one of the most popular tiling window managers across many Linux distributions, including Fedora.
   - **Estimated user base**: Large, with a significant community across GitHub, Reddit, and Arch/Fedora communities.
   - **Why it's popular**: i3 is known for being **lightweight**, **simple**, and **highly configurable**. Its **manual tiling** system appeals to users who want precise control over their window layouts. Many users also appreciate its intuitive keybindings and the straightforward configuration file.
   - **GitHub stars**: Over 7k stars.
   - **Notes**: i3 also has a fork called **Sway**, which supports Wayland, making it popular among users looking to transition away from X11.
   - **Website**: [i3](https://i3wm.org/)

### 2. **bspwm**
   - **Popularity**: Considered the second-most popular tiling window manager by many, especially in Arch and Fedora communities.
   - **Estimated user base**: Medium-to-large user base, especially among more experienced users who prefer minimalism and manual control over their window manager.
   - **Why it's popular**: **bspwm** is minimal, scriptable, and powerful. It uses **bspc**, a dedicated client, to manage the windows, and it’s favored by users who want full control over their environment, as it requires scripting for complex features.
   - **GitHub stars**: Over 6k stars.
   - **Notes**: Highly customizable but can require more setup compared to i3.
   - **Website**: [bspwm](https://github.com/baskerville/bspwm)

### 3. **Sway**
   - **Popularity**: Gaining significant traction due to its support for **Wayland**, making it a popular choice for users moving away from X11.
   - **Estimated user base**: Growing fast, particularly among users interested in Wayland-based window management. It’s especially popular among users coming from i3, as it shares the same configuration syntax.
   - **Why it's popular**: **Sway** is a drop-in replacement for i3, designed for the Wayland display server. It offers all the familiar features of i3, with the benefit of modern Wayland support.
   - **GitHub stars**: Over 12k stars.
   - **Notes**: It is becoming the **go-to** tiling manager for Wayland, making it the future-proof choice.
   - **Website**: [Sway](https://swaywm.org/)

### 4. **AwesomeWM**
   - **Popularity**: Very popular, especially for users who want a more **flexible** and **dynamic** window manager.
   - **Estimated user base**: Large, especially among those who prefer Lua for customization.
   - **Why it's popular**: **AwesomeWM** offers **dynamic tiling**, meaning windows are automatically arranged based on rules. It’s also highly customizable with Lua, making it great for users who want a programmable window manager.
   - **GitHub stars**: Over 5k stars.
   - **Notes**: **AwesomeWM** appeals to advanced users and those who want a blend of manual and automatic tiling.
   - **Website**: [AwesomeWM](https://awesomewm.org/)

### 5. **Xmonad**
   - **Popularity**: Popular, especially among more advanced users who are comfortable with Haskell.
   - **Estimated user base**: Medium-sized but with a dedicated and technically savvy user base.
   - **Why it's popular**: **Xmonad** is known for being **extremely lightweight** and highly customizable via Haskell. It offers a lot of flexibility but requires programming knowledge to set up and modify.
   - **GitHub stars**: Over 2.5k stars.
   - **Notes**: Appeals to users who prefer scripting and advanced customizations.
   - **Website**: [Xmonad](https://xmonad.org/)

### 6. **herbstluftwm**
   - **Popularity**: Less popular than i3 or bspwm, but still well-regarded in the community.
   - **Estimated user base**: Small-to-medium, with a niche user base.
   - **Why it's popular**: **herbstluftwm** is known for its **manual tiling** and **easy configuration** via bash scripts. It provides a balance between flexibility and simplicity, but its user base remains smaller compared to more mainstream TWMs.
   - **GitHub stars**: Over 1k stars.
   - **Notes**: It appeals to users looking for a scripting-friendly, dynamic manager that isn’t as bare-bones as bspwm.
   - **Website**: [herbstluftwm](https://herbstluftwm.org/)

### 7. **dwm (Dynamic Window Manager)**
   - **Popularity**: Popular among users who want a minimal, highly customizable tiling window manager.
   - **Estimated user base**: Medium, especially among power users who appreciate the **extreme minimalism** and are comfortable with modifying the source code.
   - **Why it's popular**: **dwm** is extremely minimalistic, but it requires modifying and recompiling the source code to configure it. This appeals to users who like total control but are willing to go the extra mile.
   - **GitHub stars**: N/A (patches and forks are found on GitHub, but the main project is hosted independently).
   - **Notes**: It's perfect for users who want a simple, no-frills experience and are comfortable working with C.
   - **Website**: [dwm](https://dwm.suckless.org/)

### 8. **Qtile**
   - **Popularity**: A niche window manager, but gaining traction due to its flexibility with Python scripting.
   - **Estimated user base**: Small but growing, particularly among Python developers.
   - **Why it's popular**: **Qtile** is written and configured in Python, making it appealing to users who want a tiling window manager with easy-to-read and modifiable code.
   - **GitHub stars**: Over 3k stars.
   - **Notes**: Popular with Python enthusiasts, but less so outside that crowd.
   - **Website**: [Qtile](http://www.qtile.org/)

### 9. **spectrwm**
   - **Popularity**: Less popular than the others, but it has a loyal following for being fast and lightweight.
   - **Estimated user base**: Small, typically among users who prefer ultra-minimal setups.
   - **Why it's popular**: **spectrwm** is designed to be fast, minimal, and efficient. It requires minimal configuration and is inspired by **xmonad** and **dwm**, but with simpler configuration.
   - **GitHub stars**: Over 700 stars.
   - **Notes**: Not as customizable as other TWMs, but very resource-efficient.
   - **Website**: [spectrwm](https://github.com/conformal/spectrwm)

### Summary:
1. **i3** and **Sway** dominate the popularity ranking due to their widespread use, simplicity, and flexibility, especially with Wayland support growing for Sway.
2. **bspwm** and **AwesomeWM** follow as they offer greater control for more experienced users.
3. **Xmonad** and **dwm** have niche, dedicated user bases, particularly among developers who appreciate scripting and extreme minimalism.

Would you like installation or configuration help with any of these?