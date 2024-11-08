---
title: "How do you preview HTML development in VS Code"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm developing a simple static site HTML project in VS Code. I'm not using a framework so there isn't a web server by default. Let's say the project is just one HTML file and one CSS. I would still like to be able to preview my changes visually and in real time. How do I go about doing this? Is there an extension for this purpose?

# Output

Yes, there's an excellent solution for your needs called the Live Preview extension for Visual Studio Code. This extension is perfect for simple static site projects like yours, where you're working with HTML and CSS files without a framework or built-in server.

## Live Preview Extension

The Live Preview extension, developed by Microsoft, allows you to preview your web projects in real-time directly within VS Code[1]. Here's how you can set it up and use it:

1. **Installation**:
   - Open VS Code
   - Go to the Extensions view (Ctrl+Shift+X or Cmd+Shift+X on Mac)
   - Search for "Live Preview"
   - Look for the extension by Microsoft (usually the first result)
   - Click "Install"

2. **Using Live Preview**:
   - Open your HTML file in VS Code
   - Click the "Show Preview" button in the top-right corner of your editor[1]
   - A preview will open in a new tab within VS Code

3. **Real-time Updates**:
   - As you make changes to your HTML or CSS files, the preview will update automatically
   - You don't need to save the file or manually refresh; changes appear as you type[1]

## Features

- **In-Editor Preview**: The preview opens within VS Code, allowing you to see your changes without switching to an external browser[1].
- **Live Refreshing**: See changes in real-time as you edit your files[1].
- **External Browser Support**: You can also open the preview in an external browser if you prefer[1].
- **Multi-root Workspace Support**: If you're working with multiple projects, Live Preview can handle that too[1].

## Advantages for Your Project

For your simple static site with just HTML and CSS, Live Preview is ideal because:

1. It doesn't require any setup or configuration
2. It works out of the box for static files
3. You can see changes instantly without needing to set up a local server manually

By using Live Preview, you'll be able to iterate quickly on your design and see how your HTML and CSS changes affect the layout and styling in real-time, all within the VS Code environment you're already using for development.

 