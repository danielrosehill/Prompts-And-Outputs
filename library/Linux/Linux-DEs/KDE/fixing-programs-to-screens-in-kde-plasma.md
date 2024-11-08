---
title: "Fixing programs to screens in KDE Plasma"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

in fedora linux (kde plasma) is there any way to kind of lock or bind a window to a specific screen and a specific section of that screen?

# Output

Yes, in Fedora Linux with KDE Plasma, you can bind or lock a window to a specific screen and specific section of that screen using **KWin**, which is KDE’s window manager. KWin provides advanced window management features that allow you to control window behavior, including where a window appears and whether it is locked to a particular screen.

Here’s how you can achieve this:

### Using KDE's Window Rules:
1. **Open System Settings**:
   - Open the **KDE System Settings** application.

2. **Go to Window Management**:
   - Navigate to **Window Management** > **Window Rules**.

3. **Add New Rule**:
   - Click **New** to add a new rule for the window you want to bind.

4. **Match the Window**:
   - Under the "Window Matching" section, click the **Detect Window Properties** button to select the window you want to bind (or manually input the window class or title if you know it).

5. **Set the Position and Screen**:
   - Scroll to the **Size & Position** tab.
   - Check the **Screen** option and choose the screen you want the window to appear on (if you have multiple screens).
   - Check the **Position** option and set the X and Y coordinates to specify the exact location on the screen.
   - Optionally, set the **Size** option to define the exact size of the window.

6. **Apply the Rule**:
   - After defining the rules, click **OK** to apply. The window will now be bound to the specified screen and position whenever it opens.

### Using KWin Scripts (Advanced):
For more complex window management, you can use **KWin scripts** to automate window placement and behavior. If you need to dynamically bind windows based on certain conditions, scripting is an option:

1. Open **System Settings** > **Window Management** > **KWin Scripts**.
2. You can either download and install an existing KWin script from the KDE store, or create your own by writing a custom script in JavaScript.
3. Use KWin’s scripting API to programmatically bind a window to a specific screen or position.

For example, this could be done by writing a custom script that runs whenever the window opens, ensuring it appears on the desired screen and location.

### Summary:
The simplest way is to use **Window Rules** in KDE System Settings, which provides a GUI to configure screen and position locking. If you need more control, **KWin Scripts** can offer advanced automation and custom behavior.

# Input

That's useful to know but I meant more for a window that was already open. Not like a rule that would take effect forever. But rather temporarily locking in place a window now

# Output

In KDE Plasma, if you want to temporarily lock or "bind" an already open window to a specific screen and position without creating a permanent rule, you can use the **"Window Move"** and **"Window Tiling"** features for a temporary solution.

### Steps to Bind a Window Temporarily:

1. **Move the Window to a Specific Screen**:
   - Right-click on the window’s title bar.
   - Go to **More Actions** → **Move to Screen**, then select the screen you want the window to be moved to. This will move the window to that screen.

2. **Position the Window**:
   - Once on the correct screen, you can use KDE's **Window Snapping** and **Tiling** to quickly position the window in a specific section:
     - Drag the window to the edges or corners of the screen to automatically tile it to half, quarter, or full screen.
     - Alternatively, you can use keyboard shortcuts:
       - **Meta (Windows key) + Left/Right Arrow**: Snap the window to the left or right half of the screen.
       - **Meta + Up/Down Arrow**: Snap the window to the top or bottom half.
       - Use **Shift + Meta + Arrow keys** to fine-tune the window’s size and position.

3. **Lock the Window Temporarily** (Keep Above/Below):
   - After positioning the window, you can lock it in place (to prevent it from accidentally being moved) by right-clicking the window’s title bar and selecting **More Actions** → **Keep in Place**.
   - You can also use **"Keep Above"** or **"Keep Below"** to control its stacking order on the desktop, which may help if you want to ensure that the window stays visible without moving.

### Customizing Shortcuts for More Precise Control:
If you want more granular control, you can use KWin’s custom shortcuts to move and resize windows:
1. Open **System Settings** → **Shortcuts** → **KWin**.
2. You can customize shortcuts for moving windows, resizing them, or sending them to specific screens or positions on the screen.

These steps allow you to bind a window to a specific screen and position temporarily, without creating a persistent rule. You can manually reset the window's position or screen later when you're done.