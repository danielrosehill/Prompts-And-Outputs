---
title: "Easy way to block senders in Google Workspace"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there an easy way to block email addresses in Google Workspace? Like some way that I can maintain a blocklist for senders that don't have an unsubscribe button? Or perhaps even an email filter that can be set up separate from the ibox?

# Output

Yes, in **Google Workspace**, you can easily block email addresses by creating filters or maintaining a custom blocklist. Here are some approaches you can use to manage unwanted emails from senders that don't provide an unsubscribe option:

### 1. **Create a Blocklist with Filters**
You can create a filter to automatically block or delete emails from specific senders by setting up a blocklist.

#### Steps:
1. **Go to Gmail Settings**:
   - Click the **gear icon** in Gmail (top-right) and select **See all settings**.

2. **Create a Filter**:
   - Go to the **Filters and Blocked Addresses** tab.
   - Click **Create a new filter**.

3. **Set the Filter Criteria**:
   - In the **From** field, enter the email address or domain you want to block (e.g., `example@domain.com` or `@domain.com` for the entire domain).

4. **Choose the Action**:
   - Click **Create filter**.
   - Select the action you want to apply to emails from that sender:
     - **Delete it**: Automatically deletes the email.
     - **Skip the inbox**: Archives the email without it hitting your inbox.
     - **Apply a label**: You could create a "Blocked" label to store these emails in case you want to review them later.
   
5. **Apply to Existing Emails**:
   - Check the box to apply this filter to existing emails (optional).
   
6. **Save the Filter**:
   - Click **Create filter**.

This filter will now block or delete any incoming emails from the specified addresses or domains.

### 2. **Using a Dedicated "Blocked Senders" Label**
If you prefer not to delete emails outright but want to keep them out of your inbox, you can create a filter to automatically move emails from blocked senders to a separate label:

1. **Create a Label**:
   - In the left-hand menu of Gmail, scroll down and click **Create new label**.
   - Name the label something like "Blocked Senders."

2. **Set Up the Filter**:
   - Follow the steps above to create a filter based on the email addresses or domains.
   - In the filter options, choose **Skip the Inbox (Archive it)** and then **Apply the label**. Choose the "Blocked Senders" label you just created.

This will keep the emails from cluttering your inbox, but you can still review them if necessary.

### 3. **Using Google Workspace Admin Controls (For Admins)**
If you're an admin for your Google Workspace domain, you can set up domain-wide blocking of certain senders.

1. **Go to Google Admin Console**:
   - Open the Google Admin console: [admin.google.com](https://admin.google.com).
   - Navigate to **Apps** > **Google Workspace** > **Gmail** > **Spam, phishing, and malware**.

2. **Create an Email Blocklist**:
   - Add specific email addresses or domains to a blocklist.
   - This will block emails at the organizational level, preventing them from reaching any user in your domain.

3. **Set Filters for Your Entire Organization**:
   - Admins can create custom routing rules for the organization that automatically reject or route emails from specific addresses or domains.

### 4. **Mark as Spam (Automatic Blocking)**
If you mark certain emails as **spam**, Google will automatically block future emails from that sender. While this isn't the same as a managed blocklist, it helps cut down on unwanted emails.

#### Steps:
1. **Select the Unwanted Email**.
2. Click **Report Spam** (the exclamation mark icon).
   - Future emails from that sender will automatically go to your spam folder.

### 5. **Third-Party Tools for Managing Blocklists**
You can also use third-party email management services that integrate with Google Workspace to help you manage blocklists more efficiently.

- **SaneBox**: Automatically filters out unwanted emails and creates custom folders for different categories, like newsletters or blocked senders.
- **Clean Email**: Helps you clean up and block unwanted emails, with more advanced filtering options.

### Conclusion
For blocking unwanted emails in **Google Workspace**:
- **Email Filters**: Create filters to delete or archive emails based on specific senders or domains.
- **Label System**: Use a label like "Blocked Senders" to route unwanted emails away from your inbox.
- **Admin Controls**: If you're a Google Workspace admin, you can create domain-wide blocklists.
- **Mark as Spam**: Automatically move unwanted emails to the spam folder.

These approaches give you control over managing and blocking emails efficiently, especially for senders without an unsubscribe option. Let me know if you need more help setting up any of these methods!