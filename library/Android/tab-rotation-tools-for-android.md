---
title: "Tab rotation tools for Android"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

As you know, I'm building out some dashboards in Grafana. I would like to display a couple of these in "kiosk mode" - including an Android tablet. Can you suggest any tools that might help to automatically rotate between a few dashboards on a schedule (perhaps every 3 minutes)?

# Output

For rotating between Grafana dashboards in "kiosk mode," including on an Android tablet, here are some tools and approaches you can consider:

1. **Grafana's Built-in Kiosk Mode**: 
   - Grafana natively supports a "kiosk mode" for displaying dashboards full-screen without any UI controls. You can set up different dashboards in different browser tabs and use browser automation tools to rotate them.

2. **Tab Management Tools for Android**:
   - **Fully Kiosk Browser**: A popular app that allows you to run an Android device in kiosk mode, and it supports auto-refresh and auto-tab switching. You can configure it to rotate between different Grafana dashboards by opening them in different tabs and setting a schedule to switch tabs.
   - **WallPanel**: Another Android kiosk app that lets you lock the device to show specific dashboards and can rotate between them.
   
3. **Grafana Carousel Plugin**: 
   - There is a community plugin called **Dashboard Carousel** that automatically rotates through a list of dashboards in Grafana itself. You can set the time interval for each dashboard.
   
4. **Browser Extensions for Tab Cycling**:
   - On desktop or Android with a compatible browser (such as Chrome or Firefox with desktop features), you could use a browser extension like **Revolver - Tabs** to automatically cycle between tabs displaying different dashboards.

5. **Task Automation Tools**:
   - **Tasker (Android)**: You could use Tasker to create a schedule for switching between tabs in a browser or app displaying different dashboards on your Android tablet.
   
These tools should help achieve the automatic rotation of Grafana dashboards at the desired intervals, whether on Android or desktop.