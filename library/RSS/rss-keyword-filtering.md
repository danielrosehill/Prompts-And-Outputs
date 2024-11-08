---
title: "RSS keyword filtering"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To set up an **RSS feed** that only shows items that match specific keywords, you can use various tools and methods. Below are some approaches you can use to filter an RSS feed for keyword matches.

### 1. **Using RSS Filtering Services**
There are several web services that allow you to filter an RSS feed based on keywords. These services let you input an RSS feed and set up filters for specific words or phrases, showing you only the matching items.

#### a) **Feed Rinse**
   - **Description**: **Feed Rinse** is a web-based service designed specifically for filtering RSS feeds based on keywords. It allows you to input your RSS feed and create custom filters for keywords or phrases.
   - **How it works**:
     1. Sign up for a **Feed Rinse** account.
     2. Add the RSS feed you want to filter.
     3. Create rules that specify the keywords you want to match (include or exclude).
     4. Use the filtered RSS feed URL to view the results.
   - **Website**: [Feed Rinse](https://feedrinse.com)
   
#### b) **FilterRSS**
   - **Description**: **FilterRSS** allows you to filter an existing RSS feed by keywords, excluding irrelevant content.
   - **How it works**:
     1. Enter the RSS feed URL.
     2. Define the keywords you want to filter by (you can choose to include or exclude content with certain keywords).
     3. It generates a new RSS feed URL with only the filtered results.
   - **Website**: [FilterRSS](https://filterrss.com)

#### c) **RSS.app**
   - **Description**: **RSS.app** is a tool that lets you create RSS feeds and also provides filtering options for existing feeds. You can filter based on keywords and get a clean feed that matches your criteria.
   - **How it works**:
     1. Enter the RSS feed you want to filter.
     2. Set up keyword-based rules (include or exclude specific terms).
     3. Save the filtered feed and use the new URL.
   - **Website**: [RSS.app](https://rss.app/)

### 2. **Using Feed Reader Software with Built-In Filters**
Some **RSS readers** have built-in filtering mechanisms that allow you to set up keyword-based filters directly within the reader. Here are a couple of options:

#### a) **Inoreader**
   - **Description**: **Inoreader** is a powerful RSS reader with built-in **filtering** capabilities. You can create rules to show only articles that match specific keywords.
   - **How it works**:
     1. Add your RSS feed to **Inoreader**.
     2. Go to **Subscriptions** > **Rules** > **Create a Rule**.
     3. Define the rule to filter content based on the keywords you want.
     4. Inoreader will only show articles that match the keywords.
   - **Website**: [Inoreader](https://www.inoreader.com)
   
#### b) **NewsBlur**
   - **Description**: **NewsBlur** is another RSS reader that allows you to filter feeds based on keyword matches.
   - **How it works**:
     1. Add your RSS feed to **NewsBlur**.
     2. Set up **training** for your feed by clicking on keywords to highlight content you want to see more or less of.
     3. The reader will automatically filter articles based on your keyword preferences.
   - **Website**: [NewsBlur](https://newsblur.com)

### 3. **Create Custom Filtered RSS Feeds with Yahoo Pipes Alternatives**
Yahoo Pipes was a popular service for creating custom RSS feeds with filters, but it was discontinued. However, several alternatives allow you to build custom filtered RSS feeds:

#### a) **Pipe Dream** (Self-hosted solution)
   - **Description**: **Pipe Dream** is a **self-hosted alternative to Yahoo Pipes**, allowing you to create customized workflows, including filtering RSS feeds by keyword.
   - **How it works**:
     1. Install **Pipe Dream** on your server (requires some technical knowledge).
     2. Set up a workflow that fetches your RSS feed, filters it by keyword, and generates a new RSS feed with only the relevant items.
   - **Website**: [Pipe Dream](https://github.com/pipedreamhq/pipedream)

#### b) **IFTTT (If This Then That)**
   - **Description**: **IFTTT** can be used to create custom filtered RSS feeds by combining RSS feeds with keyword triggers. It won't generate a new RSS feed, but it can send filtered articles via email or to a different platform.
   - **How it works**:
     1. Set up a new **IFTTT Applet** using the **RSS Feed** service.
     2. Use the **"New feed item matches"** trigger to only pull in articles that match your keywords.
     3. Choose where to send the filtered items (e.g., email, Slack, or other services).
   - **Website**: [IFTTT](https://ifttt.com)

### 4. **Host Your Own Filtered RSS Feed with Tiny Tiny RSS**
   - **Description**: **Tiny Tiny RSS** is a self-hosted, open-source RSS reader that includes advanced filtering options for keyword-based rules.
   - **How it works**:
     1. Install **Tiny Tiny RSS** on a server or local machine.
     2. Add your RSS feeds to the reader.
     3. Set up filters using the **Filters** menu, specifying keywords to include or exclude.
     4. Use the filtered RSS feed within Tiny Tiny RSS or export it for use elsewhere.
   - **Website**: [Tiny Tiny RSS](https://tt-rss.org)

### 5. **Custom RSS Filtering with Python (Advanced)**
   If you prefer full control, you can create a **custom script** using Python to filter an RSS feed for keywords.

#### Sample Python Script Using `feedparser`:
This simple Python script fetches an RSS feed, filters it by keyword, and prints out matching articles:

```python
import feedparser

# Your RSS feed URL
rss_feed_url = "https://example.com/rss"

# Keywords to match
keywords = ["keyword1", "keyword2"]

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

# Filter and display the matching entries
for entry in feed.entries:
    if any(keyword.lower() in entry.title.lower() or keyword.lower() in entry.description.lower() for keyword in keywords):
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Description: {entry.description}\n")
```

#### How to Use:
1. Replace the `rss_feed_url` with your desired RSS feed.
2. Add the keywords you want to filter by in the `keywords` list.
3. Run the script to get a filtered list of RSS entries that match your keywords.

---

### Conclusion:
There are plenty of options for filtering an RSS feed to only show keyword matches. Depending on your needs, you can use:

- **Web-based filtering services** like **Feed Rinse** or **FilterRSS**.
- **RSS readers with built-in filters** like **Inoreader** or **NewsBlur**.
- **Custom solutions** with Python or using services like **IFTTT**.

Let me know if you need help setting up any of these!