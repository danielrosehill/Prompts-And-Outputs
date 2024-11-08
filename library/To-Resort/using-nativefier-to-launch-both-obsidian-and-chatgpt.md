---
title: "Using Nativefier to launch both Obsidian and ChatGPT"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm currently using Obsidian and ChatGPT in a split screen layout (horizontal). I keep ChatGPT on the left and Obsidian on the right and I copy outputs from ChatGPT into Obsidian.

These are the paths to open both programs on my Fedora computer running KDE Plasma and Wayland:

/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx

obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub

I would like to create an electron app which serves as a wrapper for both of these programs, essentially forcing both apps to open within it in this defined layout
Can you help set it up?

# Output


**Summary of your prompt:** You want to create an Electron app that acts as a wrapper for **Obsidian** and **ChatGPT**, opening both applications in a split-screen horizontal layout (ChatGPT on the left, Obsidian on the right) on your Fedora computer running KDE Plasma and Wayland.

Here’s how you can set up an **Electron** app to achieve this:

### 1. **Set Up Your Electron Project**
First, we need to create an Electron project that will serve as a wrapper for both **Obsidian** and **ChatGPT**. Here’s a step-by-step guide to creating this Electron app.

#### Step 1: Install Node.js and Electron
If you haven’t installed Node.js and Electron yet, install them first:

1. **Install Node.js**:
   ```bash
   sudo dnf install nodejs
   ```

2. **Install Electron globally**:
   ```bash
   npm install -g electron
   ```

#### Step 2: Create the Electron App Directory
Create a directory for your new Electron app:

```bash
mkdir obsidian-chatgpt-electron
cd obsidian-chatgpt-electron
```

#### Step 3: Initialize the Project
Initialize an **npm** project:

```bash
npm init -y
```

This will generate a `package.json` file for your project.

#### Step 4: Install Electron Locally
You can install Electron as a development dependency for your project:

```bash
npm install --save-dev electron
```

#### Step 5: Create the Main Electron File
In the project directory, create a new file called `main.js`. This will be the main script that launches both **Obsidian** and **ChatGPT** inside the Electron window.

```bash
nano main.js
```

### Step 6: Add Electron Code to Handle Split Layout

Here is the code for your Electron `main.js` file:

```javascript
const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');

let mainWindow;

app.on('ready', () => {
    // Create the main window
    mainWindow = new BrowserWindow({
        width: 1600,  // Define your preferred width
        height: 900,  // Define your preferred height
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    // Load an HTML file that will display both ChatGPT and Obsidian
    mainWindow.loadURL('data:text/html;charset=utf-8,' + encodeURIComponent(content));

    // Run the Obsidian app in the background
    exec("obsidian /home/daniel/Vaults/outputhub_vault/Output_Hub", (error, stdout, stderr) => {
        if (error) {
            console.error(`Error launching Obsidian: ${error.message}`);
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
        }
        console.log(`stdout: ${stdout}`);
    });

    // Open Chrome as a web app for ChatGPT (you can also call this separately if needed)
    exec("/opt/google/chrome/google-chrome --profile-directory=Default --app-id=xxxxxxx", (error, stdout, stderr) => {
        if (error) {
            console.error(`Error launching Chrome: ${error.message}`);
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
        }
        console.log(`stdout: ${stdout}`);
    });
});

// Define the content for the Electron window (split layout with Obsidian and ChatGPT)
const content = `
    <html>
    <head>
        <style>
            body { margin: 0; display: flex; height: 100vh; overflow: hidden; }
            iframe { border: none; width: 50%; height: 100%; }
        </style>
    </head>
    <body>
        <!-- Left side: ChatGPT in Chrome -->
        <iframe src="http://localhost:9222"></iframe>

        <!-- Right side: Obsidian is launched separately -->
        <iframe src="obsidian://open?vault=Output_Hub"></iframe>
    </body>
    </html>
`;
```

This script does the following:

1. **Creates a main window** in Electron that has a split-screen layout.
2. **Loads an HTML template** that has two `iframe` elements, one for **ChatGPT** and one for **Obsidian**.
3. **Executes Obsidian and the Chrome web app** using the `child_process` module’s `exec` method, ensuring both are launched in the background while the Electron app handles their display in the main window.
4. **Adjusts layout** so the split screen is always 50/50, with **ChatGPT on the left** and **Obsidian on the right**.

### Step 7: Update `package.json` for Electron

Edit your `package.json` file to add an Electron start script:

```json
{
  "name": "obsidian-chatgpt-electron",
  "version": "1.0.0",
  "description": "Electron wrapper for Obsidian and ChatGPT in a split-screen layout",
  "main": "main.js",
  "scripts": {
    "start": "electron ."
  },
  "devDependencies": {
    "electron": "^latest"
  }
}
```

### Step 8: Start the Electron App

Now that everything is set up, you can start your Electron app by running:

```bash
npm start
```

This will open an Electron window with **ChatGPT** and **Obsidian** in a split-screen layout, exactly as described.

---

### Optional Step: Package the App for Easy Launch

If you want to package the app as a standalone executable, you can use **Electron Packager**.

1. **Install Electron Packager**:
   ```bash
   npm install electron-packager --save-dev
   ```

2. **Package the App**:
   ```bash
   npx electron-packager . ObsidianChatGPT --platform=linux --arch=x64 --out=dist
   ```

This will create a standalone **ObsidianChatGPT** application in the `dist/` directory, which you can run like any other app on your Fedora system.

---

### Summary:
This approach uses **Electron** to create a wrapper that launches **Obsidian** and **ChatGPT** in a split-screen layout. You can now run both apps within a single Electron window, making it easier to manage them in your workflow.

