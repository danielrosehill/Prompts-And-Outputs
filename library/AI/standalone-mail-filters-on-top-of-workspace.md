---
title: "Standalone mail filters on top of Workspace"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

What about standalone/external mail filters that can be added on top of Google Workspace. Is this setup possible and if so what would monthly costs be?

# Output

Yes, it is possible to use standalone or external email filtering services on top of **Google Workspace** to add extra layers of filtering, security, and spam control. These external mail filters act as intermediaries between your incoming email and your Google Workspace inbox, providing advanced features like custom blocklists, enhanced spam filtering, and more granular control over email routing.

Here are some popular standalone email filtering solutions that can integrate with **Google Workspace**, along with their typical monthly costs:

### 1. **Mailgun (Email Routing & Filtering)**
   - **Overview**: Mailgun is an email service provider that allows you to route emails through its servers before delivering them to your inbox. You can set up custom email filtering rules, blocklists, and routing policies to ensure only desired emails make it to your Google Workspace account.
   - **Features**:
     - Custom email filtering and routing.
     - Email blocking based on rules or senders.
     - Advanced spam protection and customizable filtering options.
   - **Cost**: Mailgun pricing starts at **$35/month** for basic plans, but scales depending on the number of messages routed and features required.
   - **Website**: [mailgun.com](https://www.mailgun.com)

### 2. **SpamTitan**
   - **Overview**: SpamTitan is a powerful email filtering and anti-spam solution designed for businesses. It acts as a mail gateway, scanning and filtering emails before they reach Google Workspace. It provides enhanced spam filtering, blocklist management, and virus protection.
   - **Features**:
     - Advanced spam filtering, with customizable blocklists and whitelists.
     - Virus and malware scanning.
     - Phishing protection and data loss prevention.
   - **Cost**: Pricing for SpamTitan starts around **$1.50/user/month** with various pricing tiers based on the number of users and features.
   - **Website**: [spamtitan.com](https://www.spamtitan.com)

### 3. **Mimecast**
   - **Overview**: Mimecast is an all-in-one email security and management platform. It offers robust spam and phishing protection, email filtering, and secure email delivery. Mimecast can be configured to route emails through its filtering service before they hit your Google Workspace inbox, giving you extra control over blocking unwanted emails.
   - **Features**:
     - Advanced email security with spam filtering, malware protection, and phishing defense.
     - Centralized management for email security policies.
     - Easy integration with Google Workspace.
   - **Cost**: Pricing starts around **$4/user/month**, depending on the plan and features.
   - **Website**: [mimecast.com](https://www.mimecast.com)

### 4. **Proofpoint Essentials**
   - **Overview**: Proofpoint Essentials provides enterprise-level email filtering, spam protection, and advanced threat protection for small and medium-sized businesses. It filters emails for spam, phishing, and malware before they reach your inbox.
   - **Features**:
     - Customizable spam filtering and blocklists.
     - Phishing and malware protection.
     - Enhanced email security controls.
   - **Cost**: Proofpoint Essentials pricing starts at around **$2/user/month** for basic plans.
   - **Website**: [proofpoint.com](https://www.proofpoint.com)

### 5. **MX Guarddog**
   - **Overview**: MX Guarddog is a cost-effective email filtering service that provides spam filtering, virus scanning, and blacklist management. It works as an external filter, routing email through its servers before delivering them to your Google Workspace inbox.
   - **Features**:
     - Advanced spam filtering and virus scanning.
     - Easy blacklist and whitelist management.
     - Simple setup and integration with Google Workspace.
   - **Cost**: **$0.25/user/month** with no fixed monthly minimums, making it one of the most affordable options.
   - **Website**: [mxguarddog.com](https://www.mxguarddog.com)

### 6. **MailRoute**
   - **Overview**: MailRoute provides cloud-based email security, including spam filtering, virus protection, and custom email routing. You can use it as an external filter that scans emails before they reach your Google Workspace account, with customizable rules for blocking or whitelisting.
   - **Features**:
     - Comprehensive spam filtering and email routing controls.
     - Custom email filtering rules.
     - Integration with Google Workspace via MX record changes.
   - **Cost**: Pricing starts at **$30/year per user** (or approximately **$2.50/user/month**).
   - **Website**: [mailroute.net](https://www.mailroute.net)

---

### How These Filters Work with Google Workspace:
1. **MX Record Changes**: To route emails through an external filter, you'll need to modify your **MX records** to direct incoming mail to the filtering service first. Once filtered, the emails are delivered to your Google Workspace inbox.
   - This setup ensures that unwanted emails are filtered before they hit your inbox, providing an extra layer of security and control.

2. **Custom Blocklists**: Most of these services allow you to set up customizable blocklists and whitelists to control which emails get through. You can block entire domains, specific email addresses, or configure more advanced filtering rules.

3. **Filtering Beyond Spam**: These services often include **phishing protection**, **malware scanning**, and **data loss prevention**, making them robust solutions for managing both unwanted and malicious emails.

---

### Conclusion:
For adding standalone/external email filtering to your Google Workspace, the following options are well-suited to your needs:
- **MX Guarddog**: The most affordable option, starting at **$0.25/user/month**.
- **MailRoute**: At **$2.50/user/month**, this service offers robust spam filtering and email security.
- **SpamTitan** and **Proofpoint Essentials**: Mid-range options with advanced features, starting around **$1.50-$2/user/month**.

These tools can be easily integrated with Google Workspace, allowing you to manage email filters, blocklists, and spam prevention while keeping your inbox clean.