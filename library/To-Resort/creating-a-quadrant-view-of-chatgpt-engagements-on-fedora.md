---
title: "Creating a quadrant view of ChatGPT engagements on Fedora"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I use ChatGPT a lot during the day but I would frequently like to have a few chats open at once. I use fedora + kde plasma + wayland.

My ideal UI would be something like a quadrant: a full screen for chatgpt interactions and each chat fits into one window. So I can have four open at once. I might then be able to navigate between the chats using something like the tab button and each chat might highlight once opened.

Can you suggest some ways in which I might be able to achieve this functionality? I don't mind which browser you use. And if you think that developing something custom is the best way to go, please go ahead and generate the full code and return it to me here. 

# Output

Here are a few ways to achieve a quadrant-style layout for multiple ChatGPT chats on Fedora with KDE Plasma and Wayland. You can either use existing window management features or develop a custom solution.

### 1. **Using KDE’s Native Tiling and Window Management**
KDE Plasma has built-in window tiling and keyboard shortcuts, which you can leverage for this purpose. Here’s how:

#### Steps:
1. **Open Multiple Browser Tabs**: Open four tabs in your browser (e.g., Firefox or Chrome) and load ChatGPT in each tab.
2. **Move Each Tab to a Separate Window**:
    - Right-click on each tab and select **Move Tab to New Window**.
3. **Use KDE’s Window Tiling Feature**:
    - Arrange the four browser windows into a quadrant by dragging them to the corners of the screen, or by pressing `Meta` + Arrow Keys.
4. **Assign Custom Shortcuts for Navigating Windows**:
    - Go to **System Settings > Shortcuts > Global Shortcuts**.
    - Assign shortcuts like `Alt+1`, `Alt+2`, etc., to focus on each window.
5. **Highlight Active Window**:
    - Plasma automatically highlights the active window, but if you need more customization, you can install the **Kwin Scripts** (Window Management) and adjust the window behavior.

### 2. **Using a Custom Tiling Manager**
If you want more control, you can use a custom tiling window manager or tool that integrates with KDE Plasma, such as:

- **Bismuth** (formerly KWin Tiling Extension): A KDE extension that enables automatic tiling. You can configure it for a quadrant layout.
  - Install it from KDE Store or GitHub.
  - Configure it to split your screen into four quadrants and assign custom shortcuts.

### 3. **Developing a Custom Browser Interface for Quadrant Chat Management**
If you prefer to develop something custom, you could create a simple HTML/CSS/JavaScript interface that splits the browser into four panes, with each pane holding an embedded ChatGPT session.

Here’s a basic approach:

#### HTML & CSS for Quadrant Layout
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChatGPT Quadrant Layout</title>
    <style>
        body, html {
            margin: 0;
            height: 100%;
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            grid-gap: 5px;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
        .pane {
            outline: none;
        }
        .active {
            border: 3px solid red; /* Highlight active chat */
        }
    </style>
</head>
<body>
    <iframe class="pane" src="https://chat.openai.com"></iframe>
    <iframe class="pane" src="https://chat.openai.com"></iframe>
    <iframe class="pane" src="https://chat.openai.com"></iframe>
    <iframe class="pane" src="https://chat.openai.com"></iframe>

    <script>
        let panes = document.querySelectorAll('.pane');
        let currentPane = 0;

        function highlightPane() {
            panes.forEach((pane, index) => {
                if (index === currentPane) {
                    pane.classList.add('active');
                } else {
                    pane.classList.remove('active');
                }
            });
        }

        document.addEventListener('keydown', (event) => {
            if (event.key === 'Tab') {
                event.preventDefault();
                currentPane = (currentPane + 1) % panes.length;
                highlightPane();
            }
        });

        highlightPane();
    </script>
</body>
</html>
```

#### Steps to Use the Code:
1. Save the code as `quadrant_chat.html`.
2. Open it in your browser.
3. This will create a 2x2 grid with each pane loading the ChatGPT interface.
4. Press `Tab` to cycle between the chats, and the active chat will be highlighted.

This setup allows you to keep four ChatGPT sessions open in a grid, and you can use the `Tab` key to navigate between them. You can modify this further for your specific needs.

### 4. **Custom Desktop App**
You could take the above idea and develop a desktop app using tools like **Electron.js**, which allows you to build native-like applications using web technologies. This app can load multiple browser windows and handle keyboard shortcuts for easy navigation between them.

Let me know which option appeals to you, or if you'd like me to help further with any of these approaches!