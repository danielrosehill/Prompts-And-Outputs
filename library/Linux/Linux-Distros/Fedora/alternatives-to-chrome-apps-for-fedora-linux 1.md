---
title: "Alternatives to Chrome apps for Fedora Linux"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Google Chrome allows you to create something called Chrome Apps which are launchers for specific sites or PWAs.

They're nice, but I also wonder whether it's possible to build similar tools without relying upon the built in Google features - perhaps allowing you to create more advanced programs like these.

I use Fedora Linux.

Anything that might be worth exploring for this?

# Output

Based on your query, there are several options for creating web app launchers on Linux without relying on Google Chrome's built-in features:

1. WebApp Manager: This is a popular tool for creating web app launchers on Linux[3]. It allows you to:

   - Create launcher icons for websites and web apps
   - Choose custom icons 
   - Select which browser to use
   - Decide whether to show the navigation bar

2. Nativefier: This is an open-source command-line tool that can convert websites into standalone desktop applications[4]. It creates an Electron wrapper for the website, giving it a native feel.

3. Webapp Manager: Similar to WebApp Manager, this tool lets you create launcher icons for web apps on Linux[1]. It's pre-installed on Linux Mint but can be added to other Ubuntu-based distributions.

4. Custom .desktop files: You can manually create .desktop launcher files for websites[1]. This gives you full control over the launcher properties.

5. PWAsForFirefox: If you prefer Firefox, this extension and command-line tool creates desktop launchers for websites with a minimal toolbar[4].

6. Ferdium: While not for single-site launchers, this is a good option if you want to create a multi-site web app container[4].

For your Fedora Linux system, I would recommend trying WebApp Manager or Nativefier as they offer good functionality without relying on Google's features. WebApp Manager provides a user-friendly GUI, while Nativefier offers more advanced features like CSS/JS injection if you're comfortable with command-line tools.

Remember that these solutions generally create launchers that still use your installed browsers, rather than fully independent applications. However, they do provide a more app-like experience for web services.

 