---
title: "What is xwayland and how to use it"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 
### What is XWayland?

**XWayland** is a compatibility layer that allows **X11** applications to run on **Wayland**-based desktop environments like **KDE Plasma** and **GNOME**. Since Wayland is a more modern display protocol, many legacy X11 applications do not natively support it. XWayland provides an X11 server that runs within the Wayland session, allowing these older applications to function seamlessly on Wayland, without needing to rewrite them for Wayland.

In simpler terms:
- **Wayland** is the new display server protocol that is more secure and modern.
- **X11** is the older protocol that many applications are built to support.
- **XWayland** acts as a bridge, letting older X11 apps work on Wayland-based desktops.

### Why Use XWayland?

While Wayland offers several advantages, like better security and smoother graphics rendering, many applications, especially older ones or those requiring deep hardware access, still rely on X11. For example:
- Some **DDC/CI tools** like `ddcutil` may not work directly with Wayland, but they might work via XWayland.
- Certain **graphics-intensive applications** (e.g., older games) or **development tools** may also only run on X11.

Using XWayland allows you to run these applications in a Wayland session without fully switching back to an X11 session.

### How to Use XWayland

#### 1. **Run Applications Under XWayland Automatically**
Most desktop environments like KDE Plasma or GNOME on Wayland will automatically run legacy X11 applications using XWayland. When you launch an X11-based application on a Wayland session, it will transparently start under XWayland without any additional setup.

For example:
- Run an X11-based app like `xeyes` or an older GUI app:
   ```
   xeyes
   ```
   It will automatically run in an XWayland window within your Wayland session.

You can verify this by checking which display server is being used:
- Open the terminal and run:
   ```
   echo $WAYLAND_DISPLAY
   ```
   If you see something like `wayland-0`, you're on Wayland.

Now check the same for an X11-based app:
   ```
   echo $DISPLAY
   ```
   If you see something like `:0`, the application is running in XWayland (within your Wayland session).

#### 2. **Force an Application to Run Under XWayland**
Some applications may require specific flags or variables to ensure they run under XWayland. You can force an application to use XWayland by setting the `GDK_BACKEND` environment variable to `x11` when launching it.

For example, if you want to run **Firefox** under XWayland:
   ```
   GDK_BACKEND=x11 firefox
   ```

This forces Firefox to use XWayland, even though it natively supports Wayland.

#### 3. **Detecting If an Application Is Using XWayland**
You can check if an application is running under XWayland by using the following methods:

- **Check via terminal**: Run `xprop` on the window and look for properties that indicate it's using X11.
   ```
   xprop | grep -i Xwayland
   ```
   If the output mentions `Xwayland`, the app is running in XWayland.

- **KDE Plasma Wayland System Monitor**: You can open the **KSysGuard** system monitor, and for certain applications, it will show if they are running in XWayland or Wayland.

#### 4. **Handling XWayland Settings**
XWayland has limited configuration options compared to a full X11 server. Most of the time, you won’t need to configure anything. However, if you need to customize things like **input devices** or **window handling**, it’s usually done via your Wayland compositor (like **KWin** in KDE or **Mutter** in GNOME).

#### 5. **Wayland-Native Apps vs XWayland Apps**
Not all applications will perform equally well on XWayland. Some performance-sensitive apps, like games, might have better support when running natively on Wayland, while older apps might benefit from XWayland.

You can test the performance difference between Wayland and XWayland to see which works best for your workflow.

### Practical Example: Using `ddcutil` with XWayland

If you're having trouble using `ddcutil` (or other tools) in Wayland, try running them under XWayland:

1. Open a terminal.
2. Run:
   ```
   GDK_BACKEND=x11 ddcutil detect
   ```
   This forces `ddcutil` to run using XWayland, which might help it work more reliably on Fedora Workstation 40 with KDE Plasma.

### Conclusion

**XWayland** allows you to run legacy X11 applications on a modern Wayland environment without needing to switch back to a full X11 session. It's automatically used for most applications, but you can force certain apps to use it if needed. This is especially useful for tools and applications that don't yet fully support Wayland, allowing you to take advantage of the security and performance benefits of Wayland while maintaining compatibility with older software.