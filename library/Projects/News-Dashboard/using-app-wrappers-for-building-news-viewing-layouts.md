---
title: "Using app wrappers for building news viewing layouts"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Now we're getting somewhere finally. Wrappers is an interesting idea. Let's say that I wanted to create a full screen layout that would display a few live news feeds next to one another. I'd like to build this in the quickest and easiest way possible. I@M guessing one of these might be the way to go?

# Output

Based on the search results and your specific requirements, I believe Nativefier would be the quickest and easiest way to achieve what you're looking for. Here's how you can use it to create a full-screen layout with multiple live news feeds:

## Using Nativefier

Nativefier is a tool that allows you to convert any website into a desktop application[1]. This approach would be ideal for your needs:

1. Install Nativefier:
   ```
   npm install -g nativefier
   ```

2. Create separate desktop apps for each news feed you want to display:
   ```
   nativefier "https://news-feed-url-1.com" --name "News Feed 1"
   nativefier "https://news-feed-url-2.com" --name "News Feed 2"
   nativefier "https://news-feed-url-3.com" --name "News Feed 3"
   ```

3. Use KDE Plasma's window management features to arrange these apps side by side in a full-screen layout.

4. You can create a custom launcher script that opens all these apps and arranges them using KWin commands.

## Advantages of this approach:

1. Quick and easy to set up
2. Each feed runs in its own container, which can be beneficial for performance
3. You can easily update or change feeds by creating new Nativefier apps
4. Full-screen mode is supported out of the box[5]

To create a full-screen layout, you can use KDE Plasma's window management features or create a custom script that launches and arranges the Nativefier apps.

This method combines the simplicity of web-based news feeds with the convenience of desktop applications, allowing you to create a custom, full-screen news dashboard quickly and easily.

 