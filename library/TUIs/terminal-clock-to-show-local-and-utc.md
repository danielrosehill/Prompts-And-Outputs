---
title: "Terminal clock to show local and UTC"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd love to get a clock display in my terminal showing local time and UTC - but hours and minutes only. Does such a program exist?

# Output

Yes, you can get a **clock display** in your terminal that shows both **local time** and **UTC**, focusing on just hours and minutes. While there might not be a specific tool designed exactly for this purpose, you can achieve it using a combination of common Linux utilities and terminal tools. Here are a few options:

### Option 1: Use `watch` with `date`

You can use the `watch` command to continuously display both local time and UTC, updated every second. The `date` command can format time to show hours and minutes only.

1. **Command to Display Both Local and UTC Time**:
   ```bash
   watch -n 1 'echo "Local: $(date +%H:%M) | UTC: $(date -u +%H:%M)"'
   ```

   This will show something like:
   ```
   Every 1.0s: echo "Local: $(date +%H:%M) | UTC: $(date -u +%H:%M)"    
   Local: 18:42 | UTC: 15:42
   ```

   - `$(date +%H:%M)` gives the **local time** (hours and minutes).
   - `$(date -u +%H:%M)` gives the **UTC time** (hours and minutes).
   - The `watch` command refreshes the display every second (`-n 1`).

### Option 2: `tty-clock` (Customizable Terminal Clock)

You can use `tty-clock`, a popular terminal-based clock tool, but it only shows local time. However, you can run multiple instances of `tty-clock` to show both **local time** and **UTC** in separate terminal panes (using `tmux` or separate windows).

1. **Install `tty-clock`**:
   ```bash
   sudo dnf install tty-clock
   ```

2. **Show Local Time**:
   ```bash
   tty-clock -s -S
   ```

   - `-s`: Display only hours and minutes.
   - `-S`: Use UTC, or just `tty-clock` for local.

   Since this doesn’t support showing both local and UTC in one display, you can run **two instances of `tty-clock`** side by side using `tmux` or another multiplexer.

### Option 3: Custom Script Using `watch`

If you'd like a more customized solution, you can create a **simple bash script** that shows both local time and UTC formatted as hours and minutes, and use `watch` to refresh it.

1. **Create a Bash Script**:
   ```bash
   nano ~/bin/time-display.sh
   ```

2. **Script to Display Local and UTC Time**:
   ```bash
   #!/bin/bash
   while true; do
     echo "Local Time: $(date +%H:%M)"
     echo "UTC Time:   $(date -u +%H:%M)"
     sleep 1
     clear
   done
   ```

3. **Make It Executable**:
   ```bash
   chmod +x ~/bin/time-display.sh
   ```

4. **Run the Script**:
   ```bash
   ~/bin/time-display.sh
   ```

This will show both local and UTC time in a clean format, refreshing every second.

### Option 4: Use `conky` (System Monitor)

**Conky** is a highly customizable system monitor that runs in your terminal or desktop and can display various information, including time. You can configure it to show both local and UTC time.

1. **Install Conky**:
   ```bash
   sudo dnf install conky
   ```

2. **Configure Conky**:
   You can customize `conky` to show local and UTC time with a custom `.conkyrc` configuration file. Here's an example:

   **Create `.conkyrc`**:
   ```bash
   nano ~/.conkyrc
   ```

   **Sample Configuration**:
   ```plaintext
   conky.config = {
     update_interval = 1,
   }

   conky.text = [[
   Local Time: ${time %H:%M}
   UTC Time:   ${utime %H:%M UTC}
   ]]
   ```

3. **Run Conky**:
   ```bash
   conky
   ```

This will show the local and UTC times in your terminal window with real-time updates.

---

### Conclusion:
For a simple and customizable terminal clock displaying both **local time** and **UTC**, the most direct and flexible option is using `watch` with the `date` command. If you want a more graphical terminal clock, `tty-clock` combined with `tmux` is a great solution, but you’d have to run two instances for local and UTC times.

For simplicity:
```bash
watch -n 1 'echo "Local: $(date +%H:%M) | UTC: $(date -u +%H:%M)"'
```

Or you can go further with **Conky** if you'd prefer a more graphical, system monitor-based solution.