---
title: "script for counting md files"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


You asked for the script to also email the result after counting the Markdown files.

Here’s an updated version of the script that sends an email with the count of Markdown files:

Script: count_md_files_with_email.sh

#!/bin/bash

# Replace these with your Backblaze B2 account details
B2_APPLICATION_KEY_ID="<yourApplicationKeyId>"
B2_APPLICATION_KEY="<yourApplicationKey>"

# Replace with your bucket name and folder name
BUCKET_NAME="<yourBucketName>"
FOLDER_NAME="<yourFolderName>"

# Email configuration
EMAIL_SUBJECT="Markdown File Count in B2 Bucket"
EMAIL_TO="<recipient@example.com>"
EMAIL_FROM="<your_email@example.com>"
SMTP_SERVER="<smtp.server.com>"
SMTP_PORT=587
SMTP_USERNAME="<your_smtp_username>"
SMTP_PASSWORD="<your_smtp_password>"

# Authorize the B2 account
b2 authorize-account $B2_APPLICATION_KEY_ID $B2_APPLICATION_KEY

# Count the number of Markdown files in the specified folder
COUNT=$(b2 ls $BUCKET_NAME $FOLDER_NAME | grep '\.md$' | wc -l)

# Create the email body
EMAIL_BODY="Number of Markdown (.md) files in '$FOLDER_NAME' of bucket '$BUCKET_NAME': $COUNT"

# Display the result in the terminal
echo "$EMAIL_BODY"

# Send the email
sendmail -S $SMTP_SERVER:$SMTP_PORT \
  -f $EMAIL_FROM \
  -au"$SMTP_USERNAME" \
  -ap"$SMTP_PASSWORD" \
  -t <<EOF
To: $EMAIL_TO
From: $EMAIL_FROM
Subject: $EMAIL_SUBJECT

$EMAIL_BODY
EOF

Steps to use the script:

1. Save the script: Copy the updated script and save it as count_md_files_with_email.sh.


2. Install sendmail: If you don’t have sendmail installed, you can install it based on your package manager. For example, on Fedora or similar systems:

sudo dnf install sendmail


3. Make the script executable:

chmod +x count_md_files_with_email.sh


4. Update the placeholders:

Backblaze B2 credentials: Replace <yourApplicationKeyId>, <yourApplicationKey>, <yourBucketName>, and <yourFolderName> with your actual Backblaze B2 credentials and details.

Email settings: Replace the placeholders in the email section (e.g., <recipient@example.com>, <smtp.server.com>, <your_smtp_username>, etc.) with your own email configuration.



5. Run the script:

./count_md_files_with_email.sh



What the updated script does:

Authorization: It authorizes the B2 CLI using your account credentials.

File count: It counts the .md files in the specified folder.

Email sending: It uses the sendmail command to send the result to the specified recipient.


This script assumes you have access to an SMTP server to send emails. If you don’t have one, you can use an external service (like Gmail’s SMTP server), but you might need to adjust the SMTP settings accordingly.

