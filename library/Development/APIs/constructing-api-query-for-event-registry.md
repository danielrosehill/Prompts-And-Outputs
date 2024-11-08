---
title: "Constructing API query for Event Registry"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Sure, I can help you create a query for the **Event Registry API** to search for mentions of **Hamas** within a specific **one-hour window** immediately after the attack on **October 7th, 2023**. To do this, we'll need to use the Event Registry’s API, leveraging its filtering capabilities for time, keywords, and location.

### **Step-by-Step Query Construction**:

#### **1. Set Up Your API Key**
- First, make sure you have an **Event Registry API key**. You will need this to authenticate your requests.
- Visit [Event Registry](https://eventregistry.org/) and sign up to get your **API key**.

#### **2. API Endpoint**
- The main endpoint for searching articles is:
  ```bash
  https://eventregistry.org/api/v1/article/getArticles
  ```

#### **3. Query Parameters**
To search for **mentions of "Hamas"** within the **first hour** of the attack, set the parameters as follows:

- **`keywords`**: Use `"Hamas"` to find mentions of this specific term.
- **`dateStart` and `dateEnd`**: Define the date and time range using ISO 8601 format for a **one-hour window**.
  - **Start Time**: `"2023-10-07T03:30:00Z"`
  - **End Time**: `"2023-10-07T04:30:00Z"`
- **`lang`**: Optionally, set the language parameter if you only want articles in specific languages (e.g., `"eng"` for English).

#### **4. Example Query in Python Using Requests**
Below is an example using Python to make the API call:

```python
import requests

# Define the API key and endpoint
api_key = "YOUR_API_KEY"  # Replace with your actual API key
endpoint = "https://eventregistry.org/api/v1/article/getArticles"

# Define parameters for the query
params = {
    "action": "getArticles",
    "keywords": "Hamas",
    "dateStart": "2023-10-07T03:30:00Z",
    "dateEnd": "2023-10-07T04:30:00Z",
    "lang": "eng",  # Limit to English articles if needed
    "apiKey": api_key,
    "sortBy": "date",  # Sort by date to track how the story unfolded
    "maxItems": 100  # Adjust the number of results as needed
}

# Make the request to Event Registry API
response = requests.get(endpoint, params=params)

# Check the response
if response.status_code == 200:
    articles = response.json()
    for article in articles.get("articles", []):
        print(f"Title: {article['title']}, Published on: {article['date']}")
else:
    print(f"Error: {response.status_code}")
```

#### **Explanation of Key Parameters**:
- **`action`**: `"getArticles"` specifies that you want to get news articles.
- **`keywords`**: `"Hamas"` to narrow down the results specifically mentioning Hamas.
- **`dateStart` and `dateEnd`**: Sets the specific time window from **03:30 UTC** to **04:30 UTC** on **October 7th, 2023**.
- **`lang`**: Filters articles by language. Set it to `"eng"` if you want only English articles.
- **`sortBy`**: Using `"date"` will sort the articles by their publication date and time.
- **`maxItems`**: Limits the number of returned results, which helps with controlling the response size.

### **Notes**:
- The **API key** is required to authenticate the request, so make sure you replace `"YOUR_API_KEY"` with your actual key.
- You can adjust the parameters to include additional filters like **country**, **source**, or **event** to further refine the results.

### **Result Analysis**:
- The response will contain **metadata** for each article, including the **publication time**, **title**, **source**, and **URL**.
- You can use this metadata to reconstruct a timeline of who reported first on the events and how the news spread globally.

This method will allow you to retrieve the most relevant articles mentioning Hamas within that specific **one-hour window**, giving you insight into the initial media coverage of the attack. Let me know if you need further assistance with implementing or modifying this query!