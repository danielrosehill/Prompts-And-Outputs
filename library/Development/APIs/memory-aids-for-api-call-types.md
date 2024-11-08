---
title: "Memory aids for API call types"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Let's say that I want to use news APIs to query for news articles. What's the typical type of call I'm going to be making (put/get etc). Can you give me a memory aid to remember that?

# Output
When working with **news APIs** (or any public API), the most common type of request you'll be making to **query news articles** is typically a **GET request**. The reason for this is simple: you are **retrieving data** (news articles) from the API without modifying anything on the server.

Here's a breakdown to help you remember it:

### Memory Aid: **"GET the news, PUT it out there"**

- **GET**: Use this to **fetch/retrieve** data (e.g., news articles, headlines).
  - Think: **GET** means "I want to **get** the news from the API."
  - Example: You **GET** news articles from a news API by calling an endpoint that returns the requested data.
  - Typical use case: When you want to search for news, headlines, or articles.

- **PUT**: Use this to **send/update** data on the server.
  - Think: **PUT** means "I'm going to **put** some data on the server."
  - PUT is not usually used for querying news articles because you're not updating any server data when searching for news.

- **POST**: You can think of **POST** as submitting data, but for querying news, **POST** is less common. Typically, **GET** requests are sufficient.

### Example GET Request for News API:
```bash
GET https://newsapi.org/v2/everything?q=Israel&apiKey=your_api_key
```

In this example:
- `GET`: The request method.
- The endpoint returns news articles matching the query `Israel`.

### Quick Mnemonics:
- **GET** the news = **fetching/retrieving** data (the most common for querying).
- **PUT** the information somewhere = **updating** (not typical for news queries).

Just remember: **GET the news**, and you’ll always know that you’re using a **GET** request for fetching articles from news APIs!