---
title: "Guide for implementing news monitoring with a specific stack"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 
Stack:

OpenNewsAPI
GPT 4o API
Pipedream
Email


Here’s a detailed implementation guide for building your SITREP automation using **NewsAPI.org**, **Pipedream**, **GPT-4 via API**, and sending the output as an email.

---

### Step 1: Set Up NewsAPI.org

1. **Create an Account**:
   - Go to [NewsAPI.org](https://newsapi.org/) and sign up for a free account.
   - You will receive an API key upon registration.

2. **Test the API**:
   - Test by using the following URL to pull in recent articles related to Israel’s geopolitical situation:
     ```
     https://newsapi.org/v2/everything?q=Israel&from=2024-10-01&sortBy=publishedAt&apiKey=YOUR_API_KEY
     ```
   - This will fetch news articles related to Israel, sorted by the latest publication date.

3. **Customize the Queries**:
   - Fine-tune the search queries for specific events like:
     - **Israel + Lebanon**
     - **Israel + Gaza**
     - **Israel + Iran**
     - **Red Alerts in Israel**
   - Example API request:
     ```
     https://newsapi.org/v2/everything?q=Israel+Lebanon&sortBy=publishedAt&apiKey=YOUR_API_KEY
     ```

---

### Step 2: Set Up Pipedream Workflow

1. **Create a Pipedream Account**:
   - Sign up at [Pipedream](https://pipedream.com/).

2. **Set Up a New Workflow**:
   - In Pipedream, create a new workflow that triggers every 3 hours.
   - **Trigger**: Use the **Scheduler** action to run the workflow every 3 hours. You can also use the **HTTP Request** trigger for pulling from NewsAPI.

3. **Set Up NewsAPI.org API Calls**:
   - Add the **HTTP / Webhook** action in Pipedream to make API requests to **NewsAPI.org**.
   - Use this endpoint for the request:
     ```
     https://newsapi.org/v2/everything?q=Israel+Lebanon&sortBy=publishedAt&apiKey=YOUR_API_KEY
     ```
   - Make separate API calls for each query:
     - **Israel + Lebanon**
     - **Israel + Gaza**
     - **Israel + Iran**
     - **Red Alerts in Israel**

4. **Extract the Necessary Data**:
   - Parse the JSON response from NewsAPI.org.
   - Extract relevant data:
     - Article title.
     - Published date.
     - Source.
     - URL for further reading.
     - Content snippet.

---

### Step 3: Summarize Data Using GPT-4 API

1. **Get Your GPT-4 API Key**:
   - If you don’t already have it, sign up for access to the GPT-4 API at [OpenAI](https://beta.openai.com/).

2. **Create the GPT-4 Prompt**:
   - Use Pipedream’s **OpenAI Integration** to send the news data from the NewsAPI.org call to GPT-4 for summarization.
   - Example GPT-4 prompt:
     ```
     Summarize the following news about Israel in the format provided:
     
     One-line summary
     Timestamps (Israel Time, UTC)
     BLUF
     
     # Israel - Lebanon
     [Details from articles]
     
     # Israel - Gaza
     [Details from articles]
     
     # Israel - Iran
     [Details from articles]
     
     # Israel - Global
     [Details from articles]
     
     # Red Alerts
     [Details]
     ```

3. **Send the Parsed Data to GPT-4**:
   - In Pipedream, add an action to send the news data from **NewsAPI.org** into GPT-4 for structured summarization.
   - Example API request to GPT-4:
     ```json
     {
       "model": "gpt-4",
       "messages": [
         {"role": "system", "content": "Summarize in the following format: [template]"},
         {"role": "user", "content": "News data from NewsAPI.org"}
       ]
     }
     ```

---

### Step 4: Send Output via Email

1. **Set Up an Email Integration in Pipedream**:
   - Use the **Email** action in Pipedream to send the summarized SITREP via email.
   - You can choose a service like Gmail, Outlook, or a custom SMTP server for sending emails.

2. **Format the Email Content**:
   - Use the formatted output from GPT-4 as the email body.
   - Example:
     ```
     Subject: SITREP Update - Israel Geopolitical Situation
     
     Timestamps: [Israel Time], [UTC Time]
     
     One-line summary: [GPT-4 Summary]
     
     BLUF: [GPT-4 Summary]
     
     # Israel - Lebanon
     [GPT-4 Output]
     
     # Israel - Gaza
     [GPT-4 Output]
     
     # Israel - Iran
     [GPT-4 Output]
     
     # Israel - Global
     [GPT-4 Output]
     
     # Red Alerts
     [GPT-4 Output]
     ```

3. **Test the Workflow**:
   - Run a test workflow to ensure that the email is sent with the SITREP information properly formatted.
   - Make sure the scheduling and API requests are working in sync.

---

### Optional: Add Escalation Alerts for Critical Events

1. **Keyword-based Alerting**:
   - In Pipedream, set up filters or conditions to check for specific keywords like "war," "escalation," or "missiles" in the API responses.
   - If such keywords are detected, trigger an additional, higher-priority alert (such as an SMS via Twilio or a high-priority email).

2. **Custom Alerts for Escalations**:
   - Set an additional action in Pipedream for sending SMS or high-priority emails when escalations are detected.
   - Use Twilio for SMS or additional email integrations.

---

### Step 5: Deploy and Monitor

- Once your system is live, monitor the workflow in Pipedream's dashboard to ensure everything is functioning correctly.
- You can adjust the queries, GPT-4 prompt, and email formatting as needed to refine the output.

---

### Estimated Costs

1. **NewsAPI.org**:
   - Free tier: 500 requests/day.
   - Sufficient for a SITREP every 3 hours.
   
2. **Pipedream**:
   - Free tier: 10,000 invocations/month.
   - Paid plans start at $20/month.

3. **OpenAI GPT-4 API**:
   - Pay-as-you-go pricing, depending on the volume of text sent and processed.
   - GPT-4 costs vary by model (check [OpenAI pricing](https://openai.com/pricing) for details).

---

By following this guide, you should have an automated system for generating and sending SITREPs on geopolitical developments in Israel every 3 hours, using **NewsAPI.org** for real-time data, **GPT-4** for summarization, and **Pipedream** for the entire automation workflow.

# Correct type of API call

For **NewsAPI.org**, the correct type of API call is **GET**. The NewsAPI service uses the GET method to retrieve data from the server.

You will make a GET request with the query parameters included in the URL, as shown in the examples I provided.

So, when implementing these API calls in your system, be sure to use `GET` requests.