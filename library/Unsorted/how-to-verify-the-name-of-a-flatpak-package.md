---
title: "How to verify the name of a flatpak package"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt**: You are asking how to find the name of the installed Flatpak package to ensure it’s the right one for the Stream Deck Controller app.

To find out the exact name of the Flatpak package you have installed, follow these steps:

1. Open a terminal window.
2. Run the following command to list all the installed Flatpak applications:

   ```bash
   flatpak list
   ```

   This command will show you a list of all installed Flatpak apps along with their names, versions, and Flatpak IDs.

3. Look for the entry related to the Stream Deck Controller in the output. You should see something like this:

   ```
   Name                             Application ID                      Version  Branch    Installation
   Stream Deck Controller           com.mattjakeman.StreamDeck           1.0.0    stable    system
   ```

   The **Application ID** (e.g., `com.mattjakeman.StreamDeck`) is the identifier you can use for any commands related to this package (such as overriding permissions or uninstalling).

This will help you confirm whether you have the right package installed. Let me know if you need more help!