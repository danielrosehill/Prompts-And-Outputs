---
title: "Text based browsers"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Here's an example of a text dense site that doesn't provide an RSS but which could be nice to browser from the terminal. Is there any way? https://www.janes.com/osint-insights/defence-news

# Output

Yes, you can browse text-dense websites like **Janes OSINT Insights Defence News** from the terminal using several tools that allow you to extract and view text-based content. Here are some approaches to view the website in a terminal-friendly way:

### 1. **Using `w3m` or `lynx` (Text-based Web Browsers)**
**`w3m`** and **`lynx`** are two popular terminal-based web browsers that allow you to browse websites as text.

#### Install `w3m` or `lynx`:
```bash
sudo dnf install w3m
sudo dnf install lynx
```

#### To Browse the Site with `w3m`:
1. Open `w3m` and navigate to the URL:
   ```bash
   w3m https://www.janes.com/osint-insights/defence-news
   ```
   `w3m` will display the site in a text-only format, stripping out unnecessary graphical elements, but preserving the structure.

#### To Browse the Site with `lynx`:
1. You can also use `lynx` similarly:
   ```bash
   lynx https://www.janes.com/osint-insights/defence-news
   ```

These browsers will allow you to scroll through the content in a clean, text-based format. **`w3m`** tends to handle complex sites better and might be more visually appealing, while **`lynx`** focuses on simplicity.

### 2. **Extracting Content with `curl` or `wget`**
If you just want to **extract the content** of the webpage for quick viewing in the terminal without the full interactive browsing experience, you can use **`curl`** or **`wget`** to fetch the HTML and then pipe it through tools like `w3m` to extract the text.

#### Example with `curl`:
1. Fetch the page content using `curl`:
   ```bash
   curl -s https://www.janes.com/osint-insights/defence-news | w3m -T text/html
   ```

This command will fetch the HTML of the page using `curl`, then pass it to `w3m`, which will render it as plain text.

#### Example with `wget`:
1. Alternatively, you can use `wget`:
   ```bash
   wget -q -O - https://www.janes.com/osint-insights/defence-news | w3m -T text/html
   ```

Both `curl` and `wget` are great for quickly pulling down the content without opening a browser.

### 3. **Using `readable` or `pup` to Extract Readable Content**
You can extract the **main content** of a page by using tools like **`readable`** or **`pup`**. These tools are designed to parse the DOM of a website and extract the most relevant, readable content (similar to what a "Reader Mode" does in a browser).

#### Install `pup` (HTML parser):
```bash
sudo dnf install pup
```

#### Extract Content with `pup`:
1. Use `curl` or `wget` to get the HTML and filter it with `pup`:
   ```bash
   curl -s https://www.janes.com/osint-insights/defence-news | pup 'p text{}'
   ```

This command extracts only the `<p>` (paragraph) elements, displaying the readable content of the page.

### 4. **Web Scraping for Better Formatting**
If the above methods don’t give you a satisfactory text-based rendering of the site, you can take things further by writing a small **scraper** using Python's **BeautifulSoup** and **Requests** libraries.

#### Python Script Example:
```python
import requests
from bs4 import BeautifulSoup

url = 'https://www.janes.com/osint-insights/defence-news'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print article paragraphs
for paragraph in soup.find_all('p'):
    print(paragraph.get_text())
```

- **Install dependencies**:
  ```bash
  pip install requests beautifulsoup4
  ```

- **Run the script** to extract readable content:
  ```bash
  python scrape_janes.py
  ```

This script will fetch the page, parse the HTML, and output the relevant paragraphs to your terminal.

### 5. **RSS-like Solution: Convert Pages to RSS Feeds**
If you want to keep track of updates on the page in a more automated way, you can use a service or tool to convert the page into an RSS-like feed:

- **RSS Bridge**: If you self-host **RSS Bridge**, you can scrape pages and convert them into RSS feeds. You can configure it to scrape the news section of this site and track updates.
- **FiveFilters' Create Feed**: A web service like [FiveFilters](https://createfeed.fivefilters.org/) can be used to create RSS feeds for sites that don't provide them natively. You could try generating an RSS feed for this site and then monitor it in an RSS reader like **Newsboat**.

### 6. **Using `newsboat` to Monitor Page Changes**
While `newsboat` is an RSS reader, you can also use it to **monitor web pages** that update frequently. You can use the `rss-url` feature in combination with a third-party tool like **page2rss** or **PolitePol** to generate RSS feeds from web pages that lack them.

### Conclusion:
For browsing text-heavy websites like **Janes OSINT Insights** from the terminal, tools like **`w3m`** and **`lynx`** work well to display text content. If you're more interested in extracting the main content, using **`curl`** or **`wget`** in combination with **`pup`** or **BeautifulSoup** will give you more control over the readability.

If you want to track updates from that page more easily, converting the page into an **RSS feed** using external services or building a custom scraper can also be effective.