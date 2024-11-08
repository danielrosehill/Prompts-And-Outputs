---
title: "Bookmarking a split folder view in Dolphin"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there any way that I can bookmark this exact split folder view in Linux? I'm using Dolphin file manager

![[Bookmarking a split folder view in Dolphin.png]]

# Output

In Dolphin file manager, while there is no native feature to bookmark a split-view session directly, you can use a workaround to quickly return to the same directories on both sides of the split view.

Here’s how you can set this up:

1. **Save each folder as a place in the sidebar**:
   - Navigate to each directory (e.g., `Git/Ilm-and-ai/Daniel-Goes-Prompting/Vault/Outputs/Unsorted` and `Git/Ilm-and-ai/Daniel-Goes-Prompting/Vault/Outputs/Hidden`).
   - Once you’re in the desired directory, drag the folder icon from the path bar into the Places panel (the sidebar on the left). This will add the folder to your sidebar for easy access.
   
2. **Use Dolphin session management**:
   - Dolphin has session management that remembers your last session. You can go to **Control -> Configure Dolphin -> Startup** and check the option **"Restore previous tabs and windows"**. This will reopen Dolphin with the exact same state, including split views and directories.
   
3. **Manual script for opening specific directories in split view**:
   - If you want to automate opening these specific directories in a split view, you can create a small script and run it whenever you want Dolphin to open these folders:
     ```bash
     #!/bin/bash
     dolphin --split "/path/to/first/directory" "/path/to/second/directory"
     ```
     Replace `"/path/to/first/directory"` and `"/path/to/second/directory"` with your actual folder paths. You can save this script as a `.sh` file and make it executable.

Let me know if you need more guidance on any of these options!

# Split

Scripting sounds like the way to go. You actually had the paths at the start of the output but they're each relative to my home directory. Could you try writing a quick bash script? This could really help

# output

Sure! Here's a quick Bash script that will open Dolphin in split-view mode with your two directories relative to your home directory:

```bash
#!/bin/bash
# Open Dolphin in split-view with specified directories

# Define the paths relative to the home directory
LEFT_DIR="~/Git/Ilm-and-ai/Daniel-Goes-Prompting/Vault/Outputs/Unsorted"
RIGHT_DIR="~/Git/Ilm-and-ai/Daniel-Goes-Prompting/Vault/Outputs/Hidden"

# Launch Dolphin with the split view
dolphin --split "$LEFT_DIR" "$RIGHT_DIR"
```

### Steps to create and use the script:

1. Open a text editor (like Nano or Vim) and paste the script.
2. Save the file as `open_dolphin_split.sh` (or any name you prefer).
3. Make the script executable by running the following command:
   ```bash
   chmod +x open_dolphin_split.sh
   ```
4. Run the script by typing:
   ```bash
   ./open_dolphin_split.sh
   ```

This script should now open Dolphin with the split view showing the two specified directories.

Let me know how it works for you!