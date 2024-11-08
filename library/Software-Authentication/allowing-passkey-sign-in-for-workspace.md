---
title: "Allowing passkey sign in for Workspace"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

How do I fix this error in Workspace Your admin has not enabled passkeys for sign in

# Output

To fix the error **"Your admin has not enabled passkeys for sign in"** in Google Workspace, you need to enable **passkeys** as an authentication option in the Google Admin Console. Here's how you can do it:

### Step 1: Access Google Admin Console
1. **Go to the Admin Console**:
   - Visit [admin.google.com](https://admin.google.com) and log in with your **admin account**.

### Step 2: Navigate to Security Settings
1. **Click on "Security"**:
   - From the Admin Console dashboard, click on **"Security"**. If you don’t see this option, click **"More Controls"** at the bottom.

2. **Select "Authentication"**:
   - In the Security section, click on **"Authentication"** to access authentication settings.

### Step 3: Enable Passkeys (Passwordless Sign-In)
1. **Click on "Passkeys"**:
   - Look for the **"Passkeys"** section under **Authentication** settings.

2. **Allow Passkeys for Users**:
   - Toggle the option to **enable passkeys** (sometimes referred to as **"Passwordless Sign-In"** or **"FIDO2 Security Key"**).
   - You can choose to apply this setting to specific **Organizational Units (OUs)** if you only want some users to use passkeys or apply it to **everyone**.

3. **Save Changes**:
   - Click on **"Save"** to apply the settings.

### Step 4: Propagation Time
- Changes may take up to 24 hours to propagate, although they often apply more quickly.

### Step 5: Test Sign-In with Passkeys
1. **Log in to Your Google Account**:
   - Try logging in to your Google Workspace account (`daniel@yourbusiness.cloud`).
   
2. **Enable Passkey on Your Device**:
   - You will now be prompted to add a **passkey** if the feature is successfully enabled. Follow the on-screen instructions to register a passkey (like a **fingerprint**, **Windows Hello**, or other supported biometric/key options).

### Notes:
- **Admin Privileges**: This setting must be changed by a Google Workspace administrator.
- **Security Considerations**: Make sure that enabling passkeys aligns with your organization's security policies.

Let me know if you need further assistance or run into any trouble while enabling this feature!