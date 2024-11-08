---
title: "Preventing HA from automatically reordering the sidebar"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


In Home Assistant, my sidebar seems to be ordered alphabetically. I can try to create a custom layout but it reverts. Can I take this setting off?

# Output

In Home Assistant, the sidebar ordering is often controlled by the system, and the default behavior can indeed result in alphabetical ordering. However, you can manually reorder the sidebar to suit your preferences. Here’s how you can fix this and prevent it from reverting:

### 1. **Manual Sidebar Reordering:**
   Home Assistant allows you to reorder the sidebar by dragging and dropping items.

   - **Steps:**
     1. Open your **Home Assistant** dashboard.
     2. Click on your profile icon in the bottom left corner.
     3. Scroll down to the **Sidebar** section.
     4. You can now drag and drop the items in the sidebar to your desired order.
     5. Make sure to save changes.

### 2. **Customizing with YAML (if needed):**
   If the manual reordering doesn’t persist, you may need to check the **customization settings** to ensure that your dashboard is not being reset by some other automation or configuration.

   - If you’ve configured any custom layouts through the `ui-lovelace.yaml` file, ensure it is correctly set up to retain your desired layout.

### 3. **Disable Automatic Sorting:**
   - **Steps:**
     1. Go to **Profile** in Home Assistant (click on your avatar in the bottom left).
     2. Scroll down to the section labeled **"Sidebar order"**.
     3. Toggle off **"Sort by name"** to ensure the system does not automatically sort it alphabetically.

### 4. **Check Browser Cache (if applicable):**
   If the sidebar order keeps reverting, it may also be related to browser caching. Try clearing your cache or testing the behavior in an incognito window to see if the problem persists.

Following these steps should help you reorder the sidebar as desired and stop it from reverting to alphabetical order.

Let me know if you run into any issues!