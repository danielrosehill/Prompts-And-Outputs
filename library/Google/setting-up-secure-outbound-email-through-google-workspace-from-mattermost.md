---
title: "Setting up secure outbound email through Google Workspace from Mattermost"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Is there a way to configure secure outbound email using Google Workspace in my Mattermost instance?

# Output

Yes, you can configure **secure outbound email** using **Google Workspace** in your Mattermost instance by integrating **SMTP (Simple Mail Transfer Protocol)** using Google's secure email services. This will allow Mattermost to send outbound emails (such as notifications) securely via your Google Workspace account.

### Steps to Configure Outbound Email using Google Workspace:

#### 1. **Get SMTP Settings for Google Workspace**
Google Workspace (formerly G Suite) provides SMTP server details that allow you to send emails securely. Here are the standard settings:

- **SMTP server**: `smtp.gmail.com`
- **Port**: 
  - `587` (with STARTTLS) – Recommended
  - `465` (for SSL)
- **Encryption**: TLS
- **Authentication**: Required (your full Google Workspace email address and password)

#### 2. **Generate App Password (Recommended for Better Security)**
Instead of using your main Google Workspace password, it's recommended to generate an **App Password** for Mattermost. This adds an extra layer of security:

- Go to [Google Account Security](https://myaccount.google.com/security).
- Under **"Signing in to Google"**, find **App Passwords**.
- Generate an App Password for Mattermost (or label it appropriately).

You will use this app password instead of your regular Google Workspace password in the Mattermost SMTP configuration.

#### 3. **Configure SMTP Settings in Mattermost**
To configure Mattermost to use Google Workspace's SMTP for sending emails:

1. **Open the Mattermost System Console**:
   - Navigate to the **System Console** in Mattermost.
   - Go to **Notifications** > **Email Settings**.

2. **Set SMTP Server Information**:
   - **SMTP Server**: `smtp.gmail.com`
   - **SMTP Port**: `587`
   - **Connection Security**: `STARTTLS`
   - **SMTP Username**: Your full Google Workspace email address (e.g., `yourname@yourdomain.com`).
   - **SMTP Password**: Enter the **App Password** you generated in Step 2.

3. **Set Sender Email and Feedback**:
   - **Notification Display Name**: Enter the display name you want for the emails sent from Mattermost.
   - **Notification Email Address**: This should be the same Google Workspace email address (e.g., `yourname@yourdomain.com`).
   - **Feedback Name** and **Email Address**: You can specify an email address where feedback or replies should be sent.

4. **Enable Email Notifications**:
   - Ensure that email notifications are enabled in the **System Console** under **Notifications > Email Notifications**.

5. **Test the SMTP Configuration**:
   - Scroll down and click the **Test Connection** button to verify that your SMTP settings are working correctly. If successful, you’ll receive a confirmation message.

#### 4. **Ensure Less Secure App Access is Disabled (for App Passwords)**
If you’ve set up an **App Password**, Google Workspace should handle the security. However, you may also want to ensure that “Allow less secure apps” is turned off for your Google account, as App Passwords don't require this setting to be enabled.

### Security Considerations
- **App Passwords**: Using App Passwords is more secure than your regular password and ensures better control over app-specific access.
- **TLS/STARTTLS**: Ensure you use encryption (like TLS or STARTTLS) for secure email transmission.
- **Monitor Logs**: Monitor logs in both Mattermost and Google Workspace for any potential security or authentication issues.

### Troubleshooting
- If emails aren’t being sent, check that your firewall allows outbound connections on port **587** or **465**.
- Check the SMTP logs in the **Mattermost System Console** for any authentication or connectivity errors.

By following these steps, your Mattermost instance will securely send outbound emails via your **Google Workspace** account.