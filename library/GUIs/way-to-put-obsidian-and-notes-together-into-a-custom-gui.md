---
title: "Way to put Obsidian and notes together into a custom GUI"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd like to build a custom app on Fedora Linux that combines two apps into one. 
One app is Obsidian, which is a well known notes manager. The other is a website which I would like to embed next to it as I use it together with Obsidian. Can you think of any way(s) I might be able to achieve this?

# Output

Based on your requirements, there are a few approaches you could take to combine Obsidian with an embedded website into a custom app on Fedora Linux:

1. Electron-based solution:

Electron allows you to create desktop applications using web technologies. You could create an Electron app that embeds both Obsidian and your desired website.

- Use Electron's BrowserView or webview tag to embed Obsidian and the website side-by-side.
- You'd need to package Obsidian as part of your Electron app or load it from the installed location.
- This approach gives you full control over the layout and integration.

2. Nativefier + custom scripting:

Nativefier is a command-line tool that allows you to create desktop applications from websites[1][8].

- Use Nativefier to create a desktop app from your desired website.
- Write a custom script that launches both the Nativefier-created app and Obsidian side-by-side.
- You could use a window manager or tiling script to arrange them automatically.

3. Custom WebView application:

Create a custom application using a framework like GTK+ that embeds WebViews[3].

- Use one WebView to load Obsidian's web version (if available) or embed the desktop app.
- Use another WebView to load your desired website.
- This gives you control over the layout and integration within a native Linux application.

4. Tauri framework:

Tauri is a toolkit for building desktop apps with web technologies, similar to Electron but more lightweight[4].

- Create a Tauri app that embeds both Obsidian (if it has a web version) and your desired website.
- This approach would be more resource-efficient than Electron.

5. Browser extension + custom launcher:

- Create a browser extension that modifies the layout of Obsidian's web version (if available) to include your desired website.
- Write a custom launcher script that opens the browser with this extension and the appropriate tabs.

For all these approaches, you'll need to consider Obsidian's licensing and terms of service to ensure you're allowed to embed or modify it in this way.

The Electron-based solution or the Nativefier approach might be the easiest to implement, especially if you're familiar with web technologies. They would allow you to create a seamless experience combining Obsidian and your desired website.

 