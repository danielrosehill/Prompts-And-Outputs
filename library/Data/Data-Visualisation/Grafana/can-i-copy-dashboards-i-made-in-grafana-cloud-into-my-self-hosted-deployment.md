---
title: "Can I copy dashboards I made in Grafana Cloud into my self hosted deployment"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


I created some dashboards on Grafana Cloud. I'm now using a self hosted version. I backed up the JSON configuration. Is there any way to simply copy the dashboards over assuming that I have the same plugins in both environments?
# Output

Yes, you can copy dashboards from Grafana Cloud to your self-hosted Grafana instance using the JSON configuration you backed up. Here's a step-by-step process to do that, assuming you have the same plugins installed in both environments:

### Steps to Import Dashboards

1. **Export the Dashboard JSON**:
   - In your Grafana Cloud instance, navigate to the dashboard you want to export.
   - Click on the **Dashboard settings** (gear icon).
   - Go to **JSON Model** and click on **Export JSON** to save the configuration.

2. **Access Your Self-Hosted Grafana**:
   - Log in to your self-hosted Grafana instance.

3. **Import the Dashboard**:
   - From the left-hand menu, click on the **Plus (+)** icon and select **Import**.
   - You have two options for importing:
     - **Paste JSON**: Copy the JSON configuration you exported and paste it directly into the input box.
     - **Upload JSON file**: If you saved the JSON to a file, you can upload it directly.

4. **Configure Data Sources**:
   - After importing, you may need to map the imported dashboard to the correct data sources if the names differ between the two environments. Grafana will prompt you to select the appropriate data sources during the import process.

5. **Save the Dashboard**:
   - Once the import is successful, review the dashboard to ensure everything displays correctly and save it.

### Additional Considerations

- **Plugins**: Ensure that all plugins used in the dashboards are installed on your self-hosted Grafana instance. Missing plugins can cause panels to break or not render properly.
  
- **Variable Configuration**: If your dashboard uses variables, make sure these are configured identically in both environments. Check under **Dashboard settings > Variables** to verify.

- **Testing**: After importing, review the dashboards for any discrepancies or missing data and adjust as necessary.

### References
- [Grafana Documentation: Importing and Exporting Dashboards](https://grafana.com/docs/grafana/latest/dashboards/export-import/)
- [Grafana Cloud Documentation](https://grafana.com/docs/grafana-cloud/latest/) 

This process should allow you to effectively transfer your dashboards from Grafana Cloud to your self-hosted instance while maintaining their functionality.