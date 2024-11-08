---
title: Configuring a cron job in Fedora to run on boot
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Thanks. But what happens if my computer isn't turned on at midnight?

# Output

Based on the search results and your question, here are a few key points to consider:

1. If the computer is completely turned off at the scheduled time, the task will not run. Cron jobs and scheduled tasks can only execute when the system is powered on and running.

2. For systems in sleep or hibernation mode, there are ways to wake the computer to run scheduled tasks:

   - On Windows, you can use the Task Scheduler and select the option "Wake the computer to run this task" when setting up the task.
   
   - On Linux, you can use RTC (Real-Time Clock) alarm to wake the system from sleep or hibernation.

3. To ensure your backup task runs even if the computer isn't on at midnight, you could consider these options:

   - Set up a "wake on LAN" feature if your hardware supports it, to turn on the computer shortly before the scheduled task.
   
   - Use a tool like anacron on Linux, which runs missed cron jobs when the system boots up.
   
   - Schedule the task to run "as soon as possible after the scheduled time if the computer was off at the scheduled time" in Windows Task Scheduler.

4. Another approach is to schedule the task to run when the computer starts up or when a user logs on, rather than at a specific time. This ensures the task runs daily, even if not precisely at midnight.

5. For critical tasks, some users prefer to leave their computers on or in sleep mode (rather than fully powered off) to ensure scheduled tasks can run.

Remember, the exact method will depend on your operating system and specific hardware capabilities. You might need to experiment to find the best solution for your setup.

# Input

Wow. That seems like a crazy limitation. Let's go for a job that triggers on boot. Is it possible to prevent it from running more than once every 24 hours? Ie, if I reboot the computer multiple times in a day, I don't need it to run every time?

# Output

Based on the search results and your specific requirements, we can create a systemd timer that runs on boot but not more than once every 24 hours. This approach offers more flexibility than a traditional cron job. Here's how you can set it up:

1. Create a service file for your Ansible playbook:

```bash
sudo nano /etc/systemd/system/ansible-config.service
```

Add the following content:

```ini
[Unit]
Description=Run Ansible playbook for system configuration

[Service]
Type=oneshot
ExecStart=/usr/bin/ansible-playbook /home/daniel/ansible/config.yml
User=daniel

[Install]
WantedBy=multi-user.target
```

2. Create a timer file:

```bash
sudo nano /etc/systemd/system/ansible-config.timer
```

Add the following content:

```ini
[Unit]
Description=Run Ansible playbook on boot, but not more than once per day

[Timer]
OnBootSec=5min
OnUnitInactiveSec=24h
Unit=ansible-config.service

[Install]
WantedBy=timers.target
```

This configuration does the following:
- `OnBootSec=5min`: Runs the service 5 minutes after boot.
- `OnUnitInactiveSec=24h`: Ensures the service doesn't run again for 24 hours after its last execution.

3. Enable and start the timer:

```bash
sudo systemctl enable ansible-config.timer
sudo systemctl start ansible-config.timer
```

4. You can check the status of your timer:

```bash
systemctl status ansible-config.timer
```

This setup will run your Ansible playbook on boot, but not more than once every 24 hours, even if you reboot multiple times within a day. The systemd timer keeps track of the last execution time, ensuring the 24-hour interval is respected across reboots.

Remember to adjust the paths and user in the service file to match your specific setup. This method provides more control and reliability compared to using @reboot in crontab, especially for your requirement of not running more than once per day.

Citations:
[1] https://www.howtogeek.com/replace-cron-jobs-with-systemd-timers/
[2] https://www.quickhost.uk/blog/2021/11/08/how-to-execute-a-job-automatically-at-boot-with-cron/
[3] https://www.linode.com/docs/guides/run-jobs-or-scripts-using-crontab-on-boot/
[4] https://phoenixnap.com/kb/crontab-reboot
[5] https://www.redhat.com/sysadmin/linux-cron-command