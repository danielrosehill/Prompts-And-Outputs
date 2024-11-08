---
title: "Grafana plugins for displaying RSS feeds"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


If you're looking to display **RSS feeds** on your **Grafana dashboard**, one of the most popular and powerful plugins is the **Business News** plugin by **Volkov Labs**. This plugin allows you to retrieve and display RSS and Atom feeds within Grafana, making it perfect for tracking news updates and visualizing them in a dashboard format.

### Key Features of the Business News Plugin:
- **Supports RSS 2.0, RSS 1.0, and Atom feeds**.
- Works well with the **Dynamic Text panel**, allowing for customizable feed display.
- Extracts and parses additional fields from feeds, including images and media, making the presentation more engaging.
- Filters items based on time ranges and allows for the specification of query parameters with dashboard variables.
  
### Installation:
You can install the **Business News** plugin using Grafana's CLI:
```bash
grafana-cli plugins install volkovlabs-rss-datasource
```
This will set up the plugin, after which you can configure it to fetch and display your desired RSS or Atom feeds within a Grafana dashboard.

### Additional Features:
- Combine multiple feeds into a single dashboard panel for a consolidated view.
- Handles YouTube feeds (via **Media:Group**) and supports extracting images or encoded content from metadata.

This plugin is part of the **Business Suite for Grafana**, which provides a range of additional functionalities for business use cases. If you plan to expand your dashboard beyond news feeds, the suite offers tools for calendars, charts, and input panels.

For more detailed instructions, you can refer to [Volkov Labs' official documentation](https://volkovlabs.io/plugins/business-news)【111†source】【113†source】.