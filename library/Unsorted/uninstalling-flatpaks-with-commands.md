---
title: "Uninstalling flatpaks with commands"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


**Summary of your prompt**: You are asking how to uninstall a Flatpak application from the command line.

To uninstall a Flatpak application, follow these steps:

1. Open a terminal window.
2. Use the `flatpak uninstall` command followed by the application ID to uninstall the Flatpak app. For example, to uninstall the Stream Deck Controller with the app ID `com.mattjakeman.StreamDeck`, you would run:

   ```bash
   flatpak uninstall com.mattjakeman.StreamDeck
   ```

3. You will be prompted to confirm the uninstallation. Type `y` and press Enter to proceed.

If you want to uninstall the application without confirmation, you can add the `-y` option:

   ```bash
   flatpak uninstall -y com.mattjakeman.StreamDeck
   ```

This will uninstall the app from your system. Let me know if you need further assistance!