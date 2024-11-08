---
title: "Getting email notifications when a ZFS scrub runs"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

I'd love to get an email notification when the ZFS scrub runs. Can you suggest the best way to set this up? Perhaps with a webhook notification service. I remember there was one that was free

# Output

To set up email or webhook notifications when a ZFS scrub runs, you can use **cron jobs** to trigger notifications after each scrub is executed. There are several options to achieve this, including integrating a free webhook notification service like **Healthchecks.io** or setting up direct email notifications using **mailx** or **sendmail**.

Here’s a step-by-step guide using both **webhook notification** and **email notification** options.

### **Option 1: Use Webhook Notification Service (Healthchecks.io)**

#### **Step 1: Create a Free Healthchecks.io Account**
1. Go to [Healthchecks.io](https://healthchecks.io/) and create an account.
2. Create a new check (specifically for monitoring the ZFS scrub). Copy the **unique webhook URL** they provide for this check.

#### **Step 2: Modify the Scrub Command in Cron to Notify via Webhook**
1. Open the crontab to edit your ZFS scrub job:
   ```bash
   sudo crontab -e
   ```

2. Modify the existing ZFS scrub job to include a call to the webhook once the scrub completes. For example, assuming your scrub job is scheduled on the 1st of every month at midnight:

   ```bash
   0 0 1 * * zpool scrub rpool && curl -fsS --retry 3 <your-healthchecks-url>
   ```

   - **Explanation**:
     - `zpool scrub rpool`: Starts the scrub for the ZFS pool.
     - `curl -fsS --retry 3 <your-healthchecks-url>`: Notifies Healthchecks.io that the job has completed successfully by calling the webhook URL.

#### **Step 3: Set Up Failure Notifications**
- Healthchecks.io will automatically send failure notifications if the job fails or doesn’t complete within the expected timeframe. You can configure these notifications to go to your email or even set up other integrations like **Slack**, **Telegram**, etc.

---

### **Option 2: Set Up Email Notifications Using mailx**

If you prefer email notifications, you can use the **mailx** or **sendmail** utility to send an email whenever the scrub runs.

#### **Step 1: Install mailx**
If you don’t have `mailx` installed, you can install it with the following:

```bash
sudo apt-get install mailx
```

#### **Step 2: Modify the Scrub Command in Cron to Include Email Notification**

1. Open the crontab:
   ```bash
   sudo crontab -e
   ```

2. Modify your existing ZFS scrub cron job to send an email when the scrub finishes:
   ```bash
   0 0 1 * * zpool scrub rpool && echo "ZFS scrub completed successfully on $(date)" | mailx -s "ZFS Scrub Notification" your-email@example.com
   ```

   - **Explanation**:
     - `echo "ZFS scrub completed successfully on $(date)"`: Generates the email body containing the completion message and current date.
     - `mailx -s "ZFS Scrub Notification" your-email@example.com`: Sends an email with the subject "ZFS Scrub Notification" to the specified email address.

#### **Step 3: Send Failure Notifications (Optional)**
To notify you of any **failure** during the scrub process, you can modify the cron job to send an email only if the scrub fails:

```bash
0 0 1 * * zpool scrub rpool || echo "ZFS scrub failed on $(date)" | mailx -s "ZFS Scrub Failure Alert" your-email@example.com
```

- This command will send an email notification **only if the scrub fails** (i.e., if the `zpool scrub` command exits with an error).

---

### **Conclusion**
- **Webhook Notification (Healthchecks.io)**: This is an excellent option for lightweight monitoring. It requires no email setup, and you can also set up integrations with Slack or other services.
- **Email Notifications (mailx)**: A traditional solution that works if you prefer receiving direct email notifications about the scrub process.

Either approach will keep you informed about the status of your ZFS scrubs.