---
title: How to ensure iFrames display on Grafana
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

any other changes i need to make to make sure that I can show rss feeds and embedded in grafana

# Output

To display RSS feeds and embedded content in Grafana, in addition to enabling iframes, you may need to adjust a few more settings in the `grafana.ini` file and ensure that you are using the right data source and panel plugins. Here’s a comprehensive guide:

### 1. Enable Iframes

As previously mentioned, ensure that you set the following in the `[security]` section of your `grafana.ini` file:
```plaintext
[security]
allow_embedding = true
```

### 2. CORS Settings

To allow external content, including RSS feeds, you might need to adjust CORS (Cross-Origin Resource Sharing) settings. You can do this by adding the following under the `[http]` section:
```plaintext
[http]
# Allow embedding from all domains
enable_gzip = true
```
This configuration helps ensure that Grafana can serve embedded content effectively.

### 3. Data Source for RSS Feeds

Grafana doesn’t natively support RSS feeds out of the box, so you might need a dedicated plugin or workaround:
- **Use a Plugin**: Consider using a community plugin like the **JSON Datasource** or **SimpleJSON** plugin, which can fetch data from an API. You can set up a small backend service that converts RSS feeds into JSON format and then visualize that in Grafana.
- **JSON API**: If your RSS feed can be converted into a JSON API format, this would allow Grafana to pull in the data using a JSON data source【69†source】【71†source】.

### 4. Embed Panels

Once you have the data source set up:
- Use the **Text panel** or **HTML panel** in Grafana to embed your RSS feed or any other content. You can write HTML code that includes an iframe pointing to your RSS feed or to the service that formats it appropriately.

### 5. Ensure Proper Permissions

Make sure your Grafana user has the appropriate permissions to view embedded content, especially if you’re using features that require specific access rights. This can typically be managed in the Grafana user settings or organization settings.

### 6. Restart Grafana

After making any changes to `grafana.ini`, always remember to restart the Grafana service:
```bash
sudo systemctl restart grafana-server
```

### 7. Test the Setup

Finally, create a dashboard in Grafana with the embedded RSS feed or the panel displaying your JSON data source and verify that it renders correctly.

### References

For detailed information on configuring Grafana for embedding content, you can refer to the following resources:
- [Grafana Configuration Documentation](https://grafana.com/docs/grafana/latest/administration/configuration/)
- [Grafana Plugins Directory](https://grafana.com/grafana/plugins) for finding plugins that support RSS or JSON data sources.
- [Grafana Community Forums](https://community.grafana.com/) for discussions on similar setups and community support.

These steps should help you effectively display RSS feeds and other embedded content within Grafana. If you run into any issues, checking the logs or consulting the community may provide additional insights.