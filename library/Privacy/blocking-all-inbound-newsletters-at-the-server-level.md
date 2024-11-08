---
title: "Blocking all inbound newsletters at the server level"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


Creating an inbound email filter in Google Workspace to block email newsletters based on specific header criteria involves a few steps within the Google Admin Console. Here’s how to set it up:

### Step-by-Step Guide to Create an Inbound Email Filter

1. **Access Google Admin Console**:
   - Go to the [Google Admin Console](https://admin.google.com).
   - Log in with your administrator account.

2. **Navigate to Gmail Settings**:
   - From the Admin Console home page, click on **Apps**.
   - Then click on **Google Workspace**.
   - Select **Gmail**.

3. **Configure Routing**:
   - Click on **Advanced settings** (you may need to scroll down).
   - In the **Spam, Phishing, and Malware** section, look for **Content compliance**.

4. **Create a New Filter**:
   - Click on **Configure** (if you see this option) or look for the **Add another rule** option.
   - You will see options to create a new rule.

5. **Set Filter Conditions**:
   - In the **Name** field, enter a name for your rule (e.g., "Block Newsletters").
   - Under **Email messages to affect**, select **Inbound**.
   - For **If the following conditions are met**, set conditions based on the email headers. For example:
     - Select **Header** from the dropdown.
     - Choose **Matches** and enter a regex pattern that matches the newsletter headers you want to block (e.g., `.*newsletter.*`).
   - You can use multiple header conditions if necessary.

6. **Set the Action**:
   - In the **Actions** section, choose what happens to the emails that match your conditions:
     - Select **Reject message** or **Delete message** if you want to block them outright.
     - You can also choose **Send a notification to the sender** if you want to notify them that their email was blocked.

7. **Review and Save**:
   - Review your filter settings to ensure everything is configured correctly.
   - Click **Save** to create the filter.

8. **Test the Filter**:
   - After setting up the filter, it’s a good idea to test it to ensure it’s working as expected. You can do this by sending an email that matches the criteria from an account you control.

### Additional Considerations

- **Regex Patterns**: Be careful with the regex patterns you use in the header condition to ensure they accurately match the newsletters you want to block. You may need to adjust the pattern based on the specific headers of the emails you’re targeting.
  
- **Monitoring**: After setting up the filter, monitor your email traffic to ensure legitimate emails are not inadvertently blocked.

- **Documentation**: Review [Google's documentation on content compliance rules](https://support.google.com/a/answer/10353230) for more details and examples of setting up filters.

### Conclusion

By following these steps, you can create an inbound email filter in Google Workspace to block email newsletters based on specific header criteria. This approach helps manage unwanted emails at the server level, reducing clutter in your inbox.