---
title: "Copying rows between Grafana dashboards"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Yes, it is possible to copy rows or panels between Grafana dashboards by copying the **JSON definition** of a row or panel from one dashboard and pasting it into another dashboard's JSON configuration. Here’s how you can do it:

### Steps to Copy Rows or Panels Between Dashboards:

#### 1. **Open the Dashboard for Editing**:
   - Navigate to the dashboard that contains the row or panel you want to copy.
   - Click on the **gear icon** (⚙) at the top of the dashboard to open the **Dashboard Settings**.

#### 2. **Go to the JSON Model**:
   - In the Dashboard Settings, select **JSON Model** from the left-hand side menu.
   - You’ll see the JSON representation of your dashboard.

#### 3. **Locate the Row or Panel**:
   - Scroll through the JSON to find the row or panel you want to copy.
   - Rows and panels are represented as **JSON objects**. You can identify them by looking for the `type` field (e.g., `"type": "row"` or `"type": "graph"`).
   - Select the JSON block corresponding to the row or panel and copy it.

#### 4. **Open the Destination Dashboard**:
   - Navigate to the dashboard where you want to paste the copied row or panel.
   - Again, click the **gear icon** (⚙) to access the **Dashboard Settings** and go to the **JSON Model**.

#### 5. **Paste the JSON**:
   - In the JSON of the destination dashboard, find the appropriate place to insert the copied row or panel.
     - You may want to place it at the end of the `"panels"` array or within a specific section, depending on where you want it to appear.
   - Paste the copied JSON code for the row or panel into the appropriate spot.

#### 6. **Save the Dashboard**:
   - Once you've pasted the JSON, click **Save** to apply the changes.
   - Exit the settings, and the row or panel should now appear in the new dashboard.

### Example of a JSON Panel:
If you want to copy a panel, it will look something like this in the JSON:

```json
{
  "type": "graph",
  "title": "My Panel",
  "gridPos": {
    "h": 9,
    "w": 12,
    "x": 0,
    "y": 0
  },
  "id": 2,
  "datasource": "my-datasource",
  "targets": [
    {
      "target": "my-query"
    }
  ]
}
```

You can copy this block and paste it into the destination dashboard’s JSON in the `"panels"` array.

### Notes:
- **Panel IDs**: Ensure that panel IDs in the destination dashboard are unique. Grafana may automatically update them if there is a conflict, but it's good to check.
- **Datasource**: Ensure the datasource used in the panel is available in both dashboards, or adjust the `"datasource"` field accordingly.

### Conclusion:
By copying and pasting the relevant JSON sections, you can move rows or panels between Grafana dashboards. This is useful for reusing existing configurations without manually recreating panels.