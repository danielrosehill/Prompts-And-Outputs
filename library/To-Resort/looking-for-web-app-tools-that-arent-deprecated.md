---
title: "Looking for web app tools that aren't deprecated"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Looks like web app manager is pretty much deprecated. 

What are these called exactly. 

Can you find any newer tools for this purpose that are more active?

Fedora

# Output

Based on your query and the context of previous discussions, it seems you're looking for more up-to-date tools to create web app launchers or site-specific browsers (SSBs) on Fedora Linux. These are often referred to as "web app wrappers" or "site-specific browsers." Here are some newer and more actively maintained options:

## Nativefier

Nativefier remains one of the most popular and actively maintained tools for this purpose[1]. It's an Electron-based solution that creates standalone desktop applications from web pages. Key features include:

- Cross-platform support (including Linux)
- Customizable icons and app names
- Injection of custom CSS and JavaScript
- Regular updates and active community support

To install Nativefier on Fedora, you'll need Node.js and npm. Then you can install it using:

```bash
npm install -g nativefier
```

## WebCatalog

WebCatalog is a more polished, GUI-based alternative to Nativefier[1]. While it's not open-source, it offers a free tier with some limitations. Features include:

- User-friendly interface for creating and managing web apps
- Automatic updates for created apps
- Large library of pre-configured web apps
- Custom CSS/JS injection

WebCatalog is available for Linux and can be downloaded from their website.

## PWAsForFirefox

If you prefer using Firefox, PWAsForFirefox is a relatively new tool that creates desktop launchers for websites with a minimal toolbar[1]. It's specifically designed for Firefox users on Linux.

## Chromium's App Mode

While not a third-party tool, Chromium (and by extension, Google Chrome) offers a built-in "app mode" that can be used to create simple web app launchers[3]. You can create a launcher using:

```bash
/usr/bin/chromium --app=https://example.com
```

This method doesn't require additional software but provides less customization than dedicated tools.

## Custom .desktop Files

For a more manual approach, you can create custom .desktop files to launch websites in your preferred browser. This method gives you full control over the launcher properties and works with any browser.

While WebApp Manager may be less actively maintained, these alternatives provide similar functionality with ongoing development and support. Nativefier and WebCatalog are particularly popular choices for creating web app wrappers on Linux systems like Fedora.

 