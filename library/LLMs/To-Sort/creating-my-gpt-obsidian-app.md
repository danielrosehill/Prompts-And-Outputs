---
title: "Creating my GPT Obsidian app"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

My goal is to develop an "app" which offers a split screen functionality. Obsidian will be on the left and on the right there will be a ChatGPT window (a PWA). Can you suggest how I might create that for Fedora?

# Output

Given that you're using **Wayland** and window management solutions were unsuccessful, here’s a revised approach for creating a split-screen "app" with **Obsidian** on the left and **ChatGPT PWA** on the right, while avoiding window management-only methods:

### 1. **Electron-Based Custom Application with Native Application Launching**
You can create a custom **Electron** app that launches both the **Obsidian** desktop client and the **ChatGPT PWA**. Since Wayland does not support some of the traditional X11-based window management techniques, this method would combine both applications within an Electron framework, ensuring compatibility with your setup.

**Steps**:
1. **Install Electron**:  
   You can install Electron using `npm`:
   ```bash
   npm install electron
   ```

2. **Create an Electron Project**:
   You can use Electron to create a custom app with two panes: one for the **Obsidian** desktop client and the other for loading **ChatGPT** as a web view. Electron can handle native applications and web content side by side.

**Basic Electron Script**:
This script will create a split-screen window, launching **Obsidian** on the left and embedding **ChatGPT** on the right.

```js
const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');

function createWindow() {
  // Create the main browser window
  let win = new BrowserWindow({
    width: 1600,
    height: 900,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
      enableRemoteModule: true
    }
  });

  // Load a custom HTML file that includes the split view
  win.loadFile('index.html');

  // Launch the Obsidian app on the left
  exec('obsidian', (err, stdout, stderr) => {
    if (err) {
      console.error(`Error launching Obsidian: ${stderr}`);
    }
  });
}

app.whenReady().then(() => {
  createWindow();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
```

3. **Create the `index.html` file**:
   In this HTML file, one pane will launch the **Obsidian** app and the other will display the **ChatGPT PWA**.

```html
<!DOCTYPE html>
<html>
<head>
  <title>Obsidian + ChatGPT</title>
  <style>
    body {
      display: flex;
      height: 100vh;
      margin: 0;
    }
    #left, #right {
      flex: 1;
      height: 100%;
    }
    #right iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
  </style>
</head>
<body>
  <div id="left">
    <h1>Obsidian Running as a Native App</h1>
    <!-- Obsidian runs as a native process, no need to embed here -->
  </div>
  <div id="right">
    <iframe src="https://chat.openai.com"></iframe> <!-- ChatGPT PWA on the right -->
  </div>
</body>
</html>
```

4. **Run the App**:
   Once you've set up the project, you can run the app using Electron. The left pane will launch **Obsidian** as a native application, and the right will embed the **ChatGPT PWA** inside the Electron window.

```bash
electron .
```

### 2. **Using `Nativefier` for ChatGPT PWA with Script to Launch Obsidian**:
If you want a simpler solution, you could use **Nativefier** to create a standalone desktop app for ChatGPT, while using a script to launch both **Obsidian** and the Nativefier app together in a pseudo-split-screen fashion.

**Steps**:
1. **Install Nativefier**:
   Install Nativefier via npm:
   ```bash
   npm install -g nativefier
   ```

2. **Create the ChatGPT App**:
   Use Nativefier to package the ChatGPT PWA into a standalone desktop application:
   ```bash
   nativefier --name "ChatGPT" "https://chat.openai.com"
   ```

3. **Script to Launch Both**:
   Create a script to launch both **Obsidian** and the **ChatGPT Nativefier app**. Since window management didn’t work for you, the split will have to be manually arranged by opening both apps, but this provides a close approximation.

```bash
#!/bin/bash
# Launch Obsidian as the desktop client
obsidian &

# Launch the ChatGPT Nativefier app
./ChatGPT-linux-x64/ChatGPT &
```

While this isn’t true split-screen functionality, it’s a way to run both apps side by side with the apps being distinct processes.

### 3. **Custom GTK or Qt App** (Advanced, Full Control)
If you're looking for deeper customization, you can develop a custom **GTK** or **Qt** application specifically for Wayland that embeds **Obsidian** as a native application in one pane and **ChatGPT** in a webview on the other.

**GTK/Qt** are highly configurable and Wayland-compatible frameworks for creating Linux desktop apps. With this method, you could create a custom UI with split-screen behavior directly integrated.

- **GTK (for GNOME environments)**:
  Use **GtkPaned** for the split-screen layout, with one side running **Obsidian** and the other using **WebKitGTK** to display ChatGPT.

- **Qt (for KDE environments)**:
  Use **QSplitter** for the same purpose, with one side being a native app container and the other embedding **QWebEngineView** to load ChatGPT.

This approach requires more in-depth programming knowledge but provides complete control over the app and its layout on **Wayland**.

### Summary of Wayland-Compatible Options:
1. **Electron-based custom app**: A cross-platform option that runs **Obsidian** natively on one side and embeds **ChatGPT** on the other.
2. **Nativefier with script**: A simpler option using **Nativefier** for the ChatGPT PWA and a bash script to run both apps together.
3. **Custom GTK or Qt app**: A more advanced option to develop a custom split-screen app directly for Wayland, using either **GTK** or **Qt**.

These approaches will give you full control over the **split-screen experience** you’re aiming for, without relying on window management features that may not work well on Wayland.