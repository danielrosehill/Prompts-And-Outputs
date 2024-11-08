---
title: "Sending out multiple emails in Google Workspace - gathering quotes"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm trying to get quotes for a product from a few different websites.

The quote requests can have the same subject line and body but I would prefer to send to one recipient at a time.

Can you recommend a smart way to do this in Google Workspace?

# Output
To efficiently send quote requests to multiple recipients using the same subject line and body in Google Workspace, while ensuring that each recipient receives a separate email, you can use the following methods:

### 1. **Mail Merge with Google Sheets and Gmail**
Using Google Sheets along with a Google Apps Script or an add-on can streamline the process of sending personalized emails. Here’s how to set it up:

- **Step 1: Prepare Your Data**
  - Create a Google Sheet with columns for the recipient's name and email address. You can also include a column for specific product details if necessary.

- **Step 2: Write Your Email Template**
  - Compose your email in Gmail, keeping the subject line and body consistent. You can use placeholders in your template (e.g., `{{Name}}`).

- **Step 3: Use a Mail Merge Add-On**
  - Add-ons like **Yet Another Mail Merge (YAMM)** or **Mail Merge with attachments** allow you to send bulk emails personalized to each recipient without revealing other recipients. Simply follow the instructions provided by the add-on to set up the merge using your Google Sheet  .

### 2. **Google Scripts**
If you're comfortable with a bit of scripting, you can write a simple Google Apps Script to automate sending the emails:

- **Step 1: Open Google Sheets**
  - Go to Extensions > Apps Script.

- **Step 2: Write the Script**
  ```javascript
  function sendQuotes() {
      var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
      var data = sheet.getDataRange().getValues();
      var subject = "Your Quote Request";
      var body = "Dear [Name],\n\nI would like to request a quote for [Product]. Thank you!\n\nBest regards,\n[Your Name]";

      for (var i = 1; i < data.length; i++) { // Skip header row
          var emailAddress = data[i][1]; // Assuming email is in the second column
          var personalizedBody = body.replace("[Name]", data[i][0]);
          MailApp.sendEmail(emailAddress, subject, personalizedBody);
      }
  }
  ```
- **Step 3: Run the Script**
  - After saving the script, you can run it to send personalized emails to each recipient in your list  .

### 3. **Gmail Templates (Canned Responses)**
If you prefer a manual approach:

- **Step 1: Enable Templates**
  - Go to Gmail settings > Advanced > Enable Templates.

- **Step 2: Create a Template**
  - Compose your email, then click the three dots in the compose window > Templates > Save draft as template.

- **Step 3: Send Emails One-by-One**
  - When you're ready to send, open the template, replace the recipient’s email, and send it. This can be slightly slower but allows for easy personalization if needed .

### Conclusion
Using mail merge methods or Google Scripts can significantly streamline your process of sending quote requests individually while maintaining the same content across all emails. Choose the method that best fits your comfort level with technology and the complexity of your requirements.