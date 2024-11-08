---
title: "Refined program for deploying custom assistant for summarising the news"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

So let's start simple then and go with the more modest approach of creating a custom GPT assistant for the purpose of providing formal synopses of emerging news developments. Let's make some decisions. We're going to use GPT 4o. For news, we're going to use whatever is going to be the most helpful in gaining real time news from the Middle East (specifically Israel). We're going to use Pipedream for automation. The workflow is going to be: the automation will run every 12 hours and the GPT will provide a summary of the emerging and evolving news according to how I've set it up. Can you write a guide?

# Output

Here's a step-by-step guide for setting up a **custom GPT assistant** using **GPT-4**, **Pipedream** for automation, and a suitable news API to provide formal summaries of real-time news from the Middle East, specifically focused on Israel. The workflow will run every 12 hours to pull in the latest news, which GPT-4 will summarize.

### **Step 1: Choose a News API**
For real-time news from the Middle East, especially Israel, you can use one of the following APIs:
- **NewsAPI**: Offers extensive news coverage and real-time updates, with the ability to filter by region.
- **Event Registry**: Specializes in global news events and can be filtered by region.
- **GDELT**: Provides real-time event data, including geopolitical news from various sources.

#### **NewsAPI Setup Example**:
1. **Sign up** at [NewsAPI](https://newsapi.org/pricing) and get your API key.
2. Configure your query to get news specifically about Israel:
   ```bash
   GET https://newsapi.org/v2/everything?q=Israel&sortBy=publishedAt&apiKey=YOUR_API_KEY
   ```

### **Step 2: Set Up Pipedream Automation**
1. **Create a Pipedream account** if you don’t already have one at [Pipedream](https://pipedream.com/).
2. **Create a new workflow**:
   - Go to your Pipedream dashboard and create a new workflow.
   - Choose "HTTP Request" as your trigger (this is where you will call the news API).
   
3. **Configure NewsAPI or other APIs**:
   - **Set up the API call**: In Pipedream, use the HTTP trigger step to fetch news data from your chosen API.
   - Example configuration for **NewsAPI**:
     - URL: `https://newsapi.org/v2/everything`
     - Query Parameters: 
       - `q`: "Israel"
       - `sortBy`: "publishedAt"
       - `apiKey`: Your NewsAPI key
   - **Set schedule**: Set the Pipedream trigger to run every 12 hours (you can configure it under workflow settings).

### **Step 3: Set Up the GPT-4 Integration**
1. **Use OpenAI’s GPT-4 API**:
   - **Get an API key**: Sign up or log into [OpenAI](https://platform.openai.com/) and retrieve your GPT-4 API key.
   
2. **Set up GPT-4 request in Pipedream**:
   - After fetching the news articles from NewsAPI (or the chosen API), add a new action step to call GPT-4 for summarization.
   - In Pipedream, choose “HTTP Request” for the GPT-4 API call.
   
3. **Configure the GPT-4 request**:
   - Set the request type to **POST**.
   - The URL will be: `https://api.openai.com/v1/completions`
   - Headers:
     - `Content-Type`: `application/json`
     - `Authorization`: `Bearer YOUR_OPENAI_API_KEY`
   - Request Body:
     ```json
     {
       "model": "gpt-4",
       "prompt": "Summarize the following news articles about Israel: {{news_articles}}. Provide a formal synopsis that highlights the key emerging and evolving developments.",
       "temperature": 0.7,
       "max_tokens": 500
     }
     ```
   - **Dynamic content**: Replace `{{news_articles}}` with the news data retrieved from the NewsAPI step.

4. **Test the workflow**:
   - You can test the workflow in Pipedream to ensure that the news articles are being retrieved and GPT-4 is generating summaries as expected.

### **Step 4: Customize the GPT-4 Response**
You can configure GPT-4 to generate summaries in a specific style. For example:
- **Formal, objective tone** for political briefings.
- **Specific emphasis** on certain issues like security, diplomatic relations, or conflict.

Modify the prompt as needed:
```text
"Summarize the following news articles about Israel in a formal, concise manner, highlighting any emerging conflicts, diplomatic efforts, and regional developments."
```

### **Step 5: Set the Output**
- You can send the summary directly to email, Slack, or any other service via Pipedream.
- **Configure Output**:
   - In Pipedream, add an additional step (e.g., “Email” or “Slack” integration) to send the GPT-generated summary.
   - For email:
     - Use the Pipedream “Send Email” action.
     - In the email body, include the GPT-generated summary.

### **Step 6: Automate and Monitor**
- Once everything is set up, the workflow will automatically run every 12 hours, fetch the latest news, send it to GPT-4 for summarization, and then deliver the summary to your desired output (e.g., email or Slack).

### **Optional: Add Error Handling**
- Add an error-handling step in Pipedream to ensure that you’re alerted if the news API or GPT-4 API call fails.
- You can set up an email alert or log errors in your Pipedream workflow.

### **Summary of Workflow Steps**:
1. **Trigger every 12 hours**: Automatically trigger Pipedream to call the news API.
2. **Fetch news**: Use the API to retrieve the latest news articles related to Israel and the Middle East.
3. **Send to GPT-4**: Summarize the news articles using GPT-4 and generate a formal synopsis.
4. **Output**: Send the summary to your desired output (email, Slack, etc.).

### **Conclusion**
This setup ensures that your custom GPT assistant will generate formal summaries of evolving geopolitical news in Israel every 12 hours. By leveraging Pipedream’s automation, GPT-4’s summarization, and real-time news APIs, you’ll have an efficient workflow to stay updated with formal synopses of important developments.

Let me know if you need help with any specific parts of the workflow or further customization!