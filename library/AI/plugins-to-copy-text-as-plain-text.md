---
title: "Plugins to copy text as plain text"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


If the **Markdown Formatting Assistant** plugin doesn't meet your needs and the other one I mentioned is not available, here are some other approaches and plugins that you could use to achieve **plain text copying** by default in Obsidian:

### **1. Custom JS Plugin / User Script**
If there isn't an existing plugin that directly provides the feature, you can implement a **simple JavaScript-based custom plugin** that will add a plain text copy command to Obsidian. This would require installing the **Templater** or **Advanced Obsidian Scripts** plugins, which can run custom scripts.

### **2. Templater Plugin**
The **Templater** plugin could be used to create a custom command that strips Markdown formatting before copying:

- **Install Templater**:
  - Go to **Settings** > **Community Plugins** > **Browse**.
  - Search for **Templater** and **install** it.

- **Create a Templater Script**:
  - You can create a Templater command that takes the selected text, processes it to strip Markdown formatting, and then copies it to the clipboard as plain text.
  - Add a snippet like the following to handle copying:

  ```js
  <%*
    const selectedText = tp.file.selection();
    const plainText = selectedText.replace(/[*_~`>#+-]/g, ''); // Example regex to remove basic MD symbols
    navigator.clipboard.writeText(plainText);
  %>
  ```

- **Assign a Hotkey**:
  - Assign **`Ctrl + C`** or **`Cmd + C`** to run this Templater command as described before.

### **3. Clipboard Manager (External Tool)**
Since the plugin route appears to be limited, you can use a **system-level clipboard manager** that runs in the background and automatically **strips formatting** from copied text. This is a very effective approach because it allows you to use **plain text copying** across all applications, not just Obsidian:

- **Windows**: Use **ClipClip** or **Ditto**. You can configure these tools to automatically strip all formatting from copied text.
- **Linux**: **CopyQ** or **Clipman** can be configured to manage clipboard content.
  - For **CopyQ**, you could add a rule to remove any Markdown formatting automatically when copying text from Obsidian.
- **Mac**: **Flycut** or **Alfred** can also be used to manage clipboard formatting.

### **4. Create a Custom Command in Obsidian Using CSS Snippets**
- You could create a **CSS snippet** that modifies how text selection is handled within Obsidian. Although this is more of a workaround and doesn’t directly strip Markdown, it could give you a way to visually select only the text without Markdown symbols and copy it.

### **5. Pandoc Integration via Hotkey**
- **Pandoc** can be integrated as a simple command via **a terminal call** using Obsidian’s **hotkey** or **command palette**. You would use Pandoc to convert selected Markdown text into plain text.
  - Create a shell script that uses **Pandoc** to strip the formatting:
  
    ```sh
    echo "$1" | pandoc -f markdown -t plain | xclip -selection clipboard
    ```
  - Create a custom command in Obsidian that triggers this shell script for whatever text is selected.

### **Recommended Plugin for Clipboard Functionality**
While there may not be a direct **clipboard plugin** for plain text copying that matches your request, **Templater** or **system-level clipboard managers** offer a practical and customizable approach.

### **Summary of Options:**
1. **Templater Plugin**: Use **Templater** to create a script that removes Markdown and copies plain text.
2. **Clipboard Manager**: Configure a **clipboard manager** like **CopyQ** (Linux) or **Flycut** (Mac) to always strip formatting.
3. **Pandoc Command via Hotkey**: Use **Pandoc** in combination with a terminal script to automate plain text copying.
4. **Custom Plugin or Script**: You could develop or use a script with **Advanced Obsidian Scripts** to automate this if you have JavaScript knowledge.

If you need further assistance with any of these methods or creating a specific script, let me know! I'm happy to help guide you through the setup.

# Prompt

If I use the javascript approach though won't that slow down the system (because it calls a custom script every time I copy text)?

# Output

You're absolutely right—using a **JavaScript-based custom plugin** (such as with **Templater**) or other scripting approaches might indeed introduce some overhead each time you **copy text**, which could potentially slow down the system or make the copying feel less smooth. This could be noticeable if you’re frequently copying text, especially since it requires running a script every time.

### **Potential Performance Impacts and Considerations**
- **Templater & Custom JavaScript**: Each time you execute a Templater or JavaScript command, it calls an underlying process that takes up **CPU and memory resources**. While for small snippets this overhead might not be huge, it can add a delay when compared to a native copy operation.
- **Running Repeatedly**: Scripts would need to be invoked each time you copy, which means the script has to fetch the selected text, process it, and then interact with the clipboard. This extra step will always take **slightly longer** compared to a direct `Ctrl + C`.

### **Alternatives for Better Performance**
To avoid introducing any performance issues while still achieving the goal of copying **plain text by default**, here are some more **efficient alternatives**:

#### **1. System Clipboard Manager – Preferred Approach**
Using a **system-level clipboard manager** is a lightweight and efficient way to accomplish what you want, without impacting Obsidian’s performance:

- **Benefits**:
  - **Minimal Overhead**: Clipboard managers are usually optimized for performance and can handle clipboard events without noticeable delays.
  - **System-Wide Plain Text**: The clipboard manager operates outside of Obsidian, meaning you can benefit from **plain text pasting** across all applications.

- **Recommended Tools**:
  - **Windows**: **Ditto** or **ClipClip** can be configured to remove all formatting automatically or on a case-by-case basis.
  - **Linux**: **CopyQ** is powerful and allows you to add **scripts** or **rules** to process text copied to the clipboard.
  - **Mac**: **Flycut** or **Alfred** allows customization for copying plain text.

#### **2. Obsidian Plugin Development Request**
If there is no existing plugin that directly does what you need, consider submitting a **feature request** to the **Obsidian community**. Many plugins are community-driven, and there could be interest in developing a plugin that supports copying plain text by default:

- **Obsidian Forum**: Visit the **Obsidian Forum** and post a feature request in the plugin development section.
- **GitHub**: Many plugins are hosted on GitHub, where developers often welcome suggestions for new features.

#### **3. Shortcut Workflow with External Tools**
Another approach would be to use an **automation tool** like **AutoHotkey** (Windows) or **Espanso** (Linux/Mac) to create a custom **copy workflow**:

- **AutoHotkey**:
  - You can create a script in **AutoHotkey** that listens for `Ctrl + C` and automatically removes Markdown formatting when you copy text specifically from Obsidian.
  - This method keeps the processing outside of Obsidian and could be more performant.

  Example **AutoHotkey Script**:
  ```ahk
  ^c::
  Send, ^c
  ClipWait
  ; Regex to remove Markdown symbols from clipboard text
  Clipboard := RegExReplace(Clipboard, "\*|\_|~|\`|#", "")
  return
  ```
  - This script will capture text copied to the clipboard, process it to remove Markdown tags, and then store the cleaned version in the clipboard.

- **Espanso (Linux/Mac)**:
  - You can configure **Espanso** to detect Markdown symbols and replace them when copying text.
  - This is a **more efficient way** since Espanso is specifically designed for real-time text replacement and operates outside of Obsidian.

### **Summary**
- Using **JavaScript-based plugins** like **Templater** might add some overhead and can lead to reduced performance during frequent text copying.
- **System Clipboard Managers** are the most efficient way to achieve plain text copying with minimal impact, and they work across all applications.
- Consider using **AutoHotkey** (Windows) or **Espanso** (Linux/Mac) to create a more automated and seamless plain text copy workflow.
- If no existing plugin suits your needs, submit a **feature request** to the **Obsidian plugin community** for a tailored solution.

Let me know if you’d like more specific help setting up a **clipboard manager** or configuring a **shortcut workflow** for plain text copying!

# Could you estimate the slowdown in miliseconds?

Perhaps the Javascript slowdown wouldn't even be perceptible. Could you estimate what the slowdown might be in miliseconds?

# Output

To estimate the **slowdown** caused by using a **JavaScript script** in **Obsidian** (e.g., via **Templater**) to strip Markdown formatting and copy text as **plain text**, we need to consider a few factors, including **script execution time**, **clipboard interaction**, and the general **processing speed** of JavaScript within Obsidian.

Here’s a breakdown of what contributes to the slowdown and an estimated **range of time in milliseconds**:

### **Components of Script Execution Time**
1. **Script Trigger Time**:
   - Triggering a command from **Templater** involves interacting with the plugin's own event listener. The time taken for this is highly efficient in JavaScript.
   - Estimated Time: **< 1 millisecond**.

2. **Text Selection Handling**:
   - Extracting the selected text from Obsidian’s editor environment (e.g., `tp.file.selection()` in **Templater**) is typically straightforward, especially since Obsidian is optimized for working with text. This is essentially reading a string from memory.
   - Estimated Time: **1-5 milliseconds** (depending on text length and system resources).

3. **Markdown Stripping**:
   - If using **Regex** to strip Markdown syntax from the selected text, the processing time will largely depend on the **length of the text** and the **complexity** of the Regex. However, JavaScript engines are quite efficient at handling such tasks:
   - For a **short text snippet** (less than 1000 characters): Estimated Time: **1-3 milliseconds**.
   - For **longer sections** (several thousand characters): Estimated Time: **3-10 milliseconds**.
   - Markdown stripping is usually fast due to JavaScript’s highly optimized Regex engine.

4. **Clipboard Write Operation**:
   - Writing to the clipboard (`navigator.clipboard.writeText()`) is relatively fast, though there is a small amount of overhead as it requires a system call to interact with the OS clipboard.
   - Estimated Time: **1-3 milliseconds**.

### **Total Estimated Slowdown**
- **Short Text Snippet (Less than 1000 Characters)**:
  - **Total Time**: 
    - Trigger Time: **< 1 ms**
    - Selection Handling: **1-2 ms**
    - Markdown Stripping: **1-3 ms**
    - Clipboard Write: **1-2 ms**
  - **Total Estimated Slowdown**: **3-8 milliseconds**

- **Longer Text Snippet (1000-5000 Characters)**:
  - **Total Time**: 
    - Trigger Time: **< 1 ms**
    - Selection Handling: **1-3 ms**
    - Markdown Stripping: **3-10 ms**
    - Clipboard Write: **1-3 ms**
  - **Total Estimated Slowdown**: **7-17 milliseconds**

### **Is This Noticeable?**
- **Human Perception Threshold**:
  - [ ] The **human eye** and brain can generally notice delays around **100 milliseconds**. Any delay under **20 milliseconds** is usually perceived as instantaneous by most people.
  - Given the **total estimated slowdown** ranges from **3 to 17 milliseconds**, this would be **well below the threshold** where it becomes noticeable in normal usage.

### **Factors Affecting Performance**
1. **Hardware**: 
   - On a modern computer (with a decent CPU), the impact would be minimal. Slower hardware might add a few milliseconds but generally would still be **imperceptible**.
2. **Obsidian Plugin Overhead**:
   - If Obsidian is running many heavy plugins simultaneously, the slowdown could accumulate slightly. However, the script itself is lightweight, and the impact would likely still be unnoticeable unless under extreme load.
3. **Text Length**:
   - For extremely **long documents** (e.g., tens of thousands of characters), there could be a more noticeable lag, but even then, it would likely be under **50 milliseconds**.

### **Conclusion**
The estimated **slowdown** from using a JavaScript script within Obsidian to **copy text as plain text** would likely be between **3 and 17 milliseconds** for typical use cases. This is well below the threshold of perceptible delay for users and would likely feel **instantaneous**.

Thus, while there may technically be a slowdown, it would almost certainly **not be perceptible** in practice. If you're comfortable implementing the JavaScript approach via **Templater** or another plugin, it should provide a smooth experience without noticeable performance issues.