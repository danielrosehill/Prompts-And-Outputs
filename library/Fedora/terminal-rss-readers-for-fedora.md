---
title: "Terminal RSS readers for Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Can you suggest any RSS feed readers that work on Fedora Linux, are terminal native, but also support viewing multiple feeds?

# Output

Yes! There are a few terminal-native RSS feed readers that work well on Fedora Linux and support viewing multiple feeds. Here are some popular options:

### 1. **Newsboat**
   - **Description**: Newsboat is a highly configurable, terminal-based RSS/Atom feed reader that is widely considered one of the best terminal-native options for Linux.
   - **Features**:
     - Supports multiple RSS and Atom feeds.
     - Allows grouping of feeds.
     - Bookmarking functionality.
     - Can be integrated with external tools like a web browser or text editor for viewing articles.
     - Simple, keyboard-driven interface with customizable key bindings.
   - **Installation on Fedora**:
     ```bash
     sudo dnf install newsboat
     ```
   - **Usage**:
     - After installation, create a file called `~/.newsboat/urls` and add your RSS feeds:
       ```
       https://example.com/rss
       https://another-example.com/feed
       ```
     - Launch Newsboat with the command:
       ```bash
       newsboat
       ```

### 2. **Canto**
   - **Description**: Canto is another terminal-based feed reader with a focus on minimalism and simplicity. It is designed to display only the essential information in a clean format.
   - **Features**:
     - Supports both RSS and Atom feeds.
     - Easy navigation through multiple feeds using keyboard shortcuts.
     - Supports fetching and reading feeds in batches.
     - Highly customizable with a config file.
   - **Installation on Fedora**:
     ```bash
     sudo dnf install canto
     ```
   - **Usage**:
     - After installation, add feeds to `~/.canto/conf.py` by editing the file and adding:
       ```python
       add("https://example.com/rss")
       add("https://another-example.com/feed")
       ```
     - Run the application by typing:
       ```bash
       canto
       ```

### 3. **sfeed**
   - **Description**: `sfeed` is a lightweight feed reader that comes with a set of command-line tools for fetching and reading RSS and Atom feeds. It's ideal for those who prefer working with scripts and the Unix philosophy.
   - **Features**:
     - Supports multiple feeds.
     - Can be piped into other programs (like `less`, `grep`, `sed`) for further processing.
     - Minimal and fast, suitable for users who like manual configurations.
   - **Installation on Fedora**:
     ```bash
     sudo dnf install sfeed
     ```
   - **Usage**:
     - Create a list of feeds in a text file (e.g., `feeds.txt`):
       ```
       https://example.com/rss
       https://another-example.com/feed
       ```
     - Fetch and view feeds:
       ```bash
       sfeed_update < feeds.txt
       sfeed_plain < ~/.sfeed/feeds/* | less
       ```

### 4. **RSS Guard (with ncurses interface)**
   - **Description**: While **RSS Guard** is primarily known for its GUI interface, it also offers a **ncurses** version that works in the terminal. It is more feature-rich and can support OPML imports, feed synchronization, and more advanced feed management.
   - **Features**:
     - Multiple feed management.
     - Supports OPML import/export.
     - Fetches articles in batches, stores them for offline reading.
     - Also offers a GUI version if you want to switch between terminal and GUI.
   - **Installation on Fedora**:
     ```bash
     sudo dnf install rssguard
     ```

---

### Conclusion:
The **best choice** for a terminal-native RSS reader on Fedora largely depends on your preference for simplicity vs. features:
- **Newsboat** is the most popular, flexible, and feature-rich option for handling multiple feeds and customization.
- **Canto** is a more minimalist alternative, still offering good customization.
- **sfeed** is for those who enjoy using minimal and scriptable tools.
- **RSS Guard (ncurses)** is an option if you want a mix of terminal and GUI functionality.

For most users, **Newsboat** will be the easiest and most powerful choice to get started with.