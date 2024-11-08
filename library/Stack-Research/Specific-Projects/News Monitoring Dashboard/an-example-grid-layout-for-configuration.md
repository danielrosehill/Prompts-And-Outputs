---
title: Test grid layout for media monitoring
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

here's an example of 4 urls that I'd like to show in a 2 x 2 grid. Can you suggest some chrome extensions or perhaps even websites that would allow me to create this layout in a way that would be easy to "reuse" (Ie it's either a standalone webpage or a shrotcut I can reuse): https://www.oref.org.il/eng/alerts-history https://www.kan.org.il/live/ https://video.i24news.tv/live/brightcove/en https://www.timesofisrael.com

# Output

To display these four URLs in a **2x2 grid layout** that you can easily reuse, here are some suggestions using **Chrome extensions** or **web-based tools**. The idea is to create a layout that you can save as a shortcut or easily reopen as a session. Here are some solutions:

### 1. **Tab Resize - Split Screen Layouts (Chrome Extension)**
This extension is perfect for setting up a reusable 2x2 grid layout.

#### Steps to Create a 2x2 Layout:
1. Install **[Tab Resize](https://chrome.google.com/webstore/detail/tab-resize-split-screen-la/xxxxxxx)** from the Chrome Web Store.
2. Open the four URLs in Chrome:
   - [https://www.oref.org.il/eng/alerts-history](https://www.oref.org.il/eng/alerts-history)
   - [https://www.kan.org.il/live/](https://www.kan.org.il/live/)
   - [https://video.i24news.tv/live/brightcove/en](https://video.i24news.tv/live/brightcove/en)
   - [https://www.timesofisrael.com](https://www.timesofisrael.com)
3. Click the **Tab Resize** icon in your Chrome toolbar.
4. Select a **2x2 grid layout**. The extension will resize and arrange the four tabs automatically.
5. To reuse this layout:
   - Save the session using **Chrome's bookmark manager** (bookmark all four URLs in a folder).
   - You can easily reopen the URLs in a new window and use **Tab Resize** again for quick grid setup.

### 2. **Tile Tabs WE (Chrome Extension)**
**Tile Tabs WE** is another Chrome extension that lets you tile tabs in a grid format.

#### Steps to Set Up:
1. Install **[Tile Tabs WE](https://chrome.google.com/webstore/detail/tile-tabs-we/xxxxxxx)** from the Chrome Web Store.
2. Open the four URLs in separate tabs.
3. Click on the **Tile Tabs WE** icon in your toolbar.
4. Choose the **grid layout (2x2)** option to tile the four tabs.
5. To reuse:
   - You can save the tile session within the extension itself.
   - The next time you open Chrome, you can restore the saved tile layout directly from **Tile Tabs WE**.

### 3. **Tab Session Manager (Chrome Extension)**
If you want a simple way to **save and restore sessions** of your grid layout, **Tab Session Manager** is a great extension.

#### Steps to Set Up:
1. Install **[Tab Session Manager](https://chrome.google.com/webstore/detail/tab-session-manager/xxxxxxx)** from the Chrome Web Store.
2. Open the four URLs and arrange them using **Tab Resize** or **Tile Tabs WE** into the 2x2 grid.
3. Save the session using Tab Session Manager:
   - Click the Tab Session Manager icon and **save the current session**.
4. To reuse the layout, simply open the saved session with all four URLs arranged in the same layout.

### 4. **Dualless (Chrome Extension)**
**Dualless** is a simple extension designed to emulate dual monitor setups but also works for splitting and organizing tabs.

#### Steps to Set Up:
1. Install **[Dualless](https://chrome.google.com/webstore/detail/dualless/xxxxxxx)** from the Chrome Web Store.
2. Open the four URLs.
3. Use **Dualless** to create a 2x2 layout:
   - Open two tabs side by side.
   - Then, manually tile the second two tabs beneath them.

### 5. **Create a Custom Standalone Web Page (Manual Setup)**

If you prefer not to use extensions, you can manually create a **standalone HTML webpage** that shows the four URLs in a 2x2 grid.

#### Steps:
1. Create a simple HTML file with `iframe` tags to embed the URLs.

```html
<!DOCTYPE html>
<html>
<head>
    <title>2x2 Grid</title>
    <style>
        body {
            margin: 0;
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            height: 100vh;
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <iframe src="https://www.oref.org.il/eng/alerts-history"></iframe>
    <iframe src="https://www.kan.org.il/live/"></iframe>
    <iframe src="https://video.i24news.tv/live/brightcove/en"></iframe>
    <iframe src="https://www.timesofisrael.com"></iframe>
</body>
</html>
```

2. Save this as `grid.html` on your local machine.
3. Open the HTML file in any browser, and it will show the four websites in a 2x2 grid.
4. You can create a desktop shortcut to this HTML file for easy reuse.

### 6. **Web-Based Tool: Browser Tiling Websites**
Alternatively, you can use web-based tools designed to tile websites:

- **Quad (quadmeup.com)**: A tool that lets you open up to four URLs in a grid layout. You can save this page as a bookmark and reuse it whenever you want.
  - Visit: [https://quadmeup.com](https://quadmeup.com)
  - Enter the four URLs and click **Create Grid**. It will display all four websites in a 2x2 grid.

### Summary of Solutions:

| Solution                 | Method                                                                    | Reusability                                       |
| ------------------------ | ------------------------------------------------------------------------- | ------------------------------------------------- |
| **Tab Resize**           | Chrome extension that arranges tabs into grids.                           | Save session using Chrome or Tab Session Manager. |
| **Tile Tabs WE**         | Chrome extension for grid tiling with save/restore functionality.         | Save tile layout within the extension.            |
| **Tab Session Manager**  | Save entire tab sessions, reopen in grid with Tab Resize or Tile Tabs WE. | One-click session restoration.                    |
| **Dualless**             | Split tabs into layouts but manually needs a bit of setup.                | Simple to reuse for 2x2.                          |
| **Standalone HTML page** | Custom web page using `iframe` to show all 4 websites in 2x2 grid.        | Create desktop shortcut for quick access.         |
| **Quad (quadmeup.com)**  | Online tool for tiling multiple URLs.                                     | Save as a bookmark for easy reuse.                |

### Conclusion:
For the easiest reusable solution:
- **Tab Resize** and **Tile Tabs WE** are great for quickly setting up grids in Chrome.
- Alternatively, creating a custom HTML page with `iframe`s provides a clean, standalone solution.

Let me know if you'd like help setting up any of these options!