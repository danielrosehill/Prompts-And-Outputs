---
title: "Terminal clocks with multiple time zone support - including local and UTC"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You're right to be surprised — and actually, there **are** terminal-based world clocks that can display multiple time zones, including both **local time** and **UTC**. These tools are great for monitoring multiple time zones in a simple way. Here are a few terminal-based solutions that can show both **local** and **UTC** (and potentially other time zones) together:

### 1. **tzclock**
   - **Description**: `tzclock` is a terminal-based world clock that can display the time for multiple time zones, including local and UTC.
   - **Features**: 
     - Displays time for multiple time zones simultaneously.
     - Configurable time formats (like hours and minutes).
     - Lightweight and easy to use.
   - **Installation**: 
     ```bash
     sudo dnf install tzclock
     ```
   - **Usage**:
     ```bash
     tzclock -z "UTC" -z "America/New_York" -z "Asia/Jerusalem"
     ```
     This would display clocks for UTC, New York, and Jerusalem time zones. You can adjust the formatting to show only hours and minutes:
     ```bash
     tzclock -f "%H:%M" -z "UTC" -z "localtime"
     ```
   - **Note**: You can add multiple time zones and customize the display format to your liking.

### 2. **gdate** with Multiple Time Zones
   - If `tzclock` isn't available or you want more control, you can use the `gdate` command (from GNU coreutils, which is available on most Linux distros) to display multiple time zones.
   - **Command**:
     ```bash
     watch -n 1 'echo "Local: $(date +%H:%M) | UTC: $(TZ=UTC date +%H:%M) | New York: $(TZ="America/New_York" date +%H:%M)"'
     ```
     - **Explanation**:
       - `date +%H:%M`: Displays the current local time.
       - `TZ=UTC date +%H:%M`: Displays UTC time.
       - `TZ="America/New_York" date +%H:%M`: Displays the time in New York.
     - You can modify this to display any number of time zones.

### 3. **`clock` (Multitime CLI Clock)**
   - **Description**: `clock` is a simple but useful command-line utility that allows you to monitor multiple time zones in the terminal.
   - **Installation**: `clock` might not be directly available in standard repositories, but you can easily install it via `cargo` (Rust's package manager).
   - **Install `cargo`** if you don't have it already:
     ```bash
     sudo dnf install cargo
     ```
   - **Install `clock`** via `cargo`:
     ```bash
     cargo install clock
     ```
   - **Usage**:
     After installing, you can run `clock` with multiple time zones:
     ```bash
     clock UTC America/New_York Asia/Jerusalem
     ```

### 4. **worldclock-cli**
   - **Description**: `worldclock-cli` is another lightweight CLI tool that allows you to display multiple time zones in your terminal.
   - **Install**: It’s typically installed via `npm` (Node.js package manager), which might require you to install Node.js first:
     ```bash
     sudo dnf install nodejs
     sudo npm install -g worldclock-cli
     ```
   - **Usage**:
     You can run `worldclock-cli` to display time for multiple zones:
     ```bash
     worldclock-cli UTC America/New_York Asia/Jerusalem
     ```
   - **Customization**: You can configure it to display only hours and minutes.

### 5. **TTY-Clock with `date`**
   - While **TTY-Clock** doesn’t natively support multiple time zones, you could combine multiple terminals or panes (using `tmux` or `screen`) with customized `date` commands in each pane to simulate a world clock. Here’s an example:
     ```bash
     tmux split-window "watch -n 1 'date +%H:%M -d now'"
     tmux split-window "watch -n 1 'date +%H:%M -u'"
     tmux split-window "watch -n 1 'TZ=America/New_York date +%H:%M'"
     ```

### Summary of Solutions:
1. **tzclock**: Terminal-based multi-time zone clock that displays multiple time zones like local and UTC.
2. **gdate (with watch)**: Using GNU `date` to display multiple time zones by manipulating `TZ` environment variable.
3. **clock**: A Rust-based CLI utility for showing multiple time zones in a simple interface.
4. **worldclock-cli**: An npm package that allows you to see world clocks in the terminal.

### Conclusion:
While there might not be a single tool explicitly called a "world clock" with all features built-in, there **are tools** like `tzclock` and `worldclock-cli` that are very close to what you're asking for. Additionally, combining `watch` with `date` or using `tmux` with multiple time zones is another simple and effective solution. 

Give **`tzclock`** a try first, as it's likely the simplest option for quickly getting both local and UTC in your terminal!