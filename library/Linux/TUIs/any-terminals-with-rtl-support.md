---
title: "Any terminals with RTL support"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Are there any terminal environments that support RTL text easily? I saw that newsboat was having a hard time rendering the text properly

# Output

Rendering **Right-to-Left (RTL)** text in terminal environments can indeed be a challenge, as many terminal emulators and text-based applications are not optimized for RTL languages like Hebrew, Arabic, or Persian. Unfortunately, many popular terminal applications and TUIs (including **Newsboat**) do not natively support RTL text rendering very well.

However, there are some approaches and terminal environments that can provide **better support** for RTL text, though solutions tend to be limited in scope and may require specific setups.

### Terminal Emulators with Better RTL Support

1. **mlterm** (Multilingual Terminal Emulator)
   - **Description**: `mlterm` is one of the few terminal emulators specifically designed to support **multilingual text rendering**, including **RTL languages**. It provides better support for complex scripts and bidirectional text.
   - **Features**:
     - Native support for **Right-to-Left (RTL)** text.
     - Handles bidirectional text better than most terminal emulators.
     - Supports **combining characters** and **ligatures**.
   - **Installation**:
     ```bash
     sudo dnf install mlterm
     ```
   - **Usage**: Simply launch `mlterm` and use it like any other terminal emulator. Applications running inside it may still need tweaks, but `mlterm` should handle RTL text better than most alternatives.

2. **Konsole** (KDE Terminal Emulator)
   - **Description**: **Konsole**, the terminal emulator for the KDE desktop, provides somewhat better support for RTL text compared to other terminal emulators.
   - **Features**:
     - Partial RTL support.
     - Customizable profiles with support for UTF-8 encoding.
   - **Installation**:
     ```bash
     sudo dnf install konsole
     ```
   - **Usage**: Launch `konsole` and try rendering RTL text. It works better for UTF-8 encoded text, but some terminal-based applications may still not render properly.

3. **iTerm2** (macOS Only)
   - **Description**: If you're on **macOS**, **iTerm2** provides some support for RTL text, although it is not perfect.
   - **Installation**: Available only on macOS via the [iTerm2 website](https://iterm2.com/).
   - **Usage**: Run applications that require RTL text in iTerm2 for slightly improved RTL handling, but the results may still be inconsistent depending on the application.

### Workarounds for RTL in Terminal Applications

1. **Bidi Unix (Bi-directional text support)**:
   - **Description**: **Bidi Unix** is a project that adds **bidirectional text support** to Unix-based systems, which is otherwise missing in most terminal emulators. It's a set of patches and tools that can help make terminals behave better with RTL text.
   - **Setup**: This requires custom patches to your terminal emulator or applications, so it can be quite involved. It’s worth exploring for environments where RTL is critical.
   - **Project**: [Bidi Unix](https://github.com/yazdipour/BidiUnix)

2. **Unicode Support with tmux or screen**:
   - **Description**: Terminal multiplexers like **tmux** or **screen** can be configured to work with **UTF-8** text. While they don’t inherently provide RTL text rendering, they ensure that characters are handled correctly, which can sometimes improve how text is displayed.
   - **Setup**: 
     - Ensure that **UTF-8** is enabled in your terminal.
     - Use `tmux` with UTF-8 support:
       ```bash
       tmux -u
       ```

3. **Using GUI-based Alternatives for Better RTL Support**
   If rendering RTL text in a terminal-based TUI is critical and you're experiencing severe issues with RTL text rendering in tools like **Newsboat**, you may want to explore **GUI-based applications** like:

   - **Liferea**: A desktop RSS reader that supports RTL text better because it relies on GTK (a GUI toolkit).
     ```bash
     sudo dnf install liferea
     ```
   - **Miniflux**: A web-based RSS reader that supports RTL text and can be run on a local server.
     - [Miniflux GitHub](https://github.com/miniflux/v2)

### Why RTL Text Rendering is Difficult in Terminals
- **Bi-directional Text Issues**: Terminals are traditionally designed to handle **Left-to-Right (LTR)** text. Implementing support for **Bi-directional (Bidi)** text requires significant changes in how text is processed and displayed.
- **Limited Font and Unicode Handling**: Terminals are limited by the fonts and encoding they use. **UTF-8** support is crucial, but many terminal applications do not handle combining characters or bidirectional text properly.
- **Applications Not Built for RTL**: Many terminal-based applications are not built with RTL support in mind, and often the logic for text direction needs to be implemented at the application level.

### How to Improve RTL Experience in Terminals

1. **Use Proper Fonts**: Ensure that you're using a terminal font that supports Unicode and RTL languages.
   - Fonts like **Noto Sans** or **DejaVu Sans Mono** are good options for RTL text.
   - In `mlterm`, you can specify a proper RTL-compatible font.

2. **Set the Locale to Support UTF-8**: Make sure your system locale is set to a UTF-8 capable language.
   ```bash
   export LANG=en_US.UTF-8
   ```

3. **Browser-based Alternatives**: When terminal-based solutions fail, using **text-based web browsers** like **w3m** or **lynx** for browsing RTL-heavy websites can help, but you'll lose out on some text formatting.

   Example of using `w3m` to browse an RTL website:
   ```bash
   w3m https://example.com
   ```

   While it won't handle RTL perfectly, you can test it to see if it fits your use case.

### Conclusion:
- **mlterm** is the best terminal emulator option for handling RTL text in a native terminal environment.
- **Konsole** offers partial support for RTL but may still struggle in complex cases.
- GUI-based tools like **Liferea** or web-based RSS readers like **Miniflux** may provide better RTL support if you run into major rendering issues with terminal tools.
- If RTL text rendering is critical and consistent behavior is required, it’s often better to rely on GUI-based solutions, as terminal environments are traditionally weak at handling RTL and complex text layouts.