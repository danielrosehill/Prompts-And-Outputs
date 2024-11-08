---
title: "Newsboat URL file template"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Certainly! Here's a **basic template** for the `urls` file (`~/.newsboat/urls`) in Newsboat. This file is where you list your RSS/Atom feed URLs and optionally assign them to categories (using tags).

### Basic `urls` File Template

```txt
# Israel News (English)
https://www.jpost.com/Rss/RssFeedsHeadlines.aspx israel_english
https://www.timesofisrael.com/feed/ israel_english

# Israel News (Hebrew)
https://www.ynet.co.il/Integration/StoryRss2.xml israel_hebrew
https://www.haaretz.co.il/cmlink/1.1458916 israel_hebrew

# World News
https://feeds.bbci.co.uk/news/rss.xml world_news
https://rss.cnn.com/rss/edition.rss world_news

# World Newswires
https://www.reuters.com/rssFeed/worldNews world_newswires
https://www.apnews.com/apf-topnews?format=rss world_newswires
```

### Key Points:
- Each line represents a **feed URL** followed by an optional **tag**.
- Tags (like `israel_english`, `world_news`, etc.) can be used to group and filter feeds in Newsboat.
- You can organize feeds into categories by using tags and grouping them with comments (`#`), although the comments are just for readability and aren't processed by Newsboat.

### How to Use:
1. **Open the `urls` file** in a text editor:
   ```bash
   nano ~/.newsboat/urls
   ```

2. **Add the RSS feed URLs** with or without tags. Tags are useful if you want to filter feeds by category in Newsboat.

3. **Save and close** the file, then refresh Newsboat to load your feeds.

### Example for a Custom Setup:
If you wanted to track **tech news** and **podcasts**, your file might look like this:

```txt
# Tech News
https://feeds.arstechnica.com/arstechnica/index tech
https://www.theverge.com/rss/index.xml tech

# Podcasts
https://feeds.megaphone.fm/WWO3519750114 podcasts
https://feeds.feedburner.com/thejournal-podcast podcasts
```

Feel free to customize the feed URLs and tags to match your categories and interests.

# Can you give titles to the feeds?

Unfortunately, **Newsboat's `urls` file** doesn't support giving individual feed entries custom titles directly within the file. The `urls` file is limited to just specifying feed URLs and optionally adding tags for organizational purposes. Titles and more detailed descriptions are handled by the RSS feeds themselves and are displayed in Newsboat based on the metadata provided by the feed.

### What You Can Do Instead:

#### 1. **Use Tags for Organization**
While you can’t give each feed a custom title, you can use **tags** to group and filter your feeds logically. This helps create categories but doesn’t give each individual feed a title.

Example:

```txt
https://feeds.bbci.co.uk/news/rss.xml world_news
https://rss.cnn.com/rss/edition.rss world_news
```

#### 2. **Use Comments to Label Feeds**
You can use **comments** (lines starting with `#`) to add descriptions or titles above each feed. Though these comments aren’t shown in the Newsboat interface, they can make the `urls` file more readable for you.

Example:

```txt
# BBC News Feed
https://feeds.bbci.co.uk/news/rss.xml world_news

# CNN News Feed
https://rss.cnn.com/rss/edition.rss world_news
```

#### 3. **Feed Titles Displayed in Newsboat**
The actual **title** of each feed will be determined by the RSS feed itself and will be displayed inside Newsboat when you load your feeds. These are controlled by the feed publishers and appear as the title of the feed (e.g., "BBC News - World" or "CNN Top Stories").

#### 4. **Filter Feeds Using Tags**
You can apply filters inside Newsboat based on tags. For example, if you have multiple feeds tagged as `world_news`, you can filter them using the `/` command within Newsboat:

- Press `/` in Newsboat and type `world_news` to filter all feeds with that tag.

#### 5. **Organizing Feeds by Folder**
If you're using **OPML files** (e.g., for bulk importing feeds), you can organize feeds in an external format by category and then extract them into the `urls` file. However, you still can't assign individual custom titles within the Newsboat interface itself.

### Conclusion:
While you can't assign custom titles to individual feeds directly in the `urls` file, you can use **tags** and **comments** to organize and annotate the feeds. The titles will be displayed in the Newsboat interface as provided by the RSS feed metadata.