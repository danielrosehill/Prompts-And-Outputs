---
title: "Creating embeddable widgets from APIs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt
Let's say that I wanted to take a news API and embed it as a widget ... something that resembled a traditional RSS feed ... what would be the best way to do that?

# Output
To embed a **news API** and display it as a widget that resembles a traditional **RSS feed**, you can follow these steps:

### 1. **Choose a News API**
   You need to first select a **news API** that allows you to pull the latest news data. Some popular news APIs include:
   - **[NewsAPI](https://newsapi.org/)**: Aggregates news from various sources and provides real-time updates.
   - **[GDELT API](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/)**: Tracks events and news worldwide.
   - **[Event Registry API](https://eventregistry.org/documentation)**: Provides news data from multiple languages and locations.

### 2. **Fetch News Data via API**
   Use the API to fetch real-time news articles. You can call the API from the client side (JavaScript) or the server side (PHP, Python, Node.js, etc.). Most APIs return data in **JSON** format.

   Here’s an example using **NewsAPI**:

   ```javascript
   fetch('https://newsapi.org/v2/everything?q=Israel&apiKey=YOUR_API_KEY')
     .then(response => response.json())
     .then(data => {
       console.log(data.articles); // Contains an array of news articles
     });
   ```

### 3. **Parse the Data**
   Once you receive the news data from the API, you need to parse the **JSON** response and extract the relevant details like title, URL, description, and publication date. For example:

   ```javascript
   data.articles.forEach(article => {
     const title = article.title;
     const description = article.description;
     const url = article.url;
     const publishedAt = article.publishedAt;
     // Use this information to build your widget
   });
   ```

### 4. **Display Data in Widget Format**
   To display the news articles, you can create an HTML structure that mimics an RSS feed. For example:

   ```html
   <div id="news-widget">
     <!-- Articles will be inserted here dynamically -->
   </div>
   ```

   With JavaScript, append the articles to this `#news-widget` container:

   ```javascript
   data.articles.forEach(article => {
     const articleHTML = `
       <div class="news-item">
         <h3><a href="${article.url}" target="_blank">${article.title}</a></h3>
         <p>${article.description}</p>
         <span>${new Date(article.publishedAt).toLocaleString()}</span>
       </div>
     `;
     document.getElementById('news-widget').innerHTML += articleHTML;
   });
   ```

### 5. **Styling the Widget**
   Use **CSS** to make the widget look like a traditional RSS feed:

   ```css
   #news-widget {
     font-family: Arial, sans-serif;
     border: 1px solid #ccc;
     padding: 10px;
     width: 300px;
     max-height: 400px;
     overflow-y: scroll;
   }
   .news-item {
     margin-bottom: 15px;
   }
   .news-item h3 {
     font-size: 16px;
     margin: 0;
   }
   .news-item p {
     font-size: 14px;
     color: #555;
   }
   .news-item span {
     font-size: 12px;
     color: #888;
   }
   ```

### 6. **Auto-refresh (Optional)**
   If you want the feed to refresh automatically, you can use JavaScript’s `setInterval` to fetch new data at intervals:

   ```javascript
   setInterval(() => {
     fetchNews(); // Function to fetch news and update the widget
   }, 60000); // Refresh every 60 seconds
   ```

### 7. **Host the Widget**
   Once your widget is complete, you can embed it into any webpage or dashboard by copying and pasting the HTML, CSS, and JavaScript code into the site’s `<head>` and `<body>` sections.

### Key Considerations:
- **API Limits**: Free versions of news APIs often have limits on the number of requests you can make (e.g., 100 requests per day).
- **Responsiveness**: Ensure that your widget is mobile-friendly by using responsive CSS.
- **Caching**: Consider caching the API response if you have a high-traffic website to reduce API requests.

### Tools to Simplify the Process:
If you don't want to code everything yourself, you can use tools like:
- **Taggbox Widget** or **Curator.io**: They allow you to create embeddable content feeds from APIs and RSS feeds with easy customization.

By following these steps, you can create a news widget that pulls real-time updates from a news API and displays it like a traditional RSS feed, allowing users to stay informed about specific topics, such as geopolitical developments in Israel.