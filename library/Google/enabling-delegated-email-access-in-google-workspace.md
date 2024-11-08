---
title: "Enabling delegated email access in Google Workspace"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


 To enable the **"Grant access to your account"** feature in Google Workspace, you'll need to adjust settings in the **Google Admin Console** to make sure account delegation is allowed. Follow these steps:

### Step 1: Access the Google Admin Console
1. **Go to the Admin Console**:
   - Visit [admin.google.com](https://admin.google.com) and sign in with your **admin account** for the business workspace (`daniel@yourbusiness.cloud`).

### Step 2: Navigate to User Settings
1. **Click on "Apps"**:
   - In the Admin Console dashboard, click on **"Apps"**.

2. **Click on "Google Workspace"**:
   - Select **"Google Workspace"** from the list of apps.

3. **Click on "Gmail"**:
   - Select **"Gmail"** to access Gmail settings for your organization.

### Step 3: Allow Mail Delegation
1. **Go to User Settings**:
   - Under the Gmail settings, select **"User settings"**.

2. **Enable Mail Delegation**:
   - Scroll down to the **"Mail delegation"** section.
   - Make sure the option to **"Let users delegate access to their mailbox"** is checked. This allows users to grant other people access to their mailbox.

3. **Save Changes**:
   - After enabling this setting, click **"Save"** at the bottom to apply the changes.

### Step 4: Propagation Time
- The changes may take some time to propagate (up to 24 hours, but often much quicker).
  
### Step 5: Test Delegation
1. **Log Back In to Your Business Account** (`daniel@yourbusiness.cloud`):
   - Go to [Gmail](https://mail.google.com) and log in again after the settings have been updated.

2. **Go to Gmail Settings**:
   - Click on the **gear icon** > **"See all settings"** > **"Accounts and Import"**.

3. **Grant Access**:
   - You should now see the option to **"Grant access to your account"** under the **"Accounts and Import"** tab.

This should allow you to successfully enable the feature and grant access to your personal workspace account.

If you don’t have admin privileges, you may need to contact your Google Workspace admin to make these changes. Let me know if you need further guidance!

