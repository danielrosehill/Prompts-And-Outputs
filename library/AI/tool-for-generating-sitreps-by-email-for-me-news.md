---
title: "Tool for generating SITREPs by email for ME news"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please write me a tutorial on how to achieve the following. You can use a placeholder for the API key.

I would like to generate an automation which polls for news from Israel every 6 hours. 

It can use any reliable news API but try to use the real APi structure in your model

It then passes that response onto GPT API.

the news is passed to an assistant which is briefed on its role as being to generate a situational report (sitrep) according to a a standard template on developments in israel over the past 6 hours. 

Ideally it would be able to generate this updated sitrep by referring to its previous report, comparing that against the updated news, and briefing only on the devlopments since the last run. But that's not a hard requirement right now. 

Give me thoughts on how and where i could implemeent this. Could this be deployed and run on Reptl? An open source equivalent / server? Pipedream? 

Lay out a plan to build this tool!

# Output

### **Plan Overview**

The goal of this project is to create an automated system that polls for news about Israel every **6 hours** using a reliable news API, processes that news via GPT-4, and generates a **situational report (SITREP)** based on the latest developments. Ideally, the system will compare the new news with the previous SITREP to brief only on changes, though the first phase will focus on simple updates.

You can deploy this on platforms like **Replit**, **Pipedream**, or an open-source server (such as a **VPS** with **Python scripts and cron jobs**). Below is a detailed step-by-step guide on how to achieve this.

### **Step 1: Choose a News API**
We’ll use **NewsAPI** (or a similar one like **Currents API**) to poll for news on Israel. The structure of the API query will look something like this:
- **API endpoint**: `https://newsapi.org/v2/everything`
- **Parameters**:
  - `q`: "Israel" (to get news related to Israel).
  - `sortBy`: "publishedAt" (to sort articles by their publication date).
  - `apiKey`: Replace this with your own API key.

### **Step 2: Set Up GPT-4 Integration**
We'll use **OpenAI's GPT-4** API to process the news and generate the SITREP.

- **API endpoint**: `https://api.openai.com/v1/completions`
- **Model**: GPT-4
- **Prompt**: This will be dynamically generated from the news articles pulled by the news API. The prompt will instruct GPT to generate a SITREP based on a template.

### **Step 3: Automation Platform Options**
You can deploy this solution on several platforms, each with its own benefits:
- **Pipedream**: Allows easy scheduling of API calls and workflow automation.
- **Replit**: Supports Python code, can run scheduled tasks using its native cron-like functionality, and is ideal for building out the logic.
- **Open-source server**: You can use a VPS (like **DigitalOcean** or **Linode**) and deploy the automation using a Python script with a cron job.

We'll use **Pipedream** for this tutorial, but I'll explain how to adapt it for Replit or a self-hosted solution.

---

### **Step 4: Build the Workflow (Pipedream Example)**

