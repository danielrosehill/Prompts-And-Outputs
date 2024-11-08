---
title: "Duplicating Grafana dashboards"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, you can easily **duplicate a dashboard** in Grafana. This can be useful when you want to create a similar dashboard with slight modifications or use it as a template for other dashboards.

### Steps to Duplicate a Dashboard in Grafana:

#### Method 1: Using the "Save As" Option
1. **Open the Dashboard**:
   - Navigate to the dashboard you want to duplicate.

2. **Click on the Dashboard Title**:
   - Click on the dashboard's title at the top of the page, or use the gear icon (⚙) on the top right of the dashboard to open the dashboard menu.

3. **Select "Save As"**:
   - In the dropdown menu, click on **Save As**.

4. **Rename the Duplicated Dashboard**:
   - A dialog box will appear where you can change the name of the dashboard.
   - Enter a new name for the duplicated dashboard.

5. **Click "Save"**:
   - The new dashboard will now be saved as a copy of the original one.

#### Method 2: Export and Import
1. **Export the Dashboard**:
   - Open the dashboard you want to duplicate.
   - Click on the **dashboard menu** (three dots in the top-right corner).
   - Select **Share** and then go to the **Export** tab.
   - Click **Save to file** to download the dashboard's JSON file.

2. **Import the Dashboard**:
   - Go back to the main Grafana dashboard.
   - Click the **+ (Create)** button on the left-hand menu, then select **Import**.
   - You can either paste the JSON code or upload the JSON file you just downloaded.
   - Give the imported dashboard a new name.

3. **Save the Imported Dashboard**:
   - Once imported, you can make any changes and save the new dashboard under a different name.

#### Method 3: Copy JSON Definition
1. **Copy JSON from Original Dashboard**:
   - Go to the **Settings** (⚙) of the dashboard you want to duplicate.
   - Click on **JSON Model** under the settings menu.
   - Copy the entire JSON content.

2. **Create a New Dashboard**:
   - In Grafana, click **+ (Create)** from the left-hand menu and select **Dashboard**.
   - In the newly created dashboard, go to the **Settings** (⚙) and select **JSON Model**.

3. **Paste the Copied JSON**:
   - Paste the JSON that you copied from the original dashboard.
   - Save the new dashboard.

### Conclusion:
The easiest way to duplicate a dashboard is using the **Save As** method, but if you want more control over the content or structure, you can also use the **export/import** method or manually copy the JSON model.

Let me know if you need further guidance on any of these methods!