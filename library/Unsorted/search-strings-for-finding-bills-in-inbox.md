---
title: "Search strings for finding bills in inbox"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'm going to search through my inbox for bills and invoices (Google Workspace). Could you give me a few search strings to use

# Output

Sure! Here are some effective search strings you can use in Google Workspace (Gmail) to locate bills and invoices in your inbox:

### General Keywords Search
1. **For Bills:**
   ```
   subject:(bill OR billing) OR filename:(bill OR billing)
   ```
   - Searches for emails with "bill" or "billing" in the subject line or filename (attachment name).

2. **For Invoices:**
   ```
   subject:(invoice OR receipt) OR filename:(invoice OR receipt)
   ```
   - Searches for emails with "invoice" or "receipt" in the subject line or filename.

3. **Payment-Related Keywords:**
   ```
   subject:(payment OR "payment confirmation") OR filename:(payment)
   ```
   - Searches for "payment" or "payment confirmation" in the subject line or as an attachment.

### Filtering by Attachments
1. **Emails with Attachments:**
   ```
   has:attachment (bill OR invoice OR receipt)
   ```
   - Searches for emails that have an attachment and contain "bill," "invoice," or "receipt."

2. **Specific File Types (PDF, Excel):**
   ```
   has:attachment (filename:pdf OR filename:xlsx) (bill OR invoice OR receipt)
   ```
   - Searches for bills, invoices, or receipts in PDF or Excel format.

### Filtering by Date
1. **Recent Bills/Invoices (Last Month):**
   ```
   newer_than:1m (bill OR invoice OR receipt)
   ```
   - Finds any email with "bill," "invoice," or "receipt" received in the last month.

2. **Older Invoices (Last Year):**
   ```
   older_than:1y (invoice OR receipt) has:attachment
   ```
   - Searches for invoice emails older than one year, with attachments.

### Filtering by Specific Senders
1. **By Known Vendors or Utility Companies:**
   ```
   from:(company1.com OR company2.com) (bill OR invoice OR receipt)
   ```
   - Replace **company1.com** or **company2.com** with specific vendors you deal with.

### Using Labels
1. **If You Have Labels for Finance or Receipts:**
   ```
   label:(finance OR receipts)
   ```
   - Searches for emails under specific labels like "finance" or "receipts" that you might have already organized.

### Combining Multiple Filters
1. **Bills and Invoices with Attachments from Known Sources:**
   ```
   from:(company1.com OR company2.com) has:attachment (bill OR invoice OR receipt)
   ```
   - Combines sender, attachment, and keyword filters.

### Quick Examples:
1. **General Search for Bills:**
   ```
   subject:(bill) OR body:(bill) has:attachment
   ```
2. **General Search for Invoices with PDF Attachments:**
   ```
   subject:(invoice) has:attachment filename:pdf
   ```

These should help you quickly narrow down the relevant emails for bills and invoices! Let me know if you'd like more specific examples or if you need anything else.