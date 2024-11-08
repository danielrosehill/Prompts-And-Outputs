---
title: "Dashboard builders that support local builds"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

These sound promising, but my ultimate target might be creating an Android app that can run in (so called) kiosk mode and display this dashboard continuously. Or I might wish to make the dashboard available as a desktop software to run on Linux computers. Are there any dashboard builders that would be suitable for this purpose?

# Output

Based on your requirements for creating a dashboard that can run in kiosk mode on Android or as desktop software on Linux, I would recommend considering the following options:

1. Grafana:
Grafana is particularly well-suited for your needs. It's open-source, highly customizable, and can be deployed in various environments:

- For Android: You can use Grafana in kiosk mode through a web browser on Android devices. There are also third-party Android apps that can display Grafana dashboards in a kiosk-like mode.
- For Linux: Grafana can be easily installed on Linux systems and run as a desktop application. There's even a specific tool called "grafana-kiosk" that helps set up Grafana in kiosk mode on devices like Raspberry Pi.

2. Dash by Plotly:
While not as comprehensive as Grafana, Dash allows you to build custom dashboards using Python:

- It can be packaged as a standalone application for Linux using tools like PyInstaller.
- For Android, you could potentially wrap the Dash app in a WebView within a native Android app.

3. Electron-based custom solution:
You could build a custom dashboard using web technologies (HTML, CSS, JavaScript) and package it using Electron:

- This approach would work well for Linux desktops.
- For Android, you'd need to create a separate app, but you could reuse much of the dashboard code.

4. Flutter:
If you're willing to invest in learning a new framework, Flutter allows you to build applications for both desktop (including Linux) and mobile (Android) from a single codebase:

- You'd have more control over the UI and functionality.
- It would require more development effort than using a pre-built dashboard solution.

Recommendation:
Given your specific requirements and the context of your previous questions, I would strongly recommend Grafana. It offers:

1. Open-source flexibility
2. Built-in support for kiosk mode
3. Easy deployment on Linux systems
4. Ability to run on Android devices (through browsers or custom apps)
5. Extensive customization options
6. Wide range of data source integrations

You can start with Grafana's open-source version to build your dashboard, and then deploy it in kiosk mode on both Linux desktops and Android devices. This approach would give you a powerful, flexible solution while minimizing the need for custom development across different platforms.

 