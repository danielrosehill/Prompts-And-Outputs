---
title: "How to launch Obsidian and ChatGPT in split screen"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use Fedora Linux with Wayland + KDE Plasma

Can you help me configure a rule that will allow me to easily launch these two programs in a split screen on a specific monitor?

/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx

obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub


# Output 

Certainly! The approach I provided earlier works, but there are some more efficient ways to automate launching applications in split-screen mode, especially when working with KDE Plasma on Wayland. Below are some improved and modernized approaches, utilizing more direct automation and powerful scripting tools available in KDE.

### Improved Approach Using KDE KWin Scripts
KWin, the window manager for KDE, supports scripting using JavaScript. You can write a script that will automate window management tasks such as opening specific applications in a particular position on a specific monitor.

Here’s how you can set this up:

#### Step 1: Install `konsave`
**`konsave`** is a powerful tool to save and load KDE Plasma desktop configurations, including window rules, layouts, and more. This can be a great way to save a complete setup and restore it as needed.

To install `konsave`, use the following command:

```bash
pip install konsave
```

#### Step 2: Write a KWin Script
If `konsave` doesn’t meet your needs, you can write your own KWin script. This gives you finer control over how your applications are handled. 

##### Example KWin Script
1. **Create a KWin Script File:**

Create a new KWin script file:

```bash
mkdir -p ~/.local/share/kwin/scripts/split_launcher
nano ~/.local/share/kwin/scripts/split_launcher/metadata.desktop
```

Add the following content to `metadata.desktop`:

```ini
[Desktop Entry]
Name=Split Launcher
Comment=Launch Chrome and Obsidian in split-screen
Type=Service
X-KDE-ServiceTypes=KWin/Script
```

Save and exit (`CTRL + X`, `Y`, `Enter`).

2. **Create the JavaScript File for the Script:**

Next, create a JavaScript file for the logic of the KWin script:

```bash
nano ~/.local/share/kwin/scripts/split_launcher/contents/code/main.js
```

Add the following JavaScript code to `main.js`:

```javascript
function main() {
    // Run the applications
    callDBus(
        "org.kde.KWin",
        "/KWin",
        "org.kde.KWin.Scripting",
        "loadScript",
        "/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx"
    );
    callDBus(
        "org.kde.KWin",
        "/KWin",
        "org.kde.KWin.Scripting",
        "loadScript",
        "obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub"
    );

    // Get the screen width and height to split into two
    var screen = workspace.clientArea(KWin.WorkArea, workspace.activeScreen, 0);
    var halfWidth = screen.width / 2;

    // Get the application clients
    var clients = workspace.clientList();
    clients.forEach(function (client) {
        if (client.resourceClass === "chrome" || client.resourceClass === "obsidian") {
            if (client.resourceClass === "chrome") {
                // Place Chrome on the left half
                client.geometry = {
                    x: screen.x,
                    y: screen.y,
                    width: halfWidth,
                    height: screen.height,
                };
            } else if (client.resourceClass === "obsidian") {
                // Place Obsidian on the right half
                client.geometry = {
                    x: screen.x + halfWidth,
                    y: screen.y,
                    width: halfWidth,
                    height: screen.height,
                };
            }
        }
    });
}

// Connect main function to relevant signal for automatic execution
workspace.clientAdded.connect(main);
```

Save the file and exit (`CTRL + X`, `Y`, `Enter`).

#### Step 3: Enable Your Script
Now that you've created the KWin script, you need to enable it in the KDE System Settings.

1. Open **System Settings** -> **Window Management** -> **KWin Scripts**.
2. Click on **Get New Scripts** to load custom scripts.
3. Select and enable the **Split Launcher** script.

This script will automatically adjust Chrome and Obsidian windows to split-screen whenever they are launched.

### Alternative - Use KDE Activities or `Krohnkite` Extension
Another improved method to consider:

#### 1. KDE Activities
- You can create a dedicated **KDE Activity** for Chrome and Obsidian and configure specific window rules that always open these applications in a split-screen arrangement.
- Activities in KDE Plasma are like separate work environments. You can set an activity for a focused setup and switch between them quickly, making it more organized and less cluttered.

#### 2. **Krohnkite** Extension for Tiling Window Management
- **Krohnkite** is an excellent tiling window manager extension for KDE Plasma that works similarly to tiling window managers like **i3** or **Awesome** but integrates natively with KDE.
- Install **Krohnkite** by going to **System Settings** -> **Window Management** -> **KWin Scripts** -> **Get New Scripts** and searching for "Krohnkite".
- Once installed, you can configure specific rules to tile Chrome and Obsidian in split-screen when they are opened. **Krohnkite** can be easily set to automatically tile these windows without manual resizing.

### Summary of the Improved Approaches
1. **Use `konsave`** to save and restore layouts, including launching and tiling apps like Chrome and Obsidian.
2. **Write a KWin JavaScript script** that automatically launches and tiles Chrome and Obsidian into a split-screen.
3. **KDE Activities** to create a dedicated workspace for these applications.
4. **Krohnkite Extension** for tiling window management with automatic layouts.

These methods provide more flexible, automated, and integrated solutions for managing your desktop environment efficiently. The **KWin JavaScript approach** provides the most customizability, while **Krohnkite** gives you a powerful tiling solution without scripting.