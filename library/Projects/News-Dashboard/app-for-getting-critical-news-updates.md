---
title: "App for getting critical news updates"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Since Iran instigated its various missile attacks against Israel, I have been more conscious about the importance of checking the news regularly (I live in Israel). Equally I don't want to get sucked into spending too much time reading speculation. I've been looking for something like an app which provides a daily (or twice daily) synopsis of the security situation in the region but which only focuses on major developments such as potential impending attacks. I would prefer a system that simply wouldn't deliver if there wasn't things to update about. Does any such system exist? If not, could you suggest how I might be able to implement my own one, perhaps using an LLM to process a news feed at set intervals?

# Output

There isn't a widely-known app that perfectly fits your request, but you can definitely set up a custom system for this purpose. Here's how you can implement your own security update service using tools like news APIs and an LLM for filtering and summarizing the news feed.

### Step 1: News Aggregation via API
You can use news APIs to gather the latest news updates related to Israel's security situation. Some recommended sources:
- **NewsAPI.org**: This API aggregates news from several sources. You can filter news based on specific keywords like "Israel security," "Iran missile," etc.
- **Bing News Search API**: Offers robust filtering and updates.
- **Google News API**: Focuses on the most recent developments and has similar filtering.

### Step 2: Filter for Major Developments
Once you've gathered news through the API, use a simple script to filter articles based on keywords or topics that match "major developments." For example, you might look for terms like "impending attack," "missile strikes," "military movements," and "escalation." You can combine this with sentiment analysis to detect potentially high-impact articles.

### Step 3: Summarizing with an LLM
To implement an LLM for summarizing, you could automate it using GPT:
1. Collect news articles at regular intervals (e.g., daily or twice a day).
2. Filter and condense the news into a short summary by using an LLM. You can host the LLM locally, or call a service like OpenAI’s GPT-4 API for this.
3. Add logic that skips sending updates if there’s no significant news to report. You could define this threshold using factors like the number of high-sentiment articles or specific threat-related terms.

### Example Setup:
- **Python script** that runs twice daily using a cron job (or another scheduler).
- API calls to the chosen news aggregator.
- News filtering based on predefined terms.
- Summarization using an LLM.
- If relevant updates are detected, the script sends a notification (via email, SMS, or your preferred messaging platform).

If you'd like, I can help you set up an example script for this system. Would you prefer email notifications, or is there another format you'd like updates delivered in?