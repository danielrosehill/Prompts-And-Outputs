---
title: "Adding clock to Grafana panel"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*



# Prompt

I'd like to add a clock to my Grafana panel with UTC + local. How do I do this?

# Output

To add a clock displaying both UTC and local time to your **Grafana** panel, you'll need to use a **Grafana plugin** designed for time displays, such as the **Clock Panel plugin**. This plugin allows you to show time in different time zones, including both UTC and local time.

### Steps to Add a Clock with UTC + Local Time in Grafana:

### 1. **Install the Clock Panel Plugin**
Grafana provides a built-in plugin called **Clock Panel** that you can use to display time. If it's not already installed, you can install it using the Grafana CLI or via the Grafana UI.

#### a. Install via CLI:
1. Run the following command to install the Clock Panel plugin:
   ```bash
   grafana-cli plugins install grafana-clock-panel
   ```

2. Restart Grafana to activate the plugin:
   ```bash
   sudo systemctl restart grafana-server
   ```

#### b. Install via Grafana UI:
1. Go to **Configuration** (gear icon) > **Plugins** in Grafana.
2. Search for the **Clock Panel** plugin and click **Install**.

### 2. **Add the Clock Panel to Your Dashboard**
Once the plugin is installed, you can now add the clock panel to your dashboard.

#### Steps:
1. **Create or edit a dashboard** in Grafana.
2. Click **"Add Panel"**.
3. In the **Visualization** section, search for and select the **Clock Panel**.
4. In the panel settings, under **Time Options**, configure the following:

   - **Time Zone 1**: Set to `UTC`.
   - **Time Zone 2**: Set to `Local browser time` (or whichever local time zone you prefer).

5. You can also configure how the time is displayed (12-hour or 24-hour format), and you can customize the panel’s appearance.

6. Once you’re satisfied with the configuration, click **Apply** to save the panel.

### 3. **Configure Multiple Clocks (Optional)**
If you want to show both UTC and Local time in separate panels, you can add multiple Clock Panels to the same dashboard. Configure one for **UTC** and another for **Local Time**.

#### Steps for Multiple Clocks:
1. Add a new Clock Panel as described above.
2. In the settings, set one panel to show **UTC** time and the other to show **Local Time**.
3. Arrange the panels in your dashboard as needed.

### 4. **Customize the Look and Feel**
You can customize the appearance of the clock by changing:
   - **Date format**: Configure how the date/time is displayed (12-hour, 24-hour, etc.).
   - **Font size** and **text color**.
   - Add a background image if needed for further customization.

### Example:
Here’s how to configure a panel showing both UTC and local time:
   - Time Zone 1: `UTC`
   - Time Zone 2: `Browser Local Time`
   - 24-hour time format.

### Summary:
1. Install the **Clock Panel** plugin via Grafana CLI or UI.
2. Add a **Clock Panel** to your dashboard.
3. Configure the panel to display both **UTC** and **Local Time**.
4. Optionally, add multiple Clock Panels for separate time zone displays.

Let me know if you need more help with this setup!