---
title: "tasker mods to keep obsidian in background"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To keep ChatGPT and Obsidian running in the background and easily accessible in Tasker, you can set up the following configurations:

1. Persistent Background Apps

To ensure these apps remain in memory and are not killed by the Android system, Tasker can periodically "refresh" them in the background.

Steps:

Create a Profile to Monitor App State:

Create a Profile with the Time context and set it to trigger every 10 or 15 minutes.


Create a Task to Launch Apps:

Add an Action: App → Launch App → ChatGPT (if the app isn't running, this will open it).

Add a similar Action for Obsidian: App → Launch App → Obsidian.

Optionally, add a short Wait action (1–2 seconds) between the app launches to avoid conflicts.


Optional: Keep in Foreground:

If you want to ensure these apps stay visible or can be returned to quickly, add an Action to bring them to the foreground when needed: App → Go Home and then App → Launch App → ChatGPT/Obsidian.



2. Whitelist the Apps from Battery Optimization:

Android tends to close apps to conserve battery life. To avoid this:

Go to your phone's Settings → Battery → Battery Optimization.

Find both ChatGPT and Obsidian in the list and set them to Not Optimized.


3. Create a Shortcut for Quick Access:

For quicker access via Tasker, you can create a Scene or widget that allows you to tap and quickly launch either app.

Steps:

In Tasker, create a new Task with the following actions:

App → Launch App → ChatGPT.

Add a second task with App → Launch App → Obsidian.


Create a Scene with two buttons, each mapped to launch one of the apps.


4. Prevent Screen Timeout (Optional)

If you want to keep these apps running without the screen turning off:

Add a Task: Display → Stay On.

Trigger this when either ChatGPT or Obsidian is open.


These steps should ensure that ChatGPT and Obsidian remain running and can be accessed quickly at any time without being closed by the system.

