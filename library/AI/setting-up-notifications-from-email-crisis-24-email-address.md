---
title: "Setting up notifications from email Crisis 24 email address"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Please help me to create a basic automation that works with my Google Workspace (I have a make.com subscription) I'd like to configure some automations that trigger whenever an email is received from this address exactly: risk-alert@notifications.crisis24.garda.com Notifications ideally on my Android + desktop (Fedora) + other devices ... and automatic copying of the alert to a couple of additional emails

# Output

To create a basic automation that works with your Google Workspace and triggers notifications and actions based on emails received from a specific address (risk-alert@notifications.crisis24.garda.com), you can use **Make.com** to build the workflow and integrate it with your Android device, desktop, and other devices. Here’s how you can achieve this:

### Step-by-Step Automation Setup

#### **Step 1: Google Workspace Setup (for triggers and email forwarding)**
1. **Login to Make.com**: Sign in to your Make.com account.
   
2. **Create a New Scenario**: Start a new scenario by clicking "Create a new scenario."

3. **Add Google Gmail as the First Module**: 
   - Choose Google Workspace Gmail as the trigger.
   - Select the trigger **"Watch Emails"** for new incoming emails.
   - Configure the filter to trigger only when the email is from **risk-alert@notifications.crisis24.garda.com**.
   
   In the filter, set:
   - Field: **From**
   - Condition: **Equals**
   - Value: **risk-alert@notifications.crisis24.garda.com**

4. **Add Forwarding Action**: 
   - After the trigger, add a **Google Gmail - Send Email** action.
   - In this action, configure it to automatically forward the received email to the additional recipients you want.

#### **Step 2: Android Notification Integration**
1. **Add Android Notifications**: 
   - Add a module for **Pushbullet** or **Pushover** (both work with Make.com and offer Android notifications).
   - Connect your Pushbullet or Pushover account.
   - Set it up to send a notification to your Android device every time an email is received from the specified address.

#### **Step 3: Desktop (Fedora) Notification**
To receive notifications on Fedora, you can either use:
   - **Pushover**: You can install Pushover on Fedora via browser integration.
   - **Slack/Telegram**: Set up a Slack or Telegram integration and push a message to a specific channel or chat every time an alert is received.

1. **Slack Integration (Optional)**:
   - Add a module for **Slack - Send Message**.
   - Configure Slack to send a message to a specific channel with the details of the alert.
   - You can access Slack from any device, including Fedora.

2. **Telegram Integration (Optional)**:
   - Add a module for **Telegram Bot** (you will need to create a Telegram bot for this).
   - Configure Telegram to send a message to a chat when the alert is received.

#### **Step 4: Finalize the Scenario**
1. **Save the Scenario**: Once all the modules are in place, save and activate your scenario.
2. **Test the Workflow**: Send a test email from risk-alert@notifications.crisis24.garda.com to verify that the automation works.

### Notifications Across Devices:
- **Android**: Use Pushbullet or Pushover for instant alerts.
- **Desktop (Fedora)**: Use Pushover, Slack, or Telegram to receive notifications.
- **Other Devices**: Install Pushbullet, Pushover, or set up email alerts via Make.com that send to multiple devices.

This setup will ensure that you receive instant notifications and automatic forwarding for any emails from **risk-alert@notifications.crisis24.garda.com** across all your devices.