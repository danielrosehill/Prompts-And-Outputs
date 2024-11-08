---
title: "Remotely controlling smart TV from Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You can control your LibreELEC smart TV from your Fedora desktop using a few methods. Here are some options:

1. **Using SSH:**
   If SSH is enabled on your LibreELEC device, you can remotely control it through a terminal on your Fedora desktop. This allows you to run commands to manage media playback, access logs, and more.

   To enable SSH:
   - Go to **Settings** > **LibreELEC** > **Services** > **SSH** and enable it.

   You can then connect to your TV from your Fedora terminal using:
   ```bash
   ssh root@<IP_ADDRESS_OF_YOUR_TV>
   ```

2. **Using a Remote Control App:**
   - **Yatse** (for Android) or **Kore** (for Android and iOS) can control your LibreELEC setup. You can install one of these apps on your phone and connect to your TV over the same network.
   - For desktop, consider **Kodi Remote** applications that support controlling Kodi installations, including those on LibreELEC.

3. **Using a Web Interface:**
   If you have a web browser, you can access the web interface of your LibreELEC installation:
   - Open your browser and go to `http://<IP_ADDRESS_OF_YOUR_TV>:8080`. This allows you to control playback and browse your library from your Fedora desktop.

4. **Using Kodi JSON-RPC API:**
   LibreELEC runs Kodi, which has a JSON-RPC API you can use to send commands programmatically. You can create scripts on your Fedora desktop to control your TV. Here's a simple example using `curl`:
   ```bash
   curl -X POST -H "Content-Type: application/json" \
   --data '{"jsonrpc": "2.0", "method": "Player.PlayPause", "params": {"playerid": 1}, "id": 1}' \
   http://<IP_ADDRESS_OF_YOUR_TV>:8080/jsonrpc
   ```

5. **Using VNC (if installed):**
   If you have a VNC server running on your LibreELEC device, you can use a VNC viewer on your Fedora desktop to control the TV's interface directly. However, setting up a VNC server may require additional configuration.

These methods should give you various ways to control your LibreELEC smart TV from your Fedora desktop. Let me know if you need more details on any of these options!