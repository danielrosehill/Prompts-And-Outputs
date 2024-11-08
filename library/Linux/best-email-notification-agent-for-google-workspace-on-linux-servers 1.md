---
title: "Best email notification agent for Google Workspace on Linux servers"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

It's an Ubuntu server. And my email runs on Google Workspace. is mailx still the right choice for configuring notifications?

# Output

For sending email notifications from your **Ubuntu server** using **Google Workspace**, configuring **mailx** is still an option, but you need to ensure it can communicate through Google’s SMTP servers. Alternatively, you could use **msmtp** or **ssmtp**, which are simpler to configure for Google SMTP. Both allow you to send emails using Google’s SMTP service securely.

Here’s a step-by-step guide to configure **msmtp** (which is more modern and straightforward than mailx for use with Google Workspace):

### **Step 1: Install msmtp and mailx**
First, you’ll install **msmtp** and **mailx** (we’ll configure mailx to use msmtp for email sending):

```bash
sudo apt-get update
sudo apt-get install msmtp msmtp-mta mailx
```

### **Step 2: Configure msmtp**
Next, configure **msmtp** to send email through Google Workspace’s SMTP server.

1. **Create the configuration file**:
   ```bash
   sudo nano /etc/msmtprc
   ```

2. **Add the following configuration** (modify for your email and domain):

   ```bash
   # Set defaults
   defaults
   tls on
   tls_trust_file /etc/ssl/certs/ca-certificates.crt
   logfile /var/log/msmtp.log

   # Gmail/Google Workspace account
   account google
   host smtp.gmail.com
   port 587
   auth on
   user your-email@example.com
   password your-google-workspace-password
   from your-email@example.com
   tls on

   # Set a default account
   account default : google
   ```

   - Replace `your-email@example.com` with your actual Google Workspace email.
   - Replace `your-google-workspace-password` with an **app-specific password** if you have 2FA enabled on your Google account. You can create one [here](https://myaccount.google.com/apppasswords).

3. **Save and exit** (`Ctrl + X`, then `Y`).

4. **Secure the configuration file** (to prevent unauthorized access):
   ```bash
   sudo chmod 600 /etc/msmtprc
   ```

### **Step 3: Configure mailx to Use msmtp**
1. **Create or edit the mailx configuration file**:
   ```bash
   sudo nano /etc/mail.rc
   ```

2. **Add the following configuration** to make **mailx** use **msmtp**:

   ```bash
   set sendmail="/usr/bin/msmtp"
   ```

3. **Save and exit** (`Ctrl + X`, then `Y`).

### **Step 4: Test the Email Configuration**
Send a test email to ensure everything works properly:

```bash
echo "This is a test email from msmtp and mailx" | mailx -s "Test Email" recipient@example.com
```

- Replace `recipient@example.com` with your actual email.

Check your inbox to confirm the test email arrives successfully.

### **Step 5: Set Up ZFS Scrub Email Notifications**
Now that email notifications work, you can set up your **ZFS scrub notification** as discussed before. Here’s how you can add email notifications to your **scrub cron job**:

1. Open the crontab:
   ```bash
   sudo crontab -e
   ```

2. Add the following line to send an email when the ZFS scrub completes successfully:

   ```bash
   0 0 1 * * zpool scrub rpool && echo "ZFS scrub completed successfully on $(date)" | mailx -s "ZFS Scrub Notification" your-email@example.com
   ```

   - Replace `your-email@example.com` with your actual email.

### **Conclusion**
Using **msmtp** with **mailx** is a reliable way to send email notifications from your Ubuntu server via **Google Workspace**. This configuration ensures secure communication with Google’s SMTP server and allows you to receive email alerts whenever a ZFS scrub runs on your server.