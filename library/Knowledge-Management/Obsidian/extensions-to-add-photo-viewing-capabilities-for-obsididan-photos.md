---
title: "Extensions to add photo viewing capabilities for Obsididan photos"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


in obsidian, when i click on a photo that I've saved in a note, I'm not able to copy it (for instance if I want to copy the note over into a tool like GIMP to edit it. Or perhaps I'd like to open it in an external app like a photo viewer in larger size. Are there any extensions that can add these functionalities?

# Output



In Obsidian, the default behavior for handling images can be somewhat limited. However, there are some community plugins that can extend the functionality you're looking for, allowing you to either copy images directly or open them in an external app.

Here are a few options to enhance image handling in Obsidian:

### 1. **"Image Toolkit" Plugin**
   - The **Image Toolkit** plugin provides more advanced options for handling images, including copying images to the clipboard and exporting them.
   - Once installed, you can right-click on an image and select options such as copying to the clipboard or exporting the image to an external tool.
   - This plugin may also allow resizing or performing simple image operations directly in Obsidian, enhancing the image management capabilities.

### 2. **"Custom Frames" Plugin**
   - The **Custom Frames** plugin allows you to add external applications into Obsidian.
   - You can set up a "frame" that links to your favorite image editor, like GIMP. This way, you can easily open an image from Obsidian directly in GIMP for editing.
   - It requires a bit of setup, but it can create a seamless way to transition between Obsidian and external tools.

### 3. **"Right-click Image Actions" Plugin**
   - This plugin enhances right-click functionality for images in your notes.
   - It adds options like "Open in External Viewer," which would let you view the image using the default photo viewer on your device, or "Copy Image," which places the image on the clipboard for pasting elsewhere.
   - This would be particularly helpful for copying an image into GIMP or any other image editor.

### 4. **"Obsidian Image in New Tab" Community Snippet**
   - You can use CSS snippets to customize Obsidian behavior. There is a community snippet called **Image in New Tab** that allows you to click on an image to open it in a new tab.
   - Once the image is opened in a new tab, you can right-click to copy it or use the browser’s “Open Image in New Tab” to open it larger.
   - To add this snippet:
     1. Go to **Settings > Appearance > CSS Snippets**.
     2. Add a new snippet with the necessary CSS and enable it.

### 5. **Use "Open with Default App" Setting**
   - If you want to open an image in an external application, you can enable the **"Open with Default App"** option by modifying the default behavior in the **Attachments** settings of Obsidian.
   - By default, Obsidian uses its internal viewer. But by configuring Obsidian to always open certain file types (like images) in the system's default viewer, you can click on images to open them directly in your preferred image viewer or editor.

### Summary
- **Image Toolkit** and **Right-click Image Actions** plugins provide features like copying images and opening them in external tools.
- **Custom Frames** can integrate external applications like GIMP within Obsidian.
- CSS snippets, like **Image in New Tab**, can add flexibility to open images in a new tab.

These plugins and customizations should help give you the extended image handling functionality you're looking for in Obsidian. Let me know if you need help with installing any of these plugins or customizing the settings further!