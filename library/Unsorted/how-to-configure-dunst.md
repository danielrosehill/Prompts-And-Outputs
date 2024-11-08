---
title: "How to configure dunst"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 **Dunst** is a lightweight and customizable notification daemon for Linux that can be set up to display notifications for various events, including system notifications and custom notifications from different applications. Here's how to set it up and what else it can monitor:

### Setting Up Dunst on Fedora

1. **Install Dunst**:
   You can install Dunst using the following command:

   ```bash
   sudo dnf install dunst
   ```

2. **Start Dunst**:
   After installation, you can start Dunst by simply running:

   ```bash
   dunst &
   ```

   To ensure it starts automatically with your session, you can add it to your startup applications.

3. **Configuration**:
   Dunst uses a configuration file to customize its appearance and behavior. You can create or edit the configuration file located at `~/.config/dunst/dunstrc`. If this file doesn't exist, you can copy the default configuration from the system:

   ```bash
   cp /usr/share/doc/dunst/dunstrc ~/.config/dunst/
   ```

   Edit the file with your preferred text editor:

   ```bash
   nano ~/.config/dunst/dunstrc
   ```

   You can customize options such as:
   - Font and colors
   - Notification position on the screen
   - Timeout duration for notifications
   - Icon appearance

4. **Reload Dunst**:
   After editing the configuration file, reload Dunst to apply changes:

   ```bash
   killall dunst && dunst &
   ```

### Features of Dunst

- **Monitoring System Notifications**: Dunst will automatically capture notifications from standard applications that send notifications through the desktop environment (e.g., messaging apps, system updates, etc.).
  
- **Custom Notifications**: You can use command-line tools or scripts to send custom notifications to Dunst using the `notify-send` command:

  ```bash
  notify-send "Title" "This is a notification"
  ```

- **Monitoring Applications**: Dunst can be configured to listen for notifications from various applications that support the desktop notification standard (like messaging apps, email clients, etc.).

### Examples of Applications That Can Send Notifications to Dunst
- **Email Clients**: Applications like Thunderbird can send notifications for new emails.
- **Messaging Apps**: Clients like Slack, Discord, or Telegram can notify you of new messages.
- **System Utilities**: Updates, backup notifications, and other system utilities often use desktop notifications.
- **Custom Scripts**: Any script that uses `notify-send` can send notifications to Dunst.

### Example: Monitor Reddit Replies with Dunst
You can integrate Dunst with a script that checks Reddit for replies (as discussed previously). Here’s a simplified example of how you might implement this:

```python
import requests
import os
from time import sleep

def check_reddit():
    url = "https://www.reddit.com/user/your_username/comments/.json"
    headers = {'User-Agent': 'Notification Agent'}
    
    response = requests.get(url, headers=headers)
    comments = response.json()
    
    # Logic to determine if there are new replies goes here
    # For example, using notify-send to send notifications
    os.system('notify-send "New Reply" "You have a new reply on Reddit!"')

if __name__ == "__main__":
    while True:
        check_reddit()
        sleep(60)  # Check every minute
```

### Conclusion
Dunst is a powerful notification daemon that allows for extensive customization and can monitor notifications from various applications. Setting it up is straightforward, and it can enhance your workflow by keeping you informed of important events. Let me know if you need help with specific configurations or further integration!

