---
title: Friction points with Obsidian on Android
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here's another idea. My main frustration with Obsidian is that the Android app sucks as a way to read the outputs that I've saved. Which is annoying because it means that I can save lots of valuable info into the vault but it's really hard to actually look back over it. Which is kind of the whole idea. The Obsidian vault is just a huge collection of markdown notes that gets synced up to B2. Perhaps you can think of a stopgap solution that would give me a convenient way to read through them on my Android (it would have to support pagination / back and forward arrows to navigate through the outputs)

# Output

Your frustration with **Obsidian's Android app** when it comes to reading and navigating through saved outputs is understandable, especially since you've invested so much into organizing valuable knowledge. Since the vault is just a collection of **markdown files**, there are a few stopgap solutions that would let you easily read and navigate through your notes on Android with better usability features like pagination and navigation buttons.

Here are some ideas that might help:

### 1. **Read Obsidian Vaults with a Markdown Reader**
   You can use a dedicated **markdown reader app** that is better suited for Android and integrates with B2 (or your Obsidian sync folder). Some markdown readers offer better navigation and reading experiences than Obsidian's mobile app.

   #### Suggested Markdown Readers:
   - **Markor**:
     - **Why**: Markor is a highly rated markdown editor and viewer for Android. You can link it to your B2 folder (or any folder that Obsidian syncs to) and use it to browse through your markdown files.
     - **Features**: It supports back/forward navigation, table of contents, and allows for easier viewing of large markdown files.
     - **How to use**: Link Markor to your local folder or a synced cloud folder where your Obsidian vault resides.
   
   - **Epsilon Notes**:
     - **Why**: Epsilon Notes is another good markdown editor that works on Android. It offers a file browser interface and allows you to open and navigate markdown files easily.
     - **Features**: Supports pagination or navigation through files, and allows for easy reading and editing of markdown.
     - **How to use**: Sync your Obsidian vault folder to your Android device and use Epsilon Notes to navigate through the outputs you've saved.

   #### Integration with B2:
   - **rclone**: You can use **rclone** on your Android device to sync your B2-stored Obsidian vault to a local folder on your phone. Both Markor and Epsilon Notes will be able to open these synced files locally. Rclone supports syncing with Backblaze B2 and can automate the process of syncing your vault to your device.

### 2. **Build a Simple Web App for Reading Markdown Files**
   If you’re comfortable with a bit of setup, a simple **self-hosted web app** can be a great stopgap solution. Here’s how this could work:
   
   - **Host the markdown files**: Use a lightweight web server to serve your Obsidian vault as static markdown files.
   - **Frontend**: Build a minimal UI with navigation buttons (back/forward) and pagination to help browse through the markdown outputs.
   
   #### Example Tools:
   - **VuePress** or **MkDocs**: These are static site generators specifically built for markdown files. You can deploy your Obsidian vault with a UI for easy navigation through notes, complete with a table of contents and pagination. You can host this on a simple web server or even on your Android device.
   - **Static Hosting on Netlify**: You could deploy the vault as a static site on platforms like **Netlify**, so it’s accessible from your Android device via a web browser.

   #### How it works:
   - Use **rclone** or **Syncthing** to keep your vault synced to a server or a local folder.
   - Use MkDocs or VuePress to generate a paginated static site from your markdown notes. Access it on your phone via a browser for easier navigation.

### 3. **Use a File Manager App with Preview**
   If you’re looking for a simpler stopgap, you can use a **file manager** app that supports markdown file previews. This would let you browse the structure of your Obsidian vault more effectively and preview the contents of markdown files without needing a dedicated markdown editor.
   
   #### Suggested File Managers:
   - **Solid Explorer**: Solid Explorer supports markdown previews and has a very intuitive interface for navigating files. You can set it to open markdown files using a markdown viewer or another app like Markor.
   - **Mixplorer**: Mixplorer has markdown preview capabilities, a customizable UI, and supports various cloud services. You can integrate B2 or sync your Obsidian folder and navigate markdown files easily.

### 4. **Custom Android App with Navigation Features**
   If you're open to development, a custom Android app could be a flexible stopgap solution:
   
   - **Use a Framework like Flutter or React Native**: Both of these frameworks allow for fast mobile app development and have good markdown rendering libraries. You can create a lightweight app that reads the markdown files from your Obsidian vault, offers pagination or back/forward navigation, and displays them neatly.
     - **Flutter**: With Flutter’s markdown plugin, you can build an app with a simple UI to render markdown files and add navigation features.
     - **React Native**: Similarly, you can build a mobile app with React Native and use a markdown rendering library like `react-native-markdown-display` to handle the content.

### 5. **TiddlyWiki as an Alternative Viewer**
   If you're open to restructuring your workflow, you can convert your Obsidian markdown files into **TiddlyWiki** format and use TiddlyWiki as a mobile-friendly, self-hosted knowledge manager. TiddlyWiki can be hosted locally on your Android device or on a server, giving you a UI for navigating your notes with back/forward arrows, search, and pagination.

   - **How to use**: You could use tools like `pandoc` to convert markdown files into TiddlyWiki format.
   - **TiddlyWiki on Android**: There are apps and methods for hosting TiddlyWiki on Android, allowing you to navigate notes through a browser or app.

### Conclusion:
The simplest stopgap solution may be using **Markor** or **Epsilon Notes** in conjunction with **rclone** to sync your Obsidian vault locally and navigate the notes on Android. This gives you better file viewing and management than the native Obsidian app while allowing navigation through notes.

Alternatively, if you’re comfortable with a bit of development, creating a simple **web app** to read and paginate markdown files or building a mobile app with **Flutter** could offer a custom solution that meets your needs perfectly.

Would you like more details on setting up one of these solutions?