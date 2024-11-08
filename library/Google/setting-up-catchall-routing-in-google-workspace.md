---
title: "Setting up catchall routing in Google Workspace"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


To configure **catchall routing** in Google Workspace, you need to ensure that any email sent to your domain without a specific recipient matches a general address. This is useful if you want to make sure that emails sent to typos or non-existent addresses still get delivered to a main inbox. Follow these steps:

### Step 1: Access Google Admin Console
1. **Go to the Google Admin Console**: Visit [admin.google.com](https://admin.google.com) and sign in with your Google Workspace admin account.
2. **Navigate to Apps**: In the main Admin Console dashboard, click on **"Apps"**.
3. **Click on Google Workspace**: Select **"Google Workspace"** from the list.
4. **Click on Gmail**: Under Google Workspace apps, select **"Gmail"**.

### Step 2: Create a Catchall Address
1. **Default Routing**:
   - Click on **"Routing"** or **"Default Routing"** under the **"Advanced settings"** section.
   - This might be found under **"Hosts and Routing"** for some older versions.

2. **Add a Setting**:
   - Scroll down to the **Routing** section and click on **"Default routing"**. Alternatively, if you see **"Add another rule"** or **"Configure"**, click on it to add a new routing rule.

3. **Add Catchall Route**:
   - Under **"Add Setting"**, fill out the details:
     - **Select the option to "Catch-all address"**: This ensures that all emails that do not match an existing account are caught.
     - **Recipient Address**: Enter the recipient email address that you want the catchall to forward to. This should be an existing email account in your domain (e.g., `catchall@yourdomain.com` or `admin@yourdomain.com`).

4. **Configure Match Conditions**:
   - Choose **Inbound messages** as the category, as the catchall should only apply to incoming emails.

5. **Route Settings**:
   - Under **"Route"**, make sure to add a description (e.g., **"Catchall Routing"**).
   - Set the route to **modify message** to **change route** to the specified recipient.
   - Optionally, you can add headers, labels, or any additional information for these emails.

### Step 3: Save Settings
1. **Save Changes**:
   - Click **"Save"** at the bottom of the page.
2. **Propagation Time**:
   - Google Workspace may take up to 24 hours for the changes to propagate across all servers. However, changes typically apply much faster.

### Step 4: Testing the Catchall
1. **Send a Test Email**:
   - Send an email to a **non-existent address** at your domain (e.g., `randomname@yourdomain.com`).
2. **Check Catchall Inbox**:
   - Verify if the email arrives in the designated catchall account to ensure your configuration is working properly.

### Optional: Set Up Filters (Optional but Useful)
- If you want to **organize catchall emails**, you could set up filters in the catchall account to **label** or **auto-organize** these emails as they come in.
- For example, you can create a filter in Gmail that automatically applies a **"Catchall" label** to all messages that are routed to this inbox by the catchall.

### Summary
- Navigate to **Gmail Routing** settings in the Admin Console.
- Create a **catchall rule** under default routing, and enter the desired **recipient address**.
- **Save** and **wait for propagation**, then test by sending an email to an unknown address within your domain.

Let me know if you need more details or run into any issues while setting it up!