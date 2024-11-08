---
title: "API for extracting metadata from search strings"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there any API that can take as an input a search string and produce from it: the top 10 (or 50 results) along with their publication time and other metadata (like a summary)

# Output

If you want to get the **top results** of a **Google search query**, along with metadata like **publication date** and **summary**, using an automated solution, unfortunately, Google doesn’t provide a direct API for public use to accomplish this exactly. However, you can use the **Google Custom Search API** to get search results along with metadata. Below are some methods to achieve this:

### 1. **Google Custom Search JSON API**
   - **Description**: Google provides a **Custom Search JSON API** that allows you to programmatically query Google and get the top search results, along with metadata such as:
     - **Title**
     - **Snippet/summary**
     - **Link**
     - **Publication date** (when available for news results)
   - **Usage**:
     - This API allows you to get search results from Google using a search query and provides metadata.
     - You can customize the search to include specific **sites** or **news domains**.
   - **Steps**:
     1. **Set up a Custom Search Engine (CSE)** with the sites you want to search.
     2. Use the **Google Custom Search JSON API** to programmatically query the CSE.

   - **Free Tier**: Allows **100 queries per day** for free.
   - **Link**: [Google Custom Search API](https://developers.google.com/custom-search/v1/overview)

   **Example URL to Use the API**:
   ```
   https://www.googleapis.com/customsearch/v1?q=Hamas&cx=YOUR_CSE_ID&key=YOUR_API_KEY
   ```
   The response will include:
   - `"items"`: Contains the top search results.
   - `"title"`, `"link"`, `"snippet"`, and other metadata.

### 2. **Using SerpApi (For Google Search Results)**
   - **Description**: **SerpApi** allows you to scrape Google search results programmatically, including **news** search. It is built specifically to circumvent some limitations that the Google Custom Search API has.
   - **Features**:
     - Provides **publication time** for news articles.
     - Includes **title**, **URL**, and **summary** of the top search results.
   - **Usage**:
     - You can use SerpApi to **search Google** with any query and get **structured metadata** in the response, including the **top 10/50 results**.
   - **Link**: [SerpApi](https://serpapi.com/)

   **Example Request**:
   ```bash
   curl -G "https://serpapi.com/search" \
   -d "q=Hamas" \
   -d "location=Jerusalem" \
   -d "api_key=YOUR_SERPAPI_KEY"
   ```

### 3. **Selenium and Web Scraping** (Less Reliable, but an Option)
   - If you are familiar with **web scraping**, you could use **Selenium** or **BeautifulSoup** in Python to:
     1. Run a **Google search**.
     2. Scrape the **top search results**, including the title, link, and summary.
   - **Limitations**:
     - Google search scraping is against Google’s **Terms of Service**, and there is a risk of being blocked if done aggressively.
     - This method is less stable since Google can change its HTML structure frequently.

### Limitations
- Google **Custom Search API** and **SerpApi** are the most straightforward ways to achieve this goal, but they both have query limits for free use.
- Directly scraping Google’s search results with tools like **Selenium** may work for personal, non-commercial use but poses risks.

For a reliable and straightforward solution, I recommend using **Google Custom Search JSON API** or **SerpApi** to automate Google search and retrieve structured metadata for top search results, including publication time, link, and summary.