#### **1. Set Up a Pipedream Account**
1. Go to [Pipedream](https://pipedream.com/) and create an account.
2. Once logged in, create a new **Workflow**.

#### **2. Poll NewsAPI Every 6 Hours**
1. **Create a new workflow** and add a `cron` trigger that runs every 6 hours.
   - Use the `Cron Scheduler` option.
   - Set it to trigger every 6 hours: `0 */6 * * *`

2. **Add a step to fetch news from NewsAPI**:
   - Add an HTTP request action.
   - Use this configuration:
     - **Method**: `GET`
     - **URL**: `https://newsapi.org/v2/everything`
     - **Query Parameters**:
       - `q`: "Israel"
       - `sortBy`: "publishedAt"
       - `apiKey`: `YOUR_NEWSAPI_KEY`
     - **Save the response** to pass to the next step.

#### **3. Pass the News to GPT-4 via the OpenAI API**
1. **Add a new step** to the workflow for making an HTTP POST request to GPT-4.
2. **Configure the GPT-4 API Request**:
   - **Method**: `POST`
   - **URL**: `https://api.openai.com/v1/completions`
   - **Headers**:
     - `Content-Type`: `application/json`
     - `Authorization`: `Bearer YOUR_OPENAI_API_KEY`
   - **Body (Prompt)**: Use the news articles pulled from the previous step.
     ```json
     {
       "model": "gpt-4",
       "prompt": "Generate a situational report (SITREP) on the developments in Israel over the past 6 hours. Base this on the following news articles: {{news_articles}}. Follow this template:\n\n1. Key developments: \n2. Emerging trends: \n3. Potential implications: \n\nProvide a concise summary of each point.",
       "temperature": 0.5,
       "max_tokens": 500
     }
     ```
   - **Save the GPT-4 response** to be sent as an output.

#### **4. Set Up the Output (Email/Slack/Storage)**
1. You can send the GPT-4-generated SITREP to an email, Slack, or save it to a file.
2. For email:
   - Add an **email step** in Pipedream, using your email details.
   - The email body will be the GPT-4-generated SITREP.
3. For file storage (e.g., Dropbox, Google Drive), add an appropriate integration to store the SITREP report.

---

### **Step 5: Additional Features for the Future**

#### **1. Compare with Previous SITREP**
- Save the previous SITREP in a database (or in a simple file storage solution like Dropbox/Google Drive).
- When generating the new SITREP, retrieve the previous report and pass both the new and old reports to GPT-4, asking it to highlight differences and developments since the last report.

#### **2. Integrate with a Database (Optional)**
If you want to store all SITREPs, you can connect the workflow to a database (e.g., **PostgreSQL**, **Airtable**). This is useful for historical tracking and generating more sophisticated reports over time.

---

### **Step 6: Run and Test the Workflow**
1. Test the workflow in Pipedream to ensure it's fetching news correctly and that GPT-4 is generating a concise SITREP.
2. Ensure the automation runs every 6 hours as scheduled.

---

### **Deployment on Replit (Alternative)**
If you prefer using **Replit**:
1. Write a **Python script** to fetch the news and send the articles to the GPT-4 API.
2. Use **Replit's Secrets** feature to store your API keys securely.
3. Schedule the script using **Replit’s native scheduler** or a cron-like tool to run every 6 hours.

Here’s an example Python script:
```python
import requests
import os

# Fetch news from NewsAPI
news_url = "https://newsapi.org/v2/everything"
params = {
    "q": "Israel",
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWS_API_KEY")
}
news_response = requests.get(news_url, params=params)
news_data = news_response.json()

# Format the news into a prompt
news_articles = "\n".join([article["title"] + ": " + article["description"] for article in news_data["articles"]])
prompt = f"Generate a situational report (SITREP) on the developments in Israel over the past 6 hours based on the following news articles:\n\n{news_articles}"

# Call GPT-4 API
gpt_url = "https://api.openai.com/v1/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
}
data = {
    "model": "gpt-4",
    "prompt": prompt,
    "temperature": 0.5,
    "max_tokens": 500
}
response = requests.post(gpt_url, headers=headers, json=data)
sitrep = response.json()["choices"][0]["text"]

print(sitrep)
```

---

### **Self-Hosted Server (Alternative)**
If you have a **VPS**, set up a similar workflow:
1. Write a Python script similar to the one for Replit.
2. Use **cron** to schedule it to run every 6 hours:
   ```bash
   crontab -e
   ```
   Add:
   ```bash
   0 */6 * * * /usr/bin/python3 /path/to/script.py
   ```

---

### **Conclusion**
This project can be built using Pipedream, Replit, or an open-source server. The automation will fetch news every 6 hours and generate a SITREP using GPT-4, which can be delivered via email, stored in a file, or sent to a messaging service. As you scale, you can add features like comparing SITREPs and saving historical data.

Let me know if you’d like to dive deeper into any of the steps!