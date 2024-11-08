---
title: "Gmail filters for identifying subscriptions and spam"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Here is a list of **Gmail search strings** you can use to identify **email subscriptions**, newsletters, and **spam from salespeople**. These strings can be used to set up filters to **delete**, **archive**, or **label** such emails to keep your inbox clean.

### Identifying Email Subscriptions and Newsletters
1. **Unsubscribe Link Detection**:
   - `"unsubscribe"` or `"click here to unsubscribe"` in the body often indicates a subscription email.
   - Gmail Search:
     ```
     "unsubscribe" OR "click here to unsubscribe"
     ```
   - This will bring up emails containing common unsubscribe links used by marketing and newsletter emails.

2. **Common Subscription Keywords**:
   - Search for emails with common newsletter or subscription-related keywords:
     ```
     subject:("newsletter" OR "subscription" OR "update" OR "digest" OR "recap")
     ```
   - This will capture emails with typical subject lines used for newsletters and recurring content.

3. **Mailing Lists**:
   - Emails from mailing lists often contain "list-id" in their headers:
     ```
     list:(*@*)
     ```
   - This Gmail operator identifies emails coming from mailing lists.

4. **Promotional Keywords**:
   - Keywords like "special offer," "discount," or "promo" are frequently used in marketing emails:
     ```
     subject:("special offer" OR "discount" OR "promo" OR "exclusive")
     ```
   - This will help you locate emails that are likely promotional.

### Identifying Spam from Salespeople
Sales emails often lack unsubscribe options and might come from personal addresses, which makes them more challenging to filter. However, there are patterns you can look for:

1. **Sales Follow-Up Phrases**:
   - Salespeople typically use follow-up phrases like:
     ```
     body:("just wanted to check in" OR "following up" OR "touching base" OR "reaching out")
     ```
   - These are commonly used in cold sales emails.

2. **"Demo," "Trial," or "Meeting" Emails**:
   - Emails from sales teams often mention demos or meetings:
     ```
     subject:("demo" OR "trial" OR "meeting" OR "schedule a call")
     ```
   - Filtering based on these terms will catch a lot of sales-related emails.

3. **Company and Cold Outreach Phrases**:
   - Common phrases that indicate cold outreach include:
     ```
     body:("we noticed" OR "our solution" OR "your company" OR "great fit")
     ```
   - These phrases are typically used by salespeople trying to introduce a product or service.

4. **Sales Outreach Common Domains**:
   - You can also set filters based on domains often used for sales outreach (e.g., CRM domains):
     ```
     from:(@hubspot.com OR @salesforce.com OR @outreach.io OR @marketo.com)
     ```
   - Adding specific domains helps catch emails from known sales and marketing platforms.

### Combining Search Strings for Broad Filters
You can combine multiple search strings to create broad filters that identify various types of nuisance emails:

1. **Broad Newsletter and Subscription Filter**:
   ```
   "unsubscribe" OR subject:("newsletter" OR "digest" OR "subscription") OR list:(*@*)
   ```

2. **Comprehensive Sales Outreach Filter**:
   ```
   body:("just wanted to check in" OR "following up" OR "touching base" OR "our solution") OR subject:("demo" OR "trial" OR "meeting") OR from:(@hubspot.com OR @salesforce.com OR @outreach.io)
   ```

### Setting Up Filters with Gmail
1. **Create a Filter**:
   - Use the search strings above in the Gmail search bar.
   - Click on the **down arrow** in the search bar to open the advanced search options.
   - Adjust the fields and click **Create filter** at the bottom of the search box.

2. **Filter Actions**:
   - **Skip the Inbox**: Moves emails directly to **Archive**.
   - **Mark as Read**: Marks identified emails as read, reducing clutter.
   - **Delete It**: Automatically deletes unwanted emails.
   - **Apply a Label**: Assigns a label to easily track these types of emails.

These search strings and filter setups can help reduce the amount of unwanted email you receive from **newsletters** and **salespeople**, ensuring a cleaner, more focused inbox. You can modify and combine these filters based on the specific types of emails that bother you the most.